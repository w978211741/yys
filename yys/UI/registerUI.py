# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registerUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(531, 354)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(410, 300, 91, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit_register = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_register.setGeometry(QtCore.QRect(140, 230, 181, 21))
        self.lineEdit_register.setObjectName("lineEdit_register")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 481, 111))
        self.label.setObjectName("label")
        self.label_serial = QtWidgets.QLabel(Dialog)
        self.label_serial.setGeometry(QtCore.QRect(140, 200, 181, 16))
        self.label_serial.setObjectName("label_serial")
        self.pushButtoncopy = QtWidgets.QPushButton(Dialog)
        self.pushButtoncopy.setGeometry(QtCore.QRect(340, 190, 111, 28))
        self.pushButtoncopy.setObjectName("pushButtoncopy")
        self.pushButton_registe = QtWidgets.QPushButton(Dialog)
        self.pushButton_registe.setGeometry(QtCore.QRect(340, 230, 111, 28))
        self.pushButton_registe.setObjectName("pushButton_registe")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 200, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 230, 51, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        self.pushButton_registe.clicked.connect(Dialog.registe)
        self.pushButtoncopy.clicked.connect(Dialog.cptoClipboard)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "注册"))
        self.label.setText(_translate("Dialog", "提示语"))
        self.label_serial.setText(_translate("Dialog", "序列号"))
        self.pushButtoncopy.setText(_translate("Dialog", "复制到剪贴板"))
        self.pushButton_registe.setText(_translate("Dialog", "注册"))
        self.label_2.setText(_translate("Dialog", "序列号："))
        self.label_3.setText(_translate("Dialog", "注册码："))

