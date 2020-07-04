from Cgame import Game
from Chandle import SceneKey
from Cimg import Img
from Cmouse import Mouse
from Cwindow import Window
import sys
import codedef
import time
from win32api import GetSystemMetrics


class Zabaigui(Game):

    def __init__(self):
        super(Zabaigui, self).__init__()
        self.m = Mouse()

    def do_work(self, argument, handle):
        switcher = {
            SceneKey.NUKOWN: self.error_scene,
            SceneKey.BAI_GUI_YE_XING: self.this_begin,
            SceneKey.BAI_GUI_ZHONG: self.this_za,
            SceneKey.BAI_GUI_QI_YUE_SHU: self.fight_end,
            SceneKey.BAI_GUI_GUI_WANG: self.xuan_gui_wang
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, self.father)(argument, handle)
        # Execute the function
        return func

    def father(self, argument, handle):
        Game.do_work(self, argument, handle)
        return codedef.NORMAL_END

    def get_scene(self, handle):
        window_img = self.window.jie_tu(handle)
        window_img.save('temp/temp.bmp')
        path = "yys/scene/"
        if Game.if_exist(path + "百鬼夜行界面.bmp") == 0:
            return SceneKey.BAI_GUI_YE_XING
        if Game.if_exist(path + "百鬼中界面.bmp") == 0:
            return SceneKey.BAI_GUI_ZHONG
        if Game.if_exist(path + "百鬼契约书界面.bmp") == 0:
            return SceneKey.BAI_GUI_QI_YUE_SHU
        if Game.if_exist(path + "百鬼鬼王界面.bmp") == 0:
            return SceneKey.BAI_GUI_GUI_WANG
        return SceneKey.NUKOWN

    def this_begin(self, argument, handle):
        if self.click_img("yys/进入百鬼按钮.bmp", handle, 0.98) == 0:
            time.sleep(1.5)
        return codedef.NORMAL_END

    def this_za(self, argument, handle):

        x = handle.left + int((handle.right - handle.left) * 5 / 6)
        y = handle.top + int((handle.bottom - handle.top) / 2)
        self.m.click(x, y)
        time.sleep(0.2)
        self.m.click(x, y)
        time.sleep(0.4)
        x = handle.left + int((handle.right - handle.left) * 4 / 6)
        y = handle.top + int((handle.bottom - handle.top) / 2)
        self.m.click(x, y)
        time.sleep(0.2)
        self.m.click(x, y)
        time.sleep(0.4)
        x = handle.left + int((handle.right - handle.left) * 3 / 6)
        y = handle.top + int((handle.bottom - handle.top) / 2)
        self.m.click(x, y)
        time.sleep(0.2)
        self.m.click(x, y)
        time.sleep(0.4)
        return codedef.NORMAL_END

    def xuan_gui_wang(self, argument, handle):
        x = handle.left + int((handle.right - handle.left) / 2)
        y = handle.top + int((handle.bottom - handle.top) / 2)
        self.m.click(x, y)
        time.sleep(0.2)
        self.click_img("yys/开始百鬼按钮.bmp", handle, 0.98)
        return codedef.FIGHT_BEGIN