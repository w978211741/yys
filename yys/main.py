#encoding=utf-8
from MainWindow import My_MainWindow
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

def main():
    print("开始")
    multiprocessing.freeze_support()
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = My_MainWindow()
    my_pyqt_form.show()
    sys.exit(app.exec_())


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
