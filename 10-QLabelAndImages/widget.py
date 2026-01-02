from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
import sys

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel Image Demo")
        
        image_label = QLabel()
        image_label.setPixmap(QPixmap("10-QLabelAndImages/images/image.png"))
        v_layout = QVBoxLayout()
        v_layout.addWidget(image_label)
        self.setLayout(v_layout)

app = QApplication(sys.argv)
window = Widget()
window.show()
app.exec()