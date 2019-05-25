from Cgame import Game
from Chandle import SceneKey
from Cimg import Img
from Cmouse import Mouse
from Cwindow import Window
import time
import codedef


class Team_kun_25(Game):
    def __init__(self):
        super(Game, self).__init__()
        pass

    def judge_scenes(self, argument, handle):
        return Game.judge_scenes(self, argument, handle)

    def do_work(self, argument, handle):
        switcher = {
            SceneKey.JIE_JIE_TU_PO: self.hon_cha_exit,
            SceneKey.MO_REN_YAOQ_QING_DUI_YOU: self.this_mo_ren_yao_qing_dui_you
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, self.ffather)(argument, handle)
        # Execute the function
        return func

    def this_mo_ren_yao_qing_dui_you(self, argument, handle):
        return self.mo_ren_yao_qing_dui_you(argument, handle)

    def ffather(self, argument, handle):
        return Game.do_work(self, argument, handle)

    def exit_tang_suo(self, handle):
        if self.click_img("yys/退出探索.bmp", handle) == 0:
            time.sleep(0.8)
        if self.click_img("yys/确认退出探索按钮.bmp", handle) == 0:
            return codedef.NORMAL_END
        return codedef.ERROR_END
