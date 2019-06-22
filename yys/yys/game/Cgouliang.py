import codedef
from Cimg import Img
import time
from Cwindow import Window
from Cmouse import Mouse
import cv2
import numpy as np
import aircv as ac


class Gouliang():
    def __init__(self, metrics_x, metrics_y, handle):
        self.accuracy = 0.8
        self.metrics_x = metrics_x
        self.metrics_y = metrics_y
        self.handle = handle
        pass

    def get_point(self, left, right, bottom):
        point = [int(left * (self.handle.right - self.handle.left)), 0]
        point2 = [int(right * (self.handle.right - self.handle.left)),
                  int(bottom * (self.handle.bottom - self.handle.top))]
        return point, point2

    # 判断队员左边式神是否满级 TRUE满级
    def is_left_max(self):
        point, point2 = self.get_point(codedef.left_left, codedef.left_right, codedef.left_bottom)
        return self.is_max(point, point2, self.accuracy)

    # 判断队员中间式神是否满级 TRUE满级
    def is_mid_max(self):
        point, point2 = self.get_point(codedef.mid_left, codedef.mid_right, codedef.mid_bottom)
        return self.is_max(point, point2, self.accuracy)

    # 判断队员右边式神是否满级 TRUE满级
    def is_right_max(self):
        point, point2 = self.get_point(codedef.right_left, codedef.right_right, codedef.right_bottom)
        return self.is_max(point, point2, self.accuracy)

    # 判断队长左边式神是否满级 TRUE满级
    def is_left_max_c(self):
        point, point2 = self.get_point(codedef.left_left_c, codedef.left_right_c, codedef.left_bottom_c)
        return self.is_max(point, point2, self.accuracy)

    # 判断队长右边式神是否满级 TRUE满级
    def is_right_max_c(self):
        point, point2 = self.get_point(codedef.right_left_c, codedef.right_right_c, codedef.right_bottom_c)
        return self.is_max(point, point2, self.accuracy)

    # 判断指定位置式神是否满级 TRUE满级
    def is_max(self, point, point2, accuracy):
        # 返回找到的图的位置 在指定路径的图《裁剪后》找另一路径的图
        re, x, y = Img.find_img_in_cut_img(src_img_path='temp/temp.bmp', target_img_path='yys/满级标记.bmp',
                                           point=point, point2=point2, accuracy=accuracy)
        if re == 0:
            return True
        return False

    # 判断指定位置式神是否已上场 TRUE上场
    def is_fight(self, point, point2, accuracy):
        # 返回找到的图的位置 在指定路径的图《裁剪后》找另一路径的图
        re, x, y = Img.find_img_in_cut_img(src_img_path='temp/temp.bmp', target_img_path='yys/已上场.bmp',
                                           point=point, point2=point2, accuracy=accuracy)
        if re == 0:
            return True
        return False

    # 取队长右边式神中心坐标
    def get_right_xy_c(self):
        return self.get_xy(codedef.right_left_c, codedef.right_right_c,
                           codedef.right_top_c, codedef.right_bottom_c)

    # 取队长左边式神中心坐标
    def get_left_xy_c(self):
        return self.get_xy(codedef.left_left_c, codedef.left_right_c, codedef.left_top_c, codedef.left_bottom_c)

    # 取队员左边式神中心坐标
    def get_left_xy(self):
        return self.get_xy(codedef.left_left, codedef.left_right, codedef.left_top, codedef.left_bottom)

    # 取队员左边式神中心坐标
    def get_mid_xy(self):
        return self.get_xy(codedef.mid_left, codedef.mid_right, codedef.mid_top, codedef.mid_bottom)

    # 取队员右边式神中心坐标
    def get_right_xy(self):
        return self.get_xy(codedef.right_left, codedef.right_right, codedef.right_top, codedef.right_bottom)

    # 取中心坐标
    def get_xy(self, left, right, top, bottom):
        handle = self.handle
        x = handle.left + int((left * (handle.right - handle.left)
                               + right * (handle.right - handle.left)) / 2)
        y = handle.top + int((top * (handle.bottom - handle.top)
                              + bottom * (handle.bottom - handle.top)) / 2)
        return x, y

    # 取得第一个不满级n卡坐标 找到返回0, x, y
    def get_not_max_n(self):
        handle = self.handle
        # n 卡分块
        top = codedef.n_top
        left = codedef.n_left
        bottom = codedef.n_bottom
        right = codedef.n_right
        kuang = int((right - left) * (handle.right - handle.left) / 6)
        i = 0
        while i < 6:
            point = [int(left * (handle.right - handle.left)) + kuang * (i + 0), int(top * (handle.bottom - handle.top))]
            point2 = [int(left * (handle.right - handle.left)) + kuang * (i + 1),
                      int(bottom * (handle.bottom - handle.top))]

            # 判断指定位置式神是否满级 TRUE满级
            if self.is_max(point, point2, accuracy=0.8) is False:
                # 判断指定位置式神是否已上场 TRUE上场
                if self.is_fight(point, point2, accuracy=0.8) is False:
                    x = handle.left + int(left * (handle.right - handle.left) + kuang * (i + 0.5))
                    y = handle.top + int((bottom + top) * (handle.bottom - handle.top) / 2)
                    return 0, x, y

            i += 1
        return -1, -1, -1

    # 找没满级狗粮和拖上去替换 打手默认放右边 c_flag：队长时为True b_flag:带打手时为True
    def find_and_huang(self, c_flag, b_flag):
        if c_flag:
            # 判断队长左边式神是否满级 TRUE满级
            if self.is_left_max_c():
                # 取队长左边式神中心坐标
                tar_x, tar_y = self.get_left_xy_c()
                # 取得第一个不满级n卡坐标 找到返回0, x, y
                re, src_x, src_y = self.get_not_max_n()
                if re == 0:
                    self.tuo(src_x, src_y, tar_x, tar_y)

            if b_flag is False:
                # 判断队长右边式神是否满级 TRUE满级
                if self.is_right_max_c():
                    # 取队长左边式神中心坐标
                    tar_x, tar_y = self.get_right_xy_c()
                    # 取得第一个不满级n卡坐标 找到返回0, x, y
                    re, src_x, src_y = self.get_not_max_n()
                    if re == 0:
                        self.tuo(src_x, src_y, tar_x, tar_y)
        else:
            # 判断队员左边式神是否满级 TRUE满级
            if self.is_left_max():
                # 取队长左边式神中心坐标
                tar_x, tar_y = self.get_left_xy()
                # 取得第一个不满级n卡坐标 找到返回0, x, y
                re, src_x, src_y = self.get_not_max_n()
                if re == 0:
                    self.tuo(src_x, src_y, tar_x, tar_y)

            # 判断队员中间式神是否满级 TRUE满级
            if self.is_mid_max():
                # 取队员中间式神中心坐标
                tar_x, tar_y = self.get_mid_xy()
                # 取得第一个不满级n卡坐标 找到返回0, x, y
                re, src_x, src_y = self.get_not_max_n()
                if re == 0:
                    self.tuo(src_x, src_y, tar_x, tar_y)

            if b_flag is False:
                # 判断队员右边式神是否满级 TRUE满级
                if self.is_right_max():
                    # 取队员右边式神中心坐标
                    tar_x, tar_y = self.get_right_xy()
                    # 取得第一个不满级n卡坐标 找到返回0, x, y
                    re, src_x, src_y = self.get_not_max_n()
                    if re == 0:
                        self.tuo(src_x, src_y, tar_x, tar_y)

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

        while i < 10:
            time.sleep(0.03)
            m.mouse_to(x, y + ddy * i)  # 鼠标移动到
            i += 1

        i = 1
        ddx = int(dx / 10)

        while i < 10:
            time.sleep(0.03)
            m.mouse_to(x + ddx * i, tar_y)  # 鼠标移动到
            i += 1

        m.mouse_to(tar_x, tar_y)  # 鼠标移动到

        m.left_up()

        time.sleep(1)
        Window.temp_jie_tu(self.handle)# 更新截图
        return

