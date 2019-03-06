from pymouse import PyMouse
import win32api
import win32con
class cmouse:
    m = None
    def __init__(self):
        self.m = PyMouse()

    def Mouseto(self,x,y):
        self.m.move(x,y)

    def Click(self,x,y):
        #self.m.click(x,y,1,1)
        self.m.click(x, y, 1, 1)

    def DoubleClick(self,x,y):
        #self.m.click(x,y,1,1)
        self.m.click(x, y, 1, 2)

    # 发送esc退出事件
    def sendEsc(self,hwnd):
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_ESCAPE, 0)
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_ESCAPE, 0)

    def gun_lun(self, n, m):
        self.m.scroll(n, m)

    def vertical_tuo(self, x, y, n):
        self.m.press(x, y, 1)
        self.m.move(x, y - n)
        self.m.release(x, y, 1)


