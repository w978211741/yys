from Cgame import Game, SceneKey
from Cimg import Img
from Cmouse import Mouse
from Cwindow import Window
import sys
import time


class Team_kun_25(Game):

    def do_work(self, argument, handle):
        switcher = {
            SceneKey.NUKOWN: self.error_scene,
            SceneKey.ZHANG_DOU_SHI_BAI: self.fight_end,
            SceneKey.ZHANG_DOU_SHENG_LI: self.fight_end,
            SceneKey.ZHANG_DOU_JIANG_LI: self.fight_end,
            # 基类：按红叉退出(经测试，结界突破和探索章节的退出按钮，与细红叉一致)
            SceneKey.JIE_JIE_TU_PO: self.hon_cha_exit,
            SceneKey.TANG_SUO: self.find_25_button,
            SceneKey.ZHANG_DOU_ZHONG: self.waiting,
            SceneKey.XUAN_SHANG_FENG_YING_YAO_QING: self.hon_cha_exit,
            SceneKey.TANG_SUO_ZHANG_JIE: self.team_kun_25_main,
            SceneKey.TANG_SUO_ZHONG: self.da_tang_suo
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, self.error_scene)(handle)
        # Execute the function
        return func

    def find_25_button(self,handle):
        if self.click_img("yys/第十五章.bmp", handle, 0.90) == 0:
            print("第十五章")
            return 0
        re, x, y = self.window.find_img(handle, "yys/大第.bmp", 0.5)
        if re == 0:
            mouse = Mouse()
            mouse.absolute(x, y, 0, -100)
            return 0
        return 0


    def team_kun_25_main(self,handle):
        if self.if_exist("yys/第十五章阴界裂缝.bmp") == 0:
            if self.click_img("yys/探索困难按钮.bmp", handle, 0.90) == 0:
                print("探索困难按钮")
                return 0
            if self.click_img("yys/探索按钮.bmp", handle, 0.90) == 0:
                print("探索按钮")
                return 0
        else:
            # 不是目标章节
            self.hon_cha_exit(handle)
        return 0