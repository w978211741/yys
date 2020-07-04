from Cgame import Game
from Chandle import SceneKey
from Cimg import Img
from Cmouse import Mouse
from Cwindow import Window
import sys
import codedef
import time
from win32api import GetSystemMetrics


class Nka(Game):

    def __init__(self):
        super(Nka, self).__init__()
        self.metrics_x = GetSystemMetrics(0)    # 获取分辨率
        self.metrics_y = GetSystemMetrics(1)    # 获取分辨率

    def do_work(self, argument, handle):
        switcher = {
            SceneKey.NUKOWN: self.error_scene,
            SceneKey.ZHAO_HUAN: self.this_begin,
            SceneKey.CHOU_N_KA: self.this_chou
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
        if Game.if_exist(path + "召唤界面.bmp") == 0:
            return SceneKey.ZHAO_HUAN
        if Game.if_exist(path + "抽N卡界面.bmp") == 0:
            return SceneKey.CHOU_N_KA
        return SceneKey.NUKOWN

    def this_begin(self, argument, handle):
        if self.click_img("yys/普通召唤按钮.bmp", handle, 0.98) == 0:
            time.sleep(1.5)
        return codedef.FIGHT_BEGIN

    def this_chou(self, argument, handle):
        if self.click_img("yys/再次召唤按钮.bmp", handle, 0.98) == 0:
            time.sleep(0.5)
            return codedef.FIGHT_BEGIN
        else:
            src_y = handle.top + int((handle.bottom - handle.top) * 2 / 5)
            tar_y = src_y
            src_x = handle.left + int((handle.right - handle.left) * 1 / 6)
            tar_x = handle.left + int((handle.right - handle.left) * 5 / 6)
            self.tuo(src_x, src_y, tar_x, tar_y)
            return codedef.FIGHT_END


    def tuo(self, src_x, src_y, tar_x, tar_y):
        m = Mouse(self.metrics_x, self.metrics_y)
        dx = tar_x - src_x
        dy = tar_y - src_y
        x = src_x
        y = src_y
        m.mouse_to(x, y)  # 鼠标移动到
        m.left_down()
        i = 1
        ddy = int(dy / 10)
        ddx = int(dx / 10)

        while i < 10:
            time.sleep(0.03)
            m.mouse_to(x + ddx * i, y + ddy * i)  # 鼠标移动到
            i += 1

        time.sleep(0.02)
        m.mouse_to(tar_x, tar_y)  # 鼠标移动到
        time.sleep(0.1)
        m.left_up()

        time.sleep(1)
        return
