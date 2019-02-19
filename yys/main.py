#encoding=utf-8
from Cwindow import cwindow
from Cgame import cgame,SceneKey
from Cmouse import cmouse
from Cimg import cimg
from pymouse import PyMouse
import cv2
import  os
import string
from Cluping import cluping
from CcutBG import ccutBG
import time
class WindowHandle:
    Handle = 0
    left = 0
    top = 0
    right = 0
    bottom = 0

Handle = 0
left = 0
top = 0
right = 0
bottom = 0


def findwindow(window,WindowHandle,name):

    clasename = None

    WindowHandle.Handle,WindowHandle.left,WindowHandle.top,WindowHandle.right,WindowHandle.bottom \
        = window.GetWindow(clasename,name)
    gao = WindowHandle.bottom - WindowHandle.top
    while gao > 520:
        gao = gao - 20
        if gao < 520:
            gao = 520
        WindowHandle.Handle, WindowHandle.left, WindowHandle.top, WindowHandle.right, WindowHandle.bottom \
            = window.SetWindow(WindowHandle.Handle, WindowHandle.left,WindowHandle.top, WindowHandle.right - WindowHandle.left, gao)
        time.sleep(1)

    if WindowHandle.Handle == 0:
        print("找不到窗口")
        return -1
    else:
        print("窗口句柄：%s" % (WindowHandle.Handle))
        return 0

def Douji():
    findedwindow = False
    errornumber = 1
    sceneF = -1  # -1 未确定场景 0：庭院 ；1 ： 探索 ；2 ： 町中 ;3 : 结界突破;4 : 战斗中；
    scene = cwindow()
    sceneerror = 0
    game = cgame()
    mou = cmouse()
    yys1 = WindowHandle()
    findwindow(scene, yys1, "[#] [yys1] 阴阳师-网易游戏 [#]")  # 注意空格
    print(yys1.Handle, yys1.left, yys1.top, yys1.right, yys1.bottom)
    if yys1.Handle == 0 :
        print("不能找全窗口")
        return 0
    while 1:
        # 确定自己在哪个场景
        sceneF = game.Getscene(scene, yys1.left, yys1.top, yys1.right, yys1.bottom, errornumber)
        errornumber = errornumber + 1
        print("1" + str(sceneF))
        # 将判断后的结果场景代码传入，根据不同场景调用不同函数
        game.douji(sceneF, scene, yys1)
        time.sleep(3)



def HunShiMain():
    findedwindow = False
    errornumber = 1
    sceneF = -1  # -1 未确定场景 0：庭院 ；1 ： 探索 ；2 ： 町中 ;3 : 结界突破;4 : 战斗中；
    scene = cwindow()
    sceneerror = 0
    game = cgame()
    mou = cmouse()
    yys1 = WindowHandle()
    findwindow(scene,yys1,"[#] [yys2] 阴阳师-网易游戏 [#]")#注意空格
    print(yys1.Handle, yys1.left, yys1.top, yys1.right, yys1.bottom)
    yys2 = WindowHandle()
    findwindow(scene,yys2,"[#] [yys4] 阴阳师-网易游戏 [#]")#注意空格
    print(yys2.Handle, yys2.left, yys2.top, yys2.right, yys2.bottom)
    if yys1.Handle == 0 or yys2.Handle == 0:
        print("不能找全窗口")
        return 0
    while 1 :
        # 确定自己在哪个场景
        sceneF = game.Getscene(scene, yys1.left, yys1.top, yys1.right, yys1.bottom, errornumber)
        errornumber = errornumber + 1
        print("1"+str(sceneF))
        #将判断后的结果场景代码传入，根据不同场景调用不同函数
        game.hunshiteam(sceneF,scene,yys1)
        time.sleep(3)
        sceneF = game.Getscene(scene, yys2.left, yys2.top, yys2.right, yys2.bottom, errornumber)
        errornumber = errornumber + 1
        print("2"+str(sceneF))
        # 将判断后的结果场景代码传入，根据不同场景调用不同函数
        game.hunshiteam(sceneF, scene, yys2)
        time.sleep(3)

def main():
    findedwindow = False
    errornumber = 1
    sceneF = -1#-1 未确定场景 0：庭院 ；1 ： 探索 ；2 ： 町中 ;3 : 结界突破;4 : 战斗中；
    scene = cwindow()
    sceneerror = 0
    game = cgame()
    mou = cmouse()
    while(1):
        #找虚拟机窗口，找不到退出
        if findedwindow == False:
            if findwindow(scene) == -1 :
                return 0
            findedwindow = True

        #确定自己在哪个场景
        sceneF = game.Getscene(scene, left, top, right, bottom, errornumber)
        errornumber = errornumber + 1
        print(sceneF)
        if sceneF != -1:
            sceneerror = 0
        if sceneF == 0 :#在庭院
            re = game.ClickImg(scene,"yys/探索场景按钮.bmp", left,top, right, bottom)
            if re != 0:
                #进探索
                print("zhoabudao探索场景按钮")
            else :
                print("zhoadao探索场景按钮")
                time.sleep(1)
        elif sceneF == 1:#在探索
            re = game.jiejiehaishitangsuo(game,scene, left, top, right, bottom)
            if re == "探索":
                game.jinrutangsuo(scene, left, top, right, bottom)
            elif re == "结界突破":
                re = game.ClickImg(scene, "yys/结界突破入口.bmp", left, top, right, bottom)
            elif re == "没了":
                print("退出")
                return 0
            else:
                print("-1")
        elif sceneF == 2:#在町中
            re = game.ClickImg(scene, "yys/庭院.bmp", left, top, right, bottom)
            if re != 0:
                # 进探索
                print("zhoabudao庭院")
            else:
                print("zhoadao庭院")
        elif sceneF == 3:  # 在结界突破；
            juan = game.GetTuPoJuan2(scene, left, top, right, bottom)
            print(juan)
            if juan == 0:
                re, x, y = scene.Findimg(left, top, right, bottom, "yys/关闭按钮.bmp")
                if re == 0:
                    mou.Click(x, y)
                else :
                    print("没卷了，找不到关闭按钮")
                continue

            re,x,y = game.datupo(scene,left, top, right, bottom)
            print(re,x,y)
            if re == 0:# 0: 打；1：刷新
                mou.Click(x,y)
                time.sleep(1)
                re,x,y = scene.Findimg(left, top, right, bottom,"yys/进攻结界按钮.bmp")
                if re == 0:
                    mou.Click(x, y)
            if re == 1:# 0: 打；1：刷新
                mou.Click(x,y)
                time.sleep(1)
                re,x,y = scene.Findimg(left, top, right, bottom,"yys/结界刷新确定按钮.bmp")
                if re == 0:
                    mou.Click(x, y)
        elif sceneF == 4:
            time.sleep(3)
        elif sceneF == 7 or sceneF == 5 or sceneF == 6 :  # 在战斗结束
            print("战斗结束")
            mou.Click(left+200, top+200)
        elif sceneF == 8:
            game.datangsuo(scene,left,top,right,bottom)
        elif sceneF == -1:
            if game.ClickImg(scene,"yys/关闭按钮.bmp",left, top, right, bottom) == 0:
                print("关闭按钮")
            #elif game.ClickImg(scene, "yys/斗技开始.bmp", left, top, right, bottom) == 0:
             #   print("斗技开始")
            #elif game.ClickImg(scene, "yys/退出战斗.bmp", left, top, right, bottom) == 0:
            #    print("退出战斗")
            #    time.sleep(1)
            #   game.ClickImg(scene, "yys/确认退出.bmp", left, top, right, bottom)
            #   print("确认退出")
            else:
                if sceneerror > 10:
                    errornumber = errornumber + 1
                    scene.errorjietu(left, top, right, bottom, errornumber)
                    return 0
                sceneerror = sceneerror + 1
                time.sleep(3)


        time.sleep(3)


def test():
    m = cmouse()
    scene = cwindow()
    yys1 = WindowHandle()
    #findwindow(scene, yys1, "海外实施部_田明银")  # 注意空格
    findwindow(scene, yys1, "[#] [yys1] 阴阳师-网易游戏 [#]")  # 注意空格
    if yys1.Handle != 0:
        m.sendEsc(yys1.Handle)

print("开始")

Douji()
print("结束")