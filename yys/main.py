#encoding=utf-8
from Cgame import Game, SceneKey
from Chandle import Handle
import time


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


def jie_jie():
    game = Game()
    yys1 = Handle()
    set_yys(1, game, yys1)
    index = 1
    while 1:
        index = index + 1
        if index > 5500:
            return
        scene = game.get_scene(yys1)
        print(scene)
        game.da_jie_jie(scene, yys1)
        time.sleep(1)


def jie_jie2():
    game = Game()
    yys1 = Handle()
    set_yys(1, game, yys1)
    yys2 = Handle()
    set_yys(2, game, yys2)
    index = 1
    while 1:
        index = index + 1
        if index > 5500:
            return
        scene = game.get_scene(yys1)
        print(scene)
        game.da_jie_jie(scene, yys1)
        time.sleep(1)
        scene = game.get_scene(yys2)
        print(scene)
        game.da_jie_jie(scene, yys2)
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





if __name__ == "__main1__":
    print("开始")
    set_windows()
    print("结束")

if __name__ == "__main1__":
    print("开始")
    jie_jie2()
    print("结束")
if __name__ == "__main__":
    print("开始")
    hun_shi()
    print("结束")
