# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yysUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(341, 851)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 430, 181, 421))
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 360, 191, 61))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton_1 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 10, 81, 41))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 10, 81, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 240, 191, 51))
        self.groupBox_2.setObjectName("groupBox_2")
        self.comboBox_1 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_1.setGeometry(QtCore.QRect(10, 20, 41, 22))
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setGeometry(QtCore.QRect(50, 20, 41, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_3.setGeometry(QtCore.QRect(90, 20, 41, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_4.setGeometry(QtCore.QRect(130, 20, 41, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 300, 191, 61))
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit_times = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_times.setGeometry(QtCore.QRect(10, 20, 71, 31))
        self.lineEdit_times.setMaxLength(4)
        self.lineEdit_times.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_times.setObjectName("lineEdit_times")
        self.lineEdit_qqname = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_qqname.setGeometry(QtCore.QRect(100, 20, 81, 31))
        self.lineEdit_qqname.setMaxLength(10)
        self.lineEdit_qqname.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_qqname.setObjectName("lineEdit_qqname")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 10, 311, 221))
        self.groupBox_5.setObjectName("groupBox_5")
        self.comboBox_jienum = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_jienum.setGeometry(QtCore.QRect(140, 50, 41, 22))
        self.comboBox_jienum.setEditable(False)
        self.comboBox_jienum.setObjectName("comboBox_jienum")
        self.comboBox_jienum.addItem("")
        self.comboBox_jienum.addItem("")
        self.comboBox_jienum.addItem("")
        self.comboBox_jienum.addItem("")
        self.comboBox_xuenum = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_xuenum.setGeometry(QtCore.QRect(140, 80, 41, 22))
        self.comboBox_xuenum.setObjectName("comboBox_xuenum")
        self.comboBox_xuenum.addItem("")
        self.comboBox_xuenum.addItem("")
        self.comboBox_xuenum.addItem("")
        self.comboBox_xuenum.addItem("")
        self.comboBox_UP = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_UP.setGeometry(QtCore.QRect(220, 10, 61, 22))
        self.comboBox_UP.setEditable(False)
        self.comboBox_UP.setObjectName("comboBox_UP")
        self.comboBox_UP.addItem("")
        self.comboBox_UP.addItem("")
        self.comboBox_UP.addItem("")
        self.comboBox_UP.addItem("")
        self.comboBox_BOSS = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_BOSS.setGeometry(QtCore.QRect(200, 40, 101, 22))
        self.comboBox_BOSS.setEditable(False)
        self.comboBox_BOSS.setObjectName("comboBox_BOSS")
        self.comboBox_BOSS.addItem("")
        self.comboBox_BOSS.addItem("")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_6.setGeometry(QtCore.QRect(30, 190, 61, 19))
        self.radioButton_6.setObjectName("radioButton_6")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_6)
        self.comboBox_dounum = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_dounum.setGeometry(QtCore.QRect(140, 190, 41, 22))
        self.comboBox_dounum.setObjectName("comboBox_dounum")
        self.comboBox_dounum.addItem("")
        self.comboBox_dounum.addItem("")
        self.comboBox_dounum.addItem("")
        self.comboBox_dounum.addItem("")
        self.comboBox_qingmax = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_qingmax.setGeometry(QtCore.QRect(200, 70, 101, 22))
        self.comboBox_qingmax.setObjectName("comboBox_qingmax")
        self.comboBox_qingmax.addItem("")
        self.comboBox_qingmax.addItem("")
        self.comboBox_beater = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_beater.setGeometry(QtCore.QRect(200, 100, 101, 22))
        self.comboBox_beater.setObjectName("comboBox_beater")
        self.comboBox_beater.addItem("")
        self.comboBox_beater.addItem("")
        self.comboBox_beatmax = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_beatmax.setGeometry(QtCore.QRect(200, 130, 101, 22))
        self.comboBox_beatmax.setObjectName("comboBox_beatmax")
        self.comboBox_beatmax.addItem("")
        self.comboBox_beatmax.addItem("")
        self.label = QtWidgets.QLabel(self.groupBox_5)
        self.label.setGeometry(QtCore.QRect(80, 140, 101, 20))
        self.label.setObjectName("label")
        self.comboBox_loop = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_loop.setGeometry(QtCore.QRect(200, 160, 101, 22))
        self.comboBox_loop.setObjectName("comboBox_loop")
        self.comboBox_loop.addItem("")
        self.comboBox_loop.addItem("")
        self.comboBox_chapter = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_chapter.setGeometry(QtCore.QRect(200, 190, 101, 22))
        self.comboBox_chapter.setObjectName("comboBox_chapter")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.comboBox_chapter.addItem("")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(30, 130, 91, 19))
        self.radioButton_4.setObjectName("radioButton_4")
        self.buttonGroup.addButton(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(30, 170, 115, 19))
        self.radioButton_5.setObjectName("radioButton_5")
        self.buttonGroup.addButton(self.radioButton_5)
        self.radioButton_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_1.setGeometry(QtCore.QRect(30, 30, 115, 19))
        self.radioButton_1.setObjectName("radioButton_1")
        self.buttonGroup.addButton(self.radioButton_1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 60, 61, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup.addButton(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 90, 91, 19))
        self.radioButton_3.setObjectName("radioButton_3")
        self.buttonGroup.addButton(self.radioButton_3)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(190, 240, 120, 80))
        self.groupBox.setObjectName("groupBox")
        self.comboBox_other = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_other.setGeometry(QtCore.QRect(10, 30, 101, 22))
        self.comboBox_other.setObjectName("comboBox_other")
        self.comboBox_other.addItem("")
        self.comboBox_other.addItem("")
        self.comboBox_other.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionsadf = QtWidgets.QAction(MainWindow)
        self.actionsadf.setCheckable(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/easyicon_net_512.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionsadf.setIcon(icon)
        self.actionsadf.setObjectName("actionsadf")

        self.retranslateUi(MainWindow)
        self.pushButton_1.clicked.connect(MainWindow.start)
        self.pushButton_2.clicked.connect(MainWindow.stop)
        self.comboBox_jienum.currentTextChanged['QString'].connect(MainWindow.setjienum)
        self.comboBox_xuenum.currentTextChanged['QString'].connect(MainWindow.setxuenum)
        self.lineEdit_times.editingFinished.connect(MainWindow.settimes)
        self.lineEdit_qqname.editingFinished.connect(MainWindow.setqqname)
        self.comboBox_UP.currentTextChanged['QString'].connect(MainWindow.setUP)
        self.buttonGroup.buttonClicked['int'].connect(MainWindow.setMod)
        self.comboBox_BOSS.currentTextChanged['QString'].connect(MainWindow.setBOSS)
        self.comboBox_dounum.currentTextChanged['QString'].connect(MainWindow.setdounum)
        self.comboBox_qingmax.currentTextChanged['QString'].connect(MainWindow.setQingMax)
        self.comboBox_beater.currentTextChanged['QString'].connect(MainWindow.setBeater)
        self.comboBox_beatmax.currentTextChanged['QString'].connect(MainWindow.setBeatMax)
        self.comboBox_loop.currentTextChanged['QString'].connect(MainWindow.setLoop)
        self.comboBox_other.currentTextChanged['QString'].connect(MainWindow.setOther)
        self.comboBox_chapter.currentTextChanged['QString'].connect(MainWindow.setChapter)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "痒痒鼠1.9.0"))
        self.pushButton_1.setText(_translate("MainWindow", "启动"))
        self.pushButton_2.setText(_translate("MainWindow", "停止"))
        self.groupBox_2.setTitle(_translate("MainWindow", "窗口参数 沙盒窗口名"))
        self.comboBox_1.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_1.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_1.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_1.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "4"))
        self.groupBox_3.setTitle(_translate("MainWindow", "副本参数"))
        self.groupBox_5.setTitle(_translate("MainWindow", "副本选择"))
        self.comboBox_jienum.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_jienum.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_jienum.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_jienum.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_xuenum.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_xuenum.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_xuenum.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_xuenum.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_UP.setItemText(0, _translate("MainWindow", "不挑"))
        self.comboBox_UP.setItemText(1, _translate("MainWindow", "金币"))
        self.comboBox_UP.setItemText(2, _translate("MainWindow", "经验"))
        self.comboBox_UP.setItemText(3, _translate("MainWindow", "奖励"))
        self.comboBox_BOSS.setItemText(0, _translate("MainWindow", "打BOSS"))
        self.comboBox_BOSS.setItemText(1, _translate("MainWindow", "不打BOSS"))
        self.radioButton_6.setText(_translate("MainWindow", "斗技"))
        self.comboBox_dounum.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_dounum.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_dounum.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_dounum.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_qingmax.setItemText(0, _translate("MainWindow", "晴明已满级"))
        self.comboBox_qingmax.setItemText(1, _translate("MainWindow", "晴明没满级"))
        self.comboBox_beater.setItemText(0, _translate("MainWindow", "队长打手"))
        self.comboBox_beater.setItemText(1, _translate("MainWindow", "队员打手"))
        self.comboBox_beatmax.setItemText(0, _translate("MainWindow", "打手满级"))
        self.comboBox_beatmax.setItemText(1, _translate("MainWindow", "打手没满级"))
        self.label.setText(_translate("MainWindow", "打手放清明右手边"))
        self.comboBox_loop.setItemText(0, _translate("MainWindow", "不交叉打"))
        self.comboBox_loop.setItemText(1, _translate("MainWindow", "交叉打结界"))
        self.comboBox_chapter.setItemText(0, _translate("MainWindow", "第一章"))
        self.comboBox_chapter.setItemText(1, _translate("MainWindow", "第二章"))
        self.comboBox_chapter.setItemText(2, _translate("MainWindow", "第三章"))
        self.comboBox_chapter.setItemText(3, _translate("MainWindow", "第四章"))
        self.comboBox_chapter.setItemText(4, _translate("MainWindow", "第五章"))
        self.comboBox_chapter.setItemText(5, _translate("MainWindow", "第六章"))
        self.comboBox_chapter.setItemText(6, _translate("MainWindow", "第七章"))
        self.comboBox_chapter.setItemText(7, _translate("MainWindow", "第八章"))
        self.comboBox_chapter.setItemText(8, _translate("MainWindow", "第九章"))
        self.comboBox_chapter.setItemText(9, _translate("MainWindow", "第十章"))
        self.comboBox_chapter.setItemText(10, _translate("MainWindow", "第十一章"))
        self.comboBox_chapter.setItemText(11, _translate("MainWindow", "第十二章"))
        self.comboBox_chapter.setItemText(12, _translate("MainWindow", "第十三章"))
        self.comboBox_chapter.setItemText(13, _translate("MainWindow", "第十四章"))
        self.comboBox_chapter.setItemText(14, _translate("MainWindow", "第十五章"))
        self.comboBox_chapter.setItemText(15, _translate("MainWindow", "第十六章"))
        self.comboBox_chapter.setItemText(16, _translate("MainWindow", "第十七章"))
        self.comboBox_chapter.setItemText(17, _translate("MainWindow", "第十八章"))
        self.comboBox_chapter.setItemText(18, _translate("MainWindow", "第十九章"))
        self.comboBox_chapter.setItemText(19, _translate("MainWindow", "第二十章"))
        self.comboBox_chapter.setItemText(20, _translate("MainWindow", "第二十一章"))
        self.comboBox_chapter.setItemText(21, _translate("MainWindow", "第二十二章"))
        self.comboBox_chapter.setItemText(22, _translate("MainWindow", "第二十三章"))
        self.comboBox_chapter.setItemText(23, _translate("MainWindow", "第二十四章"))
        self.comboBox_chapter.setItemText(24, _translate("MainWindow", "第二十五章"))
        self.comboBox_chapter.setItemText(25, _translate("MainWindow", "第二十六章"))
        self.comboBox_chapter.setItemText(26, _translate("MainWindow", "第二十七章"))
        self.comboBox_chapter.setItemText(27, _translate("MainWindow", "第二十八章"))
        self.radioButton_4.setText(_translate("MainWindow", "组队探索"))
        self.radioButton_5.setText(_translate("MainWindow", "组队御魂觉醒"))
        self.radioButton_1.setText(_translate("MainWindow", "设置窗口"))
        self.radioButton_2.setText(_translate("MainWindow", "结界"))
        self.radioButton_3.setText(_translate("MainWindow", "其他功能"))
        self.groupBox.setTitle(_translate("MainWindow", "其他功能"))
        self.comboBox_other.setItemText(0, _translate("MainWindow", "抽N卡"))
        self.comboBox_other.setItemText(1, _translate("MainWindow", "砸百鬼"))
        self.comboBox_other.setItemText(2, _translate("MainWindow", "血月"))
        self.actionsadf.setText(_translate("MainWindow", "sadf"))

import res_rc
