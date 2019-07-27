from Cteam_kun_25 import Team_kun_25
from Cmouse import Mouse
import time
from Cgame import Game
from Chandle import SceneKey
import codedef
from Cimg import Img
from win32api import GetSystemMetrics
from Cgouliang import Gouliang


class Team_kun_25_teammate(Team_kun_25):
    def __init__(self, Beater=True, BeatMax=True):
        super(Team_kun_25, self).__init__()
        self.metrics_x = GetSystemMetrics(0)    # 获取分辨率
        self.metrics_y = GetSystemMetrics(1)    # 获取分辨率
        self.huang_flag = False                 # 是否换狗粮

        self.Beater = Beater                    # 是否队长是打手
        self.BeatMax = BeatMax                  # 打手是否满级

        self.can_exited = False                 # 是否退出探索

    def set_exit(self, can_exited):
        self.can_exited = can_exited
        # print("set_exit")

    def judge_scenes(self, argument, handle):
        return Game.judge_scenes(self, argument, handle)

    def do_work(self, argument, handle):
        if self.judge_scenes(argument, handle) == codedef.SCENCE_REPEAT_END:
            if Game.if_exist("yys/进攻结界按钮.bmp", handle) == 0:
                self.fight_end(argument, handle)
                return codedef.TANG_GO_RIGHT
            return codedef.SCENCE_REPEAT_END
        switcher = {
            SceneKey.TANG_SUO_ZHONG: self.this_da_tang_suo,
            SceneKey.SHOU_DAO_YAO_QING: self.shou_dao_yao_qing,
            SceneKey.ZHANG_DOU_SHENG_LI: self.fight_win,
            SceneKey.ZHANG_DOU_ZHONG: self.this_zhang_dou_zhong,
            SceneKey.JIE_JIE_TU_PO: self.exit_jie_jie
        }
        func = switcher.get(argument, self.father)(argument, handle)
        return func

    def father(self, argument, handle):
        return Team_kun_25.do_work(self, argument, handle)

    def shou_dao_yao_qing(self, argument, handle):
        self.can_exited = False
        if self.click_img("yys/接受邀请按钮.bmp", handle) == 0:
            print("接受邀请按钮")
            return codedef.NORMAL_END
        return codedef.NORMAL_END

    def this_da_tang_suo(self, argument, handle):
        if self.huang_flag is True:     # 如果要换狗粮
            # 取消固定阵容
            if self.click_img("yys/已固定阵容.bmp", handle) != 0:
                pass
        else:
            # 固定阵容
            if self.click_img("yys/未固定阵容.bmp", handle) != 0:
                pass

        if self.if_exist("yys/探索奖励.bmp") == 0:
            self.can_exited = True

        if self.can_exited:
            if self.exit_tang_suo(handle) == codedef.EXIT_TANG_SUO:
                self.can_exited = False
                return codedef.NORMAL_END

        if self.click_img("yys/确认退出探索按钮.bmp", handle) == 0:
            return codedef.NORMAL_END

        return codedef.ZAI_TANG_SUO

    def this_zhang_dou_zhong(self, argument, handle):
        if self.huang_flag:
            # 如果要换狗粮
            # 如果没有全部稀有度按钮
            if self.if_exist("yys/全部稀有度按钮.bmp") != 0:
                if self.if_exist("yys/N卡选择按钮.bmp") != 0:
                    # 点晴明附近
                    x = int(handle.left + (handle.right - handle.left) / 4)
                    y = int(handle.top + (handle.bottom - handle.top) * 3 / 4)
                    m = Mouse()
                    m.click(x, y)
                else:
                    # 找没满级狗粮和拖上去替换
                    gouliang = Gouliang(self.metrics_x, self.metrics_y, handle)
                    gouliang.find_and_huang(False, bool(1 - self.Beater) and self.BeatMax)
                    self.click_img("yys/战斗中准备按钮.bmp", handle)
                    self.huang_flag = False
            else:
                if self.if_exist("yys/N卡选择按钮.bmp") != 0:
                    if self.click_img("yys/全部稀有度按钮.bmp", handle) == 0:
                        time.sleep(0.3)
                        self.click_img("yys/N卡选择按钮.bmp", handle)
        else:
            self.click_img("yys/战斗中准备按钮.bmp", handle)
            self.waiting(argument, handle)
        return codedef.NORMAL_END

    def fight_win(self, argument, handle):
        # 查找已满级的数量
        num_max_l = Img.find_all_img_in_img('temp/temp.bmp', "yys/已满级.bmp", 0.8)
        print("队员找已满级的数量:" + str(num_max_l))
        huan_num = 0    # 超过就换狗粮

        if self.Beater is False and self.BeatMax is True:
            huan_num += 1

        if num_max_l != -1:
            if num_max_l > huan_num:
                # 换狗粮标记
                self.huang_flag = True
        self.fight_end(argument, handle)
        return num_max_l

