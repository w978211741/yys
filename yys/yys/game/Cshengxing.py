from Cgame import Game
from Chandle import SceneKey
from Cimg import Img
from Cmouse import Mouse
from Cwindow import Window
import sys
import codedef
import time
from win32api import GetSystemMetrics


class shengxing(Game):

    def __init__(self):
        super(shengxing, self).__init__()
        # 获取分辨率
        self.m = Mouse(GetSystemMetrics(0), GetSystemMetrics(1))

    def do_work(self, argument, handle):
        switcher = {
            SceneKey.NUKOWN: self.this_main
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, self.father)(argument, handle)
        # Execute the function
        return func

    def father(self, argument, handle):
        Game.do_work(self, argument, handle)
        return codedef.NORMAL_END

    def get_scene(self, handle):
        return SceneKey.NUKOWN

    def this_main(self, argument, handle):

        if Game.if_exist("yys/轮回秘境.bmp") == 0:
            return codedef.SCENCE_REPEAT_END
        elif Game.if_exist("yys/红蛋.bmp") == 0:
            return codedef.SCENCE_REPEAT_END
        elif Game.if_exist("yys/蓝蛋.bmp") == 0:
            return codedef.SCENCE_REPEAT_END
        elif Game.if_exist("yys/黑蛋.bmp") == 0:
            return codedef.SCENCE_REPEAT_END
        elif Game.if_exist("yys/白蛋.bmp") == 0:
            return codedef.SCENCE_REPEAT_END
        elif self.click_img("yys/确认升星按钮.bmp", handle, 0.98) == 0:
            time.sleep(1)
        elif self.click_img("yys/继续升星按钮.bmp", handle, 0.98) == 0:
            time.sleep(1)

        return codedef.NORMAL_END

