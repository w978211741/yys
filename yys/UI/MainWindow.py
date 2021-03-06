from yysUI import Ui_MainWindow
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
import datetime


class My_MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(My_MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint |
                            QtCore.Qt.WindowMinimizeButtonHint)
        # self.setFixedSize(self.width(), self.height())
        self.radioButton_1.setChecked(True)
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
        self.comboBox_2.setCurrentIndex(1)
        self.comboBox_3.setCurrentIndex(2)
        # 设置最大行数
        self.textBrowser.document().setMaximumBlockCount(23)
        self.log_queue = Queue()
        self.main_process = None
        self.mod = codedef.MOD_SET
        self.str_log = ""
        self.bool_run = False
        self.timer = QTimer()  # 初始化一个定时器
        self.timer.timeout.connect(self.show_log)  # 计时结束调用operate()方法
        self.timer.start(300)
        # self.timer11 = QTimer()  # 初始化一个定时器
        # self.timer11.timeout.connect(self.dian_guai_11)  # 计时结束调用operate()方法
        # self.timer11.start(30000)
        self.qq_name = ''
        self.Maxtimes = ''
        self.UP = codedef.UP_C_NULL
        self.BOSS = True
        self.register_show = False
        self.QingMax = True
        self.Beater = True
        self.BeatMax = True
        self.Loop = False
        self.other = codedef.XUE_YUE        # 其他功能默认'御灵'
        self.Chapter = '第一章'

        self.testF = False   # true的话，结界是测试
        pass

    def setMod(self, id):
        # 单选按钮组 -2  -  -7
        self.mod = id
        if id == -5:
            self.mod = codedef.MOD_SET
        elif id == -6:
            self.mod = codedef.MOD_JIE
        elif id == -7:
            self.mod = codedef.MOD_XUE
        elif id == -3:
            self.mod = codedef.MOD_TANG
        elif id == -4:
            self.mod = codedef.MOD_YU
        elif id == -2:
            self.mod = codedef.MOD_DOU

        self.comboBox_1.setEnabled(False)
        self.comboBox_2.setEnabled(False)
        self.comboBox_3.setEnabled(False)
        self.comboBox_4.setEnabled(False)
        # self.comboBox_jienum.setEnabled(False)
        # self.comboBox_xuenum.setEnabled(False)
        self.lineEdit_times.setEnabled(False)
        if self.mod == codedef.MOD_SET:# 设置窗口
            self.comboBox_1.setEnabled(True)
            self.comboBox_2.setEnabled(True)
            self.comboBox_3.setEnabled(True)
            self.comboBox_4.setEnabled(True)
        elif self.mod == codedef.MOD_JIE:# 打结界
            self.comboBox_jienum.setEnabled(True)
            text = self.comboBox_jienum.currentText()
            self.setjienum(text)
            pass
        elif self.mod == codedef.MOD_XUE:# 打血月
            self.comboBox_xuenum.setEnabled(True)
            text = self.comboBox_xuenum.currentText()
            self.setxuenum(text)
            self.lineEdit_times.setEnabled(True)
        elif self.mod == codedef.MOD_TANG:# 组队困25
            self.comboBox_1.setEnabled(True)
            self.comboBox_2.setEnabled(True)

            self.lineEdit_times.setEnabled(True)
        elif self.mod == codedef.MOD_YU:# 组队魂十
            self.comboBox_1.setEnabled(True)
            self.comboBox_2.setEnabled(True)
            self.comboBox_3.setEnabled(True)

            self.lineEdit_times.setEnabled(True)
        elif self.mod == codedef.MOD_DOU:# 刷斗技
            self.comboBox_dounum.setEnabled(True)
            text = self.comboBox_dounum.currentText()
            self.setdounum(text)
            self.lineEdit_times.setEnabled(True)
        return 0

    def start(self):
        try:
            if self.testF:
                self.register_show = True

            my_register = register()
            re = my_register.check()
            # print('check1:' + str(re))
            if re == 0:
                if self.register_show is False:
                    self.register_show = True
                    my_registerWindow = My_registerWindow(my_register)
                    my_registerWindow.show()
                    my_registerWindow.exec_()
            else:
                my_registerWindow = My_registerWindow(my_register)
                my_registerWindow.show()
                my_registerWindow.exec_()
                re = my_register.check()
                # print('check2:' + str(re))
                if re != 0:
                    return 0
                else:
                    self.register_show = True


            self.add_in_text_browser("正在启动\r\n")
            self.bool_run = True

            if self.mod == codedef.MOD_SET:# 设置窗口
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
            elif self.mod == codedef.MOD_JIE:# 打结界

                if self.testF:
                    self.main_process = multiprocessing.Process(
                        target=my_test_main_process, args=(
                            self.log_queue, self.qq_name), name='my_process')
                    self.main_process.start()
                    return

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
            elif self.mod == codedef.MOD_XUE:# 刷血月
                self.add_in_text_browser("启动 刷其他\r\n")
                inum = int(self.comboBox_xuenum.currentText())
                strMaxtimes = self.Maxtimes
                iMaxtimes = 9999
                if strMaxtimes.isdigit() is False:
                    self.add_in_text_browser("刷其他次数不为数字，启动次数9999\r\n")
                else:
                    iMaxtimes = int(strMaxtimes)

                ibuyyan = 0
                ibuyyu = 0
                if self.other == codedef.RI_LUN_CENG or self.other == codedef.RI_LUN_YU :
                    strbuyyan = self.lineEdit_buyyan.text()
                    if strbuyyan.isdigit() is False:
                        self.add_in_text_browser("日轮之城，买眼次数不为数字，最多买0次\r\n")
                    else:
                        ibuyyan = int(strbuyyan)

                    strbuyyu = self.lineEdit_buyyu.text()
                    if strbuyyu.isdigit() is False:
                        self.add_in_text_browser("日轮之城，买溯玉次数不为数字，最多买0次\r\n")
                    else:
                        ibuyyu = int(strbuyyu)

                    self.add_in_text_browser("日轮之城，买眼最多买" + strbuyyan +
                                             "买溯玉最多买" + strbuyyu + "次\r\n")

                if self.main_process is None or self.main_process.is_alive() is False:
                    self.main_process = multiprocessing.Process(
                        target=my_xue_yue_process, args=(
                            self.log_queue, self.qq_name, self.comboBox_1.currentText(), self.comboBox_2.currentText(),
                            self.comboBox_3.currentText(), self.comboBox_4.currentText(), inum, iMaxtimes, self.other,
                            ibuyyan, ibuyyu),
                        name='my_process')
                    self.main_process.start()
                else:
                    self.add_in_text_browser("已经有副本正在运行，请先按停止\r\n")
                pass
            elif self.mod == codedef.MOD_TANG:
                self.add_in_text_browser("启动 组队探索\r\n")
                strMaxtimes = self.Maxtimes
                iMaxtimes = 9999
                if strMaxtimes.isdigit() is False:
                    self.add_in_text_browser("组队探索次数不为数字，启动次数9999\r\n")
                else:
                    iMaxtimes = int(strMaxtimes)
                if self.main_process is None or self.main_process.is_alive() is False:
                    if self.Loop:
                        self.main_process = multiprocessing.Process(
                            target=my_tang_suo_jie_jie_process, args=(
                                self.log_queue, self.qq_name, self.comboBox_1.currentText(),
                                self.comboBox_2.currentText(), self.UP, self.BOSS, self.QingMax,
                                self.Beater, self.BeatMax, iMaxtimes, self.Chapter,), name='my_process')
                        self.main_process.start()
                    else:
                        self.main_process = multiprocessing.Process(
                            target=my_team_kun_25_process, args=(
                                self.log_queue, self.qq_name, self.comboBox_1.currentText(),
                                self.comboBox_2.currentText(), self.UP, self.BOSS, self.QingMax,
                                self.Beater, self.BeatMax, iMaxtimes, self.Chapter,), name='my_process')
                        self.main_process.start()
                else:
                    self.add_in_text_browser("已经有副本正在运行，请先按停止\r\n")
                pass
            elif self.mod == codedef.MOD_YU:
                self.add_in_text_browser("启动 组队御魂觉醒\r\n")
                iMaxtimes = 9999
                strMaxtimes = self.Maxtimes
                if strMaxtimes.isdigit() is False:
                    self.add_in_text_browser("组队探索次数不为数字，启动次数9999\r\n")
                else:
                    iMaxtimes = int(strMaxtimes)
                if self.main_process is None or self.main_process.is_alive() is False:
                    self.main_process = multiprocessing.Process(
                        target=my_hun_shi_process, args=(
                            self.log_queue, self.qq_name, self.comboBox_1.currentText(),
                            self.comboBox_2.currentText(), self.comboBox_3.currentText(),iMaxtimes), name='my_process')
                    self.main_process.start()
                else:
                    self.add_in_text_browser("已经有副本正在运行，请先按停止\r\n")
                pass
            elif self.mod == codedef.MOD_DOU:
                self.add_in_text_browser("启动 刷斗技荣誉点\r\n")
                inum = int(self.comboBox_dounum.currentText())
                iMaxtimes = 9999
                strMaxtimes = self.Maxtimes
                if strMaxtimes.isdigit() is False:
                    self.add_in_text_browser("刷斗技次数不为数字，启动次数9999\r\n")
                else:
                    iMaxtimes = int(strMaxtimes)
                if self.main_process is None or self.main_process.is_alive() is False:
                    self.main_process = multiprocessing.Process(
                        target=my_dou_ji_process, args=(
                            self.log_queue, self.qq_name, self.comboBox_1.currentText(),
                            self.comboBox_2.currentText(), self.comboBox_3.currentText(),
                            self.comboBox_4.currentText(), inum, iMaxtimes), name='my_process')
                    self.main_process.start()
                else:
                    self.add_in_text_browser("已经有副本正在运行，请先按停止\r\n")
                pass
        except Exception as e:
            self.add_in_text_browser("Exception:" + traceback.format_exc() + "\r\n")
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

    def try_get_qq(self):
        self.qq_name = self.lineEdit_qqname.text()
        if self.qq_name != '':
            handle = Window.check_window(self.qq_name)
            if handle != 0:
                Fuben.get_qq_cmd(self.qq_name)
        return 0

    def setjienum(self, text):
        self.radioButton_2.setChecked(True)
        self.mod = codedef.MOD_JIE
        inum = int(text)
        self.set_yys_wins(inum)
        self.add_in_text_browser("打结界的窗口数量设置成功\r\n")

    def setxuenum(self, text):
        self.radioButton_3.setChecked(True)
        self.mod = codedef.MOD_XUE
        inum = int(text)
        self.set_yys_wins(inum)
        self.add_in_text_browser("其他功能窗口数量设置成功\r\n")

    def setdounum(self, text):
        self.radioButton_6.setChecked(True)
        self.mod = codedef.MOD_DOU
        inum = int(text)
        self.set_yys_wins(inum)
        self.add_in_text_browser("刷斗技的窗口数量设置成功\r\n")

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

    def setUP(self, text):
        if text == codedef.UP_Z_NULL:
            self.UP = codedef.UP_C_NULL
        elif text == codedef.UP_Z_COIN:
            self.UP = codedef.UP_C_COIN
        elif text == codedef.UP_Z_EXP:
            self.UP = codedef.UP_C_EXP
        elif text == codedef.UP_Z_REWARD:
            self.UP = codedef.UP_C_REWARD
        else:
            self.UP = codedef.UP_C_NULL

    def setBOSS(self, text):
        if text == codedef.BOSS_TRUE:
            self.BOSS = True
        elif text == codedef.BOSS_FALSE:
            self.BOSS = False
        else:
            self.BOSS = True

    def setQingMax(self, text):
        if text == codedef.QING_MAX_TRUE:
            self.QingMax = True
        elif text == codedef.QING_MAX_FALSE:
            self.QingMax = False
        else:
            self.QingMax = True

    def setBeater(self, text):
        if text == codedef.C_BEAT_TRUE:
            self.Beater = True
        elif text == codedef.C_BEAT_FALSE:
            self.Beater = False
        else:
            self.Beater = True

    def setBeatMax(self, text):
        if text == codedef.BEAT_MAX_TRUE:
            self.BeatMax = True
        elif text == codedef.BEAT_MAX_FALSE:
            self.BeatMax = False
        else:
            self.BeatMax = True

    def setLoop(self, text):
        if text == codedef.LOOP_TRUE:
            self.Loop = True
        elif text == codedef.LOOP_FALSE:
            self.Loop = False
        else:
            self.Loop = True

    def setOther(self, text):
        self.other = text
        self.radioButton_3.setChecked(True)
        self.mod = codedef.MOD_XUE
        self.add_in_text_browser("其他功能设置成功\r\n")

    def setChapter(self, text):
        self.Chapter = text


def my_set_windows_process(log_queue, qq_name, yys1, yys2, yys3, yys4):
    fuben = Fuben(log_queue, qq_name)
    try:
        fuben.set_windows(yys1)
        fuben.set_windows(yys2)
        fuben.set_windows(yys3)
        fuben.set_windows(yys4)
        fuben.add_log("设置窗口成功\r\n")
    except Exception as e:
        str_log = "Exception:" + traceback.format_exc() + "\r\n"
        fuben.add_log(str_log)
        send_qq(fuben, qq_name, str_log)


def my_jie_jie_process(log_queue, qq_name, yys1, yys2, yys3, yys4, inum):
    fuben = Fuben(log_queue, qq_name)
    try:
        fuben.jie_jie(yys1, yys2, yys3, yys4, inum)
    except Exception as e:
        str_log = "Exception:" + traceback.format_exc() + "\r\n"
        fuben.add_log(str_log)
        print(str_log)
        send_qq(fuben, qq_name, str_log)
    fuben.add_log("结界 结束\r\n")


def my_hun_shi_process(log_queue, qq_name, yys1, yys2, yys3, imax_times):
    fuben = Fuben(log_queue, qq_name)
    try:
        fuben.hun_shi(yys1, yys2, yys3, imax_times)
    except Exception as e:
        str_log = "Exception:" + traceback.format_exc() + "\r\n"
        fuben.add_log(str_log)
        send_qq(fuben, qq_name, str_log)
    fuben.add_log("魂十 结束\r\n")


def my_xue_yue_process(log_queue, qq_name, yys1, yys2, yys3, yys4, inum, imax_times, mod, buyyan, buyyu):
    fuben = Fuben(log_queue, qq_name)
    try:
        fuben.xue_yue(yys1, yys2, yys3, yys4, inum, imax_times, mod,buyyan=buyyan, buyyu=buyyu)
    except Exception as e:

        str_log = "Exception:" + traceback.format_exc() + "\r\n"
        fuben.add_log(str_log)
        send_qq(fuben, qq_name, str_log)
    fuben.add_log("刷血月副本 结束\r\n")


def my_team_kun_25_process(log_queue, qq_name, yys1, yys2, UP, BOSS, QingMax, Beater, BeatMax, imax_times, Chapter):
    fuben = Fuben(log_queue, qq_name)
    try:
        if fuben.team_kun_25(yys1, yys2, UP, BOSS, QingMax, Beater, BeatMax, imax_times, Chapter) != 0:
            fuben.add_log("阴阳师 组队探索副本 不对\r\n")
    except Exception as e:
        str_log = "Exception:" + traceback.format_exc() + "\r\n"
        fuben.add_log(str_log)
        send_qq(fuben, qq_name, str_log)
    fuben.add_log("组队探索副本 结束\r\n")


def my_dou_ji_process(log_queue, qq_name, yys1, yys2, yys3, yys4, inum, imax_times):
    fuben = Fuben(log_queue, qq_name)
    try:
        fuben.dou_ji(yys1, yys2, yys3, yys4, inum, imax_times)
    except Exception as e:
        str_log = "Exception:" + traceback.format_exc() + "\r\n"
        fuben.add_log(str_log)
        send_qq(fuben, qq_name, str_log)
    fuben.add_log("结界 结束\r\n")


# 主动发qq消息
def send_qq(fuben, qq_name, msg):
    if qq_name == '':
        fuben.add_log("设置的qq名为空，不发送qq消息\r\n")
        return
    fuben.add_log("发送qq消息给" + qq_name + "\r\n")
    send_QQ = SendQQ(qq_name)
    send_QQ.send_qq_text(msg)

def my_tang_suo_jie_jie_process(log_queue, qq_name, yys1, yys2, UP, BOSS, QingMax,
                                Beater, BeatMax, imax_times, Chapter):
    fuben = Fuben(log_queue, qq_name)
    try:
        while 1:
            start_time = datetime.datetime.now()

            fuben.team_kun_25(yys1, yys2, UP, BOSS, QingMax, Beater, BeatMax, imax_times, Chapter)
            fuben.jie_jie(yys1, yys2, '1', '1', 2, maxt=True)

            end_time = datetime.datetime.now()
            if (end_time - start_time).seconds < 60:
                break

    except Exception as e:
        str_log = "Exception:" + traceback.format_exc() + "\r\n"
        fuben.add_log(str_log)
        send_qq(fuben, qq_name, str_log)
    fuben.add_log("组队探索副本 结束\r\n")

def my_test_main_process(log_queue, qq_name):
    fuben = Fuben(log_queue, qq_name)
    try:
        fuben.test_main()
    except Exception as e:

        str_log = "Exception:" + traceback.format_exc() + "\r\n"
        fuben.add_log(str_log)
        print(str_log)
        send_qq(fuben, qq_name, str_log)
    fuben.add_log("test_main 结束\r\n")