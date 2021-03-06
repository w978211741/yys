from Cgame import Game
from Chandle import SceneKey
from Cmouse import Mouse
from Cimg import Img
import time
import codedef


class Team_hun_10(Game):

    def judge_scenes(self, argument, handle):
        return Game.judge_scenes(self, argument, handle)

    def do_work(self, argument, handle):
        if self.judge_scenes(argument, handle) == codedef.SCENCE_REPEAT_END:
            return codedef.SCENCE_REPEAT_END
        switcher = {
            SceneKey.XIE_ZHAN_DUI_WU: self.inTeam,
            SceneKey.MO_REN_YAOQ_QING_DUI_YOU: self.mo_ren_yao_qing_dui_you,
            SceneKey.SHI_FOU_YAO_QING_JI_XU: self.yao_qing_dui_you_ji_xu,
            SceneKey.SHOU_DAO_YAO_QING: self.shou_dao_yai_qing
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, self.father)(argument, handle)
        # Execute the function
        return func

    def inTeam(self, argument, handle):
        return codedef.HUN_SHI_TEAMING

    def father(self, argument, handle):
        return Game.do_work(self, argument, handle)

    def team_hun_10_main(self, argument, handle):
        pass

    def shou_dao_yai_qing(self, argument, handle):
        if self.click_img("yys/自动加入队伍按钮.bmp", handle, 0.90) == 0:
            print("自动加入队伍按钮")
            time.sleep(0.8)
            return self.mo_ren_yao_qing_dui_you(argument, handle)
        if self.click_img("yys/接受邀请按钮.bmp", handle, 0.90) == 0:
            print("接受邀请按钮")
            return codedef.NORMAL_END
        return codedef.NORMAL_END

    def dian_guai_11(self, handle):
        x = int((handle.right + handle.left) / 2)
        xishu = 0.2
        y = int((handle.top + (handle.bottom - handle.top) * xishu))
        m = Mouse()
        m.click(x, y)