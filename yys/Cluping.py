"""python + opencv 实现屏幕录制_by-_Zjh_"""
from PIL import ImageGrab
import numpy as np
import cv2
class cluping:
    def luping(self,left, top, right, bottom):
        p = ImageGrab.grab((left, top, right, bottom))#获得当前屏幕
        #k=np.zeros((200,200),np.uint8)
        a,b=p.size#获得当前屏幕的大小
        #fourcc = cv2.VideoWriter_fourcc(*'XVID')#编码格式
        #video = cv2.VideoWriter('test.avi', fourcc, 32, (a, b))#输出文件命名为test.mp4,帧率为16，可以自己设置
        fgbg2 = cv2.createBackgroundSubtractorMOG2()
        while True:

            im = ImageGrab.grab((left, top, right, bottom))
            imm=cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)#转为opencv的BGR格式
            fg_mask2 = fgbg2.apply(imm)
            #video.write(fg_mask2)
            #np.zeros((a, b), np.uint8)
            #result = np.hstack(imm)
            cv2.imshow('imm', fg_mask2)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        #video.release()
        cv2.destroyAllWindows()
