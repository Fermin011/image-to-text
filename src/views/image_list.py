from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QListWidget,
    QListWidgetItem, QPushButton, QLabel, QFileDialog
)
from PyQt6.QtCore import pyqtSignal, Qt
import os


SUPPORTED_FORMATS = "Imagenes (*.png *.jpg *.jpeg *.bmp *.tiff *.tif *.webp)"


class DropZone(QWidget):
    files_dropped = pyqtSignal(list)
    browse_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setMinimumHeight(120)
        self.setObjectName("dropzone")
        self.setStyleSheet("""
            QWidget#dropzone {
                border: 2px dashed #3d2a5c;
                border-radius: 10px;
                background-color: #2d1b4e;
            }
            QWidget#dropzone:hover {
                border-color: #f5c518;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        hint = QLabel("Arrastra imagenes aqui")
        hint.setStyleSheet("color: #9b8fb0; font-size: 15px; border: none; background: transparent;")
        hint.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.browse_btn = QPushButton("Seleccionar archivos")
        self.browse_btn.setFixedWidth(200)
        self.browse_btn.clicked.connect(self.browse_clicked.emit)

        layout.addWidget(hint)
        layout.addWidget(self.browse_btn, alignment=Qt.AlignmentFlag.AlignCenter)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            self.setStyleSheet("""
                QWidget#dropzone {
                    border: 2px dashed #f5c518;
                    border-radius: 10px;
                    background-color: #3d2a5c;
                }
            """)

    def dragLeaveEvent(self, event):
        self.setStyleSheet("""
            QWidget#dropzone {
                border: 2px dashed #3d2a5c;
                border-radius: 10px;
                background-color: #2d1b4e;
            }
            QWidget#dropzone:hover {
                border-color: #f5c518;
            }
        """)

    def dropEvent(self, event):
        self.dragLeaveEvent(event)
        paths = []
        for url in event.mimeData().urls():
            path = url.toLocalFile()
            ext = os.path.splitext(path)[1].lower()
            if ext in (".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".tif", ".webp"):
                paths.append(path)
        if paths:
            self.files_dropped.emit(paths)


class ImageListWidget(QWidget):
    images_changed = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self._image_paths = []
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)

        self.drop_zone = DropZone()
        layout.addWidget(self.drop_zone)

        # Header con contador y botones
        header = QHBoxLayout()
        self.count_label = QLabel("0 imagenes")
        self.count_label.setStyleSheet("color: #9b8fb0; font-size: 12px;")

        self.btn_remove = QPushButton("Quitar")
        self.btn_remove.setObjectName("danger")
        self.btn_remove.setFixedWidth(80)
        self.btn_remove.setEnabled(False)

        self.btn_clear = QPushButton("Limpiar")
        self.btn_clear.setObjectName("danger")
        self.btn_clear.setFixedWidth(80)
        self.btn_clear.setEnabled(False)

        self.btn_up = QPushButton("Subir")
        self.btn_up.setFixedWidth(70)
        self.btn_up.setEnabled(False)

        self.btn_down = QPushButton("Bajar")
        self.btn_down.setFixedWidth(70)
        self.btn_down.setEnabled(False)

        header.addWidget(self.count_label)
        header.addStretch()
        header.addWidget(self.btn_up)
        header.addWidget(self.btn_down)
        header.addWidget(self.btn_remove)
        header.addWidget(self.btn_clear)

        layout.addLayout(header)

        self.list_widget = QListWidget()
        self.list_widget.setSelectionMode(QListWidget.SelectionMode.ExtendedSelection)
        layout.addWidget(self.list_widget)

        self._connect_signals()

    def _connect_signals(self):
        self.drop_zone.browse_clicked.connect(self._open_file_dialog)
        self.drop_zone.files_dropped.connect(self.add_images)
        self.btn_remove.clicked.connect(self._remove_selected)
        self.btn_clear.clicked.connect(self._clear_all)
        self.btn_up.clicked.connect(self._move_up)
        self.btn_down.clicked.connect(self._move_down)
        self.list_widget.itemSelectionChanged.connect(self._update_buttons)

    def _open_file_dialog(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "Seleccionar imagenes", "", SUPPORTED_FORMATS
        )
        if files:
            self.add_images(files)

    def add_images(self, paths):
        existing = set(self._image_paths)
        for p in paths:
            if p not in existing and len(self._image_paths) < 500:
                self._image_paths.append(p)
                name = os.path.basename(p)
                size_mb = os.path.getsize(p) / (1024 * 1024)
                item = QListWidgetItem(f"{name}  ({size_mb:.1f} MB)")
                item.setData(Qt.ItemDataRole.UserRole, p)
                self.list_widget.addItem(item)
        self._update_state()

    def _remove_selected(self):
        for item in reversed(self.list_widget.selectedItems()):
            row = self.list_widget.row(item)
            self.list_widget.takeItem(row)
            self._image_paths.pop(row)
        self._update_state()

    def _clear_all(self):
        self.list_widget.clear()
        self._image_paths.clear()
        self._update_state()

    def _move_up(self):
        rows = sorted(set(self.list_widget.row(i) for i in self.list_widget.selectedItems()))
        if not rows or rows[0] == 0:
            return
        for row in rows:
            self._swap_items(row, row - 1)
            self.list_widget.item(row - 1).setSelected(True)
            self.list_widget.item(row).setSelected(False)

    def _move_down(self):
        rows = sorted(set(self.list_widget.row(i) for i in self.list_widget.selectedItems()), reverse=True)
        if not rows or rows[0] == self.list_widget.count() - 1:
            return
        for row in rows:
            self._swap_items(row, row + 1)
            self.list_widget.item(row + 1).setSelected(True)
            self.list_widget.item(row).setSelected(False)

    def _swap_items(self, row_a, row_b):
        self._image_paths[row_a], self._image_paths[row_b] = (
            self._image_paths[row_b], self._image_paths[row_a]
        )
        item_a = self.list_widget.takeItem(row_a)
        self.list_widget.insertItem(row_b, item_a)

    def _update_state(self):
        count = len(self._image_paths)
        self.count_label.setText(f"{count} {'imagen' if count == 1 else 'imagenes'}")
        self.btn_clear.setEnabled(count > 0)
        self._update_buttons()
        self.images_changed.emit(self._image_paths.copy())

    def _update_buttons(self):
        has_selection = len(self.list_widget.selectedItems()) > 0
        self.btn_remove.setEnabled(has_selection)
        self.btn_up.setEnabled(has_selection)
        self.btn_down.setEnabled(has_selection)

    def get_image_paths(self):
        return self._image_paths.copy()
