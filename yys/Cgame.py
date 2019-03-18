from Cimg import Img
from enum import Enum, unique
from Cmouse import Mouse
from Cwindow import Window
import sys
import time
from abc import ABCMeta, abstractmethod

class Game:
    da_guo_le_path = 'yys/打过了.bmp'
    da_bu_guo_path = 'yys/打不过.bmp'
    mei_da_guo_path = 'yys/没打过.bmp'

    # 探索界面的上部分，最后是最上面的长条形截图
    def __init__(self):
        self.src_img_path = 'temp/temp.bmp'
        self.window = Window()

    @abstractmethod
    def do_work(self, argument, handle):
        pass

    # 查找指定windows程序窗口，并设置到指定位置和大小，找不到返回-1，找到返回0
    def set_window(self, handle, window_name, index, position=True):
        class_name = None
        if self.window.get_window(handle, class_name, window_name) == -1:
            return -1
        left = 10
        top = 10
        if position:
            if index == 1:
                left = 10
                top = 10
            elif index == 2:
                left = 1050
                top = 10
            elif index == 3:
                left = 10
                top = 520
            elif index == 4:
                left = 1050
                top = 520
            if left != handle.left or top != handle.top:
                self.window.set_window(handle, left, top, handle.right - handle.left, handle.bottom - handle.top)

        target_height = 520
        dx = handle.bottom - handle.top - target_height
        i_depth = 20
        if dx != 0:
            temp_times = int(dx/i_depth)
            temp_i = 1
            while temp_i <= temp_times:
                temp_i = temp_i + 1
                self.window.set_window(handle, left, top, handle.right - handle.left,
                                       handle.bottom - handle.top - i_depth * temp_i)
                time.sleep(0.8)
            self.window.set_window(handle, left, top, handle.right - handle.left, target_height)

        return 0

    # 在探索界面获取突破卷数量
    def get_tu_po_juan(self, handle):
        tu = self.window.jie_tu(handle)
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

    # 在结界突破界面获取突破卷数量
    def get_tu_po_juan2(self, handle):
        # 获得游戏界面截图
        tu = self.window.jie_tu(handle)
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

    # 在探索界面获取体力数量
    def get_ti_li(self, handle):
        # 获得游戏界面截图
        tu = self.window.jie_tu(handle)
        tu.save('temp/temp.bmp')
        target_img_path = "yys/体力数量.bmp"
        x1 = 65  # 左右偏移量
        y1 = 1  # 上下偏移量
        width = 95  # 目标宽度
        height = 30  # 目标高度
        power_number_str = Img.find_str_in_img(self.src_img_path, target_img_path, x1, y1, width, height)
        if power_number_str != "-1":
            power_number_str = power_number_str.split('/')
            power_number = power_number_str[0]
            if power_number == '':
                return -1
            return int(power_number)
        return power_number_str

    # 查找图片是否在temp图片中是否存在
    @staticmethod
    def if_exist(path):
        re, x, y = Img.find_img_in_img('temp/temp.bmp', path, 0.90)
        return re

    def jie_tu_if_exist(self, handle, path):
        window_img = self.window.jie_tu(handle)
        window_img.save('temp/temp.bmp')
        re = Game.if_exist(path)
        return re

    # 判断当前所在是哪个场景
    def get_scene(self, handle):
        window_img = self.window.jie_tu(handle)
        window_img.save('temp/temp.bmp')
        path = "yys/scene/"
        if self.click_img("yys/自动加入队伍按钮.bmp", handle, 0.90) == 0:
            print("自动加入队伍按钮")
            return SceneKey.NUKOWN
        if self.click_img("yys/接受邀请按钮.bmp", handle, 0.90) == 0:
            print("接受邀请按钮")
            return SceneKey.NUKOWN
        if Game.if_exist(path + "购买体力界面.bmp") == 0:
            return SceneKey.GOU_MAI_TI_LI
        if Game.if_exist(path + "默认邀请队友界面.bmp") == 0:
            return SceneKey.MO_REN_YAOQ_QING_DUI_YOU
        if Game.if_exist(path + "是否邀请继续.bmp") == 0:
            return SceneKey.SHI_FOU_YAO_QING_JI_XU
        if Game.if_exist(path + "悬赏封印邀请界面.bmp") == 0:
            return SceneKey.XUAN_SHANG_FENG_YING_YAO_QING
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
        if Game.if_exist(path + "战斗胜利界面.bmp") == 0:
            return SceneKey.ZHANG_DOU_SHENG_LI
        if Game.if_exist(path + "战斗失败界面.bmp") == 0:
            return SceneKey.ZHANG_DOU_SHI_BAI
        if Game.if_exist(path + "探索中界面.bmp") == 0:
            return SceneKey.TANG_SUO_ZHONG
        if Game.if_exist(path + "协战队伍界面.bmp") == 0:
            return SceneKey.XIE_ZHAN_DUI_WU
        if Game.if_exist(path + "斗技界面.bmp") == 0:
            return SceneKey.DOU_JI
        if Game.if_exist(path + "战斗中界面.bmp") == 0:
            return SceneKey.ZHANG_DOU_ZHONG
        if Game.if_exist(path + "探索章节界面.bmp") == 0:
            return SceneKey.TANG_SUO_ZHANG_JIE


        # if Game.if_exist(path + "斗技准备界面.bmp") == 0:
        #   return SceneKey.DOU_JI_ZHUN_BEI
        return SceneKey.NUKOWN

    # 单击指定图片
    def click_img(self, img_path, handle, accuracy=0.9):
        re, x, y = self.window.find_img(handle, img_path, accuracy)
        if re == 0:
            mouse = Mouse()
            mouse.click(x, y)
            return 0
        return -1

    # 双击指定图片
    def double_click_img(self, img_path, handle, accuracy=0.9):
        re, x, y = self.window.find_img(handle, img_path, accuracy)
        if re == 0:
            mouse = Mouse()
            mouse.click(x, y)
            mouse.click(x, y)
            return 0
        return -1

    # 决策打结界还是探索
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

    # 结界数量（打过了、打不过、没打过）
    def jie_jie_number(self, handle):
        # 获得游戏界面截图
        tu = self.window.jie_tu(handle)
        tu.save('temp/temp.bmp')
        re1 = Img.find_all_img_in_img('temp/temp.bmp', self.da_guo_le_path, 0.8)
        re2 = Img.find_all_img_in_img('temp/temp.bmp', self.da_bu_guo_path, 0.96)  # 匹配精度0.96
        re3 = Img.find_all_img_in_img('temp/temp.bmp', self.mei_da_guo_path, 0.90)
        print("打过了" + str(re1) + ";打不过:" + str(re2) + ";没打过:" + str(re3))
        return re1, re2, re3

    # 逐个结界块进行找图，找到第一个没打过的返回
    def jie_chu_tu_po_block(self, handle):
        tu = self.window.jie_tu(handle)
        tu.save('temp/temp.bmp')
        x = 100 - 2 * 10 + 15
        y = 100 - 2 * 10 + 12
        w = 300 - 80
        h = 120 - 35
        point0 = [x, y]
        for i in range(9):
            if i == 0:
                point = point0
            else:
                point = [int(point0[0] + int(i % 3) * 230), int(point0[1] + int(i / 3) * 91)]
            point2 = [point[0] + w, point[1] + h]
            print(str(i) + str(point))
            src_img = Img.cut_img_path('temp/temp.bmp', point, point2)
            Img.save('temp/temp'+str(i)+'.bmp', src_img)
            re, x, y = Img.find_img_in_img('temp/temp'+str(i)+'.bmp', self.mei_da_guo_path)
            if re == 0:
                return 0, x + handle.left + point[0], y + handle.top + point[1]
        return -1, 0, 0

    # 从探索进入探索界面
    def jin_ru_tang_suo(self, handle):
        if self.click_img(self.window, "yys/探索按钮.bmp", handle) == 0:
            print("探索按钮")

    # 在探索中界面打探索怪
    def da_tang_suo(self, handle):
        # 获取体力数量
        ti_li = self.get_ti_li(handle)
        if self.click_img("yys/探索奖励.bmp", handle) == 0:
            return 0
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
                self.click_img("yys/探索向右走.bmp", handle)
        elif ti_li == -1:
            print("体力获取失败")
        return 0

    # 用于去除未使用对象成员变量的函数参数使用了self而出现的波浪线
    def qu_bo_lang_xian(self):
        window = self.window

    def teaming(self, handle):
        print("teaming")
        print(sys._getframe().f_code.co_name)  # 当前位置所在的函数名
        if self.click_img("yys/开始战斗按钮.bmp", handle, 0.98) == 0:
            print("开始战斗按钮")
        return 0

    def error_scene(self, handle):
        print(sys._getframe().f_code.co_name)  # 当前位置所在的函数名
        if self.click_img("yys/退出斗技按钮.bmp", handle, 0.98) == 0:
            print("退出斗技按钮")
        if self.click_img("yys/确认退出斗技按钮.bmp", handle, 0.98) == 0:
            print("确认退出斗技按钮")
        return 0

    def fighting(self, handle):
        print(sys._getframe().f_code.co_name)  # 当前位置所在的函数名
        self.qu_bo_lang_xian()
        return 0

    def fight_end(self, handle):
        print(sys._getframe().f_code.co_name)  # 当前位置所在的函数名
        self.qu_bo_lang_xian()
        mouse = Mouse()
        mouse.click(handle.left + 100, handle.top + 100)
        return 0

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

    def start_dj_fight(self, handle):
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

    def waiting(self, handle):
        time.sleep(1)
        return 0

    def enter_jie_jie(self, handle):
        if self.click_img("yys/进入突破按钮.bmp", handle, 0.98) == 0:
            print("进入突破按钮")
        return 0

    # 刷新结界突破
    def refresh_jie_jie(self, handle):
        if self.click_img("yys/结界刷新冷却中.bmp", handle, 0.98) == 0:
            print("结界刷新冷却中")
            return 1
        else:
            if self.click_img("yys/结界刷新按钮.bmp", handle, 0.98) == 0:
                print("结界刷新按钮")
                time.sleep(1)
                if self.click_img("yys/结界刷新确定按钮.bmp", handle, 0.98) == 0:
                    print("结界刷新确定按钮")
        return 0

    # 查看结界突破剩余数量，判断是否打，还是刷新
    def select_fight_jie_jie(self, handle):
        na = self.ge_ren_or_liao(handle)
        if na == -1:
            return 1
        if na == 1:
            if self.click_img("yys/个人结界灰.bmp", handle, 0.98) == 0:
                print("个人结界灰")
            return 0
        da_guo, da_bug_uo, mei_da_guo = self.jie_jie_number(handle)
        if da_guo >= 3 or mei_da_guo == 0:
            return self.refresh_jie_jie(handle)
        re, x, y = self.jie_chu_tu_po_block(handle)
        if re != 0:
            return 2
        mouse = Mouse()
        mouse.click(x, y)
        self.waiting(handle)
        if self.click_img("yys/进攻结界按钮.bmp", handle, 0.90) == 0:
            print("进攻结界按钮")
        return 0

    def hon_cha_exit(self, handle):
        if self.click_img("yys/细红叉按钮.bmp", handle, 0.90) == 0:
            print("细红叉按钮")
        if self.click_img("yys/粗红叉按钮.bmp", handle, 0.90) == 0:
            print("粗红叉按钮")
        return 0

    def mo_ren_yao_qing_dui_you(self, handle):
        if self.click_img("yys/默认邀请队友按钮灰.bmp", handle, 0.90) == 0:
            print("默认邀请队友按钮灰")
            time.sleep(1)
        if self.jie_tu_if_exist(handle, "yys/默认邀请队友按钮.bmp") == 0:
            if self.click_img("yys/确定按钮.bmp", handle, 0.90) == 0:
                print("确定按钮")

    # 判断是在个人结界还是在寮结界 -1 错误；0 个人结界； 1 寮结界
    def ge_ren_or_liao(self, handle):
        if self.jie_tu_if_exist(handle, "yys/个人结界.bmp") == 0 and self.jie_tu_if_exist(handle, "yys/寮结界灰.bmp") == 0:
            print("个人结界")
            return 0
        if self.jie_tu_if_exist(handle, "yys/个人结界灰.bmp") == 0 and self.jie_tu_if_exist(handle, "yys/寮结界.bmp") == 0:
            print("寮结界")
            return 1
        return -1

    def yao_qing_dui_you_ji_xu(self, handle):
        if self.click_img("yys/确定按钮.bmp", handle) == 0:
            print("确定按钮")
            return 0

    def dou_ji(self, argument, handle):
        switcher = {
            SceneKey.NUKOWN: self.error_scene,
            SceneKey.DOU_JI: self.get_ready,
            SceneKey.ZHANG_DOU_SHI_BAI: self.fight_end,
            SceneKey.ZHANG_DOU_SHENG_LI: self.fight_end,
            SceneKey.ZHANG_DOU_JIANG_LI: self.fight_end,
            SceneKey.DOU_JI_ZHUN_BEI: self.start_dj_fight,
            SceneKey.DOU_JI_ZHONG: self.exit_fighting
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, self.error_scene)(handle)
        # Execute the function
        return func

    def lia_ren_da(self, argument, handle):
        print(argument)
        switcher = {
            SceneKey.NUKOWN: self.error_scene,
            SceneKey.ZHANG_DOU_SHI_BAI: self.fight_end,
            SceneKey.ZHANG_DOU_SHENG_LI: self.fight_end,
            SceneKey.ZHANG_DOU_JIANG_LI: self.fight_end,
            SceneKey.XIE_ZHAN_DUI_WU: self.teaming,
            SceneKey.ZHANG_DOU_ZHONG: self.waiting,
            SceneKey.GOU_MAI_TI_LI: self.hon_cha_exit,
            SceneKey.XUAN_SHANG_FENG_YING_YAO_QING: self.hon_cha_exit,
            SceneKey.MO_REN_YAOQ_QING_DUI_YOU: self.mo_ren_yao_qing_dui_you,
            SceneKey.SHI_FOU_YAO_QING_JI_XU: self.yao_qing_dui_you_ji_xu
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, self.error_scene)(handle)
        # Execute the function
        return func

    def da_jie_jie(self, argument, handle):
        switcher = {
            SceneKey.NUKOWN: self.error_scene,
            SceneKey.ZHANG_DOU_SHI_BAI: self.fight_end,
            SceneKey.ZHANG_DOU_SHENG_LI: self.fight_end,
            SceneKey.ZHANG_DOU_JIANG_LI: self.fight_end,
            SceneKey.JIE_JIE_TU_PO: self.select_fight_jie_jie,
            SceneKey.TANG_SUO: self.enter_jie_jie,
            SceneKey.ZHANG_DOU_ZHONG: self.waiting,
            SceneKey.XUAN_SHANG_FENG_YING_YAO_QING: self.hon_cha_exit
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
    GOU_MAI_TI_LI = 13
    XUAN_SHANG_FENG_YING_YAO_QING = 14
    TANG_SUO_ZHONG = 15
    MO_REN_YAOQ_QING_DUI_YOU = 16
    TANG_SUO_ZHANG_JIE = 17
    SHI_FOU_YAO_QING_JI_XU = 18

