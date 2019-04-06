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
        self.lineEdit_1.setText("1")
        self.lineEdit_2.setText("2")
        self.lineEdit_3.setText("3")
        self.lineEdit_4.setText("4")
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
        if self.mod == -2:
            self.lineEdit_1.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
            self.lineEdit_4.setEnabled(True)
        elif self.mod == -3:
            self.lineEdit_1.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_3.setEnabled(False)
            self.lineEdit_4.setEnabled(False)
            pass
        elif self.mod == -4:
            self.lineEdit_1.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
            self.lineEdit_4.setEnabled(False)
        elif self.mod == -5:
            self.lineEdit_1.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_3.setEnabled(False)
            self.lineEdit_4.setEnabled(False)
        elif self.mod == -6:
            self.lineEdit_1.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
            self.lineEdit_4.setEnabled(True)
        elif self.mod == -7:
            self.lineEdit_1.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_3.setEnabled(False)
            self.lineEdit_4.setEnabled(False)
        return 0



    def start(self):
        print("启动")
        self.str_log += "启动"
        self.bool_run = True
        # 设置窗口
        try:
            if self.mod == -2:
                self.main_process = multiprocessing.Process(target=my_process, args=(self.log_queue, self.lineEdit_1.text(),), name='my_process')
                self.main_process.start()

                print("mod == -2")
                #self.set_windows(self.lineEdit_1.text())
                #self.set_windows(self.lineEdit_2.text())
                #self.set_windows(self.lineEdit_3.text())
                #self.set_windows(self.lineEdit_4.text())
            elif self.mod == -3:
                self.jie_jie2(self.lineEdit_1.text(), self.lineEdit_2.text())
                pass
            elif self.mod == -4:
                self.jie_jie3(self.lineEdit_1.text(), self.lineEdit_2.text(), self.lineEdit_3.text())
                pass
            elif self.mod == -5:
                self.team_kun_25(self.lineEdit_1.text(), self.lineEdit_2.text())
                pass
            elif self.mod == -6:
                self.jie_jie4(self.lineEdit_1.text(), self.lineEdit_2.text(),
                              self.lineEdit_3.text(), self.lineEdit_4.text())
                pass
            elif self.mod == -7:
                self.hun_shi(self.lineEdit_1.text(), self.lineEdit_2.text())
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
            self.add_in_text_browser(self.log_queue.get(timeout=1))
        except Exception as e:
            print("log_queue Exception:" + e.__str__())
        pass


def my_process(log_queue, yys):
    try:
        fuben = Fuben(log_queue)
        fuben.set_windows(yys)
    except Exception as e:
        print("Exception:" + e.__str__())
