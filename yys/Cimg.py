import aircv as ac
import cv2
import numpy as np
from Cdisdigit import cdisdigit


class cimg:
    def FindALLImgInImg(self,srcimg,targetimg,jingdu):
        srcimg = cv2.imdecode(np.fromfile(srcimg,dtype=np.uint8),-1)
        targetimg = cv2.imdecode(np.fromfile(targetimg, dtype=np.uint8), -1)
        #srcimg = ac.imread(srcimg)
        #targetimg = ac.imread(targetimg)
        pos = ac.find_all_template(srcimg, targetimg,jingdu)
        if pos == None :
            return -1
        #circle_center_pos = pos['result']
        return len(pos)

    def FindImgInImg(self,srcimg,targetimg,jingdu = 0.5):
        srcimg = cv2.imdecode(np.fromfile(srcimg,dtype=np.uint8),-1)
        targetimg = cv2.imdecode(np.fromfile(targetimg, dtype=np.uint8), -1)
        #srcimg = ac.imread(srcimg)
        #targetimg = ac.imread(targetimg)
        pos = ac.find_template(srcimg, targetimg,jingdu)
        if pos == None :
            return -1,-1,-1
        circle_center_pos = pos['result']
        return 0, int(circle_center_pos[0]), int(circle_center_pos[1])

    #x1 = 60  # 左右偏移量
    #y1 = 1  # 上下偏移量
    #width = 70  # 目标宽度
    #heigh = 30  # 目标高度
    def FindStrInImg(self,srcimgpath,tagimgpath,x1,y1,width,heigh):
        re, x, y = self.FindImgInImg(srcimgpath, tagimgpath)
        if re != 0:
            return "-1"
        srcimg = cv2.imread(srcimgpath)
        se = srcimg.shape
        Maxheight = se[0]
        Maxwidth = se[1]
        point1 = [int(x - width / 2) + x1, int(y - heigh / 2) + y1]  # 左上角
        point2 = [int(x + width / 2) + x1, int(y + heigh / 2) + y1]  # 右下角
        if point1[0] < 0:
            point1[0] = 0
        if point1[1] < 0:
            point1[1] = 0
        if point2[0] < 0:
            point2[0] = 0
        if point2[1] < 0:
            point2[1] = 0
        if point2[0] > Maxwidth:
            point2[0] = Maxwidth
        if point2[1] > Maxheight:
            point2[1] = Maxheight
        if point1[0] >  point2[0] or point1[1] > point2[1]:
            return -2;
        tagimg = self.CutImg(srcimg, point1, point2)
        grayimg = cv2.cvtColor(tagimg, cv2.COLOR_BGR2GRAY)
        img_info = tagimg.shape
        image_height = img_info[0]
        image_weight = img_info[1]
        dst = np.zeros((image_height, image_weight, 1), np.uint8)
        for i in range(image_height):
            for j in range(image_weight):
                grayPixel = grayimg[i][j]
                dst[i][j] = 255 - grayPixel
        tempPath = "temp/findStrInImg.bmp"
        cv2.imwrite(tempPath, dst)
        img2str = cdisdigit()  # 文字识别对象
        text = img2str.imgPathtostring(tempPath)
        return text

        # 裁剪
    def CutImg(self,srcimg,pointfrom,pointto):
        tagimg = srcimg[pointfrom[1]:pointto[1], pointfrom[0]:pointto[0]]
        return tagimg

    def CutImgPath(self,srcimgPath,pointfrom,pointto):
        srcimg = cv2.imread(srcimgPath)
        tagimg = srcimg[pointfrom[1]:pointto[1], pointfrom[0]:pointto[0]]
        return tagimg

    def save(self,name,img):
        cv2.imwrite(name,img)