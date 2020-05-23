from tkinter import *
from tkinter.font import Font
import sqlite3
import os  #accessing the os functions
#import check_camera
#import Capture_Image
import Train_Image
import Recognize
#import pandas as pd


#calling the camera test function from check_camera.py file
def check():
    #check_camera.camer()
    os.system('py check_camera.py')
#---------------------------------------------------------
#calling the take image function from Capture_Image.py file
def capturefaces():
    #Capture_Image.takeImages()
    os.system("py Capture_Image.py")
    
#----------------------------------------------------------
#calling the train image function from Train_Image.py file
def trainimages():
    #os.system("py Train_Image.py")
    Train_Image.TrainImages()
    
#------------------------------------------------------------
#calling the Recognize_attendence from Recognize.py file
def recognizefaces():
    Recognize.recognize_attendence()
    #os.system("py Recognize.py")

def sendmail():
    os.system("py mail.py")

#==========================================================================
def Back():
    Home.destroy()
    root.deiconify()

    
Home = Tk()
Home.title(" Home ")
width = 500
height = 600
screen_width = Home.winfo_screenwidth()
screen_height = Home.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
Home.resizable(0, 0)

lbl_home = Label(Home, text="", font=('times new roman', 20)).pack()
btn_1 = Button(Home, text='Check Camera', command=check,width = 45,bg = "gray", height=2).pack(pady=20)
btn_2 = Button(Home, text='Capture Image', command=capturefaces,width = 45,bg = "gray", height=2).pack(pady=20)
btn_3 = Button(Home, text='Train Image', command=trainimages,width = 45,bg = "gray", height=2).pack(pady=20)
btn_4 = Button(Home, text='Mark Attendence', command=recognizefaces,width = 45,bg = "gray", height=2).pack(pady=20)
btn_5 = Button(Home, text='Mail', command=sendmail,width = 45,bg = "gray", height=2).pack(pady=20)
btn_6 = Button(Home, text='logout', command=Back,width = 45,bg = "gray", height=2).pack(pady=20)

Home.mainloop()


    
