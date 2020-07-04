from Cteam_kun_25 import Team_kun_25
from Cgame import Game
from Chandle import SceneKey
from Cimg import Img
from Cmouse import Mouse
from CfightUp import FightUp
import sys
import time
import codedef
from win32api import GetSystemMetrics
from Cgouliang import Gouliang


class Team_kun_25_captain(Team_kun_25):
    right = True
    def __init__(self, UP=None, BOSS=True, QingMax=True, Beater=True,
                 BeatMax=True, Chapter='第二十八章',IsOne=False):
        super(Team_kun_25, self).__init__()
        self.metrics_x = GetSystemMetrics(0)    # 获取分辨率
        self.metrics_y = GetSystemMetrics(1)    # 获取分辨率
        self.fight_up = FightUp(self.metrics_x)
        self.UP = UP                            # 狗粮up
        self.BOSS = BOSS                        # 是否打boss
        self.Beater = Beater                    # 是否是打手
        self.QingMax = QingMax                  # 清明是否满级
        self.BeatMax = BeatMax                  # 打手是否满级

        self.huang_flag = False                 # 是否换狗粮
        self.yao_qing = True                    # 是否邀请队员继续
        self.yao_qing_wait = 0                  # 邀请队员后等待
        self.da_guai = True                     # 是否打怪
        self.go_right_times = 0                 # 向右走计数
        self.can_exited = False                 # 是否退出探索

        self.index_dian_friend = 0              # 点第几个好友，0~5
        self.Chapter = Chapter                  # 章节

        self.IsOne = IsOne                      # 是否是单人模式

    def set_da_guai(self, da_guai):
        self.da_guai = da_guai

    def set_yao_qing(self, yao_qing):
        self.yao_qing = yao_qing

    def judge_scenes(self, argument, handle):
        return Team_kun_25.judge_scenes(self, argument, handle)

    def do_work(self, argument, handle):
        if self.judge_scenes(argument, handle) == codedef.SCENCE_REPEAT_END:
            if Game.if_exist("yys/进攻结界按钮.bmp") == 0:
                self.fight_end(argument, handle)
                return codedef.TANG_GO_RIGHT
            return codedef.SCENCE_REPEAT_END
        switcher = {
            SceneKey.TANG_SUO_ZHONG: self.this_da_tang_suo,
            SceneKey.SHI_FOU_YAO_QING_JI_XU: self.this_yao_qing_dui_you_ji_xu,
            SceneKey.SHOU_DAO_YAO_QING: self.shou_dao_yai_qing,
            SceneKey.ZHANG_DOU_SHENG_LI: self.fight_win,
            SceneKey.ZHANG_DOU_ZHONG: self.this_zhang_dou_zhong,
            SceneKey.TANG_SUO_ZHANG_JIE: self.this_tang_suo_zhang_jie,
            SceneKey.TANG_SUO: self.this_tang_suo,
            SceneKey.JIE_JIE_TU_PO: self.exit_jie_jie
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, self.father)(argument, handle)

        return func



    def this_tang_suo(self, argument, handle):
        # 4 管 1-6 ；10 管 7-12；
        # 选28章
        if self.click_img("yys/" + self.Chapter + ".bmp", handle) != 0:
            m = Mouse(self.metrics_x, self.metrics_y)
            dx = 0
            dy = -1 * int(0.5 * (handle.top - handle.bottom))

            imax = 6
            index = 0
            while index < imax:
                x1 = int(handle.left + 0.85 * (handle.right - handle.left))
                y1 = int(handle.top + 0.35 * (handle.bottom - handle.top))
                m.absolute(x1, y1, dx, dy)
                time.sleep(1.5)
                window_img = self.window.jie_tu(handle)
                window_img.save('temp/temp.bmp')
                if Game.if_exist("yys/第一章.bmp", 0.95) == 0:
                    break
                index += 1

            index = 0
            imax = 12
            dy = int(-1 * dy / 3)
            while index < imax:
                window_img = self.window.jie_tu(handle)
                window_img.save('temp/temp.bmp')
                if self.click_img("yys/" + self.Chapter + ".bmp", handle) == 0:
                    break

                x1 = int(handle.left + 0.85 * (handle.right - handle.left))
                y1 = int(handle.top + 0.8 * (handle.bottom - handle.top))
                m.absolute(x1, y1, dx, dy)
                time.sleep(1.5)

                index += 1

            time.sleep(1.5)
        else:
            time.sleep(3)
        return codedef.NORMAL_END

    def this_tang_suo_zhang_jie(self, argument, handle):
        if self.IsOne:
            if self.click_img("yys/探索困难按钮.bmp", handle) != 0:
                time.sleep(1)
            elif self.click_img("yys/探索按钮.bmp", handle) != 0:
                time.sleep(1)
            return codedef.NORMAL_END

        # 可邀请继续就点邀请
        if self.yao_qing:
            if self.click_img("yys/组队按钮.bmp", handle) != 0:
                self.click_img("yys/探索困难按钮.bmp", handle)
            else:
                time.sleep(2)

            if self.click_img("yys/组队好友.bmp", handle) == 0 or self.click_img("yys/组队好友灰.bmp", handle) == 0:
                if self.yao_qing_wait == 0:
                    time.sleep(2.5)
                    self.dian_friend(handle, self.index_dian_friend)

                    # i = 4
                    # while i >= 0:
                    #     self.dian_friend(handle, i)
                    #     time.sleep(0.3)
                    #     i -= 1

                    time.sleep(0.5)
                    # 如果后续有自动选中了一个，那就先点一下别的，再回来，如想点1，先点了2，再点1，即可
                    if self.click_img("yys/邀请按钮.bmp", handle) == 0:
                        self.yao_qing_wait = 2
                        self.index_dian_friend += 1
                        if self.index_dian_friend >= 5:
                            self.index_dian_friend = 0
                else:
                    self.yao_qing_wait -= 1
            return codedef.YAO_QING_ZHONG
        return codedef.NORMAL_END

    def this_zhang_dou_zhong(self, argument, handle):
        self.set_da_guai(False)
        if self.huang_flag:
            # 如果要换狗粮
            # 如果没有全部稀有度按钮
            if Game.if_exist("yys/全部稀有度按钮.bmp") != 0:
                if Game.if_exist("yys/N卡选择按钮.bmp") != 0:
                    # 点晴明附近
                    x = int(handle.left + (handle.right - handle.left) / 4)
                    y = int(handle.top + (handle.bottom - handle.top) * 3 / 5)
                    m = Mouse()
                    m.click(x, y)
                    time.sleep(2)
                else:
                    # 找没满级狗粮和拖上去替换
                    gouliang = Gouliang(self.metrics_x, self.metrics_y, handle)
                    gouliang.find_and_huang(True, self.Beater and self.BeatMax)
                    self.click_img("yys/战斗中准备按钮.bmp", handle)
                    print("yys/战斗中准备按钮.bmp")
                    self.huang_flag = False
            else:
                if Game.if_exist("yys/N卡选择按钮.bmp") != 0:
                    if self.click_img("yys/全部稀有度按钮.bmp", handle) == 0:
                        time.sleep(0.3)
                        self.click_img("yys/N卡选择按钮.bmp", handle)
        else:
            self.waiting(argument, handle)
        return codedef.NORMAL_END

    def fight_win(self, argument, handle):
        # 查找已满级的数量
        num_max_l = Img.find_all_img_in_img('temp/temp.bmp', "yys/已满级.bmp", 0.8)
        print("队长找已满级的数量:" + str(num_max_l))
        huan_num = 0    # 超过就换狗粮

        if self.QingMax is True:
            huan_num = huan_num + 1

        if self.Beater is True and self.BeatMax is True:
            huan_num = huan_num + 1

        print("队长数量:" + str(huan_num))
        if num_max_l != -1:
            if num_max_l > huan_num:
                # 换狗粮标记
                self.huang_flag = True

        self.fight_end(argument, handle)

        return num_max_l

    def this_da_tang_suo(self, argument, handle):
        if self.yao_qing:
            self.yao_qing = False
            self.yao_qing_wait = 0
            self.index_dian_friend = 0

        if self.huang_flag is True:     # 如果要换狗粮
            # 取消固定阵容
            if self.click_img("yys/已固定阵容.bmp", handle) != 0:
                pass
        else:
            # 固定阵容
            if self.click_img("yys/未固定阵容.bmp", handle) != 0:
                pass

        if Game.if_exist("yys/探索奖励.bmp") == 0:
            self.can_exited = True

        if self.can_exited:
            if self.exit_tang_suo(handle) == codedef.EXIT_TANG_SUO:
                self.can_exited = False
                self.go_right_times = 0
                return codedef.EXIT_TANG_SUO

        if self.click_img("yys/确认退出探索按钮.bmp", handle) == 0:
            self.go_right_times = 0
            return codedef.EXIT_TANG_SUO

        return self.da_tang_suo_gui(handle)

    def this_yao_qing_dui_you_ji_xu(self, argument, handle):
        self.can_exited = False
        # 可邀请继续就点邀请
        print('可邀请继续就点邀请' + str(self.yao_qing))
        if self.yao_qing:
            self.yao_qing_wait = 3
            print('yao_qing')
            return self.yao_qing_dui_you_ji_xu(argument, handle)
        return codedef.YAO_QING_DUI_YOU_JI_XU

    # 其他情况按父类的处理
    def father(self, argument, handle):
        return Team_kun_25.do_work(self, argument, handle)

    # 拒绝悬赏封印邀请
    def shou_dao_yai_qing(self, argument, handle):
        if self.click_img("yys/粗红叉按钮2.bmp", handle, 0.90) == 0:
            print("粗红叉按钮2")
        return codedef.NORMAL_END

    # 在探索中界面打探索怪
    def da_tang_suo_gui(self, handle):
        if self.yao_qing_wait > 0:
            self.yao_qing_wait -= 1
            return codedef.NORMAL_END

        if self.da_guai:
            if self.UP != codedef.UP_C_NULL:
                if self.fight_up.fight_UP_guai(handle, self.UP, "yys/打小怪.bmp") == codedef.NORMAL_END:
                    return codedef.BEGIN_DA_GUAI
            else:
                if self.click_img("yys/打小怪.bmp", handle) == 0:
                    print("打小怪")
                    return codedef.BEGIN_DA_GUAI

            if self.BOSS and self.click_img("yys/打boss.bmp", handle) == 0:
                print("打boss")
                return codedef.BEGIN_DA_BOSS

            if self.right and self.click_img("yys/探索向右走.bmp", handle) == 0:
                print("探索向右走")
                time.sleep(0.5)
                self.click_img("yys/探索向右走.bmp", handle)
                time.sleep(1.5)
                self.go_right_times += 1
                if self.go_right_times >= codedef.TANG_GO_RIGHT_MAX:
                    self.can_exited = True
                return codedef.TANG_GO_RIGHT

        return codedef.NORMAL_END

    def dian_friend(self, handle, index):
        # （0.4 0.3）（0.6 0.3）
        # （0.4 0.45）（0.6 0.45）
        # （0.4 0.6）（0.6 0.6）
        dxy = [[0.4, 0.35], [0.6, 0.35], [0.4, 0.45], [0.6, 0.45], [0.4, 0.6], [0.6, 0.6]]
        x = dxy[index][0]
        y = dxy[index][1]
        xx = int(handle.left + x * (handle.right - handle.left))
        yy = int(handle.top + y * (handle.bottom - handle.top))
        m = Mouse()
        m.click(xx, yy)
        return codedef.NORMAL_END





