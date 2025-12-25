from PySide6.QtWidgets import QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("This is ButtonHolder Class")
        button = QPushButton("Press Me")
        button.setCheckable(True)
        button.clicked.connect(self.onClicked)

        # set up the button as our  central widget
        self.setCentralWidget(button)

    # Notify when pressed
    def onClicked(self, data):
        if data:
            print("You pressed the button!")
        else:
            print("You just released the button")