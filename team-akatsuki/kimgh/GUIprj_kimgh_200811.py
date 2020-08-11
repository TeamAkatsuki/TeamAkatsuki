import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Dicers_main(QWidget):

    def __init__(self):
        super().__init__()
        self.main()
        self.show()

    def main(self):
        # 프레임
        self.setWindowTitle('D   I   C   E   R   S')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(700, 500)
        # 로고
        main_logo = QPixmap('main.png')
        logo_img = QLabel()
        logo_img.setPixmap(main_logo)
        # 이름
        inputname = QLineEdit('이름을 입력하세요',self)
        # 입장
        gobtn = QPushButton('입장',self)
        gobtn.setIcon(QIcon('icon.png'))
        # gobtn.clicked.connect(QCoreApplication.)
        # 도움말
        hebtn = QPushButton('도움말',self)
        hebtn.setIcon(QIcon('icon.png'))
        # 종료
        qbtn = QPushButton('종료', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        # 반복 배열
        def main_array(pi):
            a = QHBoxLayout()
            a.addStretch(1)
            a.addWidget(pi)
            a.addStretch(1)
            return a
        #
        btnlist = [logo_img, inputname, gobtn, hebtn, qbtn]
        #
        v = QVBoxLayout()
        v.addStretch(5)
        for i in btnlist:
            v.addLayout(main_array(i))
            v.addStretch(1)
        self.setLayout(v)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = Dicers_main()
    sys.exit(app.exec_())
