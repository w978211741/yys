from Cimg import cimg
from enum import Enum, IntEnum, unique
from Cmouse import cmouse
import sys
import win32con
import time


class cgame:
    daguolePath = 'yys/打过了.bmp'
    dabuguoPath = 'yys/打不过.bmp'
    meidaguoPath = 'yys/没打过.bmp'

    # 探索界面的上部分，最后是最上面的长条形截图
    def __init__(self):
        self.src_img_path = 'temp/temp.bmp'
    # t4 复杂图 tupo1 突破 来找到简单图 再识别文字

    def GetTuPoJuan(self,window,left, top, right, bottom):
        cfindimg = cimg()
        #获得游戏界面截图
        tu = window.jietu(left, top+ 50, right, top + 80)
        tu.save('temp/temp.bmp')
        tagimgpath = "yys/突破卷数量.bmp"
        x1 = 60  # 左右偏移量
        y1 = 1  # 上下偏移量
        width = 70  # 目标宽度
        heigh = 30  # 目标高度
        tupoNumberstr = cfindimg.FindStrInImg(self.src_img_path, tagimgpath, x1, y1, width, heigh)
        if tupoNumberstr != "-1":
            tupoNumberstr = tupoNumberstr.split('/')
            tupoNumber = tupoNumberstr[0]
            return int(tupoNumber)
        return tupoNumberstr

    def GetTuPoJuan2(self,window,left, top, right, bottom):
        cfindimg = cimg()
        #获得游戏界面截图
        tu = window.jietu(left, bottom - 130, right, bottom - 75)
        tu.save('temp/temp.bmp')
        tagimgpath = "yys/突破卷数量2.bmp"
        x1 = 54  # 左右偏移量
        y1 = 1  # 上下偏移量
        width = 70  # 目标宽度
        heigh = 30  # 目标高度
        tupoNumberstr = cfindimg.FindStrInImg(self.srcimgpath, tagimgpath, x1, y1, width, heigh)
        if tupoNumberstr != "-1":
            tupoNumberstr = tupoNumberstr.split('/')
            tupoNumber = tupoNumberstr[0]
            if tupoNumber == '':
                return -1
            return int(tupoNumber)
        return tupoNumberstr

    def GetTiLi(self,window,left, top, right, bottom):
        c_find_img = cimg()
        # 获得游戏界面截图
        tu = window.jietu(left, top + 50, right, top + 80)
        tu.save('temp/temp.bmp')
        target_img_path = "yys/体力数量.bmp"
        x1 = 65  # 左右偏移量
        y1 = 1  # 上下偏移量
        width = 95  # 目标宽度
        height = 30  # 目标高度
        power_number_str = c_find_img.FindStrInImg(self.srcimgpath, target_img_path, x1, y1, width, height)
        if power_number_str != "-1":
            power_number_str = power_number_str.split('/')
            power_number = power_number_str[0]
            if power_number == '':
                return -1
            return int(power_number)
        return power_number_str


    def IfExist(self,Path):
        findimg = cimg()
        re, x, y = findimg.FindImgInImg('temp/temp.bmp', Path, 0.90)
        return re

    def newGetscene(self,window,WindowHandle):
        windowimg = window.jietu((WindowHandle.left, WindowHandle.top, WindowHandle.right, WindowHandle.bottom))
        windowimg.save('temp/temp.bmp')
        path = "yys/scene/"
        if self.IfExist(path + "庭院界面.bmp") == 0:
            return SceneKey.TINGYUAN
        if self.IfExist(path + "探索界面.bmp") == 0:
            return SceneKey.TANGSUO
        if self.IfExist(path + "町中界面.bmp") == 0:
            return SceneKey.DINGZHONG







    # 确定自己在哪个场景
    def Getscene(self, scene, left, top, right, bottom, errornumber):
        re, x, y = scene.Findimg(left, top, right, bottom, "yys/庭院界面.bmp")
        if re == 0:
            sceneF = 0
            return sceneF
        re, x, y = scene.Findimg(left, top, right, bottom, "yys/探索界面.bmp")#有探索是在探索
        if re == 0:
            sceneF = 1
            return sceneF
        re, x, y = scene.Findimg(left, top, right, bottom, "yys/町中界面.bmp")#有庭院是在町中
        if re == 0:
            sceneF = 2
            return sceneF
        re, x, y = scene.Findimg(left, top, right, bottom, "yys/结界突破界面.bmp")  # 结界突破界面
        if re == 0:
            sceneF = 3
            re, x, y = scene.Findimg(left, top, right, bottom, "yys/战斗奖励.bmp")  # 战斗奖励界面
            if re == 0:
                sceneF = 6
            return sceneF
        re, x, y = scene.Findimg(left, top, right, bottom, "yys/斗技中界面.bmp")  # 斗技中界面
        if re == 0:
            sceneF = 11
            return sceneF
        re, x, y = scene.Findimg(left, top, right, bottom, "yys/退出战斗按钮.bmp")  # 战斗界面
        if re == 0:
            sceneF = 4
            return sceneF
        re, x, y = scene.Findimg(left, top, right, bottom, "yys/退出斗技按钮.bmp")  # 战斗界面
        if re == 0:
            sceneF = 4
            return sceneF
        re, x, y = scene.Findimg(left, top, right, bottom, "yys/战斗胜利.bmp")  # 战斗胜利界面
        if re == 0:
            sceneF = 5
            return sceneF
        re, x, y = scene.Findimg(left, top, right, bottom, "yys/战斗奖励.bmp")  # 战斗奖励界面
        if re == 0:
            sceneF = 6
            return sceneF
        re, x, y = scene.Findimg(left, top, right, bottom, "yys/战斗失败.bmp")  # 战斗失败界面
        if re == 0:
            sceneF = 7
            return sceneF
        re, x, y = scene.Findimg(left, top, right, bottom, "yys/探索中界面.bmp")  # 探索中界面
        if re == 0:
            sceneF = 8
            return sceneF
        re, x, y = scene.Findimg(left, top, right, bottom, "yys/协战队伍界面.bmp")  # 组队中界面
        if re == 0:
            sceneF = 9
            return sceneF
        re, x, y = scene.Findimg(left, top, right, bottom, "yys/斗技界面.bmp")  # 斗技界面
        if re == 0:
            sceneF = 10
            return sceneF

        sceneF = -1
        return sceneF

    def ClickImg(self,scene,img,left, top, right, bottom,jingdu = 0.9):
        re, x, y = scene.Findimg(left, top, right, bottom, img,jingdu)
        if re == 0:
            mouse = cmouse()
            mouse.Click(x, y)
            return 0
        return -1
    def DoubleClickImg(self,scene,img,left, top, right, bottom):
        re, x, y = scene.Findimg(left, top, right, bottom, img)
        if re == 0:
            mouse = cmouse()
            mouse.Click(x, y)
            mouse.Click(x, y)
            return 0
        return -1
    def jiejiehaishitangsuo(self,game,scene, left, top, right, bottom):
        # 获取体力结界券
        TuPoJuan = game.GetTuPoJuan(scene, left, top, right, bottom)
        print("突破卷:" + str(TuPoJuan))
        TiLi = game.GetTiLi(scene, left, top, right, bottom)
        print("体力:" + str(TiLi))
        if TuPoJuan != -1 and TiLi != -1:
            #if TuPoJuan <= 25 and TiLi > 25:
            if TiLi > 25:
                return "探索"
            elif  TuPoJuan == 0 and TiLi < 25:
                return "没了"
            else:
                return "结界突破"

    def jjNumber(self,window,left, top, right, bottom):
        img = cimg()
        # 获得游戏界面截图
        tu = window.jietu(left, top, right, bottom)
        tu.save('temp/temp.bmp')
        re1 = img.FindALLImgInImg('temp/temp.bmp', self.daguolePath,0.8)
        re2 = img.FindALLImgInImg('temp/temp.bmp', self.dabuguoPath,0.96)#匹配精度0.96
        re3 = img.FindALLImgInImg('temp/temp.bmp', self.meidaguoPath,0.90)

        print("打过了" + str(re1) + ";打不过:" + str(re2)+ ";没打过:" + str(re3))
        return re1,re2,re3




    def jiechutupkuai(self,window,left, top, right, bottom):
        img = cimg()
        # 获得游戏界面截图
        tu = window.jietu(left, top, right, bottom)
        tu.save('temp/temp.bmp')
        x = 100 + 2 * 10 + 5
        y = 100 + 2 * 10
        point0 = [x, y]
        for i in range(9):
            if i == 0:
                point = point0
            else :
                point = [int(point0[0] + int((i)%3) * 305), int(point0[1] + int((i)/3) * 120)]
            w = 300-5
            h = 120-5
            point2 = [point[0] + w, point[1] + h]
            print(str(i) + str(point))
            srcimg = img.CutImgPath('temp/temp.bmp',point,point2)
            img.save('temp/temp'+str(i)+'.bmp',srcimg)
            re,x,y = img.FindImgInImg('temp/temp'+str(i)+'.bmp',self.meidaguoPath)
            if re == 0:
                return 0,x+left+point[0],y+top+point[1]
        return -1,0,0

    def datupo(self, window, left, top, right, bottom):
        re1,re2,re3 = self.jjNumber(window, left, top, right, bottom)
        if re1 >= 3 :
            re,x,y = window.Findimg(left, top, right, bottom, "yys/结界刷新冷却中.bmp")
            if re == 0:
                re = self.ClickImg(window,"yys/关闭按钮.bmp",left, top, right, bottom)
                if re == 0:
                    print("关闭按钮")
                    return -1,0,0
                else:
                    print("打过" + str(re1) + "但是找不到关闭按钮")
                    return -1,0,0
            else:
                re, x, y = window.Findimg(left, top, right, bottom, "yys/结界刷新按钮.bmp")
                if re == 0:
                    return 1,x,y
                else :
                    print("打过"+str(re1)+"没在刷新冷却中但是找不到刷新按钮")
                    return -1,0,0
        elif re3 == 0:
            re, x, y = window.Findimg(left, top, right, bottom, "yys/结界刷新按钮.bmp")
            if re == 0:
                return 1, x, y
            else:
                print("打过" + str(re1) + "没在刷新冷却中但是找不到刷新按钮")
                return -1, 0, 0
        else:
            re, x, y = self.jiechutupkuai(window, left, top, right, bottom)
            if re == 0:
                print("打他！")
                return 0, x, y
            else:
                print("打过" + str(re1) + "但是找不到没打过的")
                return -1, 0, 0

    def jinrutangsuo(self, window, left, top, right, bottom):
        if self.ClickImg(window, "yys/第三章.bmp", left, top, right, bottom) == 0:
            time.sleep(1)
            if self.ClickImg(window, "yys/探索按钮.bmp", left, top, right, bottom) == 0:
                print("探索")
                time.sleep(1)
            else:
                print("探索按钮找不到")
        else:
            print("第十一章找不到")
        print("进入探索")

    def datangsuo(self,window,left, top, right, bottom):
        # 获取体力数量
        tili = self.GetTiLi(window, left, top, right, bottom)
        if tili > 6:
            if self.ClickImg(window, "yys/打小怪.bmp", left, top, right, bottom) == 0:
                print("打小怪")
            elif self.ClickImg(window, "yys/打boss.bmp", left, top, right, bottom) == 0:
                print("打boss")
            elif self.ClickImg(window, "yys/探索奖励.bmp", left, top, right, bottom) == 0:
                print("探索奖励")
            elif self.ClickImg(window, "yys/打小怪2.bmp", left, top, right, bottom) == 0:
                print("打小怪2")
            else:
                re,x,y = window.Findimg(left, top, right, bottom, "yys/获得奖励.bmp")
                if re == 0:
                    mouse = cmouse()
                    mouse.Click(x,y-200)
                else:
                    self.ClickImg(window, "yys/探索向右走.bmp", left, top, right, bottom)
                #mouse = cmouse()
                #point = [left + int(3 * (right - left) / 4), top + int(3 * (bottom - top) / 4)]
                #mouse.m.click(point[0],point[1],1,2)
                #mouse.Click(point[0],point[1])
        elif tili == -1:
            print("体力获取失败")
        print("打探索")


    def teaming(self,window,yys):
        print(sys._getframe().f_code.co_name)  # 当前位置所在的函数名
        if self.ClickImg(window, "yys/开始战斗按钮.bmp", yys.left, yys.top, yys.right, yys.bottom,0.98) == 0:
            print("开始战斗按钮")
        pass

    def errorscence(self,window,yys):
        print(sys._getframe().f_code.co_name)  # 当前位置所在的函数名
        if self.ClickImg(window, "yys/退出斗技按钮.bmp", yys.left, yys.top, yys.right, yys.bottom,0.98) == 0:
            print("退出斗技按钮")
        if self.ClickImg(window, "yys/确认退出斗技按钮.bmp", yys.left, yys.top, yys.right, yys.bottom,0.98) == 0:
            print("确认退出斗技按钮")
        pass

    def fighting(self,window,yys):
        print(sys._getframe().f_code.co_name)  # 当前位置所在的函数名
        pass

    def fightend(self,window,yys):
        print(sys._getframe().f_code.co_name)  # 当前位置所在的函数名
        mouse = cmouse()
        mouse.Click(yys.left + 100, yys.top + 100)
        pass

    def hunshiteam(self,argument,window,yys):
        switcher = {
            0: self.errorscence,
            4: self.fighting,
            5: self.fightend,
            6: self.fightend,
            7: self.fightend,
            9: self.teaming
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, self.errorscence)(window,yys)
        # Execute the function
        return func

    def exitfighting(self,window,yys):
        print(sys._getframe().f_code.co_name)  # 当前位置所在的函数名
        if self.ClickImg(window, "yys/退出斗技按钮.bmp", yys.left, yys.top, yys.right, yys.bottom, 0.90) == 0:
            print("退出斗技按钮")
        if self.ClickImg(window, "yys/确认退出斗技按钮.bmp", yys.left, yys.top, yys.right, yys.bottom, 0.90) == 0:
            print("确认退出斗技按钮")
        pass

    def startfight(self,window,yys):
        print(sys._getframe().f_code.co_name)  # 当前位置所在的函数名
        if self.ClickImg(window, "yys/开始斗技按钮.bmp", yys.left, yys.top, yys.right, yys.bottom, 0.98) == 0:
            print("开始斗技按钮")
        pass

    def zhunbei(self,window,yys):
        print(sys._getframe().f_code.co_name)  # 当前位置所在的函数名
        if self.ClickImg(window, "yys/斗技准备按钮.bmp", yys.left, yys.top, yys.right, yys.bottom, 0.98) == 0:
            print("斗技准备按钮")
        re, x, y = window.Findimg(yys.left, yys.top, yys.right, yys.bottom, "yys/斗技中界面.bmp")  # 斗技中界面
        if re == 0:
            if self.ClickImg(window, "yys/退出战斗按钮.bmp", yys.left, yys.top, yys.right, yys.bottom, 0.98) == 0:
                print("退出战斗按钮")
        pass

    def douji(self,argument,window,yys):
        switcher = {
            0: self.errorscence,
            4: self.zhunbei,
            5: self.fightend,
            6: self.fightend,
            7: self.fightend,
            10: self.startfight,
            11: self.exitfighting
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, self.errorscence)(window,yys)
        # Execute the function
        return func

    def enumtest(self):
        return SceneKey.MON

@unique
class SceneKey(Enum):
    NUKOWN = 0
    TINGYUAN = 1
    TANGSUO = 2
    DINGZHONG = 3
    JIEJIETUPO = 4
    ZHANGDOU = 5
    ZHANGDOUJIANGLI = 6
    ZHANGDOUSHENGLI = 7
    ZHANGDOUSHIBAI = 8
    XIEZAHNDUIWU = 9
    DOUJI = 10