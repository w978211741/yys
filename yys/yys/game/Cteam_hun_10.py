from Cgame import Game, SceneKey
from Cmouse import Mouse
from Cimg import Img
import time


class Team_hun_10(Game):
    def do_work(self, argument, handle):
        switcher = {
            SceneKey.XIE_ZHAN_DUI_WU: self.teaming,
            SceneKey.MO_REN_YAOQ_QING_DUI_YOU: self.mo_ren_yao_qing_dui_you,
            SceneKey.SHI_FOU_YAO_QING_JI_XU: self.yao_qing_dui_you_ji_xu
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, self.father)(handle)
        # Execute the function
        return func

    def father(self, argument, handle):
        Game.do_work(self, argument, handle)
        return 0

    def team_hun_10_main(self, argument, handle):
        pass
