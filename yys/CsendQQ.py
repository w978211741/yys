from Cwindow import Window
from Chandle import Handle
from Cmouse import Keyboard, Mouse
import win32gui
import win32con
import win32clipboard as w
from io import StringIO
from PIL import Image
import cv2
import ctypes
import time


class SendQQ:
    m_handle = Handle()
    def __init__(self, name):
        class_name = None
        re = Window.get_window(self.m_handle, class_name, name)
        if re != 0:
            print("找不到窗口:" + name)
            #self.add_log("找不到窗口:" + name + str(handle.hwnd) + "\r\n")
        else:
            print("窗口:" + name)
            #self.add_log("窗口:" + name + str(handle.hwnd) + "\r\n")


    @staticmethod
    def get_clipboard_text():
        """获取剪贴板文本"""
        w.OpenClipboard()
        d = w.GetClipboardData(win32con.CF_UNICODETEXT)
        w.CloseClipboard()
        return d

    @staticmethod
    def set_image(data):
        w.OpenClipboard()  # 打开剪贴板
        w.EmptyClipboard()  # 先清空剪贴板
        w.SetClipboardData(win32con.CF_BITMAP, data)  # 将图片放入剪贴板
        w.CloseClipboard()

    @staticmethod
    def set_text(aString):
        """设置剪贴板文本"""
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
        w.CloseClipboard()

    def send_qq_text(self, msg):
        qq = self.m_handle.hwnd
        if qq == 0:
            print("句柄为0")
            return -1

        SendQQ.set_text(msg)

        # 投递剪贴板消息到QQ窗体
        time.sleep(0.3)
        win32gui.ShowWindow(qq, 1)
        win32gui.SetForegroundWindow(qq)

        win32gui.SendMessage(qq, 258, 22, 2080193)
        win32gui.SendMessage(qq, 770, 0, 0)
        SendQQ.send_key()

        time.sleep(0.3)
        win32gui.ShowWindow(qq, 2)
        return 0

    def send_qq_bmp(self, image_path):
        qq = self.m_handle.hwnd
        if qq == 0:
            print("句柄为0")
            return -1
        #im = Image.open('new.jpg')
        #im.save('11.bmp')
        aString = ctypes.windll.user32.LoadImageW(0, image_path, win32con.IMAGE_BITMAP, 0, 0, win32con.LR_LOADFROMFILE)
        print(aString)
        SendQQ.set_image(aString)

        time.sleep(0.3)
        win32gui.ShowWindow(qq, 1)
        win32gui.SetForegroundWindow(qq)

        win32gui.SendMessage(qq, 258, 22, 2080193)
        win32gui.SendMessage(qq, 770, 0, 0)
        SendQQ.send_key()

        time.sleep(0.3)
        win32gui.ShowWindow(qq, 2)
        return 0

    @staticmethod
    def send_key():
        # pyuserinput 的 Keyboard
        key_board = Keyboard()
        # 发送消息的快捷键
        key_board.alt_s()

    def get_text(self, name):
        re = Window.get_window(self.m_handle, None, name)
        if re != 0:
            print("找不到窗口:" + name)
            return ""
        else:
            print("窗口:" + name)

        win32gui.ShowWindow(self.m_handle.hwnd, 1)
        win32gui.SetForegroundWindow(self.m_handle.hwnd)
        time.sleep(0.3)

        re = Window.get_window(self.m_handle, None, name)
        if re != 0:
            print("找不到窗口:" + name)
            return ""
        else:
            print("窗口:" + name)

        center_x = (self.m_handle.right + self.m_handle.left) / 2
        center_y = (self.m_handle.bottom + self.m_handle.top) / 2
        mouse = Mouse()
        mouse.click(int(center_x), int(center_y))

        time.sleep(0.3)
        key_board = Keyboard()
        key_board.ctrl_A_C()

        time.sleep(0.3)
        win32gui.ShowWindow(self.m_handle.hwnd, 2)

        text = SendQQ.get_clipboard_text()
        cmd = SendQQ.get_last_cmd(text, name)
        return cmd

    @staticmethod
    def get_last_cmd(msg, name):
        # 按回车切割成list
        temp_list = msg.splitlines()
        list_len = len(temp_list)
        if list_len == 0:
            return ""

        # 如果最后一条消息是对方发的才取，否则返回空
        re = temp_list[list_len - 2]
        if re[:len(name)] == name:
            re = temp_list[list_len - 1]
        else:
            re = ''

        return re


    @staticmethod
    def find_last(string, str):
        last_position = -1
        while True:
            position = string.find(str, last_position + 1)
            if position == -1:
                return last_position
            last_position = position

    def send_jie_tu(self):
        window_img = Window.jie_tu()
        image_path = "error/error.bmp"
        window_img.save(image_path)
        self.send_qq_bmp(image_path)

