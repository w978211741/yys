from Cgame import Game
from Chandle import SceneKey
from Cmouse import Mouse
from Cimg import Img
import time


class Team_hun_10(Game):
    def do_work(self, argument, handle):
        switcher = {
            SceneKey.XIE_ZHAN_DUI_WU: self.teaming,
            SceneKey.MO_REN_YAOQ_QING_DUI_YOU: self.mo_ren_yao_qing_dui_you,
            SceneKey.SHI_FOU_YAO_QING_JI_XU: self.yao_qing_dui_you_ji_xu,
            SceneKey.SHOU_DAO_YAO_QING: self.shou_dao_yai_qing
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, self.father)(argument, handle)
        # Execute the function
        return func

    def father(self, argument, handle):
        Game.do_work(self, argument, handle)
        return 0

    def team_hun_10_main(self, argument, handle):
        pass

    def shou_dao_yai_qing(self, argument, handle):
        if self.click_img("yys/自动加入队伍按钮.bmp", handle, 0.90) == 0:
            print("自动加入队伍按钮")
            return 0
        if self.click_img("yys/接受邀请按钮.bmp", handle, 0.90) == 0:
            print("接受邀请按钮")
            return 0
        return 0
