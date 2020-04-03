# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 13:06:26 2020

@author: Acer
"""# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 00:36:08 2019

@author: Acer
"""

import tkinter
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import cv2 
import numpy as np  
import copy
import tkinter as tk

from skimage.segmentation import clear_border

import imutils
import numpy as np
import imutils
import cv2
import numpy as np
import os
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm
from scipy import ndimage
from skimage.measure import regionprops
from skimage import io
from skimage.filters import threshold_otsu   # For finding the threshold for grayscale to binary conversion
import tensorflow as tf
import pandas as pd
import numpy as np
from time import time
import keras
import warnings  

import sqlite3
import scrpit1
import scrpitdata
import scrpitamount
import scrpitblue
import scrpitaccount
import scrpitsignature

conn  =  sqlite3.connect('accountdetail.db')
c = conn.cursor()

def select_data(account_no):
    c.execute(f"select name,id,amount FROM  accountt where account == {account_no}")
    data = c.fetchall()
    return data



lower_red = np.array([160,100,66]) 
upper_red = np.array([179,255,255]) 
  
lower_green = np.array([37,100,100])
upper_green = np.array([75,255,255])

lower_blue = np.array([100,38,0])
upper_blue = np.array([140,255,255])

lower_yellow = np.array([15,150,150])
upper_yellow = np.array([32,255,255])
arr = ["red","blue","green","yellow"]
dictt = {1:[lower_red,upper_red],2:[lower_blue,upper_blue],3:[lower_green,upper_green],4:[lower_yellow,upper_yellow]}


def connectt():
    count= 0
    frame = cv2.imread(B.get())
    micrv = scrpit1.micrno(B.get())
    datev = scrpitdata.date(B.get())
    amountv = scrpitamount.amountfile(B.get())
    scrpitblue.blue_extract(B.get())
    acc = scrpitaccount.acount_no()
    idd = select_data(acc)
    print(idd[0][1])
    if idd[0][1]== 1:
        input_of_signature = "001"
    print(input_of_signature)
    condition = scrpitsignature.signature(input_of_signature)
    print(condition)
    
    
    
    window = tk.Toplevel(root)
    window.geometry("900x700+0+0")
    window.configure(background="#C7F0DB")
    top = Label(window,text = "Bank Cheque Reader",width =48,height = 2,fg = "white",anchor = CENTER)
    top.config(font=("Times", 25,'bold'))
    top.configure(background="#464159")
    top.place(x = 0,y = 0)
    color_seperate = Image.open(B.get())
        
    photoq = PhotoImage(file = "C:/Users/Acer/Desktop/error.png")
    FRAME.photoq = photoq
    button1 = Button(window,image = photoq,command = window.destroy,background="#464159",highlightthickness = 0, bd = 0)
    button1.place(x =840,y =14)
    Canva2 = Canvas(window,width = 571,height = 296,bd = 16)
    Canva2.configure(background = "#6C7B95")
    Canva2.place(x = 120,y = 99)
    image22 = Image.open(B.get())
    resized22 = image22.resize((550,290),Image.ANTIALIAS)
    image122 = ImageTk.PhotoImage(resized22)
    window.image122 = image122
    Canva2.create_image(30,5, image=image122,anchor = NW)
    
    
    boxx = Label(window,width = 112,height = 13,bg = 'white',anchor = CENTER)
    boxx.place(x =70, y = 480)
    
    
    micr = Label(window,text = "MICR",bg = 'white',anchor = NW)
    micr.config(font=("open sans",18))
    micr.place(x = 145,y = 500)
    micrvalue = Label(window,text = micrv,anchor = 'e' ,bg = 'white')
    micrvalue.config(font = ("open sans",18,'underline'))
    micrvalue.place(x = 230,y = 500)
    amount = Label(window,text = "Amount",bg = 'white')
    amount.config(font=("open sans",18))
    amount.place(x = 110,y = 540) 
    amountvalue = Label(window,text = amountv,bg = 'white')
    amountvalue.config(font=("open sans",18,'underline'))
    amountvalue.place(x = 230,y = 540)    
    date = Label(window,text = "Date",bg = 'white')
    date.config(font=("open sans",18))
    date.place(x = 150,y = 580)
    datevalue = Label(window,text = datev,bg = 'white')
    datevalue.config(font=("open sans",18,'underline'))
    datevalue.place(x = 230,y = 580)    
    accountno = Label(window,text = "Account",bg = 'white')
    accountno.config(font=("open sans",18))
    accountno.place(x = 110,y = 620) 
    accountnovalue = Label(window,text = acc,bg = 'white')
    accountnovalue.config(font=("open sans",18,'underline'))
    accountnovalue.place(x = 230,y = 620)     
    signature = Label(window,text = "Signature",bg = 'white')
    signature.config(font= ('open sans',18))
    signature.place(x= 680,y= 620)   
    if condition == "Genuine":
        signatureq = PhotoImage(file = "C:/Users/Acer/Desktop/correctcopy.png")
    else:
        signatureq = PhotoImage(file = "C:/Users/Acer/Desktop/incorrectcopy.png")
    FRAME.signatureq = signatureq
    signaturevalue = Label(window,image= signatureq)
    signaturevalue.place(x = 680,y = 500)
        
       
def openfilex():
    global c
    file1= filedialog.askopenfilename()
    B.set(file1)
    original = Image.open(file1)
    resized = original.resize((550,290),Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(resized)
    Canva1 = Canvas(FRAME,width = 571,height = 296,bd = 16)
    Canva1.configure(background = "#6C7B95")
    Canva1.place(x = 120,y = 99)
    FRAME.image1 = image1
    Canva1.create_image(30,5, image=image1,anchor = NW)

root=tkinter.Tk()
root.geometry("900x700+0+0")
root.configure(background="#C7F0DB")
B = StringVar()
FRAME=Frame(root, width=900, height =600)
FRAME.configure(background="#C7F0DB")
FRAME.pack()
top = Label(FRAME,text = "Bank Cheque Reader",width =48,height = 2,fg = "white",anchor = CENTER)
top.config(font=("Times", 25,'bold'))
top.configure(background="#464159")
top.place(x = 0,y = 0)

Canva = Canvas(FRAME,width = 604,height = 350)
Canva.configure(background = "#6C7B95")
Canva.place(x = 120,y = 99)

#COLOR= StringVar()
colorl = Label(FRAME,text = "Select",bg = "#C7F0DB")
colorl.config(font=("Open Sans", 24))

colorl.place(x =360,y = 480)
'''
r1  = Radiobutton(FRAME,text = "   Red   ",value = "red",variable = COLOR,bg = "#FF545C",anchor = CENTER, indicatoron=0, highlightthickness = 0, bd = 0, width = 10,padx = 20,pady = 20)
r2  = Radiobutton(FRAME,text = "  Blue   ",value = "blue",variable = COLOR,bg = "#2596D3 ",anchor =CENTER, indicatoron=0, highlightthickness = 0, bd = 0, width = 10,padx = 17,pady = 20)
r3  = Radiobutton(FRAME,text = "  Green  ",value = "green",variable = COLOR,bg = "#66CE63",anchor = CENTER, indicatoron=0, highlightthickness = 0, bd = 0, width = 10,padx = 14,pady = 20)
r4 = Radiobutton(FRAME,text = "  Yellow  ",value = "yellow",variable = COLOR,bg = "#F2F239",anchor =CENTER, indicatoron=0, highlightthickness = 0, bd = 0, width = 10,padx = 11,pady = 20)
r1.config(font=("Open Sans", '20'))
r2.config(font=("Open Sans", 20))
r3.config(font=("Open Sans", 20))
r4.config(font=("Open Sans", 20))
r1.place(x =155,y = 534)
r2.place(x =388,y = 534)
r3.place(x =621,y = 534)
r4.place(x =855,y = 534)

FRAME2 = Frame(root,width = 1200,height =200)
FRAME2.configure(background="#C7F0DB")

shapesl = Label(FRAME2,text = "Select Shape",bg = "#C7F0DB")
shapesl.config(font=("Open Sans", 22))
shapesl.place(x = 512,y = 10)
'''
button1 = Button(FRAME,text = "Click to load file on canvas",command = openfilex,bg = "#464159",highlightthickness = 0, bd = 0,fg = "white",height = 1,width = 43)
button1.config(font = ("open sans",18))
button1.place(x =121,y = 428)
'''
SHAPE = StringVar()
photo2 = PhotoImage(file = "C:/Users/Acer/Desktop/traingle copy.png")
FRAME2.photo1 = photo2
photoimaget = photo2.subsample(3,3)
r5 = Radiobutton(FRAME2,image = photoimaget,value = "triangle",variable =SHAPE,height =89,anchor = W,bg = "#C7F0DB", indicatoron=0, highlightthickness = 0, bd = 0,width = 120)

photo2 = PhotoImage(file = "C:/Users/Acer/Desktop/rectangle copy.png")
FRAME2.photo2 = photo2
photoimager = photo2.subsample(1,1)
r6 = Radiobutton(FRAME2,image = photo2,value = "rectangle",variable = SHAPE,height =100,anchor = W,bg = "#C7F0DB", indicatoron=0, highlightthickness = 0, bd = 0,width = 140)

photo3 = PhotoImage(file = "C:/Users/Acer/Desktop/circlee copy.png")
FRAME2.photo1 = photo3
r7 = Radiobutton(FRAME2,image =photo3,value = "circle",variable = SHAPE,anchor = W,bg = "#C7F0DB", indicatoron=0, highlightthickness = 0, bd = 0,width = 92)

photo4 = PhotoImage(file = "C:/Users/Acer/Desktop/pentagon copy.png")
FRAME2.photo1 = photo4
r8 = Radiobutton(FRAME2,image = photo4,value = "pentagon",variable = SHAPE,anchor = W,bg = "#C7F0DB", indicatoron=0, highlightthickness = 0, bd = 0,width = 100)

photo5 = PhotoImage(file = "C:/Users/Acer/Desktop/ellipsess copy.png")
FRAME2.photo1 = photo5
r9 = Radiobutton(FRAME2,image = photo5,value = "ellipse",variable = SHAPE,anchor = W,bg = "#C7F0DB", indicatoron=0, highlightthickness = 0, bd = 0,width = 124)

r5.place(x =130,y = 52)
r6.place(x =310,y = 50)
r7.place(x =530,y = 50)
r8.place(x =680,y = 50)
r9.place(x =870,y = 50)

FRAME2.pack()

labelt = Label(FRAME2,text = "trianagle",compound = RIGHT,bg = "#C7F0DB",highlightthickness = 0, bd = 0)
labelt.config(font=("Open Sans", 15))
labelt.place(x =140,y = 160)



labelt = Label(FRAME2,text = "Rectangle",compound = RIGHT,bg = "#C7F0DB",highlightthickness = 0, bd = 0)
labelt.config(font=("Open Sans", 15))
labelt.place(x =320,y = 160)


labelt = Label(FRAME2,text = "Circle",compound = RIGHT,bg = "#C7F0DB",highlightthickness = 0, bd = 0)
labelt.config(font=("Open Sans", 15))
labelt.place(x =550,y = 160)



labelt = Label(FRAME2,text = "Pentagon",compound = RIGHT,bg = "#C7F0DB",highlightthickness = 0, bd = 0)
labelt.config(font=("Open Sans", 15))
labelt.place(x =700,y = 160)


labelt = Label(FRAME2,text = "Ellipse ",compound = RIGHT,bg = "#C7F0DB",highlightthickness = 0, bd = 0)
labelt.place(x =900,y = 160)
labelt.config(font=("Open Sans", 15))

'''
count  = IntVar()
photoar = PhotoImage(file = "C:/Users/Acer/Desktop/right-arrow.png")
#FRAME2.photo1 = photoar

button2 = Button(FRAME,image = photoar,compound = BOTTOM,bg = "#C7F0DB",highlightthickness = 0, bd = 0,command = connectt)
button2.place(x =700,y = 500)
photoq = PhotoImage(file = "C:/Users/Acer/Desktop/error.png")
FRAME.photoq = photoq
button1 = Button(FRAME,image = photoq,command = root.destroy,background="#464159",highlightthickness = 0, bd = 0)
button1.place(x =840,y =14)
root.mainloop()




