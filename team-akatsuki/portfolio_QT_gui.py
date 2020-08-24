import sys
from PyQt5.QtWidgets \
    import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('한식', self)
        #btn1.resize(70, 70)

        btn2 = QPushButton('일식',self)
        #btn2.resize(70, 70)

        btn3 = QPushButton('중식',self)
        #btn3.resize(70, 70)

        btn4 = QPushButton('양식',self)
        #btn4.resize(70, 70)

        btn5 = QPushButton('분식',self)
        #btn5.resize(70,70)



        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        vbox.addWidget(btn5)


        self.setLayout(vbox)
        self.setWindowTitle('Random 점심 뽑기')
        self.setGeometry(750, 300, 400, 500)
        self.show()



    def closeEvent(self,QCloseEvent):
        ans = QMessageBox.question(self, "EXIT", "종료하시겠습니까?",
                                   QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
        if ans == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
