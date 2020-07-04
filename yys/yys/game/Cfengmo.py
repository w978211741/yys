from Cgame import Game
from Chandle import SceneKey
import codedef
import time
from Cmouse import Mouse
from win32api import GetSystemMetrics


class fengmo(Game):
    def __init__(self, mod=0):
        super(fengmo, self).__init__()
        self.metrics_x = GetSystemMetrics(0)    # 获取分辨率
        self.metrics_y = GetSystemMetrics(1)    # 获取分辨率
        self.can_exited = False
        self.mod = mod
        pass

    def judge_scenes(self, argument, handle):
        return Game.judge_scenes(self, argument, handle)

    def do_work(self, argument, handle):
        if self.judge_scenes(argument, handle) == codedef.SCENCE_REPEAT_END:
            return codedef.SCENCE_REPEAT_END
        switcher = {
            SceneKey.TU_YAO: self.enter_feng_mo,
            SceneKey.TING_YUAN: self.find_feng_mo,
            SceneKey.FENG_MO_ZHI_SHI: self.feng_mo_zhi_shi,
            SceneKey.GE_REN_SHE_ZHI: self.she_zhi,
            SceneKey.XUAN_QU: self.enter_game,
            SceneKey.YOU_XIANG_DENG_LU: self.deng_lu,
            SceneKey.XUAN_ZHE_PING_TAI: self.xuan_ping_tai,
            SceneKey.YOU_XI_GONG_GAO: self.cha
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
        if Game.if_exist(path + "土曜界面.bmp") == 0:
            return SceneKey.TU_YAO
        if Game.if_exist("yys/batch_feng/个人设置界面.bmp") == 0:
            return SceneKey.GE_REN_SHE_ZHI
        if Game.if_exist("yys/batch_feng/选区界面.bmp") == 0:
            return SceneKey.XUAN_QU
        if Game.if_exist("yys/batch_feng/邮箱登录界面.bmp") == 0:
            return SceneKey.YOU_XIANG_DENG_LU
        if Game.if_exist("yys/batch_feng/选择平台界面.bmp") == 0:
            return SceneKey.XUAN_ZHE_PING_TAI
        if Game.if_exist("yys/batch_feng/游戏公告界面.bmp") == 0:
            return SceneKey.YOU_XI_GONG_GAO

        if Game.if_exist("yys/卷轴打开.bmp") == 0:
            return SceneKey.TING_YUAN
        if Game.if_exist("yys/卷轴未打开.bmp") == 0:
            return SceneKey.TING_YUAN
        return Game.get_scene(self, handle)

    def xuan_ping_tai(self, argument, handle):
        if self.click_img("yys/batch_feng/安卓平台按钮.bmp", handle, 0.90) == 0:
            time.sleep(2)
            return codedef.NORMAL_END

    def deng_lu(self, argument, handle):
        if self.click_img("yys/batch_feng/下拉按钮.bmp", handle, 0.90) == 0:
            time.sleep(0.2)
            return codedef.NORMAL_END
        else:
            if Game.if_exist("yys/batch_feng/收回按钮.bmp") == 0:
                time.sleep(0.2)
                if self.mod == 0:
                    re, x, y = self.window.find_img(handle, "yys/batch_feng/扫码登录.bmp", 0.9)
                    if re == 0:
                        mouse = Mouse()
                        mouse.click(x, y - 40)
                        time.sleep(1)
                        if self.click_img("yys/batch_feng/登录按钮.bmp", handle, 0.90) == 0:
                            time.sleep(1)
                    else:
                        re, x, y = self.window.find_img(handle, "yys/batch_feng/叉叉按钮.bmp", 0.9)
                        if re == 0:
                            mouse = Mouse()
                            mouse.mouse_to(x, y)
                            time.sleep(0.2)
                            mouse.m.scroll(vertical=-13)
                else:
                    src_x = int((handle.left + handle.right) / 2)
                    src_y = handle.top + int((handle.bottom - handle.top) * 2 / 3)
                    m = Mouse(self.metrics_x, self.metrics_y)
                    m.click(src_x, src_y)
                    time.sleep(1)
                    if self.click_img("yys/batch_feng/登录按钮.bmp", handle, 0.90) == 0:
                        time.sleep(1)
        return codedef.NORMAL_END

    def enter_game(self, argument, handle):
        # if self.can_exited is False:
        src_x = int((handle.left + handle.right) / 2)
        src_y = handle.top + int((handle.bottom - handle.top) * 4 / 5)
        m = Mouse(self.metrics_x, self.metrics_y)
        m.click(src_x, src_y)
        time.sleep(3)
        self.can_exited = True
        return codedef.FIGHT_BEGIN
        # else:
        #     src_x = handle.left + int((handle.right - handle.left)  * 19 / 20)
        #     src_y = handle.top + int((handle.bottom - handle.top) / 10)
        #     m = Mouse(self.metrics_x, self.metrics_y)
        #     m.click(src_x, src_y)
        #     time.sleep(2)
        #     self.can_exited = False
        #     if self.click_img("yys/batch_feng/切换账号按钮.bmp", handle) == 0:
        #         time.sleep(2.8)
        #         return codedef.FIGHT_END

        # return codedef.NORMAL_END

    def cha(self, argument, handle):
        return self.ju_jue_xuan_shang(argument, handle)

    def enter_feng_mo(self, argument, handle):
        if self.can_exited is False:
            if self.click_img("yys/逢魔之时按钮.bmp", handle, 0.90) == 0:
                time.sleep(0.8)
                if self.click_img("yys/前往按钮.bmp", handle, 0.90) == 0:
                    time.sleep(1.2)
                    self.can_exited = True

            else:
                self.click_img("yys/日常按钮.bmp", handle, 0.90)

        else:
            self.ju_jue_xuan_shang(argument, handle)

        return codedef.NORMAL_END

    def find_feng_mo(self, argument, handle):
        if self.click_img("yys/batch_feng/取消按钮.bmp", handle, 0.90) == 0:
            time.sleep(0.5)
        if self.can_exited is False:
            if self.click_img("yys/土曜按钮.bmp", handle, 0.90) == 0:
                time.sleep(0.5)
            else:
                src_x = handle.left + int((handle.right - handle.left) / 3)
                src_y = handle.top + int((handle.bottom - handle.top) * 2 / 3)
                tar_x = int(handle.left + handle.right / 2)
                tar_y = src_y
                self.tuo(src_x, src_y, tar_x, tar_y)

        else:
            src_x = handle.left + int((handle.right - handle.left) / 20)
            src_y = handle.top + int((handle.bottom - handle.top) / 10)
            m = Mouse(self.metrics_x, self.metrics_y)
            m.click(src_x, src_y)
            time.sleep(2)

        return codedef.NORMAL_END


    def feng_mo_zhi_shi(self, argument, handle):
        if Game.if_exist("yys/奖励未领.bmp") == 0:
            if self.click_img("yys/发现按钮.bmp", handle, 0.90) == 0:
                time.sleep(2)
        if Game.if_exist("yys/奖励已领.bmp") == 0:
            self.can_exited = True

        if self.can_exited:
            if self.click_img("yys/退出探索.bmp", handle) == 0:
                time.sleep(0.8)

        return codedef.NORMAL_END

    def she_zhi(self, argument, handle):
        if self.click_img("yys/batch_feng/切换账号按钮.bmp", handle) == 0:
            time.sleep(2.8)
            return codedef.FIGHT_END
        else:
            self.click_img("yys/batch_feng/用户中心按钮.bmp", handle)

        return codedef.NORMAL_END


    def tuo(self, src_x, src_y, tar_x, tar_y):
        m = Mouse(self.metrics_x, self.metrics_y)
        dx = tar_x - src_x
        dy = tar_y - src_y
        x = src_x
        y = src_y
        m.mouse_to(x, y)  # 鼠标移动到
        m.left_down()
        i = 1
        # ddy = int(dy / 10)

        # while i < 10:
        #     time.sleep(0.03)
        #     m.mouse_to(x, y + ddy * i)  # 鼠标移动到
        #     i += 1
        #
        # i = 1
        ddx = int(dx / 6)

        while i < 6:
            time.sleep(0.05)
            m.mouse_to(x + ddx * i, tar_y)  # 鼠标移动到
            i += 1

        time.sleep(0.1)
        m.mouse_to(tar_x + 3, tar_y)  # 鼠标移动到
        time.sleep(0.3)
        m.left_up()

        # time.sleep(1)
        # Window.temp_jie_tu(self.handle)# 更新截图
        return


