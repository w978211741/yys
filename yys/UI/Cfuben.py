from yysUI import Ui_MainWindow
from PyQt5 import QtWidgets
from Cgame import Game, SceneKey
from Chandle import Handle
from yys.game.Cliaojiejie import Liaojiejie
from win32api import GetSystemMetrics
from yys.game.Cteam_kun_25_captain import Team_kun_25_captain
from yys.game.Cteam_kun_25_teammate import Team_kun_25_teammate
from yys.game.Cpersonal_jiejie import Personal_jiejie
from yys.game.Cteam_hun_10 import Team_hun_10
import time
from Cimg import Img
from yys.game.Cdashitou import dashitou
from CsendQQ import SendQQ
import win32gui
import codedef
from Cwindow import Window
from Cdouji import Dou_ji
from CNka import Nka
from Czabaigui import Zabaigui
import time
from Cmouse import Mouse
from Cgouliang import Gouliang


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
            if self.set_yys(windowslist[i], game, yyslist[i]) != 0:
                self.add_log("沙盒窗口不完全存在，进程结束。\r\n")
                return codedef.NORMAL_END
            i = i + 1

        finishlist = [0, 0, 0, 0]
        waitlist = [0, 0, 0, 0]

        while 1:
            i = 0
            while i < inum:
                if finishlist[i] != 2:
                    if waitlist[i] == 0:
                        scene = game.get_scene(yyslist[i])
                        if scene == SceneKey.TANG_SUO and finishlist[i] == 1:
                            finishlist[i] = 2
                            continue
                        self.add_log(scene.__str__() + "\r\n")
                        if finishlist[i] == 0:
                            re = game.do_work(scene, yyslist[i])
                        elif finishlist[i] == 1:
                            re = game.exit(scene, yyslist[i])
                        else:
                            re = codedef.NORMAL_END

                        if re == codedef.SCENCE_REPEAT_END:
                            finishlist[i] = 1
                            self.add_log("yys" + windowslist[i] + "场景重复超限\r\n")
                            self.send_qq_jie_tu(yyslist[i])
                        elif re > codedef.NORMAL_END:
                            yyslist[i].iold_scene = 0
                            waitlist[i] = re
                            self.add_log("yys" + windowslist[i] + "冷却中，场景重复次数重置\r\n")

                    else:
                        waitlist[i] = waitlist[i] - 1
                    if waitlist[i] < 0:
                        waitlist[i] = 0
                    self.time_sleep(inum)
                i = i + 1
            i = 0
            while i < inum:
                if finishlist[i] != 2:
                    break
                i = i + 1
            if i == inum:
                break
        self.send_qq(r'结界全部 打完，进程结束')
        return codedef.NORMAL_END

    def hun_shi(self, y1, y2, imax_times):
        if Window.check_window("[#] [yys" + y1 + "] 阴阳师-网易游戏 [#]") == 0 \
                or Window.check_window("[#] [yys" + y2 + "] 阴阳师-网易游戏 [#]") == 0:
            self.add_log("沙盒窗口不完全存在，进程结束。\r\n")
            return codedef.NORMAL_END

        game = Team_hun_10()
        yys1 = Handle()
        yys2 = Handle()
        self.set_yys(y1, game, yys1)
        self.set_yys(y2, game, yys2)
        ju_flag = False
        dian_guai_flag = 0
        dian_guai_time = 0
        times = 0
        t = time.time()

        print(t)  # 原始时间数据
        print(int(t))
        while 1:
            scene = game.get_scene(yys1)

            # 手动阵容需点怪
            if scene == SceneKey.ZHANG_DOU_ZHONG:
                if dian_guai_flag == 1:
                    dian_guai_flag = 2
                    dian_guai_time = int(time.time())
                elif dian_guai_flag == 2 and int(time.time()) - dian_guai_time >= 30:
                    dian_guai_flag = 3
                    game.dian_guai_11(yys1)
                    self.add_log("yys" + y1 + "点主怪\r\n")
                    print("点主怪")
                    time.sleep(1)
                    game.dian_guai_11(yys1)

            re = game.do_work(scene, yys1)
            self.add_log(scene.__str__() + str(re) + "\r\n")
            if re == codedef.SCENCE_REPEAT_END:
                self.add_log("yys" + y1 + "场景重复超限\r\n")
                self.send_qq_jie_tu(yys1)
            elif re == codedef.FIGHT_BEGIN and ju_flag is False:
                ju_flag = True
                dian_guai_flag = 1
            elif re == codedef.FIGHT_END and ju_flag is True:
                dian_guai_time = 0
                dian_guai_flag = 0
                ju_flag = False
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

    def xue_yue(self, y1, y2, y3, y4, inum, imax_times, mod):
        windowslist = [y1, y2, y3, y4]

        if mod == codedef.CHOU_N_KA:
            game = Nka()
        elif mod == codedef.ZA_BAI_GUI:
            game = Zabaigui()
        elif mod == codedef.XUE_YUE:
            game = dashitou()
        else:
            game = dashitou()

        yys1 = Handle()
        yys2 = Handle()
        yys3 = Handle()
        yys4 = Handle()
        yyslist = [yys1, yys2, yys3, yys4]

        i = 0
        while i < inum:
            if self.set_yys(windowslist[i], game, yyslist[i]) != 0:
                self.add_log("沙盒窗口不完全存在，进程结束。\r\n")
                return codedef.NORMAL_END
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
                    self.time_sleep(inum)
                i = i + 1
            i = 0
            while i < inum:
                if finishlist[i] is False:
                    break
                i = i + 1
            if i == inum:
                break
        self.send_qq(r'进程结束')
        return codedef.NORMAL_END

    def team_kun_25(self, captain, teammate, UP, BOSS, QingMax, Beater, BeatMax, imax_times, Chapter):
        if Window.check_window("[#] [yys" + captain + "] 阴阳师-网易游戏 [#]") == 0 \
                or Window.check_window("[#] [yys" + teammate + "] 阴阳师-网易游戏 [#]") == 0:
            self.add_log("沙盒窗口不完全存在，进程结束。\r\n")
            return codedef.NORMAL_END

        game = Team_kun_25_captain(UP=UP, BOSS=BOSS, QingMax=QingMax, Beater=Beater, BeatMax=BeatMax, Chapter=Chapter)
        yys1 = Handle()
        self.set_yys(captain, game, yys1)
        game2 = Team_kun_25_teammate(Beater=Beater, BeatMax=BeatMax)
        yys2 = Handle()
        self.set_yys(teammate, game2, yys2)
        times = 0
        ju_flag = False

        oldc_c = ''

        while 1:
            # 队长
            scene = game.get_scene(yys1)
            if oldc_c != str(scene):
                oldc_c = str(scene)
                self.add_log(str(scene) + "\r\n")
            re = game.do_work(scene, yys1)
            if re > 0:
                self.add_log('队长满级数量' + str(re) + "\r\n")
            if re == codedef.BEGIN_DA_GUAI or re == codedef.BEGIN_DA_BOSS:
                ju_flag = True
            elif re == codedef.FIGHT_END and ju_flag is True:
                ju_flag = False
                times = times + 1
                self.add_log(times.__str__() + "\r\n")
                if times > imax_times:
                    self.add_log("达到最大次数，进程结束\r\n")
                    self.send_qq(r'困25 达到最大次数，进程结束')
                    return codedef.NORMAL_END
            elif re == codedef.SCENCE_REPEAT_END:
                self.add_log("场景重复超限\r\n")
                self.send_qq_jie_tu(yys1)
                return codedef.NORMAL_END
            elif re == codedef.TANG_GO_RIGHT:
                yys1.iold_scene = 0
                yys2.iold_scene = 0
            elif re == codedef.EXIT_TANG_SUO:
                game2.set_exit(True)
            elif re == codedef.YAO_QING_ZHONG:
                yys1.iold_scene = 0
                yys2.iold_scene = 0

            # 队员
            scene = game2.get_scene(yys2)

            if oldc_c != str(scene):
                oldc_c = str(scene)
                self.add_log(str(scene) + "\r\n")

            if scene == SceneKey.TANG_SUO or scene == SceneKey.TANG_SUO_ZHANG_JIE:
                game.set_yao_qing(True)     # 队长可邀请

            re = game2.do_work(scene, yys2)
            if re > 0:
                self.add_log('队友满级数量' + str(re) + "\r\n")
            if re == codedef.ZAI_TANG_SUO:
                game.set_da_guai(True)

    def time_sleep(self, inum):
        time.sleep(1.5 - inum * 0.3)

    def dou_ji(self, y1, y2, y3, y4, inum, imax_times):
        windowslist = [y1, y2, y3, y4]
        #只有一个结界类实例，不同的只是窗口句柄和窗口坐标
        game = Dou_ji()
        yys1 = Handle()
        yys2 = Handle()
        yys3 = Handle()
        yys4 = Handle()
        yyslist = [yys1, yys2, yys3, yys4]

        i = 0
        while i < inum:
            if self.set_yys(windowslist[i], game, yyslist[i]) != 0:
                self.add_log("沙盒窗口不完全存在，进程结束。\r\n")
                return codedef.NORMAL_END
            i = i + 1

        finishlist = [False, False, False, False]
        waitlist = [0, 0, 0, 0]
        ji_shulist = [0, 0, 0, 0]
        ju_flag = [False, False, False, False]

        while 1:
            i = 0
            while i < inum:
                if finishlist[i] is False:
                    scene = game.get_scene(yyslist[i])
                    self.add_log(scene.__str__() + "\r\n")
                    re = game.do_work(scene, yyslist[i])
                    if re == codedef.SCENCE_REPEAT_END:
                        finishlist[i] = True
                        self.add_log("yys" + windowslist[i] + "场景重复超限\r\n")
                        self.send_qq_jie_tu(yyslist[i])
                    elif re == codedef.FIGHT_BEGIN:
                        ju_flag[i] = True
                    elif re == codedef.FIGHT_END and ju_flag[i] is True:
                        ju_flag[i] = False
                        ji_shulist[i] += 1
                        self.add_log(ji_shulist[i].__str__() + "\r\n")
                        if ji_shulist[i] > imax_times:
                            finishlist[i] = True
                    self.time_sleep(inum)
                i = i + 1
            i = 0
            while i < inum:
                if finishlist[i] is False:
                    break
                i = i + 1
            if i == inum:
                break
        self.send_qq(r'斗技 打完，进程结束')
        return codedef.NORMAL_END

    def Nka(self, y1, y2, y3, y4, inum, imax_times):
        windowslist = [y1, y2, y3, y4]
        #只有一个结界类实例，不同的只是窗口句柄和窗口坐标
        game = Nka()
        yys1 = Handle()
        yys2 = Handle()
        yys3 = Handle()
        yys4 = Handle()
        yyslist = [yys1, yys2, yys3, yys4]

        i = 0
        while i < inum:
            if self.set_yys(windowslist[i], game, yyslist[i]) != 0:
                self.add_log("沙盒窗口不完全存在，进程结束。\r\n")
                return codedef.NORMAL_END
            i = i + 1

        finishlist = [False, False, False, False]
        ji_shulist = [0, 0, 0, 0]
        ju_flag = [False, False, False, False]

        while 1:
            i = 0
            while i < inum:
                if finishlist[i] is False:
                    scene = game.get_scene(yyslist[i])
                    self.add_log(scene.__str__() + "\r\n")
                    re = game.do_work(scene, yyslist[i])
                    if re == codedef.SCENCE_REPEAT_END:
                        finishlist[i] = True
                        self.add_log("yys" + windowslist[i] + "场景重复超限\r\n")
                        self.send_qq_jie_tu(yyslist[i])
                    elif re == codedef.NORMAL_END:
                        ju_flag[i] = True
                    elif re == codedef.NORMAL_END and ju_flag[i] is True:
                        ju_flag[i] = False
                        ji_shulist[i] += 1
                        self.add_log(ji_shulist[i].__str__() + "\r\n")
                        if ji_shulist[i] > imax_times:
                            finishlist[i] = True
                    self.time_sleep(inum)
                i = i + 1
            i = 0
            while i < inum:
                if finishlist[i] is False:
                    break
                i = i + 1
            if i == inum:
                break
        self.send_qq(r'抽完N卡，进程结束')
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

    def test_main(self):
        # 测试函数：截取游戏窗口temp.bmp
        # 再截出N卡的小块，确定准确后的百分比
        handle = Handle()
        game = Game()
        if self.set_yys("1", game, handle) == 0:
            while 1:
                game.get_scene(handle)  # 产生temp.bmp
                # metrics_x = GetSystemMetrics(0)  # 获取分辨率
                # metrics_y = GetSystemMetrics(1)  # 获取分辨率
                # gou = Gouliang(metrics_x, metrics_y, handle)
                # gou.find_and_huang(False, False)


                if game.if_exist('yys/进入探索按钮.bmp', 0.5) == 0:
                    print('找到探索按钮2')

                time.sleep(0.2)

