import sys
from random import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui

class QtGUI(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("당신은 당첨이 될 것인가!?")
        self.resize(320, 250)
        self.intialL1 = '--------------당첨 번호--------------'
        self.intialL2 = '[1등 당첨번호], [2등 당첨번호]'

        label1 = QLabel(self.intialL1, self)
        label1.move(50,10)
        label1.resize(380, 100)

        label2 = QLabel(self.intialL2, self)
        label2.move(40, 50)
        label2.resize(380, 100)

        button = QPushButton('당첨번호 확인', self)
        button.move(10, 130)
        button.resize(300,100)
        button.clicked.connect(lambda: self.print_label(label2))

        self.show()

    def Make_Number(self):
        Number = []
        while len(Number) < 6:
            v = randint(1, 100)
            if v not in Number :
                Number.append(v)
        return Number

    def print_label(self,label):
        Number = self.Make_Number()
        text = f'1등 번호: [{Number[0]}], 2등 번호: {Number[1:]}'
        Number.sort()
        label.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QtGUI()
    app.exec_()
