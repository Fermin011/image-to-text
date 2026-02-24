from PyQt6.QtWidgets import QFileDialog, QMessageBox
from src.models.ocr_engine import OcrEngine
from src.models.pdf_builder import PdfBuilder


class AppController:
    def __init__(self, view):
        self.view = view
        self.ocr = OcrEngine()
        self.pdf = PdfBuilder()
        self._connect_signals()
        self._check_tesseract()

    def _connect_signals(self):
        self.view.image_list.images_changed.connect(self._on_images_changed)
        self.view.btn_convert.clicked.connect(self._start_conversion)
        self.view.btn_cancel.clicked.connect(self._cancel_conversion)

    def _check_tesseract(self):
        if not self.ocr.is_available():
            self.view.status_label.setText(
                "Tesseract OCR no detectado. Instalalo para poder convertir."
            )
            self.view.status_label.setStyleSheet("color: #e74c3c; font-size: 12px;")

    def _on_images_changed(self, paths):
        has_images = len(paths) > 0
        has_tesseract = self.ocr.is_available()
        self.view.btn_convert.setEnabled(has_images and has_tesseract)

    def _start_conversion(self):
        paths = self.view.image_list.get_image_paths()
        if not paths:
            return

        output_path, _ = QFileDialog.getSaveFileName(
            self.view, "Guardar PDF", "output.pdf", "PDF (*.pdf)"
        )
        if not output_path:
            return

        self._output_path = output_path
        self.pdf.clear()
        language = self.view.get_selected_language()

        self.view.set_converting(True)
        self.view.set_progress(0, "Iniciando procesamiento...")

        self.ocr.start_processing(paths, language, {
            "progress": self._on_progress,
            "page_ready": self._on_page_ready,
            "finished": self._on_finished,
            "error": self._on_error,
        })

    def _cancel_conversion(self):
        self.ocr.cancel()
        self.view.set_converting(False)
        self.view.set_progress(0, "Conversion cancelada")
        self.pdf.clear()

    def _on_progress(self, value, text):
        self.view.set_progress(value, text)

    def _on_page_ready(self, index, pdf_bytes):
        self.pdf.add_page(index, pdf_bytes)

    def _on_finished(self):
        count = self.pdf.page_count
        if count == 0:
            self.view.set_converting(False)
            self.view.set_progress(0, "")
            return

        try:
            self.pdf.build(self._output_path)
            self.view.set_converting(False)
            self.view.set_progress(0, "")
            QMessageBox.information(
                self.view, "Listo",
                f"PDF generado con {count} paginas.\n"
                f"Guardado en: {self._output_path}"
            )
        except Exception as e:
            self._on_error(f"Error al guardar PDF: {e}")

    def _on_error(self, message):
        self.view.set_converting(False)
        self.view.set_progress(0, "")
        self.pdf.clear()
        QMessageBox.critical(self.view, "Error", message)
