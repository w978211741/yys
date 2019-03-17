from Cgame import Game, SceneKey
from Cimg import Img
from Cmouse import Mouse
from Cwindow import Window
import sys
import time


class Liaojiejie (Game):

    def do_work(self, argument, handle):
        switcher = {
            SceneKey.NUKOWN: self.error_scene,
            SceneKey.ZHANG_DOU_SHI_BAI: self.fight_end,
            SceneKey.ZHANG_DOU_SHENG_LI: self.fight_end,
            SceneKey.ZHANG_DOU_JIANG_LI: self.fight_end,
            SceneKey.JIE_JIE_TU_PO: self.da_liao_jie_jie_main,
            SceneKey.TANG_SUO: self.enter_jie_jie,
            SceneKey.ZHANG_DOU_ZHONG: self.waiting,
            SceneKey.XUAN_SHANG_FENG_YING_YAO_QING: self.hon_cha_exit
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, self.error_scene)(handle)
        # Execute the function
        return func

    def enter_liao_jie_jie(self, handle):
        if self.click_img("yys/寮结界灰.bmp", handle, 0.90) == 0:
            print("寮结界灰")

    def get_ji_bai_times(self):
        target_img_path = "yys/击败次数.bmp"
        re, x, y = Img.find_img_in_img('temp/temp.bmp', target_img_path, 0.90)
        if re != 0:
            return -1
        x1 = 60  # 左右偏移量
        y1 = 0  # 上下偏移量
        width = 34  # 目标宽度
        height = 20  # 目标高度
        # 最后一个参数，如果是黑底白字 赋True 白底黑字 赋False
        power_number_str = Img.find_str_in_img(self.src_img_path, target_img_path, x1, y1, width, height, False)
        if power_number_str != "-1":
            power_number_str = power_number_str.split('/')
            power_number = power_number_str[0]
            if power_number == '':
                return -1
            return int(power_number)
        return -1

    # 逐个寮结界块进行找图，找到第一个没打过的返回
    def jie_chu_tu_po_block_liao(self, handle):
        tu = self.window.jie_tu(handle)
        tu.save('temp/temp.bmp')
        x = 100 - 2 * 10 + 15 + 188
        y = 100 - 2 * 10 + 12 + 10
        w = 300 - 82
        h = 120 - 35
        point0 = [x, y]
        for i in range(8):
            if i == 0:
                point = point0
            else:
                point = [int(point0[0] + int(i % 2) * 226), int(point0[1] + int(i / 4) * 91)]
            point2 = [point[0] + w, point[1] + h]
            print(str(i) + str(point))
            src_img = Img.cut_img_path('temp/temp.bmp', point, point2)
            Img.save('temp/temp' + str(i) + '.bmp', src_img)
            re, x, y = Img.find_img_in_img('temp/temp' + str(i) + '.bmp', self.mei_da_guo_path)
            if re == 0:
                return 0, x + handle.left + point[0], y + handle.top + point[1]
        return -1, 0, 0

    # 返回值
    # 0：完成
    # 1：无法判断是在个人还是寮突破（右侧按钮无法识别）
    # 2：会长未选择寮进行突破
    # 3：次数已经用完（十分钟回复一次，最高存储6次）
    # 4：分块后找不到没打过的（理应不出现，因为是先识别出没打过的数量之后才会调用到的）
    def da_liao_jie_jie_main(self, handle):
        na = self.ge_ren_or_liao(handle)
        if na == -1:
            return 1
        if na == 0:
            self.enter_liao_jie_jie(handle)
            return 0
        if self.jie_tu_if_exist(handle, "yys/会长未选择寮进行突破.bmp") == 0:
            print("会长未选择寮进行突破")
            return 2
        times = self.get_ji_bai_times()
        if times <= 0:
            return 3
        r1, r2, r3 = self.jie_jie_number(handle)
        if r1 == 0:
            # 向下滚四排
            Liaojiejie.xia_yi_pai(4, handle)
            return 0
        if r3 == 0:
            # 向上滚一排
            Liaojiejie.xia_yi_pai(-1, handle)
            return 0
        # 此时已经找到最底部且没打过的
        re, x, y = self.jie_chu_tu_po_block_liao(handle)
        if re != 0:
            return 4
        mouse = Mouse()
        mouse.click(x, y)
        self.waiting(handle)
        if self.click_img("yys/进攻结界按钮.bmp", handle, 0.90) == 0:
            print("进攻结界按钮")
        return 0

    @staticmethod
    def xia_yi_pai(pai, handle):
        m = Mouse()
        m.mouse_to(handle.left + 600, handle.top + 200)
        time.sleep(0.2)
        # 滚轮滚2为一排
        m.gun_lun(-2 * pai, 0)
        time.sleep(0.2)
