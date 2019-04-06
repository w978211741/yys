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


class Fuben():

    def __init__(self, log_queue):
        self.log_queue = log_queue
        self.str_log = ""
        self.bool_run = False

    @abstractmethod
    def showlog(self):
        self.log_queue.put(self.str_log.__str__())
        pass
    
    def set_yys(self, index, game, handle):
        re = game.set_window(handle, "[#] [yys" + index + "] 阴阳师-网易游戏 [#]", index, True)
        if re != 0:
            self.str_log ="阴阳师窗口不对 yys[" + index + "] " + "窗口句柄：" + str(handle.hwnd) + "\r\n"
            self.showlog()
        else:
            self.str_log = "阴阳师 yys[" + index + "] " + "窗口句柄：" + str(handle.hwnd) + "\r\n"
            self.showlog()
        return re

    def set_windows(self, yys):
        if yys == "" or yys == " ":
            self.str_log ="阴阳师 参数不对\r\n"
            self.showlog()
            return -1
        game = Game()
        yys1 = Handle()
        self.set_yys(yys, game, yys1)
        return 0

    def jie_jie1(self, y1):
        if y1 == "" or y1 == " ":
            return -1
        game = Personal_jiejie()
        yys1 = Handle()
        self.set_yys(y1, game, yys1)
        finish1 = False
        wait1 = 0
        while 1:
            self.showlog()
            if self.bool_run is False:
                return 0
            if finish1 is False:
                if wait1 == 0:
                    scene = game.get_scene(yys1)
                    self.str_log =scene.__str__()
                    re = game.do_work(scene, yys1)
                    if re == -3:
                        finish1 = True
                    elif re > 0:
                        wait1 = re
                else:
                    wait1 = wait1 - 1
                if int(wait1) < 0:
                    wait1 = 0
                time.sleep(1)
            if finish1:
                break
        return 0

    def jie_jie2(self, y1, y2):
        if y1 == "" or y1 == " " or y2 == "" or y2 == " ":
            return -1
        game = Personal_jiejie()
        yys1 = Handle()
        yys2 = Handle()
        self.set_yys(y1, game, yys1)
        self.set_yys(y2, game, yys2)
        finish1 = False
        wait1 = 0
        finish2 = False
        wait2 = 0
        while 1:
            self.showlog()
            if self.bool_run is False:
                return 0
            if finish1 is False:
                if wait1 == 0:
                    scene = game.get_scene(yys1)
                    self.str_log =scene.__str__()
                    re = game.do_work(scene, yys1)
                    if re == -3:
                        finish1 = True
                    elif re > 0:
                        wait1 = re
                else:
                    wait1 = wait1 - 1
                if int(wait1) < 0:
                    wait1 = 0
                time.sleep(1)
            if finish2 is False:
                if wait2 == 0:
                    scene = game.get_scene(yys2)
                    re = game.do_work(scene, yys2)
                    if re == -3:
                        finish2 = True
                    elif re > 0:
                        wait2 = re
                    self.str_log =scene.__str__()
                else:
                    wait2 = wait2 - 1
                if int(wait2) < 0:
                    wait2 = 0
                time.sleep(1)
            if finish1 and finish2:
                break
        return 0

    def jie_jie3(self, y1, y2, y3):
        if y1 == "" or y1 == " " or y2 == "" or y2 == " " or y3 == "" or y3 == " ":
            return -1
        game = Personal_jiejie()
        yys1 = Handle()
        yys2 = Handle()
        yys3 = Handle()
        self.set_yys(y1, game, yys1)
        self.set_yys(y2, game, yys2)
        self.set_yys(y3, game, yys3)
        finish1 = False
        wait1 = 0
        finish2 = False
        wait2 = 0
        finish3 = False
        wait3 = 0
        while 1:
            self.showlog()
            if self.bool_run is False:
                return 0
            if finish1 is False:
                if wait1 == 0:
                    scene = game.get_scene(yys1)
                    self.str_log =scene.__str__()
                    re = game.do_work(scene, yys1)
                    if re == -3:
                        finish1 = True
                    elif re > 0:
                        wait1 = re
                else:
                    wait1 = wait1 - 1
                if int(wait1) < 0:
                    wait1 = 0
                time.sleep(1)
            if finish2 is False:
                if wait2 == 0:
                    scene = game.get_scene(yys2)
                    re = game.do_work(scene, yys2)
                    if re == -3:
                        finish2 = True
                    elif re > 0:
                        wait2 = re
                    self.str_log =scene.__str__()
                else:
                    wait2 = wait2 - 1
                if int(wait2) < 0:
                    wait2 = 0
                time.sleep(1)
            if finish3 is False:
                if wait3 == 0:
                    scene = game.get_scene(yys3)
                    re = game.do_work(scene, yys3)
                    if re == -3:
                        finish3 = True
                    elif re > 0:
                        wait3 = re
                    self.str_log =scene.__str__()
                else:
                    wait3 = wait3 - 1
                if int(wait3) < 0:
                    wait3 = 0
                time.sleep(1)
            if finish1 and finish2 and finish3:
                break
        return 0

    def jie_jie4(self, y1, y2, y3, y4):
        if y1 == "" or y1 == " " or y2 == "" or y2 == " " or y3 == "" or y3 == " " or y4 == "" or y4 == " ":
            return -1
        game = Personal_jiejie()
        yys1 = Handle()
        yys2 = Handle()
        yys3 = Handle()
        yys4 = Handle()
        self.set_yys(y1, game, yys1)
        self.set_yys(y2, game, yys2)
        self.set_yys(y3, game, yys3)
        self.set_yys(y4, game, yys4)
        finish1 = False
        wait1 = 0
        finish2 = False
        wait2 = 0
        finish3 = False
        wait3 = 0
        finish4 = False
        wait4 = 0
        while 1:
            self.showlog()
            if self.bool_run is False:
                return 0
            if finish1 is False:
                if wait1 == 0:
                    scene = game.get_scene(yys1)
                    self.str_log =scene.__str__()
                    re = game.do_work(scene, yys1)
                    if re == -3:
                        finish1 = True
                    elif re > 0:
                        wait1 = re
                else:
                    wait1 = wait1 - 1
                if int(wait1) < 0:
                    wait1 = 0
                time.sleep(1)
            if finish2 is False:
                if wait2 == 0:
                    scene = game.get_scene(yys2)
                    re = game.do_work(scene, yys2)
                    if re == -3:
                        finish2 = True
                    elif re > 0:
                        wait2 = re
                    self.str_log =scene.__str__()
                else:
                    wait2 = wait2 - 1
                if int(wait2) < 0:
                    wait2 = 0
                time.sleep(1)
            if finish3 is False:
                if wait3 == 0:
                    scene = game.get_scene(yys3)
                    re = game.do_work(scene, yys3)
                    if re == -3:
                        finish3 = True
                    elif re > 0:
                        wait3 = re
                    self.str_log =scene.__str__()
                else:
                    wait3 = wait3 - 1
                if int(wait3) < 0:
                    wait3 = 0
                time.sleep(1)
            if finish4 is False:
                if wait4 == 0:
                    scene = game.get_scene(yys4)
                    re = game.do_work(scene, yys4)
                    if re == -3:
                        finish4 = True
                    elif re > 0:
                        wait4 = re
                    self.str_log =scene.__str__()
                else:
                    wait4 = wait4 - 1
                if int(wait4) < 0:
                    wait4 = 0
                time.sleep(1)
            if finish1 and finish2 and finish3 and finish4:
                break
        return 0

    def hun_shi(self, y1, y2):
        if y1 == "" or y1 == " " or y2 == "" or y2 == " ":
            return -1
        game = Team_hun_10()
        yys1 = Handle()
        yys2 = Handle()
        self.set_yys(y1, game, yys1)
        self.set_yys(y2, game, yys2)
        while 1:
            self.showlog()
            self.showlog()
            if self.bool_run is False:
                return 0
            scene = game.get_scene(yys1)
            self.str_log =scene.__str__()
            game.do_work(scene, yys1)
            if scene == SceneKey.GOU_MAI_TI_LI:
                return
            time.sleep(0.6)
            scene = game.get_scene(yys2)
            game.do_work(scene, yys2)
            self.str_log =scene.__str__()
            if scene == SceneKey.GOU_MAI_TI_LI:
                return
            time.sleep(0.6)

    def shua_xue_yue(self, y1, ju_shu_max):
        if y1 == "" or y1 == " ":
            return -1
        game = dashitou()
        yys1 = Handle()
        self.set_yys(y1, game, yys1)
        finish1 = False
        wait1 = 0
        ju_shu= 0
        while 1:
            self.showlog()
            if self.bool_run is False:
                return 0
            if finish1 is False:
                if wait1 == 0:
                    scene = game.get_scene(yys1)
                    self.str_log =scene.__str__()
                    re = game.do_work(scene, yys1)
                    if re == -3:
                        finish1 = True
                    elif re > 0:
                        wait1 = re
                    elif re == -2:
                        ju_shu = ju_shu + 1
                        try:
                            if ju_shu >= int(ju_shu_max):
                                return 0
                        except Exception as e:
                            print("ju_shu >= int(ju_shu_max) Exception:" + e.__str__())
                else:
                    wait1 = wait1 - 1
                if int(wait1) < 0:
                    wait1 = 0
                time.sleep(1)
            if finish1:
                break
        return 0

    def team_kun_25(self, captain, teammate):
        if captain == "" or captain == " " or teammate == "" or teammate == " ":
            return -1
        # team_kun_25()
        captain_wait = 0
        game = Team_kun_25_captain()
        yys1 = Handle()
        self.set_yys(captain, game, yys1)
        game2 = Team_kun_25_teammate()
        yys2 = Handle()
        self.set_yys(teammate, game, yys2)
        while 1:
            self.showlog()
            if self.bool_run is False:
                return 0
            if captain_wait == 0:
                scene = game.get_scene(yys1)
                self.str_log =scene.__str__()
                captain_wait = game.do_work(scene, yys1)
                time.sleep(0.5)
                if captain_wait == -3:
                    return 0
            else:
                captain_wait = captain_wait - 1
            if int(captain_wait) < 0:
                captain_wait = 0
            scene = game2.get_scene(yys2)
            self.str_log =scene.__str__()
            re = game2.do_work(scene, yys2)
            time.sleep(0.5)
            if re == -3:
                return 0

