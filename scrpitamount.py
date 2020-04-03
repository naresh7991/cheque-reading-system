# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 13:00:15 2020

@author: Acer
"""
import imutils
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras import layers
from sklearn.externals import joblib
from tensorflow.keras.models import model_from_json
import os
import numpy as np
def amountfile(filename):
    image = cv2.imread(filename)

    (h, w,) = image.shape[:2]
    delta = int(h - (h * 0.45))
    bottom = image[int(h*0.30):delta, int(w-w*0.27):int(w-w*0.046)]

    hsv = cv2.cvtColor(bottom,cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv1",hsv)
    black_lower = np.array([35,30,120])
    black_uper = np.array([255,255,150])
    MASK = cv2.inRange(hsv,black_lower,black_uper)
    RES =cv2.bitwise_and(hsv,hsv,mask= MASK)
    cv2.imshow("hsv",RES)
    color = cv2.cvtColor(RES,cv2.COLOR_HSV2BGR)
    cv2.imshow("frame",color)


    cv2.waitKey(0) 
    cv2.destroyAllWindows() 
    cv2.imwrite("image6.png",RES)

    img = cv2.imread("image6.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5,5),np.uint8)
    gray2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    dilation = cv2.dilate(gray,kernel,iterations = 1)
    cv2.imwrite("dilation2.png",dilation)
    cv2.imwrite("dialtion.png",closing)
    cv2.imwrite("grayy.png",gray)
    dilation22 = cv2.imread("dilation2.png")
    thresh = cv2.cvtColor(dilation22,cv2.COLOR_BGR2GRAY)
    thresh2 = cv2.threshold(thresh,0,255,cv2.THRESH_BINARY_INV |
        cv2.THRESH_OTSU)[1]
    cv2.imwrite("dillla.png",thresh2)


    "predicting"


    #load model from disk
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    print("Loaded model from disk")

#creating the list of categories
    listt = ['0','1','2','3','4','5','6','7','8','9']
#reading the image
    im = cv2.imread("dillla.png")
#image preprocessing
    im_gray= cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im_gray = cv2.GaussianBlur(im_gray, (5, 5), 0)
    ret, im_th = cv2.threshold(im_gray, 90, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("image",im_th)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    ctrs,her = cv2.findContours(im_th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#calculating the rectangle around the dgit
    rects = [cv2.boundingRect(ctr) for ctr in ctrs]
    print(rects)
    from operator import itemgetter

    rects= sorted(rects, key=itemgetter(0))
    x = []
    for rect in rects:
    # Draw the rectangles
        if rect[2]>10 or rect[3]>12:
            cv2.rectangle(im, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3) 
    # Make the rectangular region around the digit
            leng = int(rect[3] * 1.6)
            pt1 = int(rect[1] + rect[3] // 2 - leng // 2)
            pt2 = int(rect[0] + rect[2] // 2 - leng // 2)
            roi = im_th[pt1:pt1+leng, pt2:pt2+leng]
            roi = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)
            roi = cv2.dilate(roi, (3, 3))
            roi  = roi/255.0
            roi =  np.expand_dims(roi, axis=0)
    #predicting the image
            text = loaded_model.predict(roi)
            x.append(listt[text.argmax()])
            cv2.putText(im, listt[text.argmax()], (rect[0], rect[1]),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 3)
    
    cv2.imshow("Resulting Image with Rectangular ROIs", im)
#imagw close after 6 sec
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#printing the number
    x = "".join(x)
    print("---------------------------------------------------------------------------")
    print("amount:",x)
    return x