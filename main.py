import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("MyFirstApp")
        self.first_label = QLabel(self)

        self.button = QPushButton("Push me", self)

        self.first_label.setText("Hello")
        self.vbox = QVBoxLayout(self)
        self.hbox = QHBoxLayout()
        self.vbox.addWidget(self.first_label)
        self.vbox.addLayout(self.hbox)

        self.button.clicked.connect(self.changeText)

    def changeText(self):
        self.first_label.setText("Привет")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
