from Cimg import Img

from Cmouse import Mouse
from Cwindow import Window
import sys
import time
from abc import ABCMeta, abstractmethod
from Chandle import Handle, SceneKey
from CsendQQ import SendQQ
import codedef


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
        if Game.judge_scene(argument, handle) != 0:
            return codedef.SCENCE_REPEAT_END

        switcher = {
            SceneKey.NUKOWN: self.error_scene,
            SceneKey.ZHANG_DOU_ZHONG: self.waiting,
            SceneKey.ZHANG_DOU_SHI_BAI: self.fight_end,
            SceneKey.ZHANG_DOU_SHENG_LI: self.fight_end,
            SceneKey.ZHANG_DOU_JIANG_LI: self.fight_end,
            SceneKey.GOU_MAI_TI_LI: self.hon_cha_exit,
            SceneKey.XUAN_SHANG_FENG_YING_YAO_QING: self.ju_jue_xuan_shang
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, self.error_scene)(argument, handle)
        # Execute the function
        return func

    # 判断场景是否重复，重复是否超限
    @staticmethod
    def judge_scene(scene, handle):
        if scene != handle.old_scene:
            handle.old_scene = scene
            handle.iold_scene = 0
        elif scene != SceneKey.DOU_JI_ZHONG and scene != SceneKey.ZHANG_DOU_ZHONG:
            if handle.iold_scene + 1 >= codedef.SCENCE_REPEAT_TIMES:
                return codedef.ERROR_END
            handle.iold_scene += 1
        return codedef.NORMAL_END

    def waiting(self, argument, handle):
        time.sleep(1)
        return codedef.NORMAL_END

    def error_scene(self, argument, handle):
        if self.click_img("yys/退出斗技按钮.bmp", handle, 0.98) == 0:
            print("退出斗技按钮")
        if self.click_img("yys/确认退出斗技按钮.bmp", handle, 0.98) == 0:
            print("确认退出斗技按钮")
        return codedef.NORMAL_END

    def enter_jie_jie(self, argument, handle):
        if self.click_img("yys/进入突破按钮.bmp", handle, 0.98) == 0:
            print("进入突破按钮")
        return codedef.NORMAL_END

    def fight_end(self, argument, handle):
        self.qu_bo_lang_xian()
        mouse = Mouse()
        mouse.click(handle.left + 100, handle.top + 150)
        return codedef.FIGHT_END

    # 查找指定windows程序窗口，并设置到指定位置和大小，找不到返回-1，找到返回0
    def set_window(self, handle, window_name, index, position=True):
        class_name = None
        if self.window.get_window(handle, class_name, window_name) == -1:
            return -1
        if handle.bottom - handle.top < 100 or handle.top < 0:
            return -1

        left = 10
        top = 10
        if position:
            if index == "1":
                left = 10
                top = 10
            elif index == "2":
                left = 1050
                top = 10
            elif index == "3":
                left = 10
                top = 520
            elif index == "4":
                left = 1050
                top = 520
            if left != handle.left or top != handle.top:
                self.window.set_window(handle, left, top, handle.right - handle.left, handle.bottom - handle.top)

        target_height = 520
        dx = handle.bottom - handle.top - target_height
        i_depth = 10
        if dx != 0:
            temp_times = int(dx / i_depth)
            temp_i = 1
            while temp_i <= temp_times:
                temp_i = temp_i + 1
                self.window.set_window(handle, left, top, handle.right - handle.left,
                                       handle.bottom - handle.top - i_depth * temp_i)
                time.sleep(0.8)
            self.window.set_window(handle, left, top, handle.right - handle.left, target_height)
        return codedef.NORMAL_END

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
            if tu_po_number.isdigit():
                return int(tu_po_number)
            else:
                return -1
        return -1

    # 在结界突破界面获取突破卷数量
    def get_tu_po_juan2(self, handle):
        # 获得游戏界面截图
        tu = self.window.jie_tu(handle)
        tu.save('temp/temp.bmp')
        tag_img_path = "yys/突破卷数量2.bmp"
        x1 = 38  # 左右偏移量
        y1 = 1  # 上下偏移量
        width = 46  # 目标宽度
        height = 20  # 目标高度
        tu_po_number_str = Img.find_str_in_img(self.src_img_path, tag_img_path, x1, y1, width, height, False)
        print(tu_po_number_str)
        if tu_po_number_str != "-1":
            tu_po_number_str = tu_po_number_str.split('/')
            tu_po_number = tu_po_number_str[0]
            if tu_po_number == '':
                return -1
            if tu_po_number.isdigit():
                return int(tu_po_number)
            else:
                return -1
        return -1

    # 在探索界面获取体力数量
    def get_ti_li(self, handle, xishu=0.6):
        # 获得游戏界面截图
        tu = self.window.jie_tu(handle)
        tu.save('temp/temp.bmp')
        target_img_path = "yys/体力数量.bmp"
        x1 = 55  # 左右偏移量
        y1 = 1  # 上下偏移量
        width = 80  # 目标宽度
        height = 24  # 目标高度
        power_number_str = Img.find_str_in_img(self.src_img_path, target_img_path, x1, y1, width, height, True, xishu)
        if power_number_str != "-1":
            power_number_str = power_number_str.split('/')
            power_number = power_number_str[0]
            if power_number == '':
                return -1
            try:
                int_tili = int(power_number)
            except Exception as e:
                print(e)
                return -1
            return int(int_tili)
        return power_number_str

    # 查找图片是否在temp图片中是否存在
    @staticmethod
    def if_exist(path, accuracy=0.90):
        re, x, y = Img.find_img_in_img('temp/temp.bmp', path, accuracy)
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
        if Game.if_exist(path + "悬赏封印邀请界面.bmp") == 0:
            return SceneKey.XUAN_SHANG_FENG_YING_YAO_QING
        if Game.if_exist("yys/接受邀请按钮.bmp") == 0:
            return SceneKey.SHOU_DAO_YAO_QING
        if Game.if_exist(path + "购买体力界面.bmp") == 0:
            return SceneKey.GOU_MAI_TI_LI
        if Game.if_exist(path + "默认邀请队友界面.bmp") == 0:
            return SceneKey.MO_REN_YAOQ_QING_DUI_YOU
        if Game.if_exist(path + "是否邀请继续.bmp") == 0:
            print("是否邀请继续")
            return SceneKey.SHI_FOU_YAO_QING_JI_XU
        if Game.if_exist(path + "是否邀请继续2.bmp") == 0:
            print("是否邀请继续2")
            return SceneKey.SHI_FOU_YAO_QING_JI_XU
        if Game.if_exist(path + "组队选择队友界面.bmp") == 0:
            return SceneKey.ZU_DUI_XUAN_ZE_DUI_YOU
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
            return codedef.NORMAL_END
        return -1

    # 双击指定图片
    def double_click_img(self, img_path, handle, accuracy=0.9):
        re, x, y = self.window.find_img(handle, img_path, accuracy)
        if re == 0:
            mouse = Mouse()
            mouse.click(x, y)
            mouse.click(x, y)
            return codedef.NORMAL_END
        return -1

    # 从探索进入探索界面
    def jin_ru_tang_suo(self, handle):
        if self.click_img(self.window, "yys/探索按钮.bmp", handle) == 0:
            print("探索按钮")

    # 在探索中界面打探索
    def da_tang_suo(self, handle):
        if self.click_img("yys/探索奖励.bmp", handle) == 0:
            return codedef.NORMAL_END
        if self.click_img("yys/获得奖励.bmp", handle) == 0:
            if self.click_img("yys/scene/探索中界面.bmp", handle) == 0:
                return codedef.NORMAL_END
            return codedef.NORMAL_END
        return codedef.ERROR_END

    # 用于去除未使用对象成员变量的函数参数使用了self而出现的波浪线
    def qu_bo_lang_xian(self):
        window = self.window

    def teaming(self, argument, handle):
        if self.click_img("yys/开始战斗按钮.bmp", handle, 0.98) == 0:
            print("开始战斗按钮")
            return codedef.FIGHT_BEGIN
        return codedef.NORMAL_END

    def exit_fighting(self, argument, handle):
        if self.click_img("yys/退出斗技按钮.bmp", handle, 0.90) == 0:
            print("退出斗技按钮")
        if self.click_img("yys/确认退出斗技按钮.bmp", handle, 0.90) == 0:
            print("确认退出斗技按钮")
        pass

    def start_dj_fight(self, handle):
        if self.click_img("yys/开始斗技按钮.bmp", handle, 0.98) == 0:
            print("开始斗技按钮")
        pass

    def get_ready(self, argument, handle):
        if self.click_img("yys/斗技准备按钮.bmp", handle, 0.98) == 0:
            print("斗技准备按钮")
        re, x, y = self.window.find_img(handle, "yys/斗技中界面.bmp")  # 斗技中界面
        if re == 0:
            if self.click_img("yys/退出战斗按钮.bmp", handle, 0.98) == 0:
                print("退出战斗按钮")
        pass

    def ju_jue_xuan_shang(self, argument, handle):
        if self.click_img("yys/细红叉按钮.bmp", handle, 0.90) == 0:
            print("细红叉按钮")
        if self.click_img("yys/粗红叉按钮.bmp", handle, 0.90) == 0:
            print("粗红叉按钮")
        return codedef.NORMAL_END

    # 返回值-900 表示没体力
    def hon_cha_exit(self, argument, handle):
        if self.click_img("yys/细红叉按钮.bmp", handle, 0.90) == 0:
            print("细红叉按钮")
        return -900

    def mo_ren_yao_qing_dui_you(self, argument, handle):
        if self.click_img("yys/默认邀请队友按钮灰.bmp", handle, 0.90) == 0:
            print("默认邀请队友按钮灰")
            time.sleep(1)
        if self.jie_tu_if_exist(handle, "yys/默认邀请队友按钮.bmp") == 0:
            if self.click_img("yys/确定按钮.bmp", handle, 0.90) == 0:
                print("确定按钮")
        return codedef.NORMAL_END

    # 判断是在个人结界还是在寮结界 -1 错误；0 个人结界； 1 寮结界
    def ge_ren_or_liao(self, handle):
        if self.jie_tu_if_exist(handle, "yys/个人结界.bmp") == 0 and self.jie_tu_if_exist(handle, "yys/寮结界灰.bmp") == 0:
            print("个人结界")
            return codedef.NORMAL_END
        if self.jie_tu_if_exist(handle, "yys/个人结界灰.bmp") == 0 and self.jie_tu_if_exist(handle, "yys/寮结界.bmp") == 0:
            print("寮结界")
            return 1
        return -1

    def yao_qing_dui_you_ji_xu(self, argument, handle):
        if self.click_img("yys/确定按钮.bmp", handle) == 0:
            print("确定按钮")
        return codedef.NORMAL_END

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

    # 发送 temp.bmp 给qq好友消息窗口，窗口名name ，一般是好友昵称还在备注，或者群名称
    def send_qq_temp_img(self, name):
        send_QQ = SendQQ(name)
        return send_QQ.send_qq_bmp('temp/temp.bmp')

    # 发送 text 文本 给qq好友消息窗口，窗口名name ，一般是好友昵称还在备注，或者群名称
    def send_qq_text(self, name, text):
        send_QQ = SendQQ(name)
        return send_QQ.send_qq_text(text)



