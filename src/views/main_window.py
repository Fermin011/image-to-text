from PyQt6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OCR Images to PDF")
        self.setMinimumSize(800, 600)
