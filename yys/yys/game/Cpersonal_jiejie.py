from Cgame import Game
from Chandle import SceneKey
from Cmouse import Mouse
from Cimg import Img
import time
import codedef
from win32api import GetSystemMetrics
import random


class Personal_jiejie(Game):

    def __init__(self):
        super(Personal_jiejie, self).__init__()
        self.metrics_x = GetSystemMetrics(0)

    # -1 找个人结界或寮结界按钮失败
    # -2 在没打过的数量大于零时，却在分块找到这个结界时找不到
    # -3 结界突破卷数量为0
    def judge_scenes(self, argument, handle):
        return Game.judge_scenes(self, argument, handle)

    def do_work(self, argument, handle):
        if self.judge_scenes(argument, handle) == codedef.SCENCE_REPEAT_END:
            return codedef.SCENCE_REPEAT_END
        switcher = {
            SceneKey.SHI_FOU_YAO_QING_JI_XU: self.this_yao_qing_dui_you_ji_xu,
            SceneKey.TANG_SUO_ZHANG_JIE: self.this_exit_zhang_jie,
            SceneKey.TANG_SUO_ZHONG: self.this_exit_tang_suo,
            SceneKey.JIE_JIE_TU_PO: self.personal_jiejie_main,
            SceneKey.TANG_SUO: self.this_enter_jie_jie,
            SceneKey.SHOU_DAO_YAO_QING: self.shou_dao_yai_qing
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, self.father)(argument, handle)
        # Execute the function
        return func

    def father(self, argument, handle):
        return Game.do_work(self, argument, handle)

    def this_enter_jie_jie(self, argument, handle):
         return self.enter_jie_jie(argument, handle)

    def this_exit_zhang_jie(self, argument, handle):
        return self.click_img("yys/关闭按钮.bmp", handle, 0.98)

    def this_yao_qing_dui_you_ji_xu(self, argument, handle):
        return self.click_img("yys/取消邀请按钮.bmp", handle, 0.98)

    def this_exit_tang_suo(self, argument, handle):
        return self.exit_tang_suo(handle)

    # 查看结界突破剩余数量，判断是否打，还是刷新
    def personal_jiejie_main(self, argument, handle):
        print("personal_jiejie_main")
        if self.click_img("yys/结界奖励.bmp", handle, 0.98) == 0:
            print("结界奖励")
        da_guo, da_bug_uo, mei_da_guo = self.jie_jie_number(handle)
        if da_guo >= 3 or mei_da_guo == 0:
            return self.refresh_jie_jie(handle)
        re, x, y = self.jie_chu_tu_po_block(handle)
        if re != 0:
            return -2
        time.sleep(random.randint(0, 5))
        mouse = Mouse()
        mouse.click(x, y)
        self.waiting(argument, handle)
        if self.click_img("yys/进攻结界按钮.bmp", handle, 0.90) == 0:
            return codedef.NORMAL_END
        else:
            if self.click_img("yys/进攻结界按钮2.bmp", handle, 0.90) == 0:
                return codedef.NORMAL_END
        return codedef.NORMAL_END

    # 刷新结界突破
    def refresh_jie_jie(self, handle):
        if self.click_img("yys/结界刷新冷却中.bmp", handle, 0.98) == 0:
            print("结界刷新冷却中")
            return 10
        else:
            if self.click_img("yys/结界刷新按钮.bmp", handle, 0.98) == 0:
                print("结界刷新按钮")
                time.sleep(1)
                if self.click_img("yys/结界刷新确定按钮.bmp", handle, 0.98) == 0:
                    print("结界刷新确定按钮")
        return codedef.NORMAL_END

    # 逐个结界块进行找图，找到第一个没打过的返回
    def jie_chu_tu_po_block(self, handle):
        tu = self.window.jie_tu(handle)
        tu.save('temp/temp.bmp')
        if self.metrics_x == 1920:
            x = 100 - 2 * 10 + 15
            y = 100 - 2 * 10 + 12
            w = 300 - 80
            h = 120 - 35
            w_silde = 230
            h_silde = 91
            jindu = 0.5
        else:
            x = 68
            y = 74
            w = 151
            h = 58
            w_silde = 158
            h_silde = 61
            jindu = 0.7


        point0 = [x, y]
        for i in range(9):
            if i == 0:
                point = point0
            else:
                point = [int(point0[0] + int(i % 3) * w_silde), int(point0[1] + int(i / 3) * h_silde)]
            point2 = [point[0] + w, point[1] + h]
            # print(str(i) + str(point))
            src_img = Img.cut_img_path('temp/temp.bmp', point, point2)
            Img.save('temp/temp' + str(i) + '.bmp', src_img)
            re, x, y = Img.find_img_in_img('temp/temp' + str(i) + '.bmp', self.mei_da_guo_path, jindu)
            if re == 0:
                return 0, x + handle.left + point[0], y + handle.top + point[1]
        return -1, 0, 0

    # 结界数量（打过了、打不过、没打过）
    def jie_jie_number(self, handle):
        # 获得游戏界面截图
        tu = self.window.jie_tu(handle)
        tu.save('temp/temp.bmp')
        re1 = Img.find_all_img_in_img('temp/temp.bmp', self.da_guo_le_path, 0.8)
        re2 = Img.find_all_img_in_img('temp/temp.bmp', self.da_bu_guo_path, 0.96)  # 匹配精度0.96
        re3 = Img.find_all_img_in_img('temp/temp.bmp', self.mei_da_guo_path, 0.90)
        # print("打过了" + str(re1) + ";打不过:" + str(re2) + ";没打过:" + str(re3))
        return re1, re2, re3

    def shou_dao_yai_qing(self, argument, handle):
        if self.click_img("yys/粗红叉按钮2.bmp", handle, 0.90) == 0:
            print("粗红叉按钮2")
        return 0

    def exit(self, argument, handle):
        if argument == SceneKey.JIE_JIE_TU_PO:
            if self.click_img("yys/退出结界黑.bmp", handle, 0.98) == 0:
                time.sleep(0.5)
                self.this_exit_zhang_jie(argument, handle)
            else:
                self.this_exit_zhang_jie(argument, handle)
        else:
            switcher = {
                SceneKey.SHI_FOU_YAO_QING_JI_XU: self.this_yao_qing_dui_you_ji_xu,
                SceneKey.TANG_SUO_ZHANG_JIE: self.this_exit_zhang_jie,
                SceneKey.TANG_SUO_ZHONG: self.this_exit_tang_suo,
                SceneKey.TANG_SUO: self.this_enter_jie_jie,
                SceneKey.SHOU_DAO_YAO_QING: self.shou_dao_yai_qing
            }
            # Get the function from switcher dictionary
            func = switcher.get(argument, self.father)(argument, handle)
            # Execute the function
            return func
        return codedef.NORMAL_END

