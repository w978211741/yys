from pymouse import PyMouse
import win32api
import win32con
import time


class Mouse:
    m = None

    def __init__(self):
        self.m = PyMouse()

    def mouse_to(self, x, y):
        self.m.move(x,y)

    def click(self, x, y):
        self.m.click(x, y, 1, 1)

    def double_click(self, x, y):
        self.m.click(x, y, 1, 2)

    # 发送esc退出事件
    def send_esc(self, hwnd):
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_ESCAPE, 0)
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_ESCAPE, 0)

    def gun_lun(self, n, m):
        self.m.scroll(n, m)

    def vertical_tuo(self, x, y, n):
        self.m.press(x, y, 1)
        self.m.move(x, y - n)
        self.m.release(x, y, 1)

    def absolute(self, x, y, dx, dy):
        SW = 1920
        SH = 1080
        self.mouse_to(x, y)  # 鼠标移动到
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 左键按下
        time.sleep(0.2)
        mw = int((dx + x) * 65535 / SW)
        mh = int((dy + y) * 65535 / SH)
        win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE + win32con.MOUSEEVENTF_MOVE, mw, mh, 0, 0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)