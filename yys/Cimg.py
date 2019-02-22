import aircv as ac
import cv2
import numpy as np
from Cdistinguish import Distinguish


class Img:

    # 返回找到的图的数量
    @staticmethod
    def find_all_img_in_img(src_img_path, target_img_path, accuracy):
        src_img = cv2.imdecode(np.fromfile(src_img_path,dtype=np.uint8), -1)
        target_img = cv2.imdecode(np.fromfile(target_img_path, dtype=np.uint8), -1)
        pos = ac.find_all_template(src_img, target_img, accuracy)
        if pos is None:
            return -1
        return len(pos)

    @staticmethod
    def find_img_in_img(src_img_path,target_img_path, accuracy=0.5):
        src_img = cv2.imdecode(np.fromfile(src_img_path,dtype=np.uint8), -1)
        target_img = cv2.imdecode(np.fromfile(target_img_path, dtype=np.uint8), -1)
        pos = ac.find_template(src_img, target_img, accuracy)
        if pos is None:
            return -1
        circle_center_pos = pos['result']
        return 0, int(circle_center_pos[0]), int(circle_center_pos[1])

    @staticmethod
    def find_str_in_img(src_img_path, target_img_path, x1, y1, width, height):
        re, x, y = Img.find_img_in_img(src_img_path, target_img_path)
        if re != 0:
            return "-1"
        src_img = cv2.imread(src_img_path)
        se = src_img.shape
        max_height = se[0]
        max_width = se[1]
        point1 = [int(x - width / 2) + x1, int(y - height / 2) + y1]  # 左上角
        point2 = [int(x + width / 2) + x1, int(y + height / 2) + y1]  # 右下角
        if point1[0] < 0:
            point1[0] = 0
        if point1[1] < 0:
            point1[1] = 0
        if point2[0] < 0:
            point2[0] = 0
        if point2[1] < 0:
            point2[1] = 0
        if point2[0] > max_width:
            point2[0] = max_width
        if point2[1] > max_height:
            point2[1] = max_height
        if point1[0] > point2[0] or point1[1] > point2[1]:
            return "-2"
        tag_img = Img.cut_img(src_img, point1, point2)
        gray_img = cv2.cvtColor(tag_img, cv2.COLOR_BGR2GRAY)
        img_info = gray_img.shape
        image_height = img_info[0]
        image_weight = img_info[1]
        dst = np.zeros((image_height, image_weight, 1), np.uint8)
        for i in range(image_height):
            for j in range(image_weight):
                gray_pixel = gray_img[i][j]
                dst[i][j] = 255 - gray_pixel
        temp_path = "temp/findStrInImg.bmp"
        cv2.imwrite(temp_path, dst)
        # 文字识别
        text = Distinguish.img_path2string(temp_path)
        return text

    # 裁剪
    @staticmethod
    def cut_img(src_img, point_from, point_to):
        tag_img = src_img[point_from[1]:point_to[1], point_from[0]:point_to[0]]
        return tag_img

    @staticmethod
    def cut_img_path(src_img_Path, point_from, point_to):
        src_img = cv2.imread(src_img_Path)
        tag_img = src_img[point_from[1]:point_to[1], point_from[0]:point_to[0]]
        return tag_img

    @staticmethod
    def save(name, img):
        cv2.imwrite(name, img)
