from Cteam_kun_25 import Team_kun_25
from Cgame import Game
from Chandle import SceneKey
from Cimg import Img
from Cmouse import Mouse
from CfightUp import FightUp
import sys
import time
import codedef
from win32api import GetSystemMetrics
from Cgouliang import Gouliang


class SuperGhostKing(Game):

    def __init__(self):
        super(Game, self).__init__()
        pass

    # 重置庭院位置，进町中再回庭院，这样能更好找到探索按钮
    def reset_ting_yuan(self, handle):
        self.click_img("yys/町中.bmp", handle)
        time.sleep(1)
        self.click_img("yys/庭院.bmp", handle)
        time.sleep(1)

    def do_work(self, argument, handle):
        if self.judge_scenes(argument, handle) == codedef.SCENCE_REPEAT_END:
            return codedef.SCENCE_REPEAT_END
        switcher = {
            SceneKey.TANG_SUO_ZHONG: self.this_da_tang_suo,
            SceneKey.SHOU_DAO_YAO_QING: self.this_ju_jue,
            SceneKey.NUKOWN: self.this_nukown,
            SceneKey.TANG_SUO_ZHANG_JIE: self.this_ju_jue,
            SceneKey.TANG_SUO: self.this_tang_suo,
            SceneKey.TING_YUAN: self.this_ting_yuan
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, self.father)(argument, handle)

        return func

    def this_ting_yuan(self, argument, handle):
        if self.click_img("yys/进入探索按钮.bmp", handle) != 0:
            self.reset_ting_yuan(handle)
        return codedef.NORMAL_END

    # 在探索 找鬼王
    def this_tang_suo(self, argument, handle):
        if self.if_exist("yys/超鬼王.bmp") == 0:
            self.click_img("yys/大岳丸.bmp", handle)
            time.sleep(2)
        return codedef.NORMAL_END

    # 探索中，退出
    def this_da_tang_suo(self, argument, handle):
        self.exit_tang_suo(handle)

    # 故事直接跳过
    def this_nukown(self, argument, handle):
        if self.if_exist("yys/故事平安京.bmp") == 0:
            return self.click_img("yys/退出探索.bmp", handle)
        return self.father(argument, handle)

    # 拒绝和叉掉探索章节
    def this_ju_jue(self, argument, handle):
        return self.ju_jue_xuan_shang(argument, handle)

    # 其他情况按父类的处理
    def father(self, argument, handle):
        return Game.do_work(self, argument, handle)


