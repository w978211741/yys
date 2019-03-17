#encoding=utf-8
from Cgame import Game, SceneKey
from Chandle import Handle
import time
from yys.game.Cliaojiejie import Liaojiejie
from yys.game.Cteam_kun_25 import Team_kun_25


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


def hun_shi():
    game = Game()
    yys1 = Handle()
    yys2 = Handle()
    set_yys(1, game, yys1)
    set_yys(2, game, yys2)
    index = 1
    while 1:
        if index > 2500:
            return
        # print(index)
        index = index + 1
        scene = game.get_scene(yys1)
        print(scene)
        game.lia_ren_da(scene, yys1)
        if scene == SceneKey.GOU_MAI_TI_LI:
            return
        time.sleep(1)
        scene = game.get_scene(yys2)
        game.lia_ren_da(scene, yys2)
        print(scene)
        if scene == SceneKey.GOU_MAI_TI_LI:
            return
        time.sleep(1)


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
            re = game.da_jie_jie(scene, yys1)
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



def jie_jie2():
    game = Game()
    yys1 = Handle()
    yys2 = Handle()
    set_yys(1, game, yys1)
    set_yys(2, game, yys2)
    index = 1
    while 1:
        if index > 2500:
            return
        index = index + 1
        scene = game.get_scene(yys1)
        print(scene)
        game.lia_ren_da(scene, yys1)
        time.sleep(1)
        scene = game.get_scene(yys2)
        game.lia_ren_da(scene, yys2)
        print(scene)
        time.sleep(1)


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
        game.da_jie_jie(scene, yys1)
        time.sleep(1)
        scene = game.get_scene(yys2)
        print(scene)
        game.da_jie_jie(scene, yys2)
        time.sleep(1)
        scene = game.get_scene(yys3)
        print(scene)
        game.da_jie_jie(scene, yys3)
        time.sleep(1)
        scene = game.get_scene(yys4)
        print(scene)
        game.da_jie_jie(scene, yys4)
        time.sleep(1)

def team_kun_25():
    game = Team_kun_25()
    yys1 = Handle()
    set_yys(1, game, yys1)
    while 1:
        scene = game.get_scene(yys1)
        print(scene)
        game.do_work(scene, yys1)
        time.sleep(1)

def tt():
    team_kun_25()

if __name__ == "__main1__":
    print("开始")
    set_windows()
    print("结束")

if __name__ == "__main1__":
    print("开始")
    jie_jie2()
    print("结束")

if __name__ == "__main1__":
    print("开始")
    hun_shi()
    print("结束")

if __name__ == "__main1__":
    print("开始")
    da_liao_jie_jie()
    print("结束")

if __name__ == "__main1__":
    print("开始")
    # 组队打困25
    team_kun_25()
    print("结束")

if __name__ == "__main__":
    print("开始")
    tt()
    print("结束")


