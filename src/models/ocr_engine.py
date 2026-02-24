import pytesseract
from PIL import Image
from PyQt6.QtCore import QObject, QThread, pyqtSignal
import os
import sys


def find_tesseract():
    if sys.platform == "win32":
        candidates = [
            r"C:\Program Files\Tesseract-OCR\tesseract.exe",
            r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
            os.path.expanduser(r"~\AppData\Local\Tesseract-OCR\tesseract.exe"),
        ]
        for path in candidates:
            if os.path.isfile(path):
                return path
    return "tesseract"


def check_tesseract():
    try:
        pytesseract.get_tesseract_version()
        return True
    except Exception:
        return False


class OcrWorker(QObject):
    progress = pyqtSignal(int, str)
    page_ready = pyqtSignal(int, bytes)
    page_error = pyqtSignal(int, str)
    finished = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, image_paths, language):
        super().__init__()
        self.image_paths = image_paths
        self.language = language
        self._cancelled = False

    def cancel(self):
        self._cancelled = True

    def run(self):
        total = len(self.image_paths)
        for i, path in enumerate(self.image_paths):
            if self._cancelled:
                break

            name = os.path.basename(path)
            self.progress.emit(
                int((i / total) * 100),
                f"Procesando {i + 1}/{total}: {name}"
            )

            try:
                pdf_bytes = self._process_image(path)
                self.page_ready.emit(i, pdf_bytes)
            except Exception as e:
                self.page_error.emit(i, f"{name}: {e}")

        if not self._cancelled:
            self.progress.emit(100, "Generando PDF final...")
        self.finished.emit()

    def _process_image(self, path):
        img = Image.open(path)
        if img.mode != "RGB":
            img = img.convert("RGB")
        # pytesseract genera un PDF searchable por imagen
        pdf_bytes = pytesseract.image_to_pdf_or_hocr(
            img, lang=self.language, extension="pdf"
        )
        return pdf_bytes


class OcrEngine:
    def __init__(self):
        tesseract_path = find_tesseract()
        pytesseract.pytesseract.tesseract_cmd = tesseract_path
        self._thread = None
        self._worker = None

    def is_available(self):
        return check_tesseract()

    def start_processing(self, image_paths, language, callbacks):
        self._thread = QThread()
        self._worker = OcrWorker(image_paths, language)
        self._worker.moveToThread(self._thread)

        self._worker.progress.connect(callbacks["progress"])
        self._worker.page_ready.connect(callbacks["page_ready"])
        self._worker.page_error.connect(callbacks.get("page_error", lambda *_: None))
        self._worker.finished.connect(callbacks["finished"])
        self._worker.error.connect(callbacks["error"])
        self._worker.finished.connect(self._cleanup)

        self._thread.started.connect(self._worker.run)
        self._thread.start()

    def cancel(self):
        if self._worker:
            self._worker.cancel()

    def _cleanup(self):
        if self._thread:
            self._thread.quit()
            self._thread.wait()
            self._thread = None
            self._worker = None
