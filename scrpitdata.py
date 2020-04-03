# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:59:05 2020

@author: Acer
"""
import imutils
import numpy as np


from imutils import contours
import tensorflow as tf
from tensorflow.keras import layers
from sklearn.externals import joblib
from tensorflow.keras.models import model_from_json
import os
import cv2

def date(filename):
	image = cv2.imread('sample9.png')
	(h, w,) = image.shape[:2]
	delta = int(h - (h * 0.8))
	bottom = image[0:delta, w - int(w*.3):w]


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

	from operator import itemgetter

	rects= sorted(rects, key=itemgetter(0))

	print(rects)
	x = []
	y = []
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
			print(text)
			print("asasasasasasasa")
			print(text.argmax())
			if max(text[0])>0.65:
				x.append(listt[text.argmax()])
				y.append(listt[text.argmax()])
				cv2.putText(im, listt[text.argmax()], (rect[0], rect[1]),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 3)
			else:
            #cv2.putText(im, listt[text.argmax()], (rect[0], rect[1]),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 3)
				print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
				x.append(listt[text.argmax()])
				para = text.argmax()
				para2 = max(text[0])
				l1 = list(text[0])
				print("-----------------list-----------------------")
				print(l1)
				l1.remove(max(l1))
				para3 = max(l1)
				print(l1)
				indexx = l1.index(max(l1))
				print("----------------------para checking------------------------")
				print(indexx,para)
				if abs(para2 -para3) <.15:
					if indexx>= para:
						y.append(listt[indexx+1])
					else:
						y.append(listt[indexx])
				else:
					y.append(para)
            
	cv2.imshow("Resulting Image with Rectangular ROIs", im)
#imagw close after 6 sec
	cv2.waitKey(0)
	cv2.destroyAllWindows()
#printing the number
	x = "".join(x)
	print(x)
	print(y)
	import datetime
	date_object = datetime.date.today()
	mm =  date_object.month
	yyyy = date_object.year
	dd = date_object.day
	print(mm,yyyy)
	mm1 = ""
	mm1 = mm1 +str(y[2])+str(y[3])
	print(mm1)
	mm2 = ""
	mm2 = mm2+str(x[2])+str(x[3])
	print(mm2)
	yyyy1 = ""
	yyyy1 = yyyy1+str(y[4])+str(y[5])+str(y[6])+str(y[7])
	print(yyyy1)
	yyyy2 = ""
	yyyy2 = yyyy2 +x[4:]
	print(yyyy2)
	datee = ""
	if int(yyyy2) == yyyy:
		datee = datee +"/"+ yyyy2

	elif int(yyyy1) == yyyy:
		datee = datee  +"/" +yyyy1
	else:
		print("date error")
	if abs(int(mm2) - mm)<2:
		datee = mm2 + datee
	elif abs(int(mm1) - mm)<2:
		datee = mm1 +datee
	else:
		print("date error")
	datee = "".join(y[:2])  +"/"+ datee
	print("date :",datee)
	return datee
  
  