from Cteam_kun_25 import Team_kun_25
from Cgame import Game, SceneKey
from Cimg import Img
from Cmouse import Mouse
from Cwindow import Window
import sys
import time


class Team_kun_25_captain(Team_kun_25):
    def do_work(self, argument, handle):

        switcher = {
            SceneKey.TANG_SUO_ZHANG_JIE: self.team_kun_25_captain_main,
            SceneKey.ZU_DUI_XUAN_ZE_DUI_YOU: self.xuan_ze_dui_you,
            SceneKey.TANG_SUO_ZHONG: self.this_da_tang_suo,
            SceneKey.SHI_FOU_YAO_QING_JI_XU: self.this_yao_qing_dui_you_ji_xu
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, self.father)(argument, handle)
        # Execute the function
        return func

    def this_da_tang_suo(self, argument, handle):
        if self.da_tang_suo(handle) != -1:
            self.da_tang_suo_gui(handle)
        return 0

    def this_yao_qing_dui_you_ji_xu(self, argument, handle):
        self.yao_qing_dui_you_ji_xu(handle)
        return 5

    def father(self, argument, handle):
        Team_kun_25.do_work(self, argument, handle)
        return 0

    def team_kun_25_captain_main(self, argument, handle):
        if self.if_exist("yys/第二十五章祭品巫女后编.bmp") == 0:
            if self.click_img("yys/探索困难按钮.bmp", handle, 0.90) == 0:
                print("探索困难按钮")
                return 0
            if self.click_img("yys/组队按钮.bmp", handle, 0.90) == 0:
                print("组队按钮")
                return 0
        else:
            # 不是目标章节
            self.hon_cha_exit(handle)
        return 0

    def xuan_ze_dui_you(self, argument, handle):
        if self.click_img("yys/组队好友灰.bmp", handle, 0.90) == 0:
            print("组队好友灰")
        if self.if_exist("yys/选定好友.bmp") == 0:
            if self.click_img("yys/邀请按钮.bmp", handle, 0.90) == 0:
                print("邀请按钮")
                captainwait = 5
                return captainwait
        if self.click_img("yys/组队让他让.bmp", handle, 0.90) == 0:
            print("组队让他让")
            return 0
        re, x, y = self.window.find_img(handle, "yys/scene/组队选择队友界面.bmp", 0.5)
        if re == 0:
            mouse = Mouse()
            mouse.absolute(x, y + 200, 0, -100)
            return 0
        return 0
