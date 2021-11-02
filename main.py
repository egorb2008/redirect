import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()

        self.setWindowTitle("Calculator")

        self.hbox_line = QHBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox_res = QHBoxLayout()
        self.hbox_clear = QHBoxLayout()
        self.vbox = QVBoxLayout()

        self.vbox.addLayout(self.hbox_line)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox_res)
        self.vbox.addLayout(self.hbox_clear)

        self.line = QLineEdit(self)

        # задаём кнопки цифр
        self.b_1 = QPushButton("1", self)
        self.b_2 = QPushButton("2", self)
        self.b_3 = QPushButton("3", self)
        self.b_4 = QPushButton("4", self)
        self.b_5 = QPushButton("5", self)
        self.b_6 = QPushButton("6", self)
        self.b_7 = QPushButton("7", self)
        self.b_8 = QPushButton("8", self)
        self.b_9 = QPushButton("9", self)
        self.b_0 = QPushButton("0", self)
        # задаём кнопки операций
        self.b_plus = QPushButton("+", self)
        # self.b_plus.setStyleSheet('background: rgb(32,178,170);')
        self.b_minus = QPushButton("-", self)
        # self.b_minus.setStyleSheet('background: rgb(32,178,170);')
        self.b_divide = QPushButton("/", self)
        # self.b_divide.setStyleSheet('background: rgb(32,178,170);')
        self.b_multiply = QPushButton("*", self)
        # self.b_multiply.setStyleSheet('background: rgb(32,178,170);')
        self.b_res = QPushButton("=", self)
        self.clear= QPushButton("Очистить поле ввода", self)

        self.clear.setStyleSheet('background: rgb(139,0,0);')

        self.hbox_line.addWidget(self.line)
        self.hbox1.addWidget(self.b_1)
        self.hbox1.addWidget(self.b_2)
        self.hbox1.addWidget(self.b_3)
        self.hbox1.addWidget(self.b_4)
        self.hbox1.addWidget(self.b_5)
        self.hbox1.addWidget(self.b_6)
        self.hbox1.addWidget(self.b_7)
        self.hbox1.addWidget(self.b_8)
        self.hbox1.addWidget(self.b_9)
        self.hbox1.addWidget(self.b_0)
        self.hbox1.addWidget(self.b_plus)
        self.hbox1.addWidget(self.b_minus)
        self.hbox1.addWidget(self.b_divide)
        self.hbox1.addWidget(self.b_multiply)
        self.hbox_res.addWidget(self.b_res)
        self.hbox_clear.addWidget(self.clear)

        self.setLayout(self.vbox)

        self.b_1.clicked.connect(lambda: self.addText("1"))
        self.b_2.clicked.connect(lambda: self.addText("2"))
        self.b_3.clicked.connect(lambda: self.addText("3"))
        self.b_4.clicked.connect(lambda: self.addText("4"))
        self.b_5.clicked.connect(lambda: self.addText("5"))
        self.b_6.clicked.connect(lambda: self.addText("6"))
        self.b_7.clicked.connect(lambda: self.addText("7"))
        self.b_8.clicked.connect(lambda: self.addText("8"))
        self.b_9.clicked.connect(lambda: self.addText("9"))
        self.b_0.clicked.connect(lambda: self.addText("0"))
        self.b_plus.clicked.connect(lambda: self.operation("+"))
        self.b_minus.clicked.connect(lambda: self.operation("-"))
        self.b_divide.clicked.connect(lambda: self.operation("/"))
        self.b_multiply.clicked.connect(lambda: self.operation("*"))
        self.b_res.clicked.connect(self.result)
        self.clear.clicked.connect(self.clearWidget)

    def addText(self, param):
        line = self.line.text()
        self.line.setText(line + param)

    def operation(self, param):
        self.num1 = self.line.text()
        self.line.setText("")
        self.op = param

    def result(self):
        self.num2 = self.line.text()
        if self.op == "+":
            self.line.setText(str(int(self.num1) + int(self.num2)))
        if self.op == "-":
            self.line.setText(str(int(self.num1) - int(self.num2)))
        if self.op == "*":
            self.line.setText(str(int(self.num1) * int(self.num2)))
        if self.op == "/":
            if int(self.num2) == 0:
                self.line.setText(str("На ноль делить нельзя."))
            else:
                self.line.setText(str(int(self.num1) / int(self.num2)))
    def clearWidget(self):
        self.line.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec_())
