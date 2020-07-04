#encoding=utf-8
from MainWindow import My_MainWindow
from Mainwinfeng import mainwindeng
from PyQt5 import QtWidgets
import sys
import multiprocessing
from Cwindow import Window
import time
from Chandle import Handle
import win32gui
from Cteam_kun_25_captain import Team_kun_25_captain
import codedef
import re

from Cmouse import Mouse
from pykeyboard import PyKeyboard
from Cimg import Img
from PIL import ImageGrab
def main():
    print("开始")
    multiprocessing.freeze_support()
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = My_MainWindow()
    my_pyqt_form.show()
    sys.exit(app.exec_())

def main1():
    print("开始")
    multiprocessing.freeze_support()
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = mainwindeng()
    my_pyqt_form.show()
    sys.exit(app.exec_())

def lianjie():
    t = 0
    re = -1
    while t < 5:
        window_img = ImageGrab.grab((1920 / 2 + 300, 1080 - 50, 1920 / 2 + 800, 1080))
        window_img.save('temp/temp.bmp')
        re, x, y = Img.find_img_in_img('temp/temp.bmp', '异星工厂/警报.bmp', 0.8)
        if re == 0:
            break
        t += 1
    return re

def main1():
    print("开始")
    tMouse = Mouse()
    time.sleep(3)

    while 1:
        print("grab")
        re = lianjie()
        if re == 0:
            print("find")
            print("当前时间戳为:")
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

            tMouse.mouse_to(1920 - 200, 10)
            tMouse.click(1920 - 200, 10)
            break

        time.sleep(10*60)

    print("end")


def testtt():
    h = Window.check_window("[#] [yys1] 阴阳师-网易游戏 [#]")
    print(h)
    sleep_time = 1
    if h != 0:
        game = Team_kun_25_captain(codedef.UP_C_COIN, False)
        yys1 = Handle()
        win32gui.ShowWindow(yys1.hwnd, 1)
        re = game.set_window(yys1, "[#] [yys1] 阴阳师-网易游戏 [#]", 1, True)
        if re != 0:
            return re
        while 1:
            scene = game.get_scene(yys1)
            captain_wait = game.do_work(scene, yys1)
            time.sleep(2)


if __name__ == '__main__':
    main()
    # testtt()

if __name__ == '__main1__':
    s = 'wer1123sdf123'
    kk = re.compile(r'\d+')
    c = kk.findall(s)[1]
    # print(isinstance(c, list))
    print(int(c))
