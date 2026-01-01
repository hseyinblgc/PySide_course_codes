from PySide6.QtWidgets import QWidget, QMessageBox, QVBoxLayout, QMessageBox, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QMessageBox")

        button_hard = QPushButton("Hard")
        button_critical = QPushButton("Critical")
        button_question = QPushButton("Question")
        button_information = QPushButton("Information")
        button_warning = QPushButton("Warning")
        button_about = QPushButton("About")
        button_hard.clicked.connect(self.button_clicked_hard)
        button_critical.clicked.connect(self.button_clicked_critical)
        button_question.clicked.connect(self.button_clicked_question)
        button_information.clicked.connect(self.button_clicked_information)
        button_warning.clicked.connect(self.button_clicked_warning)
        button_about.clicked.connect(self.button_clicked_about)

        # Set up the layouts
        layout = QVBoxLayout()
        layout.addWidget(button_hard)
        layout.addWidget(button_critical)
        layout.addWidget(button_question)
        layout.addWidget(button_information)
        layout.addWidget(button_warning)
        layout.addWidget(button_about)
        self.setLayout(layout)

    # The hard way 
    def button_clicked_hard(self):
        message = QMessageBox()
        # message.setMinimumSize (700,200)
        message.setWindowTitle("Message Title")
        message.setText("Something happened")
        message.setInformativeText("Do you want to do something about it?")
        message.setIcon(QMessageBox.Critical)
        message.setStandardButtons (QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("User chose OK")
        else:
            print ("User chose Cancel")

    def button_clicked_critical(self):
        ret = QMessageBox.critical(self, "This is Critical Message",
                                   "What you gonna do now?",
                                   QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print('User chose Ok')
        else:
            print('User chose Cancel')

    def button_clicked_question(self):
        ret = QMessageBox.question(self, "This is Question Message",
                            "What you gonna do now?",
                            QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print('User chose Ok')
        else:
            print('User chose Cancel')

    def button_clicked_information(self):
        ret = QMessageBox.information(self, "This is Information Message",
                    "What you gonna do now?",
                    QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print('User chose Ok')
        else:
            print('User chose Cancel')
    def button_clicked_warning(self):
        ret = QMessageBox.warning(self, "This is Warning Message",
                    "What you gonna do now?",
                    QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print('User chose Ok')
        else:
            print('User chose Cancel')
    def button_clicked_about(self):
        QMessageBox.about(self, "This is About Message",
                    "What you gonna do now?")
        print('About dialog shown')