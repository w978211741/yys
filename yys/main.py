# encoding=utf-8
from Cgame import Game,SceneKey
from Chandle import Handle
import time


def dou_ji():
    error_number = 1
    scene = SceneKey.NUKOWN
    game = Game()
    yys1 = Handle()
    game.set_window(yys1, "[#] [yys1] 阴阳师-网易游戏 [#]", 10, 10, 520)  # 注意空格
    print(yys1.hwnd, yys1.left, yys1.top, yys1.right, yys1.bottom)
    if yys1.hwnd == 0:
        print("不能找全窗口")
        return 0
    while 1:
        # 确定自己在哪个场景
        scene = game.get_scene(yys1)
        print("1" + str(scene))
        # 将判断后的结果场景代码传入，根据不同场景调用不同函数
        game.dou_ji(scene, yys1)
        time.sleep(3)


def hun_shi_main():
    error_number = 1
    scene = SceneKey.NUKOWN
    game = Game()
    yys1 = Handle()

    game.set_window(yys1, "[#] [yys2] 阴阳师-网易游戏 [#]", 10, 10, 520)#注意空格
    print(yys1.hwnd, yys1.left, yys1.top, yys1.right, yys1.bottom)
    yys2 = Handle()
    game.set_window(yys2, "[#] [yys4] 阴阳师-网易游戏 [#]", 10, 10, 520)#注意空格
    print(yys2.hwnd, yys2.left, yys2.top, yys2.right, yys2.bottom)
    if yys1.hwnd == 0 or yys2.hwnd == 0:
        print("不能找全窗口")
        return 0
    while 1:
        # 确定自己在哪个场景
        scene = game.get_scene(yys1)
        print("1"+str(scene))
        # 将判断后的结果场景代码传入，根据不同场景调用不同函数
        game.hun_shi_team(scene,yys1)
        time.sleep(3)
        scene = game.get_scene(yys2)
        print("2"+str(scene))
        # 将判断后的结果场景代码传入，根据不同场景调用不同函数
        game.hun_shi_team(scene,yys2)
        time.sleep(3)


if __name__ == '__main__':
    print("开始")
    # dou_ji()
    print("结束")