from Cimg import Img
from enum import Enum, unique
from Mouse import Mouse
from Cwindow import Window
import sys
import time


class Game:
    da_guo_le_path = 'yys/打过了.bmp'
    da_bu_guo_path = 'yys/打不过.bmp'
    mei_da_guo_path = 'yys/没打过.bmp'

    # 探索界面的上部分，最后是最上面的长条形截图
    def __init__(self):
        self.src_img_path = 'temp/temp.bmp'
        self.window = Window()

    # 查找指定windows程序窗口，并设置到指定位置和大小，找不到返回-1，找到返回0
    def set_window(self, handle, window_name, x, y, cy):
        class_name = None
        handle.hwnd, handle.left, handle.top, handle.right, handle.bottom = \
            self.window.get_window(class_name, window_name)
        if handle.hwnd == 0:
            return -1
        else:
            height = handle.bottom - handle.top
            weigh = handle.right - handle.left
            if x != handle.left or y != handle.top:
                handle.hwnd, handle.left, handle.top, handle.right, handle.bottom = \
                    self.window.set_window(handle, x, y, weigh, height)
            while height > cy:
                height = height - 20
                if height < cy:
                    height = cy
                    handle.hwnd, handle.left, handle.top, handle.right, handle.bottom = \
                        self.window.set_window(handle.hwnd, handle.left, handle.top, handle.right - handle.left, height)
                time.sleep(1)
            while height < cy:
                height = height + 20
                if height > cy:
                    height = cy
                    handle.hwnd, handle.left, handle.top, handle.right, handle.bottom = \
                        self.window.set_window(handle.hwnd, handle.left, handle.top, handle.right - handle.left, height)
                time.sleep(1)
        return 0

    # 在探索界面获取突破卷数量
    def get_tu_po_juan(self, handle):
        tu = self.window.jie_tu(handle.left, handle.top + 50, handle.right, handle.top + 80)
        tu.save('temp/temp.bmp')
        tag_img_path = "yys/突破卷数量.bmp"
        x1 = 60  # 左右偏移量
        y1 = 1  # 上下偏移量
        width = 70  # 目标宽度
        height = 30  # 目标高度
        tu_po_number_str = Img.find_str_in_img(self.src_img_path, tag_img_path, x1, y1, width, height)
        if tu_po_number_str != "-1":
            tu_po_number_str = tu_po_number_str.split('/')
            tu_po_number = tu_po_number_str[0]
            if tu_po_number == '':
                return -1
            return int(tu_po_number)
        return -1

    def get_tu_po_juan2(self, handle):
        # 获得游戏界面截图
        tu = self.window.jietu(handle.left, handle.bottom - 130, handle.right, handle.bottom - 75)
        tu.save('temp/temp.bmp')
        tag_img_path = "yys/突破卷数量2.bmp"
        x1 = 54  # 左右偏移量
        y1 = 1  # 上下偏移量
        width = 70  # 目标宽度
        height = 30  # 目标高度
        tu_po_number_str = Img.find_str_in_img(self.src_img_path, tag_img_path, x1, y1, width, height)
        if tu_po_number_str != "-1":
            tu_po_number_str = tu_po_number_str.split('/')
            tu_po_number = tu_po_number_str[0]
            if tu_po_number == '':
                return -1
            return int(tu_po_number)
        return -1

    def get_ti_li(self, handle):
        # 获得游戏界面截图
        tu = self.window.jietu(handle.left, handle.top + 50, handle.right, handle.top + 80)
        tu.save('temp/temp.bmp')
        target_img_path = "yys/体力数量.bmp"
        x1 = 65  # 左右偏移量
        y1 = 1  # 上下偏移量
        width = 95  # 目标宽度
        height = 30  # 目标高度
        power_number_str = Img.FindStrInImg(self.src_img_path, target_img_path, x1, y1, width, height)
        if power_number_str != "-1":
            power_number_str = power_number_str.split('/')
            power_number = power_number_str[0]
            if power_number == '':
                return -1
            return int(power_number)
        return power_number_str

    @staticmethod
    def if_exist(path):
        re, x, y = Img.find_img_in_img('temp/temp.bmp', path, 0.90)
        return re

    def get_scene(self, handle):
        window_img = self.window.jietu((handle.left, handle.top, handle.right, handle.bottom))
        window_img.save('temp/temp.bmp')
        path = "yys/scene/"
        if Game.if_exist(path + "庭院界面.bmp") == 0:
            return SceneKey.TING_YUAN
        if Game.if_exist(path + "探索界面.bmp") == 0:
            return SceneKey.TANG_SUO
        if Game.if_exist(path + "町中界面.bmp") == 0:
            return SceneKey.DING_ZHONG
        if Game.if_exist(path + "结界突破界面.bmp") == 0:
            return SceneKey.JIE_JIE_TU_PO
        if Game.if_exist(path + "战斗奖励界面.bmp") == 0:
            return SceneKey.ZHANG_DOU_JIANG_LI
        if Game.if_exist(path + "斗技中界面.bmp") == 0:
            return SceneKey.DOU_JI_ZHONG
        if Game.if_exist(path + "战斗中界面.bmp") == 0:
            return SceneKey.ZHANG_DOU_ZHONG
        if Game.if_exist(path + "战斗胜利界面.bmp") == 0:
            return SceneKey.ZHANG_DOU_SHENG_LI
        if Game.if_exist(path + "战斗失败界面.bmp") == 0:
            return SceneKey.ZHANG_DOU_SHI_BAI
        if Game.if_exist(path + "战斗胜利界面.bmp") == 0:
            return SceneKey.ZHANG_DOU_SHENG_LI
        if Game.if_exist(path + "探索中界面.bmp") == 0:
            return SceneKey.TANG_SUO_ZHONG
        if Game.if_exist(path + "协战队伍界面.bmp") == 0:
            return SceneKey.XIE_ZHAN_DUI_WU
        if Game.if_exist(path + "斗技界面.bmp") == 0:
            return SceneKey.DOU_JI
        if Game.if_exist(path + "斗技准备界面.bmp") == 0:
            return SceneKey.DOU_JI_ZHUN_BEI
        return SceneKey.NUKOWN

    def click_img(self, img_path, handle, accuracy=0.9):
        re, x, y = self.window.find_img(handle, img_path, accuracy)
        if re == 0:
            mouse = Mouse()
            mouse.Click(x, y)
            return 0
        return -1

    def double_click_img(self, img_path, handle, accuracy=0.9):
        re, x, y = self.window.find_img(handle, img_path, accuracy)
        if re == 0:
            mouse = Mouse()
            mouse.Click(x, y)
            mouse.Click(x, y)
            return 0
        return -1

    def jie_jie_or_tang_suo(self, handle):
        # 获取体力结界券
        tu_po_juan = self.get_tu_po_juan(handle)
        print("突破卷:" + str(tu_po_juan))
        ti_li = self.get_ti_li(handle)
        print("体力:" + str(ti_li))
        if tu_po_juan != -1 and ti_li != -1:
            # if tu_po_juan <= 25 and ti_li > 25:
            if ti_li > 25:
                return "探索"
            elif tu_po_juan == 0 and ti_li < 25:
                return "没了"
            else:
                return "结界突破"

    def jie_jie_number(self, handle):
        # 获得游戏界面截图
        tu = self.window.jie_tu(handle)
        tu.save('temp/temp.bmp')
        re1 = Img.find_all_img_in_img('temp/temp.bmp', self.daguolePath, 0.8)
        re2 = Img.find_all_img_in_img('temp/temp.bmp', self.dabuguoPath, 0.96)  # 匹配精度0.96
        re3 = Img.find_all_img_in_img('temp/temp.bmp', self.meidaguoPath, 0.90)
        print("打过了" + str(re1) + ";打不过:" + str(re2) + ";没打过:" + str(re3))
        return re1, re2, re3

    def jie_chu_tu_po_block(self, handle):
        tu = self.window.jie_tu(handle)
        tu.save('temp/temp.bmp')
        x = 100 + 2 * 10 + 5
        y = 100 + 2 * 10
        point0 = [x, y]
        for i in range(9):
            if i == 0:
                point = point0
            else:
                point = [int(point0[0] + int(i % 3) * 305), int(point0[1] + int(i / 3) * 120)]
            w = 300-5
            h = 120-5
            point2 = [point[0] + w, point[1] + h]
            print(str(i) + str(point))
            src_img = Img.CutImgPath('temp/temp.bmp', point, point2)
            Img.save('temp/temp'+str(i)+'.bmp', src_img)
            re, x, y = Img.FindImgInImg('temp/temp'+str(i)+'.bmp', self.meidaguoPath)
            if re == 0:
                return 0, x + handle.left + point[0], y + handle.top + point[1]
        return -1, 0, 0

    def da_tu_po(self, handle):
        re1, re2, re3 = self.jie_jie_number(handle)
        if re1 >= 3:
            re, x, y = self.window.find_img(handle, "yys/结界刷新冷却中.bmp")
            if re == 0:
                re = self.click_img("yys/关闭按钮.bmp", handle)
                if re == 0:
                    print("关闭按钮")
                    return -1, 0, 0
                else:
                    print("打过" + str(re1) + "但是找不到关闭按钮")
                    return -1, 0, 0
            else:
                re, x, y = self.window.find_img(handle, "yys/结界刷新按钮.bmp")
                if re == 0:
                    return 1, x, y
                else:
                    print("打过"+str(re1)+"没在刷新冷却中但是找不到刷新按钮")
                    return -1, 0, 0
        elif re3 == 0:
            re, x, y = self.window.Findimg(handle, "yys/结界刷新按钮.bmp")
            if re == 0:
                return 1, x, y
            else:
                print("打过" + str(re1) + "没在刷新冷却中但是找不到刷新按钮")
                return -1, 0, 0
        else:
            re, x, y = self.jie_chu_tu_po_block(handle)
            if re == 0:
                print("打他！")
                return 0, x, y
            else:
                print("打过" + str(re1) + "但是找不到没打过的")
                return -1, 0, 0

    def jin_ru_tang_suo(self, handle):
        if self.click_img(self.window, "yys/第三章.bmp", handle) == 0:
            time.sleep(1)
            if self.click_img(self.window, "yys/探索按钮.bmp", handle) == 0:
                print("探索")
                time.sleep(1)
            else:
                print("探索按钮找不到")
        else:
            print("第十一章找不到")
        print("进入探索")

    def da_tang_suo(self, handle):
        # 获取体力数量
        ti_li = self.get_ti_li(handle)
        if ti_li > 6:
            if self.click_img("yys/打小怪.bmp", handle) == 0:
                print("打小怪")
            elif self.click_img("yys/打boss.bmp", handle) == 0:
                print("打boss")
            elif self.click_img("yys/探索奖励.bmp", handle) == 0:
                print("探索奖励")
            elif self.click_img("yys/打小怪2.bmp", handle) == 0:
                print("打小怪2")
            else:
                re, x, y = self.window.find_img(handle, "yys/获得奖励.bmp")
                if re == 0:
                    mouse = Mouse()
                    mouse.Click(x, y - 100)
                else:
                    self.click_img("yys/探索向右走.bmp", handle)
        elif ti_li == -1:
            print("体力获取失败")
        print("打探索")

    # 用于去除未使用对象成员变量的函数参数使用了self而出现的波浪线
    def qu_bo_lang_xian(self):
        window = self.window

    def teaming(self, handle):
        print(sys._getframe().f_code.co_name)  # 当前位置所在的函数名
        if self.click_img("yys/开始战斗按钮.bmp", handle, 0.98) == 0:
            print("开始战斗按钮")
        pass

    def error_scene(self, handle):
        print(sys._getframe().f_code.co_name)  # 当前位置所在的函数名
        if self.click_img("yys/退出斗技按钮.bmp", handle, 0.98) == 0:
            print("退出斗技按钮")
        if self.click_img("yys/确认退出斗技按钮.bmp", handle, 0.98) == 0:
            print("确认退出斗技按钮")
        pass

    def fighting(self, handle):
        print(sys._getframe().f_code.co_name)  # 当前位置所在的函数名
        self.qu_bo_lang_xian()
        pass

    def fight_end(self, handle):
        print(sys._getframe().f_code.co_name)  # 当前位置所在的函数名
        self.qu_bo_lang_xian()
        mouse = Mouse()
        mouse.click(handle.left + 100, handle.top + 100)
        pass

    def hun_shi_team(self, argument, handle):
        switcher = {
            SceneKey.NUKOWN: self.error_scene,
            SceneKey.ZHANG_DOU_ZHONG: self.fighting,
            SceneKey.ZHANG_DOU_JIANG_LI: self.fight_end,
            SceneKey.ZHANG_DOU_SHENG_LI: self.fight_end,
            SceneKey.ZHANG_DOU_SHI_BAI: self.fight_end,
            SceneKey.XIE_ZHAN_DUI_WU: self.teaming
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, self.error_scene)(handle)
        # Execute the function
        return func

    def exit_fighting(self, handle):
        print(sys._getframe().f_code.co_name)  # 当前位置所在的函数名
        if self.click_img("yys/退出斗技按钮.bmp", handle, 0.90) == 0:
            print("退出斗技按钮")
        if self.click_img("yys/确认退出斗技按钮.bmp", handle, 0.90) == 0:
            print("确认退出斗技按钮")
        pass

    def start_fight(self, handle):
        print(sys._getframe().f_code.co_name)  # 当前位置所在的函数名
        if self.click_img("yys/开始斗技按钮.bmp", handle, 0.98) == 0:
            print("开始斗技按钮")
        pass

    def get_ready(self, handle):
        print(sys._getframe().f_code.co_name)  # 当前位置所在的函数名
        if self.click_img("yys/斗技准备按钮.bmp", handle, 0.98) == 0:
            print("斗技准备按钮")
        re, x, y = self.window.find_img(handle, "yys/斗技中界面.bmp")  # 斗技中界面
        if re == 0:
            if self.click_img("yys/退出战斗按钮.bmp", handle, 0.98) == 0:
                print("退出战斗按钮")
        pass

    def dou_ji(self, argument, handle):
        switcher = {
            SceneKey.NUKOWN: self.error_scene,
            SceneKey.DOU_JI: self.get_ready,
            SceneKey.ZHANG_DOU_SHI_BAI: self.fight_end,
            SceneKey.ZHANG_DOU_SHENG_LI: self.fight_end,
            SceneKey.ZHANG_DOU_JIANG_LI: self.fight_end,
            SceneKey.DOU_JI_ZHUN_BEI: self.start_fight,
            SceneKey.DOU_JI_ZHONG: self.exit_fighting
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, self.error_scene)(handle)
        # Execute the function
        return func


@unique
class SceneKey(Enum):
    NUKOWN = 0
    TING_YUAN = 1
    TANG_SUO = 2
    DING_ZHONG = 3
    JIE_JIE_TU_PO = 4
    ZHANG_DOU_ZHONG = 5
    ZHANG_DOU_JIANG_LI = 6
    ZHANG_DOU_SHENG_LI = 7
    ZHANG_DOU_SHI_BAI = 8
    XIE_ZHAN_DUI_WU = 9
    DOU_JI = 10
    DOU_JI_ZHUN_BEI =11
    DOU_JI_ZHONG = 12


