# -*- coding:utf-8 -*-
__author__ = 'Microcosm'

import cv2
import numpy as np

class ccutBG:
    def Test(self):
        cap = cv2.VideoCapture("avi/test.avi")

        # 方法一：
        fgbg1 = cv2.createBackgroundSubtractorKNN()
        # 方法二：
        fgbg2 = cv2.createBackgroundSubtractorMOG2()

        # 方法三：  需要OpenCV3.0
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # fgbg3 = cv2.BackgroundSubtractorGMG()

        while (1):
            ret, frame = cap.read()
            if ret:
                fg_mask1 = fgbg1.apply(frame)
                fg_mask2 = fgbg2.apply(frame)

                # fgmask3 = fgbg3.apply(frame)
                # fgmask3 = cv2.morphologyEx(fgmask3, cv2.MORPH_OPEN, kernel)

                result = np.hstack((fg_mask1, fg_mask2))
                cv2.imshow('frame', result)

                k = cv2.waitKey(30) & 0xff
                if k == 27:
                    break
            else:
                break

        cap.release()
        cv2.destroyAllWindows()
