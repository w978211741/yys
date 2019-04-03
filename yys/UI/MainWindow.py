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

        self.mod = 0
        # self.para1 = 0
        # self.para2 = 0
        # self.para3 = 0
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
        # 设置窗口
        if self.mod == -2:
            self.set_windows(self.lineEdit_1.text())
            self.set_windows(self.lineEdit_2.text())
            self.set_windows(self.lineEdit_3.text())
            self.set_windows(self.lineEdit_4.text())
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
        return 0

    def stop(self):
        pass

    def set_yys(self, index, game, handle):
        game.set_window(handle, "[#] [yys" + str(index) + "] 阴阳师-网易游戏 [#]", index, True)
        print(handle.hwnd, handle.left, handle.top, handle.right, handle.bottom)
        pass

    def set_windows(self, yys):
        if yys == "" or yys == " ":
            return -1
        game = Game()
        yys1 = Handle()
        self.set_yys(yys, game, yys1)
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
            if finish1 is False:
                if wait1 == 0:
                    scene = game.get_scene(yys1)
                    print(scene)
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
                    print(scene)
                else:
                    wait2 = wait2 - 1
                if int(wait2) < 0:
                    wait2 = 0
                time.sleep(1)
            if finish1 and finish2:
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
            scene = game.get_scene(yys1)
            print(scene)
            game.do_work(scene, yys1)
            if scene == SceneKey.GOU_MAI_TI_LI:
                return
            time.sleep(0.6)
            scene = game.get_scene(yys2)
            game.do_work(scene, yys2)
            print(scene)
            if scene == SceneKey.GOU_MAI_TI_LI:
                return
            time.sleep(0.6)

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
            if finish1 is False:
                if wait1 == 0:
                    scene = game.get_scene(yys1)
                    print(scene)
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
                    print(scene)
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
                    print(scene)
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
            if finish1 is False:
                if wait1 == 0:
                    scene = game.get_scene(yys1)
                    print(scene)
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
                    print(scene)
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
                    print(scene)
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
                    print(scene)
                else:
                    wait4 = wait4 - 1
                if int(wait4) < 0:
                    wait4 = 0
                time.sleep(1)
            if finish1 and finish2 and finish3 and finish4:
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
            if captain_wait == 0:
                scene = game.get_scene(yys1)
                print(scene)
                captain_wait = game.do_work(scene, yys1)
                time.sleep(0.5)
                if captain_wait == -3:
                    return 0
            else:
                captain_wait = captain_wait - 1
            if int(captain_wait) < 0:
                captain_wait = 0
            scene = game2.get_scene(yys2)
            print(scene)
            re = game2.do_work(scene, yys2)
            time.sleep(0.5)
            if re == -3:
                return 0