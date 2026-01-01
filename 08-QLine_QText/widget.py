from PySide6.QtCore import QLocale, QPoint, QRect, QSize, Qt
from PySide6.QtGui import QCursor, QFont, QIcon, QPalette, QRegion
from PySide6.QtWidgets import QSizePolicy, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel

class Widget(QWidget):
    def __init__(self):
        super().__init__()