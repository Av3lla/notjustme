import os
import sys
import random

from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtTest

import pandas as pd
import datetime


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
    
form = resource_path('notjustme.ui')
form_class = uic.loadUiType(form)[0]

form2 = resource_path('notjustme_result.ui')
form_class2 = uic.loadUiType(form2)[0]

form3 = resource_path('notjustme_option.ui')
form_class3 = uic.loadUiType(form3)[0]


#variables
numdict_102 = {1: '강민재', 2: '강승주', 3: '권일훈', 4: '김동혁', 5: '김현준', 6: '민지환', 7: '박건우', 8: '박시준', 9: '송성제', 10: '송종우', 11: '용승환', 12: '유현준', 13: '이시훈', 14: '이정현', 15: '이지원', 16: '이창현', 17: '임태호', 18: '정세윤', 19: '조정민', 20: '지관우', 21: '하재명'}
randomnums = []
randomnames = []
strrandnums = ''
strrandnames = ''
totalnum = 0
want = 0
i = 0
skip = 0


#define
#random numbers
def randnum(totalnum, want):
    global i, randomnums, randomnames, strrandnums, strrandnames

    randomnums = []
    randomnames = []
    strrandnums = ''
    strrandnames = ''
    i = 0

    while i < want:
        temprandnum = random.randint(1, totalnum)
        
        if temprandnum not in randomnums:
            randomnums.append(temprandnum)
            i += 1
        else:
            continue

    for i in range(len(randomnums)):
        randomnames.append(numdict_102[randomnums[i]])
    
    for i in range(len(randomnums)):
        if randomnums[i] > 2:
            randomnums[i] += 1

    strrandnums = '| ' + ' | '.join(list(map(str, randomnums))) + ' |'
    strrandnames = ', '.join(randomnames)
    print(randomnums, randomnames)
    print(strrandnums, strrandnames)

#timer
def timer(self, n):
    QtTest.QTest.qWait(n*1000)

#save histories
def savehistory(self):
    data = pd.read_csv("./cleaning_history.csv")
    print(data)


#main window
class mainWindow(QMainWindow, form_class):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.initUI()
        self.lineeditTextFunction()

        self.line_totalnum.textChanged.connect(self.lineeditTextFunction)   #line_totalnum에 문자열을 입력했을 때 동작할 함수 연결
        self.line_want.textChanged.connect(self.lineeditTextFunction)       #line_want에 문자열을 입력했을 때 동작할 함수 연결
        self.button_ok.clicked.connect(self.button_pressed_ok)                      #button_ok를 눌렀을 때 동작할 함수 연결
        self.button_ok.clicked.connect(resultWindow.loadresults)
        self.button_option.clicked.connect(self.button_pressed_option)
        self.button_option.clicked.connect(optionWindow.buttonbox)
        self.checkBox_skip.stateChanged.connect(self.skipcheck)
        

    def initUI(self):
        self.setupUi(self)
        self.setGeometry(0, 0, 960, 540)
        self.setFixedSize(960, 540)

        flags = self.windowFlags()
        flags |= Qt.CustomizeWindowHint
        flags |= Qt.WindowTitleHint
        flags |= Qt.WindowSystemMenuHint
        flags |= Qt.WindowCloseButtonHint
        flags |= Qt.WindowStaysOnTopHint
        flags |= Qt.WindowMaximizeButtonHint
        self.setWindowFlags(flags)


    #line_totalocunt, line_wantcount에 입력된 문자열을 label_totalcount, label_wantcount에 표시
    def lineeditTextFunction(self) :
        self.label_totalcount.setText(f"{self.line_totalnum.text()}명 중 {self.line_want.text()}명을 무작위로 정합니다.")


    #resultWindow를 여는 함수.
    def openresultwindow(self):
        widget.addWidget(resultWindow)
        widget.setCurrentIndex(2)

    def openoptionwindow(self):
        widget.addWidget(optionWindow)
        widget.setCurrentIndex(2)

    #button_ok를 눌렀을 때.
    def button_pressed_ok(self):
        global totalnum, want

        mainWindow.button_ok.setEnabled(False)

        totalnum = int(self.line_totalnum.text())
        want = int(self.line_want.text())

        timer(self, 0.5)

        self.openresultwindow()

        mainWindow.button_ok.setEnabled(True)
    

    def button_pressed_option(self):
        mainWindow.button_option.setEnabled(False)

        self.openoptionwindow()

        mainWindow.button_option.setEnabled(True)


    def skipcheck(self):
        global skip

        if self.checkBox_skip.isChecked():
            skip = 1
            print("skip true")
        else:
            skip = 0
            print("skip false")


class resultWindow(QDialog, form_class2):
    def __init__(self):
        super(resultWindow, self).__init__()
        self.initUI()
        

    def initUI(self):
        self.setupUi(self)
        self.setGeometry(0, 0, 960, 540)
        self.setFixedSize(960, 540)

        flags = self.windowFlags()
        flags |= Qt.CustomizeWindowHint
        flags |= Qt.WindowTitleHint
        flags |= Qt.WindowSystemMenuHint
        flags |= Qt.WindowCloseButtonHint
        flags |= Qt.WindowStaysOnTopHint
        flags |= Qt.WindowMaximizeButtonHint
        self.setWindowFlags(flags)


    #mainWindow를 여는 함수.
    def backtomainwindow(self):
        widget.setCurrentIndex(0)


    def loadresults(self):
        global skip

        def clear():
            label_result_number.hide()
            label_result_name.hide()
            button_backtomain.hide()

        print(totalnum, want)
        randnum(totalnum, want)
        timer(self, 1)

        label_result_number = QLabel(resultWindow)
        label_result_number.setObjectName("label_result_number")
        label_result_number.setGeometry(20, 190, 911, 101)
        label_result_number.setFont(QFont('나눔고딕 ExtraBold', 66))
        label_result_number.setAlignment(Qt.AlignCenter)
        label_result_number.show()

        for i in range(1500):
            temprandom = '| ' + ' | '.join(list(map(str, random.sample(range(1, totalnum), want)))) + ' |'
            label_result_number.setText(temprandom)

            if skip == 0:
                if i == 1500:
                    timer(self, i*0.001)
                elif i == 1499:
                    timer(self, i*0.00075)
                elif i == 1498:
                    timer(self, i*0.0005)
                elif i >= 1497:
                    timer(self, i*0.00025)
                elif i >= 1495:
                    timer(self, i*0.0001)
                elif i >= 1490:
                    timer(self, i*0.000075)
                elif i >= 1485:
                    timer(self, i*0.00005)
                elif i >= 1480:
                    timer(self, i*0.000025)
                elif i >= 1475:
                    timer(self, i*0.00001)
                else:
                    timer(self, 0.001)
            elif skip == 1:
                break;

        label_result_number.setText(strrandnums)

        timer(self, 1.5)

        label_result_name = QLabel(resultWindow)
        label_result_name.setObjectName("label_result_number")
        label_result_name.setGeometry(80, 330, 791, 51)
        label_result_name.setFont(QFont('나눔고딕', 36))
        label_result_name.setAlignment(Qt.AlignCenter)
        label_result_name.show()
        label_result_name.setText(strrandnames)

        timer(self, 1.25)

        button_backtomain = QPushButton(resultWindow)
        button_backtomain.setObjectName("button_backtomain")
        button_backtomain.setGeometry(780, 420, 141, 71)
        button_backtomain.setFont(QFont('나눔고딕', 12))
        button_backtomain.setText("Back")
        button_backtomain.show()
        button_backtomain.clicked.connect(lambda: clear())
        button_backtomain.clicked.connect(resultWindow.backtomainwindow)


class optionWindow(QDialog, form_class3):
    def __init__(self):
        super(optionWindow, self).__init__()
        self.initUI()


    def buttonbox(self):
        buttonBox_option = QDialogButtonBox(optionWindow)
        buttonBox_option.addButton(okButton, QDialogButtonBox.AcceptRole)
        buttonBox_option.addButton(cancelButton, QDialogButtonBox.RejectRole)
        okButton.setDefault(True)
        buttonBox_option.setObjectName("buttonBox_option")
        buttonBox_option.setGeometry(755, 470, 161, 31)
        buttonBox_option.setFont(QFont('나눔고딕', 12))
        buttonBox_option.accepted.connect(self.backtomainwindow)
        buttonBox_option.rejected.connect(self.backtomainwindow)


    def initUI(self):
        self.setupUi(self)
        self.setGeometry(0, 0, 960, 540)
        self.setFixedSize(960, 540)

        flags = self.windowFlags()
        flags |= Qt.CustomizeWindowHint
        flags |= Qt.WindowTitleHint
        flags |= Qt.WindowSystemMenuHint
        flags |= Qt.WindowCloseButtonHint
        flags |= Qt.WindowStaysOnTopHint
        flags |= Qt.WindowMaximizeButtonHint
        self.setWindowFlags(flags)


    #mainWindow를 여는 함수.
    def backtomainwindow(self):
        widget.setCurrentIndex(2)


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    mainWindow = mainWindow()
    resultWindow = resultWindow()
    optionWindow = optionWindow()
    widget.addWidget(mainWindow)
    widget.addWidget(resultWindow)
    widget.addWidget(optionWindow)
    widget.setFixedSize(960, 540)
    widget.show()
    app.exec_()