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
from abc import abstractmethod
from yys.game.Cdashitou import dashitou
from CsendQQ import SendQQ
import win32gui
import codedef
from Cwindow import Window


class Fuben():
    def __init__(self, log_queue, qq_name):
        self.log_queue = log_queue
        self.qq_name = qq_name

    def add_log(self, log):
        self.log_queue.put(log)
        return codedef.NORMAL_END

    def set_yys(self, index, game, handle):
        # 加上显示窗口，防止最小化
        win32gui.ShowWindow(handle.hwnd, 1)
        re = game.set_window(handle, "[#] [yys" + index + "] 阴阳师-网易游戏 [#]", index, True)
        if re != 0:
            self.add_log("阴阳师窗口不对 yys[" + index + "] " + "窗口句柄：" + str(handle.hwnd) + "\r\n")
        else:
            self.add_log("阴阳师 yys[" + index + "] " + "窗口句柄：" + str(handle.hwnd) + "\r\n")
        return re

    def set_windows(self, yys):
        if yys == "" or yys == " ":
            self.add_log("阴阳师 参数不对\r\n")
            return codedef.ERROR_END
        game = Game()
        yys1 = Handle()
        self.set_yys(yys, game, yys1)
        self.add_log("设置窗口完成\r\n")
        return codedef.NORMAL_END

    def jie_jie(self, y1, y2, y3, y4, inum):
        windowslist = [y1, y2, y3, y4]
        #只有一个结界类实例，不同的只是窗口句柄和窗口坐标
        game = Personal_jiejie()
        yys1 = Handle()
        yys2 = Handle()
        yys3 = Handle()
        yys4 = Handle()
        yyslist = [yys1, yys2, yys3, yys4]

        i = 0
        while i < inum:
            self.set_yys(windowslist[i], game, yyslist[i])
            i = i + 1

        finishlist = [False, False, False, False]
        waitlist = [0, 0, 0, 0]

        while 1:
            i = 0
            while i < inum:
                if finishlist[i] is False:
                    if waitlist[i] == 0:
                        scene = game.get_scene(yyslist[i])
                        self.add_log(scene.__str__() + "\r\n")
                        re = game.do_work(scene, yyslist[i])
                        if re == codedef.NOT_ENOUGH_POWER:
                            finishlist[i] = True
                        elif re == codedef.SCENCE_REPEAT_END:
                            finishlist[i] = True
                            self.add_log("yys" + windowslist[i] + "场景重复超限\r\n")
                            self.send_qq_jie_tu(yyslist[i])
                        elif re > codedef.NORMAL_END:
                            waitlist[i] = re
                    else:
                        waitlist[i] = waitlist[i] - 1
                    if waitlist[i] < 0:
                        waitlist[i] = 0
                    time.sleep(1)
                i = i + 1
            i = 0
            while i < inum:
                if finishlist[i] is False:
                    break
                i = i + 1
            if i == inum:
                break
        self.send_qq(r'结界全部 打完，进程结束')
        return codedef.NORMAL_END

    def hun_shi(self, y1, y2, imax_times):
        game = Team_hun_10()
        yys1 = Handle()
        yys2 = Handle()
        self.set_yys(y1, game, yys1)
        self.set_yys(y2, game, yys2)
        ju_flag = False
        times = 0
        while 1:
            scene = game.get_scene(yys1)
            self.add_log(scene.__str__() + "\r\n")
            re = game.do_work(scene, yys1)
            if re == codedef.SCENCE_REPEAT_END:
                self.add_log("yys" + y1 + "场景重复超限\r\n")
                self.send_qq_jie_tu(yys1)
            elif re == codedef.FIGHT_BEGIN and ju_flag is False:
                ju_flag = True
            elif re == codedef.FIGHT_END and ju_flag is True:
                times += 1
                self.add_log(times.__str__() + "\r\n")
                if times > imax_times:
                    self.add_log("达到最大次数，进程结束\r\n")
                    self.send_qq(r'御魂觉醒 达到最大次数，进程结束')
                    return codedef.NORMAL_END
            if scene == SceneKey.GOU_MAI_TI_LI:
                break
            time.sleep(0.6)
            scene = game.get_scene(yys2)
            re = game.do_work(scene, yys2)
            if re == codedef.SCENCE_REPEAT_END:
                self.add_log("yys" + y2 + "场景重复超限\r\n")
                self.send_qq_jie_tu(yys2)
            self.add_log(scene.__str__() + "\r\n")
            if scene == SceneKey.GOU_MAI_TI_LI:
                break
            time.sleep(0.6)
        self.send_qq(r'魂十 打完，进程结束')
        return codedef.NORMAL_END

    def xue_yue(self, y1, y2, y3, y4, inum, imax_times):
        windowslist = [y1, y2, y3, y4]

        game = dashitou()
        yys1 = Handle()
        yys2 = Handle()
        yys3 = Handle()
        yys4 = Handle()
        yyslist = [yys1, yys2, yys3, yys4]

        i = 0
        while i < inum:
            self.set_yys(windowslist[i], game, yyslist[i])
            i = i + 1

        finishlist = [False, False, False, False]
        waitlist = [0, 0, 0, 0]
        ji_shulist = [0, 0, 0, 0]
        ju_flag = [False, False, False, False]

        while 1:
            i = 0
            while i < inum:
                if finishlist[i] is False:
                    if waitlist[i] == 0:
                        scene = game.get_scene(yyslist[i])
                        self.add_log(scene.__str__() + "\r\n")
                        re = game.do_work(scene, yyslist[i])
                        if re > codedef.NORMAL_END:
                            waitlist[i] = re
                        elif re == codedef.FIGHT_BEGIN:
                            ju_flag[i] = True
                        elif re == codedef.FIGHT_END and ju_flag[i] is True:
                            ju_flag[i] = False
                            ji_shulist[i] = ji_shulist[i] + 1
                            self.add_log(ji_shulist[i].__str__() + "\r\n")
                            if ji_shulist[i] > imax_times:
                                finishlist[i] = True
                        elif re == codedef.SCENCE_REPEAT_END:
                            finishlist[i] = True
                            self.add_log("yys" + windowslist[i] + "场景重复超限\r\n")
                            self.send_qq_jie_tu(yyslist[i])

                    else:
                        waitlist[i] = waitlist[i] - 1
                    if int(waitlist[i]) < 0:
                        waitlist[i] = 0
                    time.sleep(1)
                i = i + 1
            i = 0
            while i < inum:
                if finishlist[i] is False:
                    break
                i = i + 1
            if i == inum:
                break
        self.send_qq(r'血月全部 打完，进程结束')
        return codedef.NORMAL_END

    def team_kun_25(self, captain, teammate, UP, BOSS, imax_times):
        game = Team_kun_25_captain(UP=UP, BOSS=BOSS)
        yys1 = Handle()
        self.set_yys(captain, game, yys1)
        game2 = Team_kun_25_teammate()
        yys2 = Handle()
        self.set_yys(teammate, game2, yys2)
        times = 0
        ju_flag = False

        # 0是其他状态，1是打完后的邀请界面，不按确定；2是队友已出来，按确定，按完恢复到0
        da_wan_flag = 0
        while 1:
            scene = game.get_scene(yys1)
            captain_wait = game.do_work(scene, yys1)
            self.add_log(scene.__str__() + captain_wait.__str__() + "\r\n")
            if captain_wait == -900:
                self.add_log("队长体力不足，进程结束\r\n")
                self.send_qq(r'困25 队长体力不足，进程结束')
                return codedef.NORMAL_END
            elif captain_wait == -3:
                self.add_log("队长体力不足或者识别失败，进程结束\r\n")
                self.send_qq(r'困25 队长体力不足或者识别失败，进程结束')
                return codedef.NORMAL_END
            elif captain_wait == -21 or captain_wait == -22:
                ju_flag = True
            elif captain_wait == -11 and ju_flag is True:
                ju_flag = False
                times = times + 1
                self.add_log(times.__str__() + "\r\n")
                if times > imax_times:
                    self.add_log("达到最大次数，进程结束\r\n")
                    self.send_qq(r'困25 达到最大次数，进程结束')
                    return codedef.NORMAL_END
            elif captain_wait == codedef.YAO_QING_DUI_YOU_JI_XU and da_wan_flag == 0:
                da_wan_flag = 1
            elif captain_wait == codedef.YAO_QING_DUI_YOU_JI_XU and da_wan_flag == 2:
                game.yao_qing_dui_you_ji_xu(scene, yys1)
                da_wan_flag = 0
            elif captain_wait == codedef.SCENCE_REPEAT_END:
                self.add_log("场景重复超限\r\n")
                self.send_qq_jie_tu(yys1)
                return codedef.NORMAL_END
            if captain_wait != -901:
                time.sleep(0.5)

            scene = game2.get_scene(yys2)
            self.add_log(scene.__str__() + "\r\n")

            if scene == SceneKey.TANG_SUO and da_wan_flag == 1:
                da_wan_flag = 2

            re = game2.do_work(scene, yys2)
            time.sleep(0.5)
            if re == -3 or re == -900:
                self.add_log("队员体力不足或者识别失败，进程结束\r\n")
                self.send_qq(r'困25 队员体力不足或者识别失败，进程结束')
                return codedef.NORMAL_END
            elif re == codedef.SCENCE_REPEAT_END:
                self.add_log("场景重复超限\r\n")
                self.send_qq_jie_tu(yys1)
                return codedef.NORMAL_END

    # 主动发qq消息
    def send_qq(self, msg):
        if self.qq_name == '':
            self.add_log("设置的qq名为空，不发送qq消息\r\n")
            return
        send_QQ = SendQQ(self.qq_name)
        send_QQ.send_qq_text(msg)

    # 主动发qq截图
    def send_qq_jie_tu(self, handle):
        if self.qq_name == '':
            self.add_log("设置的qq名为空，不发送qq消息\r\n")
            return
        send_QQ = SendQQ(self.qq_name)
        send_QQ.send_jie_tu(handle)

    @staticmethod
    def get_qq_cmd(name):
        send_QQ = SendQQ(name)
        cmd = send_QQ.get_text(name)
        cmd = cmd.upper()
        if cmd != "":
            if cmd == 'JT':
                send_QQ.send_jie_tu()
            elif cmd == '?' or cmd == 'HELP':
                send_QQ.send_qq_text("JT:截屏;?/HELP：帮助;CW：查询全部窗口句柄。不区分大小写")
            elif cmd == 'CW':
                restr = Fuben.check_yys_window(1)
                restr = restr + '\r\n' + Fuben.check_yys_window(2)
                restr = restr + '\r\n' + Fuben.check_yys_window(3)
                restr = restr + '\r\n' + Fuben.check_yys_window(4)
                send_QQ.send_qq_text(restr)

    @staticmethod
    def check_yys_window(index):
        window = Window()
        window_name = "[#] [yys" + str(index) + "] 阴阳师-网易游戏 [#]"
        handle = window.check_window(window_name)
        if handle == 0:
            return window_name + "不存在"
        return window_name + "窗口句柄：[" + str(handle) + "]"

