from Cgame import Game, SceneKey
from Cimg import Img
from Cmouse import Mouse
from Cwindow import Window
import sys
import time


class dashitou(Game):
    def __init__(self):
        Game.__init__(self)
        pass

    def do_work(self, argument, handle):
        switcher = {
            SceneKey.NUKOWN: self.da,
            SceneKey.ZHANG_DOU_SHI_BAI: self.fight_end,
            SceneKey.ZHANG_DOU_SHENG_LI: self.fight_end,
            SceneKey.ZHANG_DOU_JIANG_LI: self.fight_end,
            SceneKey.ZHANG_DOU_ZHONG: self.zhunbei,
            SceneKey.XUAN_SHANG_FENG_YING_YAO_QING: self.hon_cha_exit
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, self.father)(argument, handle)
        # Execute the function
        return func

    def father(self, argument, handle):
        Game.do_work(self, argument, handle)
        return 0

    def zhunbei(self, argument, handle):
        if self.click_img("yys/战斗中准备按钮.bmp", handle, 0.90) == 0:
            print("战斗中准备按钮")
            return -2# 局数计数用
        time.sleep(2)
        return 0

    def da(self, argument, handle):
        if self.if_exist("yys/血月.bmp") == 0:
            print("血月")
            ti_li = self.get_ti_li(handle, 0.55)
            print(ti_li)
            if ti_li > 12 or ti_li == -1:
                #if self.if_exist("yys/挑战石头按钮.bmp") == 0:
                #    print("挑战石头按钮")
                if self.click_img("yys/挑战石头按钮.bmp", handle, 0.90) == 0:
                    print("挑战石头按钮")
                pass
            else:
                return -3
        return 0
