from tkinter import *
import os
root1 = Tk()
root1.title("FACE RECOGNITION ATTENDANCE SYSTEM")
width = 400
height = 280
screen_width = root1.winfo_screenwidth()
screen_height = root1.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root1.geometry("%dx%d+%d+%d" % (width, height, x, y))
root1.resizable(0, 0)

def openFile3():
    os.system("admin.py")

def openFile1():
    os.system("user.py")

class App:
    def __init__(self, master):
        self.frame = Frame(master)
        
        # create a Form label 
        self.l1 = Label(text="FACE RECOGNITION ATTENDANCE SYSTEM", bg="gray", width="300", height="2", font=("Calibri", 14)).pack() 
        self.l2 = Label(text="CHOOSE ADMIN OR STUDENT").pack() 
        self.l3 = Label(text="").pack() 
        
        # create Login Button 
        self.b1 = Button(text="ADMIN", height="2", width="30", command = openFile3).pack() 
        self.l4 = Label(text="").pack() 
           
        # create a register button
        self.b2 = Button(text="STUDENT", height="2", width="30", command = openFile1).pack()

        

#root = Tk()
app = App(root1)
root1.mainloop()
