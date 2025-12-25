"""
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("This is My first app!")
button = QPushButton()
button.setText("Press Me")
window.setCentralWidget(button)
window.show()
app.exec()
"""

### V2
"""
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("This is ButtonHolder Class")
        button = QPushButton("Press Me")

        # set up the button as our  central widget
        self.setCentralWidget(button)


app = QApplication(sys.argv)
window = ButtonHolder()
window.show()
app.exec()
"""

import sys
from PySide6.QtWidgets import QApplication
from button_holder import ButtonHolder

app = QApplication(sys.argv)
window = ButtonHolder()
window.show()
app.exec()
