import csv
import cv2
import os
import tkinter
from tkinter import *
import tkinter.messagebox as mb
from tkinter import filedialog
import re   
import tkinter as tk  
from functools import partial  


# counting the numbers





# Take image function

def takeImages(labelResult1, labelResult, idno, name):


    Id = (idno.get())  
    name = (name.get())

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
        return False


    if(is_number(Id) and name.isalpha()):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0

        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                #incrementing sample number
                sampleNum = sampleNum+1
                #saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage" + os.sep +name + "."+Id + '.' +
                            str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
                #display the frame
                cv2.imshow('frame', img)
            #wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        root2.destroy()
        
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open("StudentDetails"+os.sep+"StudentDetails.csv", 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        
        
    else:
        if Id == "" or name == "" :
            mb.showinfo(title="Mail", message="Please Complete The Data Entry ")
        
        if(Id.isalpha() or Id == ""):
            print("Enter Numeric ID")
            labelResult1.config(text="Enter Numeric ID", fg="red")
            
        if(is_number(name) or name == ""):
            print("Enter Alphabetical Name")
            labelResult.config(text="Enter Alphabetical Name", fg="red")

        #if name == "":
            #labelResult.config(text="Enter Alphabetical Name", fg="red")
            #labelResult1.config(text="Enter Numeric ID", fg="red")
            #labelResult.config(text="Enter Alphabetical Name", fg="red")
        #if Id == "":
            #labelResult1.config(text="Enter Numeric ID", fg="red")
        
        
            
        
        

###############################################

root2 = tk.Tk()  
#root.geometry('400x200+100+200')  
  
root2.title('Student Details')  
width = 600
height = 300
screen_width = root2.winfo_screenwidth()
screen_height = root2.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root2.geometry("%dx%d+%d+%d" % (width, height, x, y))
root2.resizable(0, 0)
   
idno = tk.StringVar()  
name = tk.StringVar()  

labelNum123 = tk.Label(root2, text="Please Fill up the following", font = 14).grid(pady=20,row=1, column=3)

labelNum12 = tk.Label(root2, text="").grid(pady=20,row=2, column=3)


labelNum1 = tk.Label(root2, text="STUDENT ID").grid(padx=30,row=3, column=3)

labelNum2 = tk.Label(root2, text="NAME OF THE STUDENT").grid(row=4, column=3)  

  
labelResult1 = tk.Label(root2)  
  
labelResult1.grid(row=3, column=6)  

labelResult = tk.Label(root2)  
  
labelResult.grid(row=4, column=6)  

  
entryNum1 = tk.Entry(root2, textvariable=idno, width = 30).grid(padx=30,pady=5, row=3, column=5)  
     
entryNum2 = tk.Entry(root2, textvariable=name, width = 30).grid(padx=2,pady=5, row=4, column=5)  


takeImages = partial(takeImages, labelResult1, labelResult, idno, name)  
  
buttonCal = tk.Button(root2, text=" OK ", command=takeImages, width = 10).grid(pady=20, row=6, column=5)  

root2.mainloop()  





            
