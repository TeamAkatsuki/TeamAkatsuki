import sys, random
from PyQt5.QtWidgets import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self): # 기본 인터페이스
        lcd = QLCDNumber(self)
        self.lcd = lcd
        dial = QDial(self)
        btn1 = QPushButton('당첨 확인', self)
        btn2 = QPushButton('종료', self)

        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        dial.valueChanged.connect(lcd.display)
        btn1.clicked.connect(self.result)
        btn2.clicked.connect(self.exit_bt)

        self.setWindowTitle('경품 당첨')
        self.setGeometry(700, 300, 400,450) # 창 위치 및 크기
        self.show()

    def result(self):   # 결과 확인
        text = '아쉽지만 다음기회에 ...'
        ran = random.sample(range(1, 101), 6) # 랜덤으로 6개 뽑음
        first = ran[0] # 자동차
        second = ran[1:] # 냉장고
        display_value = self.lcd.intValue()
        print(ran) # 당첨번호 확인

        if display_value == first:
            text = '축하합니다. 자동차에 당첨 되셨습니다 !!'
        elif display_value in second:
            text = '축하합니다. 냉장고에 당첨 되셨습니다 !!'

        QMessageBox.about(self, "과연, 결과는!?", text)

    def exit_bt(self):  # 종료 버튼
        sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())