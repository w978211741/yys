from Cteam_kun_25 import Team_kun_25
from Cgame import Game
from Chandle import SceneKey
from Cimg import Img
from Cmouse import Mouse
from Cwindow import Window
import sys
import time
import codedef


class Team_kun_25_captain(Team_kun_25):
    def __init__(self, UP=None, BOSS=True):
        super(Team_kun_25, self).__init__()
        self.UP = UP
        self.BOSS = BOSS

    def do_work(self, argument, handle):
        switcher = {
            SceneKey.TANG_SUO_ZHONG: self.this_da_tang_suo,
            SceneKey.SHI_FOU_YAO_QING_JI_XU: self.this_yao_qing_dui_you_ji_xu,
            SceneKey.SHOU_DAO_YAO_QING: self.shou_dao_yai_qing
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, self.father)(argument, handle)
        # Execute the function
        return func

    def this_da_tang_suo(self, argument, handle):
        self.da_tang_suo(handle)
        return self.da_tang_suo_gui(handle)

    def this_yao_qing_dui_you_ji_xu(self, argument, handle):
        return codedef.YAO_QING_DUI_YOU_JI_XU

    def father(self, argument, handle):
        return Team_kun_25.do_work(self, argument, handle)

    def shou_dao_yai_qing(self, argument, handle):
        if self.click_img("yys/粗红叉按钮2.bmp", handle, 0.90) == 0:
            print("粗红叉按钮2")
        return codedef.NORMAL_END

    # 在探索中界面打探索怪
    def da_tang_suo_gui(self, handle):
        if self.UP != codedef.UP_C_NULL:
            if self.fight_UP_guai(handle, self.UP, "yys/打小怪.bmp") == codedef.NORMAL_END:
                return -21
            else:
                if self.fight_UP_guai(handle, self.UP, "yys/打小怪.bmp") == codedef.NORMAL_END:
                    return -21
        else:
            if self.click_img("yys/打小怪.bmp", handle) == 0:
                print("打小怪")
                return -21

        if self.BOSS and self.click_img("yys/打boss.bmp", handle) == 0:
            print("打boss")
            return -22
        elif self.click_img("yys/探索奖励.bmp", handle) == 0:
            print("探索奖励")
            return -31
        elif self.click_img("yys/打小怪2.bmp", handle) == 0:
            print("打小怪2")
            return -21
        elif self.click_img("yys/探索向右走.bmp", handle) == 0:
            print("探索向右走")
            return -32
        return codedef.NORMAL_END

    #         target_rad = [35, 45, 213]
    #         target_mi = [163, 203, 223]
    #         target_yellow = [112, 200, 217]
    def find_UP(self, x, UP, src_img_path):
        if UP == codedef.UP_C_COIN:
            target_BGR = codedef.UP_COIN
        elif UP == codedef.UP_C_EXP:
            target_BGR = codedef.UP_EXP
        elif UP == codedef.UP_C_REWARD:
            target_BGR = codedef.UP_REWARD
        else:
            return codedef.ERROR_END
        point_from = [x - 100, 0]
        point_to = [x + 100, 500]
        src_img = Img.cut_img_path(src_img_path, point_from, point_to)
        # Img.save("temp/tt.bmp", src_img)

        # src_img = Img.read_img("temp/tt.bmp")
        img_info = src_img.shape
        # BGR
        image_height = img_info[0]
        image_weight = img_info[1]

        dxx = [3, 3, 3]
        max = 20
        index = 0
        for w in range(image_height):
            for j in range(image_weight):
                yxx = list(abs(src_img[w][j] - target_BGR))
                if yxx[0] < dxx[0] and yxx[1] < dxx[1] and yxx[2] < dxx[2]:
                    index += 1
                    if index > max:
                        return codedef.NORMAL_END
        return codedef.ERROR_END

    def fight_UP_guai(self, handle, UP, target_img_path):
        Window.temp_jie_tu(handle)
        src_img_path = 'temp/temp.bmp'
        # target_img_path = 'yys/打小怪.bmp'
        pos_list = Img.find_all_pos_img_in_img(src_img_path, target_img_path, 0.9)
        if pos_list is None:
            return codedef.ERROR_END
        for i in range(len(pos_list)):
            x = int(pos_list[i]['result'][0])
            if self.find_UP(x, UP, src_img_path) == codedef.NORMAL_END:
                y = int(pos_list[i]['result'][1])
                mouse = Mouse()
                mouse.click(handle.left + x, handle.top + y)
                return codedef.NORMAL_END
        return codedef.ERROR_END