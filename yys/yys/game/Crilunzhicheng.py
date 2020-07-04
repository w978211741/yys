from Cgame import Game
from Chandle import SceneKey
from Cimg import Img
from Cmouse import Mouse
from Cwindow import Window
import sys
import codedef
import time
from win32api import GetSystemMetrics


class rilunzhicheng(Game):

    def __init__(self, buyyan=0, buyyu=0, mod=0):
        super(rilunzhicheng, self).__init__()
        # 获取分辨率
        self.m = Mouse(GetSystemMetrics(0), GetSystemMetrics(1))

        self.HadOpenEye = False

        self.mod = mod    # 0刷玉，1刷层

        self.top = 0.25
        self.left = 0.15

        self.img = Img()
        self.mouse = Mouse()

        self.arr1 = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7],
                      [2, 1], [2, 4], [2, 6],
                      [3, 1], [3, 4], [3, 6]]

        self.arr2 = [[1, 7], [1, 6], [1, 5], [1, 4], [1, 3], [1, 2], [1, 1], [1, 0],
                      [2, 1], [2, 4], [2, 6],
                      [3, 1], [3, 4], [3, 6]]

        self.arr3 = [[2, 0], [2, 1], [2, 2], [2, 3], [2, 4]     , [2, 5], [2, 6], [2, 7],
                     [1, 1], [1, 4], [1, 6],
                     [0, 1], [0, 4], [0, 6]]

        self.arr4 = [[2, 7], [2, 6], [2, 5], [2, 4], [2, 3], [2, 2], [2, 1], [2, 0],
                     [1, 1], [1, 4], [1, 6],
                     [0, 1], [0, 4], [0, 6]]

        self.da_wang = False

        self.buyyan = buyyan    # 花勾玉买眼的最大次数
        self.buyyu = buyyu      # 花勾玉买溯玉的最大次数

        self.jiao_pos = 0

    def do_work(self, argument, handle):
        switcher = {
            SceneKey.NUKOWN: self.error_scene,
            SceneKey.ZHANG_DOU_JIANG_LI: self.fight_end,
            SceneKey.ZHANG_DOU_SHENG_LI: self.fight_end,
            SceneKey.ZHANG_DOU_SHI_BAI: self.fight_end,
            SceneKey.XUAN_SHANG_FENG_YING_YAO_QING: self.fight_end,

            SceneKey.LUN_HUI_MI_JING: self.this_main,
            SceneKey.DA_GUAI_KAI_SHI: self.kai_shi_da_guai,
            SceneKey.XUAN_ZI_YUAN: self.xuan_zi_yuan,

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
        if Game.if_exist(path + "悬赏封印邀请界面.bmp") == 0:
            return SceneKey.XUAN_SHANG_FENG_YING_YAO_QING
        if Game.if_exist(path + "战斗奖励界面.bmp") == 0:
            return SceneKey.ZHANG_DOU_JIANG_LI
        if Game.if_exist(path + "战斗胜利界面.bmp") == 0:
            return SceneKey.ZHANG_DOU_SHENG_LI
        if Game.if_exist(path + "战斗失败界面.bmp") == 0:
            return SceneKey.ZHANG_DOU_SHI_BAI


        if Game.if_exist("yys/日轮之城/轮回秘境界面.bmp") == 0:
            return SceneKey.LUN_HUI_MI_JING

        if Game.if_exist("yys/日轮之城/打怪开始界面.bmp") == 0:
            return SceneKey.DA_GUAI_KAI_SHI

        if Game.if_exist("yys/日轮之城/选资源界面.bmp") == 0:
            return SceneKey.XUAN_ZI_YUAN

        return SceneKey.NUKOWN

    def xuan_zi_yuan(self, argument, handle):
        if self.click_img("yys/日轮之城/选金币按钮.bmp", handle) == 0:
            time.sleep(1)
        if self.click_img("yys/日轮之城/确认按钮.bmp", handle) == 0:
            time.sleep(1)
        return codedef.NORMAL_END

    def re_set(self):
        self.jiao_pos = 0
        self.HadOpenEye = False
        self.da_wang = False
        return codedef.NORMAL_END

    def this_main(self, argument, handle):
        self.HadOpenEye = False
        self.da_wang = False
        # 如果是刷层，先看看有没有下一关


        if self.if_exist("yys/日轮之城/已开眼.bmp", 0.8) == 0:
            self.HadOpenEye = True
        elif self.if_exist("yys/日轮之城/已开眼2.bmp", 0.8) == 0:
            self.HadOpenEye = True

        if self.click_img("yys/日轮之城/获取时玉.bmp", handle, 0.8) == 0:
            time.sleep(1)
        if self.click_img("yys/日轮之城/获取奖励.bmp", handle, 0.8) == 0:
            time.sleep(1)
        if self.click_img("yys/日轮之城/获取轮回眼.bmp", handle, 0.8) == 0:
            time.sleep(1)

        if self.mod == 1:
            if self.click_img("yys/日轮之城/时玉.bmp", handle, 0.8) == 0:
                time.sleep(1.5)
                return codedef.NORMAL_END
            elif self.click_img("yys/日轮之城/轮回眼.bmp", handle, 0.8) == 0:
                time.sleep(1.5)
                return codedef.NORMAL_END
            elif self.click_img("yys/日轮之城/下一关.bmp", handle, 0.8) == 0:
                time.sleep(1)
                if self.click_img("yys/日轮之城/确定按钮.bmp", handle, 0.8) == 0:
                    time.sleep(1)
                    self.re_set()
                return codedef.NORMAL_END

        # 没开眼
        if self.HadOpenEye is False:

            # 分格子，看看缺口在哪个角
            # if self.jiao_pos == 0:
            self.jiao_pos = self.checkJiao(handle)

            re = codedef.NORMAL_END
            if self.jiao_pos == 1:
                re = self.xunhuan_da(handle, self.arr1)
            elif self.jiao_pos == 2:
                re = self.xunhuan_da(handle, self.arr2)
            elif self.jiao_pos == 3 :
                re = self.xunhuan_da(handle, self.arr3)
            elif self.jiao_pos == 4:
                re = self.xunhuan_da(handle, self.arr4)

            if re == codedef.ERROR_END:
                self.da_wang = True
            else:
                time.sleep(1)
                # 如果还在轮回秘境界面，重新判断
                # if self.if_exist("yys/日轮之城/轮回秘境界面.bmp", 0.98) == 0:
                #     self.jiao_pos = self.checkJiao(handle)

            if self.da_wang:
                if self.if_exist("yys/日轮之城/已开眼.bmp", 0.98) == 0:
                    self.HadOpenEye = True
                elif self.if_exist("yys/日轮之城/已开眼2.bmp", 0.98) == 0:
                    self.HadOpenEye = True
                else:
                    if self.if_exist("yys/日轮之城/买眼按钮.bmp") == 0:
                        if self.buyyan > 0:
                            self.buyyan -= 1
                            if self.click_img("yys/日轮之城/买眼按钮.bmp", handle, 0.98) == 0:
                                time.sleep(2)
                        else:
                            # 直接当做打完，这样副本次数就会累加，最后结束脚本
                            return codedef.FIGHT_END
                    elif self.click_img("yys/日轮之城/开眼按钮.bmp", handle, 0.98) == 0:
                        time.sleep(2)
        else:
            if self.click_img("yys/日轮之城/时玉.bmp", handle, 0.8) == 0:
                time.sleep(1.5)
            elif self.click_img("yys/日轮之城/轮回眼.bmp", handle, 0.8) == 0:
                time.sleep(1.5)
            elif self.click_img("yys/日轮之城/下一关.bmp", handle, 0.8) == 0:
                time.sleep(1)
                if self.click_img("yys/日轮之城/确定按钮.bmp", handle, 0.8) == 0:
                    time.sleep(1)
                    self.re_set()
            elif self.click_img("yys/日轮之城/奖励.bmp", handle, 0.8) == 0:
                time.sleep(1)

        return codedef.NORMAL_END

    def kai_shi_da_guai(self, argument, handle):
        if self.click_img("yys/未固定阵容.bmp", handle) == 0:
            time.sleep(0.5)
        if self.click_img("yys/日轮之城/单人.bmp", handle) == 0:
            time.sleep(1)

        return codedef.NORMAL_END


    # 返回缺口位置 1左上角，2右上角，3左下角，4右下角
    def checkJiao(self, handle):
        jiao1 = self.Jiao(handle, 0, 0)
        jiao2 = self.Jiao(handle, 7, 0)
        jiao3 = self.Jiao(handle, 0, 3)
        jiao4 = self.Jiao(handle, 7, 3)
        if jiao1 != 0 and jiao2 == 0 and jiao3 == 0 and jiao4 == 0:
            return 1
            pass
        elif jiao1 == 0 and jiao2 != 0 and jiao3 == 0 and jiao4 == 0:
            return 2
            pass
        elif jiao1 == 0 and jiao2 == 0 and jiao3 != 0 and jiao4 == 0:
            return 3
            pass
        elif jiao1 == 0 and jiao2 == 0 and jiao3 == 0 and jiao4 != 0:
            return 4
            pass

        jiao1 = self.Jiao(handle, 0, 0)
        jiao2 = self.Jiao(handle, 7, 0)
        jiao3 = self.Jiao(handle, 0, 3)
        jiao4 = self.Jiao(handle, 7, 3)
        if jiao1 != 0 and jiao2 == 0 and jiao3 == 0 and jiao4 == 0:
            return 1
            pass
        elif jiao1 == 0 and jiao2 != 0 and jiao3 == 0 and jiao4 == 0:
            return 2
            pass
        elif jiao1 == 0 and jiao2 == 0 and jiao3 != 0 and jiao4 == 0:
            return 3
            pass
        elif jiao1 == 0 and jiao2 == 0 and jiao3 == 0 and jiao4 != 0:
            return 4
            pass

        if jiao1 != 0:
            return 1
            pass
        elif jiao2 != 0:
            return 2
            pass
        elif jiao3 != 0:
            return 3
            pass
        elif jiao4 != 0:
            return 4
            pass

        return 1

    # 判断某个位置是否是没打过，是未打过的话，返回0，否则返回非0
    def Jiao(self, handle, i, j):
        name = "temp/checkJiao.bmp"

        self.savekuai(handle, i, j, name)

        re, x, y = self.img.find_img_in_img(name, "yys/日轮之城/未打过.bmp")

        return re

    def savekuai(self, handle, i, j, name):
        kuang = int(0.1 * (handle.right - handle.left))
        point = [int(self.left * (handle.right - handle.left)) + kuang * (i + 0),
                 int(self.top * (handle.bottom - handle.top)) + kuang * (j + 0)]
        point2 = [int(self.left * (handle.right - handle.left)) + kuang * (i + 1),
                  int(self.top * (handle.bottom - handle.top)) + kuang * (j + 1)]

        tag_img = self.img.cut_img_path('temp/temp.bmp', point, point2)

        self.img.save(name, tag_img)
        return codedef.NORMAL_END

    def da(self, handle, i, j):
        name = "temp/da.bmp"

        self.savekuai(handle, i, j, name)

        re, x, y = self.img.find_img_in_img(name, "yys/日轮之城/未打过.bmp")

        if re != 0:
            re, x, y = self.img.find_img_in_img(name, "yys/日轮之城/未打过2.bmp")

        if re == 0:
            kuang = int(0.1 * (handle.right - handle.left))
            point = [int(self.left * (handle.right - handle.left)) + kuang * (i + 0),
                     int(self.top * (handle.bottom - handle.top)) + kuang * (j + 0)]
            x += handle.left + point[0]
            y += handle.top + point[1]
            self.mouse.click(x, y)
            return codedef.NORMAL_END


        return codedef.ERROR_END

    def xunhuan_da(self, handle, arr):
        name = 0

        # 0是刷玉，1是刷层，直接打一排就开眼
        if self.mod == 0:
            ilen = len(arr)
        else:
            ilen = 8

        while name < ilen:
            p = arr[name]
            i = p[1]
            j = p[0]
            if self.da(handle, i, j) == codedef.NORMAL_END:
                time.sleep(1)
                return codedef.NORMAL_END
            name += 1
        return codedef.ERROR_END