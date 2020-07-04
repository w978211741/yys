from PIL import ImageGrab
from Cimg import Img
import win32gui
import win32con
import codedef


class Window:
    @staticmethod
    def check_window(caption, class_name=None):
        return win32gui.FindWindow(class_name, caption)

    @staticmethod
    def get_window(handle, class_name, caption):
        handle.hwnd = win32gui.FindWindow(class_name, caption)
        if handle.hwnd == 0:
            handle.left = 0
            handle.top = 0
            handle.right = 0
            handle.bottom = 0
            return codedef.ERROR_END
        else:
            # 获取窗口左上角的屏幕坐标和右下角的屏幕坐标
            handle.left, handle.top, handle.right, handle.bottom = win32gui.GetWindowRect(handle.hwnd)
        return codedef.NORMAL_END

    @staticmethod
    def set_window(handle, x, y, cx, cy):
        if handle.hwnd == 0:
            handle.left = 0
            handle.top = 0
            handle.right = 0
            handle.bottom = 0
            return codedef.ERROR_END
        try:
            win32gui.SetWindowPos(handle.hwnd, win32con.HWND_TOPMOST, x, y, cx, cy, win32con.SWP_DEFERERASE)
            handle.left, handle.top, handle.right, handle.bottom = win32gui.GetWindowRect(handle.hwnd)
        except Exception as e:
            print("Exception:" + e.__str__())
            handle.hwnd = 0
            handle.left = 0
            handle.top = 0
            handle.right = 0
            handle.bottom = 0
            return codedef.ERROR_END
        return codedef.NORMAL_END

    # 在屏幕指定区域找图
    @staticmethod
    def find_img(handle, img_path, accuracy=0.90):
        window_img = ImageGrab.grab((handle.left, handle.top, handle.right, handle.bottom))
        window_img.save('temp/temp.bmp')
        re, x, y = Img.find_img_in_img('temp/temp.bmp', img_path, accuracy)
        if re == -1:
            return codedef.ERROR_END, -1, -1
        return codedef.NORMAL_END, x + handle.left, y + handle.top

    # 在屏幕指定区域截图，保存为无法识别画面 error
    @staticmethod
    def error_jie_tu(handle, number):
        window_img = Window.jie_tu(handle)
        window_img.save("error/error" + str(number) + ".bmp")
        return codedef.NORMAL_END

    @staticmethod
    def temp_jie_tu(handle, path="temp/temp.bmp"):
        window_img = Window.jie_tu(handle)
        window_img.save(path)
        return codedef.NORMAL_END

    @staticmethod
    def jie_tu(handle=None):
        if handle is None:
            return ImageGrab.grab()
        return ImageGrab.grab((handle.left, handle.top, handle.right, handle.bottom))

