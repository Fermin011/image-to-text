from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel
)
from PyQt6.QtCore import Qt
from src.views.styles import STYLESHEET


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
