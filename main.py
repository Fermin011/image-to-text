import sys
from PyQt6.QtWidgets import QApplication
from src.views.main_window import MainWindow
from src.controllers.app_controller import AppController


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    controller = AppController(window)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
