from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider
from button_holder import ButtonHolder

#The slot: responds when something happens
def respond_to_slider(data):
    print("slider moved to: ", data)

app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

# You just do the connection. The Qt system takes care of
# passing data from signal to the slot
slider.valueChanged.connect(respond_to_slider)
window = ButtonHolder()

window.button.clicked.connect(slider.show)

window.show()
app.exec()
