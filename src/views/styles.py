COLORS = {
    "bg_primary": "#1a1025",
    "bg_secondary": "#2d1b4e",
    "bg_tertiary": "#3d2a5c",
    "accent": "#f5c518",
    "accent_dark": "#d4a017",
    "accent_hover": "#ffe44d",
    "text": "#e8e0f0",
    "text_dim": "#9b8fb0",
    "border": "#3d2a5c",
    "danger": "#e74c3c",
    "success": "#2ecc71",
}

STYLESHEET = """
QMainWindow {
    background-color: #1a1025;
}

QWidget {
    background-color: #1a1025;
    color: #e8e0f0;
    font-family: "Segoe UI", sans-serif;
    font-size: 13px;
}

QLabel {
    background: transparent;
    color: #e8e0f0;
}

QLabel#title {
    font-size: 22px;
    font-weight: bold;
    color: #f5c518;
}

QLabel#subtitle {
    font-size: 12px;
    color: #9b8fb0;
}

QPushButton {
    background-color: #2d1b4e;
    color: #e8e0f0;
    border: 1px solid #3d2a5c;
    border-radius: 6px;
    padding: 8px 20px;
    font-size: 13px;
    font-weight: 500;
}

QPushButton:hover {
    background-color: #3d2a5c;
    border-color: #f5c518;
    color: #f5c518;
}

QPushButton:pressed {
    background-color: #4a3470;
}

QPushButton:disabled {
    background-color: #1a1025;
    color: #9b8fb0;
    border-color: #2d1b4e;
}

QPushButton#primary {
    background-color: #f5c518;
    color: #1a1025;
    border: none;
    font-weight: bold;
    padding: 10px 30px;
    font-size: 14px;
}

QPushButton#primary:hover {
    background-color: #ffe44d;
    color: #1a1025;
}

QPushButton#primary:pressed {
    background-color: #d4a017;
}

QPushButton#primary:disabled {
    background-color: #3d2a5c;
    color: #9b8fb0;
}

QPushButton#danger {
    border-color: #e74c3c;
    color: #e74c3c;
}

QPushButton#danger:hover {
    background-color: #e74c3c;
    color: #e8e0f0;
}

QProgressBar {
    background-color: #2d1b4e;
    border: 1px solid #3d2a5c;
    border-radius: 6px;
    text-align: center;
    color: #1a1025;
    font-weight: bold;
    min-height: 24px;
}

QProgressBar::chunk {
    background-color: #f5c518;
    border-radius: 5px;
}

QComboBox {
    background-color: #2d1b4e;
    color: #e8e0f0;
    border: 1px solid #3d2a5c;
    border-radius: 6px;
    padding: 6px 12px;
}

QComboBox:hover {
    border-color: #f5c518;
}

QComboBox::drop-down {
    border: none;
    width: 30px;
}

QComboBox QAbstractItemView {
    background-color: #2d1b4e;
    color: #e8e0f0;
    selection-background-color: #3d2a5c;
    selection-color: #f5c518;
    border: 1px solid #3d2a5c;
}

QListWidget {
    background-color: #2d1b4e;
    border: 1px solid #3d2a5c;
    border-radius: 6px;
    padding: 4px;
    outline: none;
}

QListWidget::item {
    background-color: transparent;
    color: #e8e0f0;
    padding: 6px 8px;
    border-radius: 4px;
    margin: 1px 0;
}

QListWidget::item:selected {
    background-color: #3d2a5c;
    color: #f5c518;
}

QListWidget::item:hover {
    background-color: #3d2a5c;
}

QScrollBar:vertical {
    background-color: #1a1025;
    width: 8px;
    border: none;
}

QScrollBar::handle:vertical {
    background-color: #3d2a5c;
    border-radius: 4px;
    min-height: 30px;
}

QScrollBar::handle:vertical:hover {
    background-color: #f5c518;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0;
}

QScrollBar:horizontal {
    height: 0;
}

QCheckBox {
    color: #e8e0f0;
    spacing: 6px;
    font-size: 13px;
}

QCheckBox::indicator {
    width: 16px;
    height: 16px;
    border: 2px solid #3d2a5c;
    border-radius: 4px;
    background-color: #2d1b4e;
}

QCheckBox::indicator:hover {
    border-color: #f5c518;
}

QCheckBox::indicator:checked {
    background-color: #f5c518;
    border-color: #f5c518;
}

QCheckBox:disabled {
    color: #9b8fb0;
}
"""
