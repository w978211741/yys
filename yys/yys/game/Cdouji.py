from Cgame import Game
from Chandle import SceneKey
from Cimg import Img
from Cmouse import Mouse
from Cwindow import Window
import sys
import codedef
import time


class Dou_ji(Game):

    def do_work(self, argument, handle):
        switcher = {
            SceneKey.NUKOWN: self.error_scene,
            SceneKey.DOU_JI: self.beign_dou_ji,
            SceneKey.ZHANG_DOU_ZHONG: self.exit_dou_ji
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, self.father)(argument, handle)
        # Execute the function
        return func

    def father(self, argument, handle):
        Game.do_work(self, argument, handle)
        return codedef.NORMAL_END

    def beign_dou_ji(self, argument, handle):
        print("开始斗技按钮")
        if self.click_img("yys/开始斗技按钮.bmp", handle) == 0:
            print("开始斗技按钮")
            time.sleep(15)
            return codedef.FIGHT_BEGIN
        return codedef.FIGHT_BEGIN

    def exit_dou_ji(self, argument, handle):
        if self.click_img("yys/退出斗技按钮.bmp", handle) == 0:
            print("退出斗技按钮")
            time.sleep(0.8)
            if self.click_img("yys/确认退出斗技按钮.bmp", handle) == 0:
                print("确认退出斗技按钮")
        return codedef.NORMAL_END