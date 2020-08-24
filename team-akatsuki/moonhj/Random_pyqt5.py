# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\test2\Random.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_RanDom():
    def setupUi(self, RanDom):
        RanDom.setObjectName("RanDom")
        RanDom.resize(475, 600)

        self.centralwidget = QtWidgets.QWidget(RanDom)
        self.centralwidget.setObjectName("centralwidget")

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 10, 461, 91))
        self.title.setObjectName("title")

        self.select = QtWidgets.QLabel(self.centralwidget)
        self.select.setGeometry(QtCore.QRect(10, 110, 461, 71))
        self.select.setObjectName("select")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(120, 190, 241, 371))
        self.widget.setObjectName("widget")

        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)

        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 4, 0, 1, 1)

        RanDom.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RanDom)
        self.statusbar.setObjectName("statusbar")
        RanDom.setStatusBar(self.statusbar)

        self.retranslateUi(RanDom)
        QtCore.QMetaObject.connectSlotsByName(RanDom)

    def retranslateUi(self, RanDom):
        _translate = QtCore.QCoreApplication.translate
        RanDom.setWindowTitle(_translate("RanDom", "랜덤점심뽑기"))
        self.title.setText(_translate("RanDom", "<html><head/><body><p align=\"center\"><span style=\" "
                                                "font-size:14pt; font-weight:600; font-style:italic;\""
                                                ">Random</span></p><p align=\"center\"><span style=\" "
                                                "font-size:20pt; font-weight:600;\">오늘 점심 뭐 먹지?!</span></p></body></html>"))

        self.select.setText(_translate("RanDom", "<html><head/><body><p align=\"center\""
                                                 ">아래에 메뉴 중 하나를 선택 해 주세요</p></body></html>"))
        self.pushButton.setText(_translate("RanDom", "한식"))
        self.pushButton_2.setText(_translate("RanDom", "중식"))
        self.pushButton_3.setText(_translate("RanDom", "일식"))
        self.pushButton_4.setText(_translate("RanDom", "양식"))
        self.pushButton_5.setText(_translate("RanDom", "분식"))


    # def closeEvent(self, QCloseEvent):
    #     ans = QMessageBox.question(self, "EXIT", "종료하시겠습니까?",
    #                                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    #     if ans == QMessageBox.Yes:
    #         QCloseEvent.accept()
    #     else:
    #         QCloseEvent.ignore()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RanDom = QtWidgets.QMainWindow()
    ui = Ui_RanDom()
    ui.setupUi(RanDom)
    RanDom.show()
    sys.exit(app.exec_())
