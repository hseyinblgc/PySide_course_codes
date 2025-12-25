from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("This is My first app!")
button = QPushButton()
button.setText("Press Me")
def onPressed():
    print("Pressed")
button.clicked.connect(onPressed)
window.setCentralWidget(button)

window.show()
app.exec()