from yysUI import Ui_MainWindow
from PyQt5 import QtWidgets
from Cwindow import Window
import multiprocessing
from multiprocessing import Queue
from Cfuben import Fuben
from PyQt5.QtCore import QTimer


class My_MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(My_MainWindow, self).__init__()
        self.setupUi(self)

        self.comboBox_1.setEnabled(False)
        self.comboBox_2.setEnabled(False)
        self.comboBox_3.setEnabled(False)
        self.comboBox_4.setEnabled(False)
        self.lineEdit_times.setEnabled(True)
        self.lineEdit_times.setPlaceholderText("次数")
        self.lineEdit_qqname.setEnabled(True)
        self.lineEdit_qqname.setPlaceholderText("qq昵称或备注")
        # self.comboBox_jienum.setEnabled(False)
        # self.comboBox_xuenum.setEnabled(False)

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
        # self.timer2 = QTimer()  # 初始化一个定时器
        # self.timer2.timeout.connect(self.try_get_qq)  # 计时结束调用operate()方法
        # self.timer2.start(10000)
        self.qq_name = ''
        self.Maxtimes = ''
        pass

    def setMod(self, id):
        # 单选按钮组 -2  -  -7
        self.mod = id
        self.comboBox_1.setEnabled(False)
        self.comboBox_2.setEnabled(False)
        self.comboBox_3.setEnabled(False)
        self.comboBox_4.setEnabled(False)
        # self.comboBox_jienum.setEnabled(False)
        # self.comboBox_xuenum.setEnabled(False)
        self.lineEdit_times.setEnabled(False)
        if self.mod == -2:# 设置窗口
            self.comboBox_1.setEnabled(True)
            self.comboBox_2.setEnabled(True)
            self.comboBox_3.setEnabled(True)
            self.comboBox_4.setEnabled(True)
        elif self.mod == -3:# 打结界
            self.comboBox_jienum.setEnabled(True)
            text = self.comboBox_jienum.currentText()
            self.setjienum(text)
            pass
        elif self.mod == -4:# 打血月
            self.comboBox_xuenum.setEnabled(True)
            text = self.comboBox_xuenum.currentText()
            self.setxuenum(text)
            self.lineEdit_times.setEnabled(True)
        elif self.mod == -5:# 组队困25
            self.comboBox_1.setEnabled(True)
            self.comboBox_2.setEnabled(True)

            self.lineEdit_times.setEnabled(True)
        elif self.mod == -6:# 组队魂十
            self.comboBox_1.setEnabled(True)
            self.comboBox_2.setEnabled(True)
        elif self.mod == -7:# 备用
            pass
        elif self.mod == -8:  # 备用
            pass
        elif self.mod == -9:  # 备用
            pass
        elif self.mod == -10:  # 备用
            pass
        return 0

    def start(self):
        self.add_in_text_browser("正在启动\r\n")
        self.bool_run = True
        try:
            if self.mod == -2:# 设置窗口
                self.add_in_text_browser("启动 设置窗口\r\n")
                if self.main_process is None or self.main_process.is_alive() is False:
                    self.main_process = multiprocessing.Process(
                        target=my_set_windows_process, args=(
                            self.log_queue, self.qq_name, self.comboBox_1.currentText(), self.comboBox_2.currentText(),
                            self.comboBox_3.currentText(), self.comboBox_4.currentText(),), name='my_process')
                    self.main_process.start()
                else:
                    self.add_in_text_browser("已经有副本正在运行，请先按停止\r\n")
                pass
            elif self.mod == -3:# 打结界
                self.add_in_text_browser("启动 打结界\r\n")
                inum = int(self.comboBox_jienum.currentText())

                if self.main_process is None or self.main_process.is_alive() is False:
                    self.main_process = multiprocessing.Process(
                        target=my_jie_jie_process, args=(
                            self.log_queue, self.qq_name, self.comboBox_1.currentText(), self.comboBox_2.currentText(),
                            self.comboBox_3.currentText(), self.comboBox_4.currentText(), inum), name='my_process')
                    self.main_process.start()
                else:
                    self.add_in_text_browser("已经有副本正在运行，请先按停止\r\n")
                pass
            elif self.mod == -4:# 刷血月
                self.add_in_text_browser("启动 刷血月\r\n")
                inum = int(self.comboBox_xuenum.currentText())
                strMaxtimes = self.Maxtimes
                iMaxtimes = 9999
                if strMaxtimes.isdigit() is False:
                    self.add_in_text_browser("刷血月次数不为数字，启动次数9999\r\n")
                else:
                    iMaxtimes = int(strMaxtimes)
                if self.main_process is None or self.main_process.is_alive() is False:
                    self.main_process = multiprocessing.Process(
                        target=my_xue_yue_process, args=(
                            self.log_queue, self.qq_name, self.comboBox_1.currentText(), self.comboBox_2.currentText(),
                            self.comboBox_3.currentText(), self.comboBox_4.currentText(), inum, iMaxtimes), name='my_process')
                    self.main_process.start()
                else:
                    self.add_in_text_browser("已经有副本正在运行，请先按停止\r\n")
                pass
            elif self.mod == -5:
                self.add_in_text_browser("启动 组队探索\r\n")
                strMaxtimes = self.Maxtimes
                iMaxtimes = 9999
                if strMaxtimes.isdigit() is False:
                    self.add_in_text_browser("组队探索次数不为数字，启动次数9999\r\n")
                else:
                    iMaxtimes = int(strMaxtimes)
                if self.main_process is None or self.main_process.is_alive() is False:
                    self.main_process = multiprocessing.Process(
                        target=my_team_kun_25_process, args=(
                            self.log_queue, self.qq_name, self.comboBox_1.currentText(), self.comboBox_2.currentText(),
                            iMaxtimes,), name='my_process')
                    self.main_process.start()
                else:
                    self.add_in_text_browser("已经有副本正在运行，请先按停止\r\n")
                pass
            elif self.mod == -6:
                self.add_in_text_browser("启动 组队御魂觉醒\r\n")
                if self.main_process is None or self.main_process.is_alive() is False:
                    self.main_process = multiprocessing.Process(
                        target=my_hun_shi_process, args=(
                            self.log_queue, self.qq_name, self.comboBox_1.currentText(),
                            self.comboBox_2.currentText()), name='my_process')
                    self.main_process.start()
                else:
                    self.add_in_text_browser("已经有副本正在运行，请先按停止\r\n")
                pass
            elif self.mod == -7:
                pass
            elif self.mod == -8:
                pass
            elif self.mod == -9:
                pass
            elif self.mod == -10:
                pass
        except Exception as e:
            self.add_in_text_browser("Exception:" + e.__str__() + "\r\n")
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
        #self.add_in_text_browser("..")
        try:
            self.add_in_text_browser(self.log_queue.get(timeout=0.1))
        except Exception as e:
            pass
            #self.add_in_text_browser("log_queue Exception:" + e.__str__())
        #self.add_in_text_browser("\r\n")
        return 0

    def try_get_qq(self):
        Fuben.get_qq_cmd('昆虫记')
        return 0

    def setjienum(self, text):
        self.radioButton_2.setChecked(True)
        self.mod = -3
        inum = int(text)
        if self.set_yys_wins(inum) != 0:
            self.add_in_text_browser("打结界的窗口数量不为1234，设置失败\r\n")
            self.comboBox_jienum.setText("")
            return 0
        self.add_in_text_browser("打结界的窗口数量设置成功\r\n")

    def setxuenum(self, text):
        self.radioButton_3.setChecked(True)
        self.mod = -4
        inum = int(text)
        if self.set_yys_wins(inum) != 0:
            self.add_in_text_browser("刷血月的窗口数量不为1234，设置失败\r\n")
            self.comboBox_xuenum.setText("")
            return 0
        self.add_in_text_browser("刷血月的窗口数量设置成功\r\n")

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
        else:
            self.add_in_text_browser("不能设置为这个值")
            return -1
        return 0

    def settimes(self):
        self.Maxtimes = self.lineEdit_times.text()
        if self.Maxtimes.isdigit() is False:
            self.add_in_text_browser("次数不全为数字，次数设置失败\r\n")
            self.lineEdit_times.setText('')
        else:
            self.add_in_text_browser("次数设置成功\r\n")
        return 0

    def setqqname(self):
        self.qq_name = self.lineEdit_qqname.text()
        if self.qq_name != '':
            handle = Window.check_window(self.qq_name)
            if handle != 0:
                self.add_in_text_browser("qq设置成功\r\n")
            else:
                self.add_in_text_browser("qq聊天窗口不存在，qq设置失败\r\n")
                self.lineEdit_qqname.setText('')
        return 0


def my_set_windows_process(log_queue, qq_name, yys1, yys2, yys3, yys4):
    fuben = Fuben(log_queue, qq_name)
    try:
        fuben.set_windows(yys1)
        fuben.set_windows(yys2)
        fuben.set_windows(yys3)
        fuben.set_windows(yys4)
    except Exception as e:
        fuben.add_log("Exception:" + e.__str__() + "\r\n")


def my_jie_jie_process(log_queue, qq_name, yys1, yys2, yys3, yys4, inum):
    fuben = Fuben(log_queue, qq_name)
    try:
        fuben.jie_jie(yys1, yys2, yys3, yys4, inum)
    except Exception as e:
        fuben.add_log("Exception:" + e.__str__() + "\r\n")
    fuben.add_log("jie_jie4 结束\r\n")


def my_hun_shi_process(log_queue, qq_name, yys1, yys2):
    fuben = Fuben(log_queue, qq_name)
    try:
        fuben.hun_shi(yys1, yys2)
    except Exception as e:
        fuben.add_log("Exception:" + e.__str__() + "\r\n")
    fuben.add_log("hun_shi 结束\r\n")


def my_xue_yue_process(log_queue, qq_name, yys1, yys2, yys3, yys4, inum, imax_times):
    fuben = Fuben(log_queue, qq_name)
    try:
        fuben.xue_yue(yys1, yys2, yys3, yys4, inum, imax_times)
    except Exception as e:
        fuben.add_log("Exception:" + e.__str__() + "\r\n")
    fuben.add_log("刷血月副本 结束\r\n")


def my_team_kun_25_process(log_queue, qq_name, yys1, yys2, imax_times):
    fuben = Fuben(log_queue, qq_name)
    try:
        if fuben.team_kun_25(yys1, yys2, imax_times) != 0:
            fuben.add_log("阴阳师 组队探索副本 不对\r\n")
    except Exception as e:
        fuben.add_log("Exception:" + e.__str__() + "\r\n")
    fuben.add_log("组队探索副本 结束\r\n")

