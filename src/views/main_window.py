from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QProgressBar, QCheckBox
)
from PyQt6.QtCore import Qt
from src.views.styles import STYLESHEET
from src.views.image_list import ImageListWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OCR Images to PDF")
        self.setMinimumSize(900, 650)
        self.setStyleSheet(STYLESHEET)
        self._build_ui()

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        self.main_layout = QVBoxLayout(central)
        self.main_layout.setContentsMargins(24, 20, 24, 20)
        self.main_layout.setSpacing(16)

        self._build_header()
        self._build_image_section()
        self._build_controls()
        self._build_progress()

    def _build_header(self):
        header = QVBoxLayout()
        header.setSpacing(2)

        self.title_label = QLabel("OCR Images to PDF")
        self.title_label.setObjectName("title")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.subtitle_label = QLabel("Convierte imagenes a PDF con texto seleccionable")
        self.subtitle_label.setObjectName("subtitle")

        header.addWidget(self.title_label)
        header.addWidget(self.subtitle_label)
        self.main_layout.addLayout(header)

    def _build_image_section(self):
        self.image_list = ImageListWidget()
        self.main_layout.addWidget(self.image_list, stretch=1)

    def _build_controls(self):
        controls = QHBoxLayout()
        controls.setSpacing(12)

        lang_label = QLabel("Idioma OCR:")
        lang_label.setStyleSheet("font-size: 13px;")

        self.chk_spa = QCheckBox("Espanol")
        self.chk_spa.setChecked(True)
        self.chk_eng = QCheckBox("Ingles")
        self.chk_eng.setChecked(True)

        controls.addWidget(lang_label)
        controls.addWidget(self.chk_spa)
        controls.addWidget(self.chk_eng)
        controls.addStretch()

        self.btn_convert = QPushButton("Convertir a PDF")
        self.btn_convert.setObjectName("primary")
        self.btn_convert.setEnabled(False)

        self.btn_cancel = QPushButton("Cancelar")
        self.btn_cancel.setObjectName("danger")
        self.btn_cancel.setVisible(False)

        controls.addWidget(self.btn_cancel)
        controls.addWidget(self.btn_convert)

        self.main_layout.addLayout(controls)

    def _build_progress(self):
        progress_layout = QVBoxLayout()
        progress_layout.setSpacing(4)

        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setVisible(False)

        self.status_label = QLabel("")
        self.status_label.setObjectName("subtitle")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        progress_layout.addWidget(self.progress_bar)
        progress_layout.addWidget(self.status_label)
        self.main_layout.addLayout(progress_layout)

    def get_selected_language(self):
        langs = []
        if self.chk_spa.isChecked():
            langs.append("spa")
        if self.chk_eng.isChecked():
            langs.append("eng")
        return "+".join(langs) if langs else ""

    def set_progress(self, value, text=""):
        self.progress_bar.setVisible(value > 0)
        self.progress_bar.setValue(value)
        self.status_label.setText(text)

    def set_converting(self, active):
        self.btn_convert.setEnabled(not active)
        self.btn_cancel.setVisible(active)
        self.image_list.setEnabled(not active)
        self.chk_spa.setEnabled(not active)
        self.chk_eng.setEnabled(not active)
        if not active:
            self.progress_bar.setVisible(False)
