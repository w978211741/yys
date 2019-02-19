from PIL import ImageGrab
from Cimg import cimg
import win32gui,win32con


class cwindow:

    def GetWindow(self,clasename,caption):
        Hhandle = win32gui.FindWindow(clasename,caption)
        if Hhandle == 0:
            return 0,0,0,0,0
        else:
            # 获取窗口左上角的屏幕坐标和右下角的屏幕坐标
            left, top, right, bottom = win32gui.GetWindowRect(Hhandle)
            return Hhandle, left, top, right, bottom

    #图片识别依旧与分辨率有关，所以为了统一，以1920*1080 的四分之一为准，截图（yys文件夹下）
    def SetWindow(self,Hhandle,x,y,cx,cy):
        if Hhandle == 0:
            return 0,0,0,0,0
        try :
            win32gui.SetWindowPos(Hhandle,win32con.HWND_TOPMOST, x, y, cx, cy, win32con.SWP_DEFERERASE)
            left, top, right, bottom = win32gui.GetWindowRect(Hhandle)
        except Exception as e:
            print(e.message)
            return 0,0,0,0,0
        return Hhandle, left, top, right, bottom

    #在屏幕指定区域找图
    def Findimg(self,left, top, right, bottom, imgname,jindu = 0.90):
        windowimg = ImageGrab.grab((left, top, right, bottom))
        windowimg.save('temp/temp.bmp')
        findimg = cimg()
        re,x,y = findimg.FindImgInImg('temp/temp.bmp',imgname,jindu)
        if re == -1 :
            return -1,-1,-1
        return 0,x + left, y + top

    #在屏幕指定区域截图，保存为无法识别画面 error
    def errorjietu(self,left, top, right, bottom,number):
        windowimg = ImageGrab.grab((left, top, right, bottom))
        windowimg.save("error/error" + str(number) + ".bmp")

    def jietu(self,left, top, right, bottom):
        return ImageGrab.grab((left, top, right, bottom))

