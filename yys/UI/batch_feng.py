# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'batch_feng.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(490, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_mod = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_mod.setGeometry(QtCore.QRect(30, 10, 111, 22))
        self.comboBox_mod.setObjectName("comboBox_mod")
        self.comboBox_mod.addItem("")
        self.comboBox_mod.addItem("")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(290, 10, 75, 23))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 10, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 40, 431, 511))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 10, 61, 20))
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(2)
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 490, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox_mod.currentTextChanged['QString'].connect(MainWindow.setmod)
        self.pushButton_1.clicked.connect(MainWindow.start)
        self.pushButton_2.clicked.connect(MainWindow.stop)
        self.lineEdit.textChanged['QString'].connect(MainWindow.settimes)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "批量逢魔"))
        self.comboBox_mod.setItemText(0, _translate("MainWindow", "登录最后一个"))
        self.comboBox_mod.setItemText(1, _translate("MainWindow", "登录下一个"))
        self.pushButton_1.setText(_translate("MainWindow", "启动"))
        self.pushButton_2.setText(_translate("MainWindow", "停止"))

