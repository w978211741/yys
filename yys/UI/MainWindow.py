from yysUI import Ui_MainWindow
from PyQt5 import QtWidgets
from Cgame import Game, SceneKey
from Chandle import Handle
from yys.game.Cliaojiejie import Liaojiejie
from yys.game.Cteam_kun_25_captain import Team_kun_25_captain
from yys.game.Cteam_kun_25_teammate import Team_kun_25_teammate
from yys.game.Cpersonal_jiejie import Personal_jiejie
from yys.game.Cteam_hun_10 import Team_hun_10
import time
import multiprocessing
from multiprocessing import Queue
from Cfuben import Fuben
from PyQt5.QtCore import QTimer


class My_MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(My_MainWindow, self).__init__()
        self.setupUi(self)
        self.lineEdit_1.setInputMask("D")
        self.lineEdit_2.setInputMask("D")
        self.lineEdit_3.setInputMask("D")
        self.lineEdit_4.setInputMask("D")
        self.lineEdit_5.setInputMask("9999")
        self.lineEdit_6.setInputMask("9")
        self.lineEdit_7.setInputMask("9")
        self.lineEdit_8.setInputMask("9")
        self.lineEdit_1.setText("1")
        self.lineEdit_2.setText("2")
        self.lineEdit_3.setText("3")
        self.lineEdit_4.setText("4")
        self.lineEdit_5.setText("0000")
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")
        self.lineEdit_8.setText("")
        # 设置最大行数
        self.textBrowser.document().setMaximumBlockCount(30)
        self.log_queue = Queue()
        self.main_process = None
        self.mod = 0
        self.str_log = ""
        self.bool_run = False
        self.timer = QTimer()  # 初始化一个定时器
        self.timer.timeout.connect(self.show_log)  # 计时结束调用operate()方法
        self.timer.start(1000)
        pass

    def setMod(self, id):
        # 单选按钮组 -2  -  -7
        self.mod = id
        self.lineEdit_1.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_8.setEnabled(False)
        if self.mod == -2:# 设置窗口
            self.lineEdit_1.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
            self.lineEdit_4.setEnabled(True)
        elif self.mod == -3:# 打结界1
            self.lineEdit_1.setEnabled(True)
            pass
        elif self.mod == -4:# 打结界2
            self.lineEdit_1.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
        elif self.mod == -5:# 打结界3
            self.lineEdit_1.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
        elif self.mod == -6:# 打结界4
            self.lineEdit_1.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
            self.lineEdit_4.setEnabled(True)
        elif self.mod == -7:# 组队魂十
            self.lineEdit_1.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
        elif self.mod == -8:  # 刷血月
            self.lineEdit_1.setEnabled(True)

            self.lineEdit_5.setEnabled(True)
        elif self.mod == -9:  # 组队困25
            self.lineEdit_1.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
        elif self.mod == -10:  # 备用
            pass
        return 0

    def start(self):
        print("启动")
        self.str_log += "启动"
        self.bool_run = True
        try:
            if self.mod == -2:# 设置窗口
                if self.main_process.is_alive() == False:
                    self.main_process = multiprocessing.Process(
                        target=my_set_windows_process, args=(
                            self.log_queue, self.lineEdit_1.text(), self.lineEdit_2.text(),
                            self.lineEdit_3.text(), self.lineEdit_4.text(),), name='my_process')
                    self.main_process.start()
                else:
                    self.add_in_text_browser("已经有副本正在运行，请先按停止")
            elif self.mod == -3:# 打结界1
                if self.main_process.is_alive() is False:
                    self.main_process = multiprocessing.Process(
                        target=my_jie_jie1_process, args=(
                            self.log_queue, self.lineEdit_1.text(),), name='my_process')
                    self.main_process.start()
                else:
                    self.add_in_text_browser("已经有副本正在运行，请先按停止")
                pass
            elif self.mod == -4:# 打结界2
                if self.main_process.is_alive() is False:
                    self.main_process = multiprocessing.Process(
                        target=my_jie_jie2_process, args=(
                            self.log_queue, self.lineEdit_1.text(),self.lineEdit_2.text(),), name='my_process')
                    self.main_process.start()
                else:
                    self.add_in_text_browser("已经有副本正在运行，请先按停止")
                pass
            elif self.mod == -5:
                if self.main_process.is_alive() is False:
                    self.main_process = multiprocessing.Process(
                        target=my_jie_jie3_process, args=(
                            self.log_queue, self.lineEdit_1.text(), self.lineEdit_2.text(),
                            self.lineEdit_3.text(),), name='my_process')
                    self.main_process.start()
                else:
                    self.add_in_text_browser("已经有副本正在运行，请先按停止")
                pass
            elif self.mod == -6:
                if self.main_process.is_alive() is False:
                    self.main_process = multiprocessing.Process(
                        target=my_jie_jie4_process, args=(
                            self.log_queue, self.lineEdit_1.text(), self.lineEdit_2.text(),
                            self.lineEdit_3.text(),self.lineEdit_4.text(),), name='my_process')
                    self.main_process.start()
                else:
                    self.add_in_text_browser("已经有副本正在运行，请先按停止")
                pass
            elif self.mod == -7:
                if self.main_process.is_alive() is False:
                    self.main_process = multiprocessing.Process(
                        target=my_hun_shi_process, args=(
                            self.log_queue, self.lineEdit_1.text(), self.lineEdit_2.text(),), name='my_process')
                    self.main_process.start()
                else:
                    self.add_in_text_browser("已经有副本正在运行，请先按停止")
                pass
            elif self.mod == -8:
                if self.main_process.is_alive() is False:
                    self.main_process = multiprocessing.Process(
                        target=my_shua_xue_yue_process, args=(
                            self.log_queue, self.lineEdit_1.text(), self.lineEdit_5.text(),), name='my_process')
                    self.main_process.start()
                else:
                    self.add_in_text_browser("已经有副本正在运行，请先按停止")
                pass
            elif self.mod == -9:
                if self.main_process.is_alive() is False:
                    self.main_process = multiprocessing.Process(
                        target=my_jie_jie4_process, args=(
                            self.log_queue, self.lineEdit_1.text(), self.lineEdit_2.text(),
                            self.lineEdit_3.text(),self.lineEdit_4.text(),), name='my_process')
                    self.main_process.start()
                else:
                    self.add_in_text_browser("已经有副本正在运行，请先按停止")
                pass
            elif self.mod == -10:
                #self.hun_shi(self.lineEdit_1.text(), self.lineEdit_2.text())
                pass
        except Exception as e:
            print("Exception:" + e.__str__())

        return 0

    def stop(self):
        self.add_in_text_browser("正在停止。。。")

        if self.main_process.is_alive():
            self.main_process.terminate()
        self.add_in_text_browser("已停止")
        pass

    def add_in_text_browser(self, log):
        alllog = self.textBrowser.toPlainText() + log
        self.textBrowser.setText(alllog)
        return 0

    def show_log(self):
        print("show log")
        try:
            self.add_in_text_browser(self.log_queue.get(timeout=0.1))
        except Exception as e:
            print("log_queue Exception:" + e.__str__())
        pass


def my_set_windows_process(log_queue, yys1, yys2, yys3, yys4):
    try:
        fuben = Fuben(log_queue)
        fuben.set_windows(yys1)
        fuben.set_windows(yys2)
        fuben.set_windows(yys3)
        fuben.set_windows(yys4)
    except Exception as e:
        print("Exception:" + e.__str__())

def my_jie_jie1_process(log_queue, yys1):
    try:
        fuben = Fuben(log_queue)
        fuben.jie_jie1(yys1)
    except Exception as e:
        print("Exception:" + e.__str__())

def my_jie_jie2_process(log_queue, yys1, yy2):
    try:
        fuben = Fuben(log_queue)
        fuben.jie_jie2(yys1, yy2)
    except Exception as e:
        print("Exception:" + e.__str__())

def my_jie_jie3_process(log_queue, yys1, yy2, yy3):
    try:
        fuben = Fuben(log_queue)
        fuben.jie_jie3(yys1, yy2, yy3)
    except Exception as e:
        print("Exception:" + e.__str__())

def my_jie_jie4_process(log_queue, yys1, yy2, yy3, yy4):
    try:
        fuben = Fuben(log_queue)
        fuben.jie_jie4(yys1, yy2, yy3, yy4)
    except Exception as e:
        print("Exception:" + e.__str__())

def my_hun_shi_process(log_queue, yys1, yy2):
    try:
        fuben = Fuben(log_queue)
        fuben.hun_shi(yys1, yy2)
    except Exception as e:
        print("Exception:" + e.__str__())

def my_shua_xue_yue_process(log_queue, yys1, max_times):
    try:
        fuben = Fuben(log_queue)
        fuben.shua_xue_yue(yys1, max_times)
    except Exception as e:
        print("Exception:" + e.__str__())

def my_team_kun_25_process(log_queue, yys1, yy2):
    try:
        fuben = Fuben(log_queue)
        fuben.team_kun_25(yys1, yy2)
    except Exception as e:
        print("Exception:" + e.__str__())