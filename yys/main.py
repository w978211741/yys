#encoding=utf-8
from MainWindow import My_MainWindow
from PyQt5 import QtWidgets
import sys
import multiprocessing
from Cwindow import Window
import time
from Chandle import Handle
import win32gui


def main():
    print("开始")
    multiprocessing.freeze_support()
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = My_MainWindow()
    my_pyqt_form.show()
    sys.exit(app.exec_())


def testtt():
    yys1 = Handle()
    h = Window.check_window("[#] [yys1] 阴阳师-网易游戏 [#]")
    print(h)
    sleep_time = 1
    if h != 0:
        yys1.hwnd = h
        yys1.left, yys1.top, yys1.right, yys1.bottom = win32gui.GetWindowRect(yys1.hwnd)
        Window.temp_jie_tu(yys1,"temp/tees1.bmp")
        time.sleep(sleep_time)
        Window.temp_jie_tu(yys1, "temp/tees2.bmp")
        time.sleep(sleep_time)
        Window.temp_jie_tu(yys1, "temp/tees3.bmp")

if __name__ == '__main__':
    main()
    # testtt()
