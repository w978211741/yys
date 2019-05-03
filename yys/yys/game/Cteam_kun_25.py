from Cgame import Game, SceneKey
from Cimg import Img
from Cmouse import Mouse
from Cwindow import Window
import sys
import time


class Team_kun_25(Game):

    def do_work(self, argument, handle):
        switcher = {
            SceneKey.JIE_JIE_TU_PO: self.hon_cha_exit,
            SceneKey.TANG_SUO: self.find_25_button,
            SceneKey.TANG_SUO_ZHANG_JIE: self.team_kun_25_main,
            SceneKey.MO_REN_YAOQ_QING_DUI_YOU: self.this_mo_ren_yao_qing_dui_you
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, self.ffather)(argument, handle)
        # Execute the function
        return func

    def this_mo_ren_yao_qing_dui_you(self, argument, handle):
        ti_li = self.get_ti_li(handle)
        print(ti_li)
        if ti_li < 24 and ti_li != -1:
            return -3
        self.mo_ren_yao_qing_dui_you(argument, handle)
        return 0

    def ffather(self, argument, handle):
        return Game.do_work(self, argument, handle)

    def find_25_button(self, argument, handle):
        ti_li = self.get_ti_li(handle)
        print(ti_li)
        if ti_li < 24 and ti_li != -1:
            return -3
        if self.click_img("yys/第十五章.bmp", handle, 0.90) == 0:
            print("第十五章")
            return 0
        re, x, y = self.window.find_img(handle, "yys/大第.bmp", 0.5)
        if re == 0:
            mouse = Mouse()
            mouse.absolute(x, y, 0, -100)
            return 0
        return 0

    def team_kun_25_main(self, argument, handle):
        if self.if_exist("yys/第二十五章祭品巫女后编.bmp") == 0:
            if self.click_img("yys/探索困难按钮.bmp", handle, 0.90) == 0:
                print("探索困难按钮")
                return 0
            if self.click_img("yys/探索按钮.bmp", handle, 0.90) == 0:
                print("探索按钮")
                return 0
        else:
            # 不是目标章节
            self.hon_cha_exit(argument, handle)
        return 0
