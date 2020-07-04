from batch_feng import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from Cwindow import Window
import multiprocessing
from multiprocessing import Queue
from Cfuben import Fuben
from CsendQQ import SendQQ
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QWindow
import traceback
from win32process import CreateProcess
from PyQt5.QtWidgets import QWidget
from Chandle import Handle
from registerWindow import My_registerWindow
import codedef
from Cregister import register
from Cmouse import Mouse
import time


class mainwindeng(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(mainwindeng, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint |
                            QtCore.Qt.WindowMinimizeButtonHint)
        # self.setFixedSize(self.width(), self.height())
        # self.radioButton_1.setChecked(True)
        # self.comboBox_1.setEnabled(False)
        # self.comboBox_2.setEnabled(False)
        # self.comboBox_3.setEnabled(False)
        # self.comboBox_4.setEnabled(False)
        # self.lineEdit_times.setEnabled(True)
        self.lineEdit.setPlaceholderText("次数")
        # self.lineEdit_qqname.setEnabled(True)
        # self.lineEdit_qqname.setPlaceholderText("qq昵称或备注")
        # self.comboBox_jienum.setEnabled(False)
        # self.comboBox_xuenum.setEnabled(False)

        # 设置最大行数
        self.textBrowser.document().setMaximumBlockCount(32)
        self.log_queue = Queue()
        self.main_process = None
        # self.mod = codedef.MOD_SET
        self.str_log = ""
        self.bool_run = False
        self.timer = QTimer()  # 初始化一个定时器
        self.timer.timeout.connect(self.show_log)  # 计时结束调用operate()方法
        self.timer.start(300)
        # self.timer11 = QTimer()  # 初始化一个定时器
        # self.timer11.timeout.connect(self.dian_guai_11)  # 计时结束调用operate()方法
        # self.timer11.start(30000)
        # self.qq_name = ''
        self.Maxtimes = ''
        # self.UP = codedef.UP_C_NULL
        # self.BOSS = True
        # # self.register_show = False
        self.register_show = True
        # self.QingMax = True
        # self.Beater = True
        # self.BeatMax = True
        # self.Loop = False
        # self.other = '抽N卡'     # 其他功能
        # self.Chapter = '第一章'
        self.initwin = False
        self.mod = 0
        pass

    def setmod(self, text):
        if text == "登录最后一个":
            self.mod = 0
        else:
            self.mod = 1

    def initwindow(self):
        fuben = Fuben(self.log_queue, "")
        try:
            fuben.set_windows('1')
        except Exception as e:
            str_log = "Exception:" + traceback.format_exc() + "\r\n"
            fuben.add_log(str_log)
            print(str_log)
        fuben.add_log("初始化窗口 结束\r\n")

    def start(self):
        try:
            # my_register = register()
            # re = my_register.check()
            # # print('check1:' + str(re))
            # if re == 0:
            #     if self.register_show is False:
            #         self.register_show = True
            #         my_registerWindow = My_registerWindow(my_register)
            #         my_registerWindow.show()
            #         my_registerWindow.exec_()
            # else:
            #     my_registerWindow = My_registerWindow(my_register)
            #     my_registerWindow.show()
            #     my_registerWindow.exec_()
            #     re = my_register.check()
            #     # print('check2:' + str(re))
            #     if re != 0:
            #         return 0
            #     else:
            #         self.register_show = True

            self.add_in_text_browser("正在启动\r\n")
            self.bool_run = True

            self.add_in_text_browser("启动\r\n")

            strMaxtimes = self.Maxtimes
            iMaxtimes = 10
            if strMaxtimes.isdigit() is False:
                self.add_in_text_browser("次数不为数字，启动次数10\r\n")
            else:
                iMaxtimes = int(strMaxtimes)
            if self.main_process is None or self.main_process.is_alive() is False:
                self.main_process = multiprocessing.Process(
                    target=my_xue_yue_process, args=(
                        self.log_queue, "", "1", "1",
                        "1", "1", 1, iMaxtimes, codedef.FENG_MO, self.mod),
                    name='my_process')
                self.main_process.start()
            else:
                self.add_in_text_browser("已经有副本正在运行，请先按停止\r\n")
            pass

        except Exception as e:
            self.add_in_text_browser("Exception:" + traceback.format_exc() + "\r\n")
        return 0

    def settimes(self):
        self.Maxtimes = self.lineEdit.text()
        if self.Maxtimes.isdigit() is False:
            self.add_in_text_browser("次数不全为数字，次数设置失败\r\n")
            self.lineEdit_times.setText('')
        else:
            self.add_in_text_browser("次数设置成功\r\n")
        return 0

    def stop(self):
        self.add_in_text_browser("正在停止。。。\r\n")
        if self.main_process is None:
            self.add_in_text_browser("未启动\r\n")
            return 0
        if self.main_process is None or self.main_process.is_alive():
            self.main_process.terminate()
            self.add_in_text_browser("已停止\r\n")
        else:
            self.add_in_text_browser("未启动\r\n")
        return 0

    def add_in_text_browser(self, log):
        alllog = self.textBrowser.toPlainText() + log
        self.textBrowser.setText(alllog)
        return 0

    def show_log(self):
        if self.initwin is False:
            self.initwin = True
            self.initwindow()
        #self.add_in_text_browser("..")
        try:
            self.add_in_text_browser(self.log_queue.get(timeout=0.1))
        except Exception as e:
            pass
            #self.add_in_text_browser("log_queue Exception:" + traceback.format_exc())
        #self.add_in_text_browser("\r\n")
        return 0

    def dian_guai_11(self):
        yys1 = self.comboBox_1.currentText()
        yys_handle = Handle()
        self.add_in_text_browser("点主怪\r\n")
        if Window.get_window(yys_handle, None, "[#] [yys" + yys1 + "] 阴阳师-网易游戏 [#]") == codedef.NORMAL_END:
            x = int((yys_handle.right + yys_handle.left) / 2)
            xishu = 0.2
            y = int((yys_handle.top + (yys_handle.bottom - yys_handle.top) * xishu))
            m = Mouse()
            m.click(x, y)

    def set_yys_wins(self, inum):
        self.comboBox_1.setEnabled(False)
        self.comboBox_2.setEnabled(False)
        self.comboBox_3.setEnabled(False)
        self.comboBox_4.setEnabled(False)
        if inum == 1:
            self.comboBox_1.setEnabled(True)
        elif inum == 2:
            self.comboBox_1.setEnabled(True)
            self.comboBox_2.setEnabled(True)
        elif inum == 3:
            self.comboBox_1.setEnabled(True)
            self.comboBox_2.setEnabled(True)
            self.comboBox_3.setEnabled(True)
        elif inum == 4:
            self.comboBox_1.setEnabled(True)
            self.comboBox_2.setEnabled(True)
            self.comboBox_3.setEnabled(True)
            self.comboBox_4.setEnabled(True)
        return 0


def my_xue_yue_process(log_queue, qq_name, yys1, yys2, yys3, yys4, inum, imax_times, mod, fengmod):
    fuben = Fuben(log_queue, qq_name)
    try:
        fuben.xue_yue(yys1, yys2, yys3, yys4, inum, imax_times, mod, fengmod=fengmod)
    except Exception as e:

        str_log = "Exception:" + traceback.format_exc() + "\r\n"
        fuben.add_log(str_log)
    fuben.add_log("结束\r\n")

