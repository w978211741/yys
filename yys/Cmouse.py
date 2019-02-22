from pymouse import PyMouse
import win32api
import win32con


class Mouse:
    m = None

    def __init__(self):
        self.m = PyMouse()

    def mouse_to(self, x, y):
        self.m.move(x, y)

    def click(self, x, y):
        self.m.click(x, y, 1, 1)

    def double_click(self, x, y):
        self.m.click(x, y, 1, 2)

    def send_esc(self, hwnd):
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_ESCAPE, 0)
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_ESCAPE, 0)