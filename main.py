# -*- coding: utf-8 -*-
import math

# Form implementation generated from reading ui file 'calcl.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from math import sqrt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 0, 419, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"background-color: rgba(0, 0, 0, 38);")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(0, 320, 150, 90))
        self.btn_0.setStyleSheet("background-color: rgb(119, 118, 123);")
        self.btn_0.setObjectName("btn_0")
        self.btn_ravno = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ravno.setGeometry(QtCore.QRect(150, 320, 150, 90))
        self.btn_ravno.setStyleSheet("background-color: rgb(119, 118, 123);")
        self.btn_ravno.setObjectName("btn_ravno")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 250, 100, 70))
        self.btn_1.setStyleSheet("background-color: rgb(119, 118, 123);")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(100, 250, 100, 70))
        self.btn_2.setStyleSheet("background-color: rgb(119, 118, 123);")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(200, 250, 100, 70))
        self.btn_3.setStyleSheet("background-color: rgb(119, 118, 123);")
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 180, 100, 70))
        self.btn_4.setStyleSheet("background-color: rgb(119, 118, 123);")
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(100, 180, 100, 70))
        self.btn_5.setStyleSheet("background-color: rgb(119, 118, 123);")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(200, 180, 100, 70))
        self.btn_6.setStyleSheet("background-color: rgb(119, 118, 123);")
        self.btn_6.setObjectName("btn_6")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 110, 100, 70))
        self.btn_7.setStyleSheet("background-color: rgb(119, 118, 123);")
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(100, 110, 100, 70))
        self.btn_8.setStyleSheet("background-color: rgb(119, 118, 123);")
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(200, 110, 100, 70))
        self.btn_9.setStyleSheet("background-color: rgb(119, 118, 123);")
        self.btn_9.setObjectName("btn_9")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(0, 50, 61, 61))
        self.btn_plus.setStyleSheet("background-color: rgb(119, 118, 123);")
        self.btn_plus.setObjectName("btn_plus")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(60, 50, 61, 61))
        self.btn_minus.setStyleSheet("background-color: rgb(119, 118, 123);")
        self.btn_minus.setObjectName("btn_minus")
        self.btn_multi = QtWidgets.QPushButton(self.centralwidget)
        self.btn_multi.setGeometry(QtCore.QRect(120, 50, 61, 61))
        self.btn_multi.setStyleSheet("background-color: rgb(119, 118, 123);")
        self.btn_multi.setObjectName("btn_multi")
        self.btn_delenie = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delenie.setGeometry(QtCore.QRect(180, 50, 61, 61))
        self.btn_delenie.setStyleSheet("background-color: rgb(119, 118, 123);")
        self.btn_delenie.setObjectName("btn_delenie")
        self.btn_bs = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bs.setGeometry(QtCore.QRect(300, 50, 121, 180))
        self.btn_bs.setStyleSheet("background-color: rgb(119, 118, 123);\n"
"background-color: rgb(224, 27, 36);")
        self.btn_bs.setObjectName("btn_bs")
        self.btn_C = QtWidgets.QPushButton(self.centralwidget)
        self.btn_C.setGeometry(QtCore.QRect(300, 220, 121, 180))
        self.btn_C.setStyleSheet("background-color: rgb(255, 120, 0);")
        self.btn_C.setObjectName("btn_C")
        self.btn_stepen = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stepen.setGeometry(QtCore.QRect(240, 50, 61, 61))
        self.btn_stepen.setStyleSheet("background-color: rgb(119, 118, 123);")
        self.btn_stepen.setObjectName("btn_stepen")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_func()

        self.is_equal = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.label.setText(_translate("MainWindow", "0"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_ravno.setText(_translate("MainWindow", "="))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_multi.setText(_translate("MainWindow", "*"))
        self.btn_delenie.setText(_translate("MainWindow", "/"))
        self.btn_bs.setText(_translate("MainWindow", "⌫"))
        self.btn_C.setText(_translate('MainWindow', 'C'))
        self.btn_stepen.setText(_translate('MainWindow', '**'))

    def add_func(self):
        self.btn_0.clicked.connect(lambda: self.write_number(self.btn_0.text()))
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.btn_plus.clicked.connect(lambda: self.write_number(self.btn_plus.text()))
        self.btn_minus.clicked.connect(lambda: self.write_number(self.btn_minus.text()))
        self.btn_delenie.clicked.connect(lambda: self.write_number(self.btn_delenie.text()))
        self.btn_multi.clicked.connect(lambda: self.write_number(self.btn_multi.text()))

        self.btn_stepen.clicked.connect(lambda: self.write_number(self.btn_stepen.text()))

        self.btn_bs.clicked.connect(self.clear_one_symbol)
        self.btn_C.clicked.connect(self.clear)

        self.btn_ravno.clicked.connect(self.result)

    def write_number(self, number):
        if self.label.text() == '0' or self.is_equal and number not in '+-%**/':
            self.label.setText(number)
            self.is_equal = False
        else:
            self.label.setText(self.label.text() + number)

    def result(self):
        res = eval(self.label.text())
        self.label.setText(str(res))
        self.is_equal = True
        

    def clear_one_symbol(self):
        cl = self.label.text()[0:len(self.label.text())-1]
        self.label.setText(cl)

    def clear(self):
        self.label.setText('0')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
