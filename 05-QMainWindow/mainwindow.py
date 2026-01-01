from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar, QMessageBox
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import QSize




class MainWindow(QMainWindow):
    def __init__(self, app) -> None:
        super().__init__()
        self.app = app #declare an app member
        self.setWindowTitle("Custom MainWindow") 

        # Menu bar and menus
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("&File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        file_menu = menu_bar.addMenu("Window")
        file_menu = menu_bar.addMenu("Settings")
        file_menu = menu_bar.addMenu("Help")

        # working with toolbars
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        # add the quit action to the toolbar
        toolbar.addAction(quit_action)

        action1 = QAction("Some Action", self)
        action1.setStatusTip("Status Message for some action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)
        toolbar.addSeparator()
        action2 = QAction(QIcon("images.png"), "Some other action", self)
        action2.setStatusTip("Status message for some other action")
        action2.triggered.connect(self.toolbar_button_click)
        action2.setCheckable(True)
        toolbar.addAction(action2)
        toolbar.addSeparator()
        button = QPushButton("Click Here")
        button.clicked.connect(self.showMessageBox)
        toolbar.addWidget(button)

        # Working with status bars
        self.setStatusBar(QStatusBar(self))


    def toolbar_button_click(self):
        self.statusBar().showMessage("Message from my app", 3000)
    
    def showMessageBox(self):
        ret = QMessageBox.warning(self, "This is MessageBox",
                                      "Some Information",
                                      QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print("Ok")
        else:
            print(":(")

    def quit_app(self):
        self.app.quit()       