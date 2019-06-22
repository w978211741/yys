from pymouse import PyMouse
from pykeyboard import PyKeyboard
import win32api
import win32con
import time


class Mouse:
    m = None

    def __init__(self, metrics_x=1920, metrics_y=1080):
        self.m = PyMouse()
        self.metrics_x = metrics_x
        self.metrics_y = metrics_y

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

    def left_down(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 左键按下

    def left_up(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    def absolute(self, x, y, dx, dy):
        SW = self.metrics_x
        SH = self.metrics_y
        self.mouse_to(x, y)  # 鼠标移动到
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 左键按下
        i = 1
        ddx = int(dx / 10)
        ddy = int(dy / 10)

        while i < 10:
            time.sleep(0.02)
            self.mouse_to(x + ddx * i, y + ddy * i)  # 鼠标移动到
            i += 1
        self.mouse_to(x + dx, y + dy)  # 鼠标移动到
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        return
        time.sleep(0.5)
        self.mouse_to(x+10, y+10)  # 鼠标移动到
        time.sleep(0.5)
        mw = int((dx + x) * 65535 / SW)
        mh = int((dy + y) * 65535 / SH)
        win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE + win32con.MOUSEEVENTF_MOVE, mw, mh, 0, 0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


class Keyboard:
    k = None

    def __init__(self):
        self.k = PyKeyboard()

    def ctrl_enter(self):
        time.sleep(0.3)
        self.k.press_key(self.k.control_r_key) # 按住alt键
        time.sleep(0.3)
        self.k.tap_key(self.k.enter_key) # 点击tab键
        time.sleep(0.3)
        self.k.release_key(self.k.control_r_key) # 松开alt键

    def alt_s(self):
        #time.sleep(0.3)
        self.k.press_key(self.k.alt_l_key) # 按住alt键
        #time.sleep(0.3)
        self.k.tap_key('s') # 点击tab键
        #time.sleep(0.3)
        self.k.release_key(self.k.alt_l_key) # 松开alt键

    def api_ctrl_enter(self):
        win32api.keybd_event(win32con.RIGHT_CTRL_PRESSED, 0, 0, 0)
        win32api.keybd_event(13, 0, 0, 0)
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(win32con.RIGHT_CTRL_PRESSED, 0, win32con.KEYEVENTF_KEYUP, 0)

    def api_ctrl_down(self):
        win32api.keybd_event(win32con.RIGHT_CTRL_PRESSED, 0, 0, 0)

    def api_ctrl_up(self):
        win32api.keybd_event(win32con.RIGHT_CTRL_PRESSED, 0, win32con.KEYEVENTF_KEYUP, 0)

    def ctrl_A_C(self):
        self.k.press_key(self.k.control_r_key)  # 按住alt键
        self.k.tap_key('a')  # 点击a键
        self.k.tap_key('c')  # 点击c键
        self.k.release_key(self.k.control_r_key)  # 松开alt键


