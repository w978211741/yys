import codedef
from Cimg import Img
import time
from Cwindow import Window
from Cmouse import Mouse


class FightUp():
    def __init__(self, metrics_x):
        self.metrics_x = metrics_x  #分辨率

    #         target_rad = [35, 45, 213]
    #         target_mi = [163, 203, 223]
    #         target_yellow = [112, 200, 217]
    def find_UP(self, x, y, UP, src_img_path):
        if UP == codedef.UP_C_COIN:
            target_BGR = codedef.UP_COIN
        elif UP == codedef.UP_C_EXP:
            target_BGR = codedef.UP_EXP
        elif UP == codedef.UP_C_REWARD:
            target_BGR = codedef.UP_REWARD
        else:
            return codedef.ERROR_END
        point_from = [x - 80, y + 50]
        point_to = [x + 80, y + 160]
        src_img = Img.cut_img_path(src_img_path, point_from, point_to)
        # Img.save("temp/tt.bmp", src_img)

        # src_img = Img.read_img("temp/tt.bmp")
        img_info = src_img.shape
        # BGR
        image_height = img_info[0]
        image_weight = img_info[1]

        dxx = [3, 3, 3]
        max = 10
        if self.metrics_x == 1920:
            pass
        else:
            dxx = [5, 5, 5]
            max = 5
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
        src_img_path1 = 'temp/temp1.bmp'
        Window.temp_jie_tu(handle, src_img_path1)
        if self.witch_up(handle, UP, src_img_path1, target_img_path) == codedef.NORMAL_END:
            return codedef.NORMAL_END
        time.sleep(0.4)

        src_img_path2 = 'temp/temp2.bmp'
        Window.temp_jie_tu(handle, src_img_path2)
        if self.witch_up(handle, UP, src_img_path2, target_img_path) == codedef.NORMAL_END:
            return codedef.NORMAL_END
        time.sleep(0.4)

        src_img_path3 = 'temp/temp3.bmp'
        Window.temp_jie_tu(handle, src_img_path3)
        if self.witch_up(handle, UP, src_img_path3, target_img_path) == codedef.NORMAL_END:
            return codedef.NORMAL_END
        return codedef.ERROR_END

    def witch_up(self, handle, UP, src_img_path, target_img_path):
        pos_list = Img.find_all_pos_img_in_img(src_img_path, target_img_path, 0.9)
        if pos_list is None:
            return codedef.ERROR_END
        for i in range(len(pos_list)):
            x = int(pos_list[i]['result'][0])
            y = int(pos_list[i]['result'][1])
            if self.find_UP(x, y, UP, src_img_path) == codedef.NORMAL_END:
                mouse = Mouse()
                # mouse.mouse_to(handle.left + x, handle.top + y)
                mouse.click(handle.left + x, handle.top + y)
                return codedef.NORMAL_END
        return codedef.ERROR_END
