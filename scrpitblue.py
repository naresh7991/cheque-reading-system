# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 13:31:27 2020

@author: Acer
"""

from skimage.segmentation import clear_border

import imutils
import numpy as np
import imutils
import cv2
def blue_extract(filename):
    image = cv2.imread(filename)

    b = (image <[120,120,120])
#print(b)
    c = b.astype(int)
#background = np.array([0,0,0])
    c[c ==1] = 255
    c = 255-c
    cv2.imwrite("image2.png",c)
    x = cv2.imread("image2.png")

    res = cv2.bitwise_or(x,image)

    cv2.imshow("res",res)
    cv2.imwrite("image2.png",res)


    (h, w,) = res.shape[:2]
    delta = int(h - (h * 0.27))
    bottom = res[int(h*0.46):delta, int(w-w*0.27):int(w - w*0.04)]
    cv2.imshow("bottom",bottom)
    gray = cv2.cvtColor(bottom, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    cv2.imshow("thresh",thresh)
    cv2.imwrite("cropped.png",thresh)

    cv2.waitKey(0)
    cv2.destroyAllWindows()