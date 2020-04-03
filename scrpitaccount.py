# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 13:48:12 2020

@author: Acer
"""

import cv2
import numpy as np
def acount_no():
#######   training part    ############### 
    samples = np.loadtxt('generalsamples.data',np.float32)
    responses = np.loadtxt('generalresponses.data',np.float32)
    responses = responses.reshape((responses.size,1))

    model = cv2.ml.KNearest_create()
    print(responses)


    model.train(samples,cv2.ml.ROW_SAMPLE,responses)

############################# testing part  #########################
    im = cv2.imread('image2.png')
    (h, w,) = im.shape[:2]
    delta = int(h - (h * 0.4))
    bottom = im[int(h*0.45):delta,int(w-w*.88):int(w-w*0.65)]
    out = np.zeros(bottom.shape,np.uint8)
    gray = cv2.cvtColor(bottom,cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)

    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    final = []
    for cnt in contours:
        if cv2.contourArea(cnt)>30:
            [x,y,w,h] = cv2.boundingRect(cnt)
            if  h>20:
            #cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
                roi = thresh[y:y+h,x:x+w]
                roismall = cv2.resize(roi,(10,10))
                roismall = roismall.reshape((1,100))
                roismall = np.float32(roismall)
                retval, results, neigh_resp, dists = model.findNearest(roismall, k = 1)
                string = str(int((results[0][0])))
                final.append(string)
                cv2.putText(out,string,(x,y+h),0,1,(0,255,0))

    cv2.imshow('im',im)
#cv2.imshow('out',out)
    print("-------------------------------------------------------------------")
    print("acountno:","".join(final[::-1]))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return ("".join(final[::-1]))
