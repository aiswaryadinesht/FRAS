from tkinter import *
import os
import Recognize
root1 = Tk()
root1.title("Students Portal")
width = 400
height = 200
screen_width = root1.winfo_screenwidth()
screen_height = root1.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root1.geometry("%dx%d+%d+%d" % (width, height, x, y))
root1.resizable(0, 0)
def markattend():
    Recognize.recognize_attendence()
    #os.system("py Recognize.py")
class App:
    def __init__(self, master):
        self.frame = Frame(master)
        self.l4 = Label(text="Students Please click Here to Mark Attendance").pack() 
        self.l4 = Label(text="").pack() 
        self.l4 = Label(text="").pack() 
        
        
        # create Login Button 
        self.b1 = Button(text="MARK ATTENDANCE", height="2", width="30", command = markattend).pack() 
        self.l4 = Label(text="").pack() 
        self.l4 = Label(text="").pack() 
        self.l4 = Label(text="").pack() 
        
        

#root = Tk()
app = App(root1)
root1.mainloop()
