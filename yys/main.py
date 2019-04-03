#encoding=utf-8
from Cgame import Game, SceneKey
from Chandle import Handle
import time
from yys.game.Cliaojiejie import Liaojiejie
from yys.game.Cteam_kun_25_captain import Team_kun_25_captain
from yys.game.Cteam_kun_25_teammate import Team_kun_25_teammate
from yys.game.Cpersonal_jiejie import Personal_jiejie
from yys.game.Cteam_hun_10 import Team_hun_10
from MainWindow import My_MainWindow
from PyQt5 import QtWidgets
import sys


def set_yys(index, game, handle):
    game.set_window(handle, "[#] [yys" + str(index) + "] 阴阳师-网易游戏 [#]", index, True)
    print(handle.hwnd, handle.left, handle.top, handle.right, handle.bottom)
    pass


def set_windows():
    game = Game()
    yys1 = Handle()
    yys2 = Handle()
    yys3 = Handle()
    yys4 = Handle()
    set_yys(1, game, yys1)
    set_yys(2, game, yys2)
    set_yys(3, game, yys3)
    set_yys(4, game, yys4)
    pass


def hun_shi(y1, y2):
    game = Team_hun_10()
    yys1 = Handle()
    yys2 = Handle()
    set_yys(y1, game, yys1)
    set_yys(y2, game, yys2)
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


def da_liao_jie_jie():
    game = Liaojiejie()
    yys1 = Handle()
    set_yys(2, game, yys1)
    index = 1
    flag = True
    old_f = flag
    while 1:
        index = index + 1
        if index > 5500:
            return
        if flag != old_f:
            old_f = flag
            time.sleep(10)
        if flag:
            scene = game.get_scene(yys1)
            print(scene)
            re = game.do_work(scene, yys1)
            if re == 0:
                print("0：完成")
                time.sleep(1)
            elif re == 1:
                print("1：无法判断是在个人还是寮突破（右侧按钮无法识别）")
                flag = False
            elif re == 2:
                print("2：会长未选择寮进行突破")
                flag = False
            elif re == 3:
                print("3：次数已经用完（十分钟回复一次，最高存储6次）")
                flag = False
            elif re == 4:
                print("4：分块后找不到没打过的（理应不出现，因为是先识别出没打过的数量之后才会调用到的）")
                flag = False
            time.sleep(1)
        else:
            scene = game.get_scene(yys1)
            print(scene)
            re = game.do_work(scene, yys1)
            if re == 0:
                print("0：完成")
                time.sleep(1)
            elif re == 1:
                print("1：打完三个冷却中")
                flag = True
            elif re == 2:
                print("2：分块后找不到没打过的（理应不出现，因为是先识别出没打过的数量之后才会调用到的）")
                flag = True
            time.sleep(1)


def jie_jie2(y1, y2):
    game = Personal_jiejie()
    yys1 = Handle()
    yys2 = Handle()
    set_yys(y1, game, yys1)
    set_yys(y2, game, yys2)
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


def jie_jie3(y1, y2, y3):
    game = Personal_jiejie()
    yys1 = Handle()
    yys2 = Handle()
    yys3 = Handle()
    set_yys(y1, game, yys1)
    set_yys(y2, game, yys2)
    set_yys(y3, game, yys3)
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

def jie_jie4():
    game = Game()
    yys1 = Handle()
    set_yys(1, game, yys1)
    yys2 = Handle()
    set_yys(2, game, yys2)
    yys3 = Handle()
    set_yys(3, game, yys3)
    yys4 = Handle()
    set_yys(4, game, yys4)
    while 1:
        scene = game.get_scene(yys1)
        print(scene)
        game.do_work(scene, yys1)
        time.sleep(1)
        scene = game.get_scene(yys2)
        print(scene)
        game.do_work(scene, yys2)
        time.sleep(1)
        scene = game.get_scene(yys3)
        print(scene)
        game.do_work(scene, yys3)
        time.sleep(1)
        scene = game.get_scene(yys4)
        print(scene)
        game.do_work(scene, yys4)
        time.sleep(1)


def team_kun_25(captain, teammate):
    # team_kun_25()
    captain_wait = 0
    game = Team_kun_25_captain()
    yys1 = Handle()
    set_yys(captain, game, yys1)
    game2 = Team_kun_25_teammate()
    yys2 = Handle()
    set_yys(teammate, game, yys2)
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


if __name__ == "__main1__":
    print("开始")
    set_windows()
    print("结束")

if __name__ == "__main1__":
    print("开始")
    jie_jie2(3, 2)
    print("结束")

if __name__ == "__main1__":
    print("开始")
    jie_jie3(1, 2, 3)
    print("结束")



if __name__ == "__main1__":
    print("开始")
    hun_shi(3, 2)
    print("结束")

if __name__ == "__main1__":
    print("开始")
    da_liao_jie_jie()
    print("结束")

if __name__ == "__main1__":
    print("开始")
    # 组队打困25
    team_kun_25(3, 2)
    print("结束")



if __name__ == "__main__":
    print("开始")
    # main()
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = My_MainWindow()
    my_pyqt_form.show()
    sys.exit(app.exec_())
    print("结束")