import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import tkinter.messagebox as mb
from tkinter import filedialog
from tkinter import *
import re 
  
####################
import tkinter as tk  
from functools import partial  
   
   
def call_result(label_result, n1, n2, n3):  
    email_user = (n1.get())  
    email_password = (n2.get())
    email_send = (n3.get())
    #print(num1, num2, num3)
    #result = int(num1)+int(num2)+int(num2)
    ########################################
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    def check(email, password, email1):
        if email_user == "" or email_password == "" or email_send == "":
            label_result.config(text="PLease complete the required field!!!", fg="red")

           
        elif(re.search(regex,email) and re.search(regex,email1)):
            print("Valid Email")
            label_result.config(text="Valid Email", fg="red")
            subject = 'FRAS MAIL'
            msg = MIMEMultipart()
            msg['From'] = email_user
            msg['To'] = email_send
            msg['Subject'] = subject
            body = 'Hi there, sending this email from FRAS !!!'
            msg.attach(MIMEText(body,'plain'))
            ####___FOR ACCESSING THE FILE'S___####
            root.filename1 =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("PDF Files","*.pdf"),("all files","*.*")))
            #root.filename1 =  filedialog.askopenfilename(filetypes = (("PDF Files","*.pdf"),("all files","*.*"))
            filename=root.filename1
            root.destroy()
            root.mainloop()
            ######################################
            attachment  =open(filename,'rb')
            part = MIMEBase('application','octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',"attachment; filename= "+filename)
            msg.attach(part)
            text = msg.as_string()
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(email_user,email_password)
            server.sendmail(email_user,email_send,text)
            mb.showinfo(title="Mail", message="Mail Sended Successfully")
            server.quit()

        else :
            print("Invalid Email Address Plz check it!!")
            #labelNum3 = tk.Label(root, text="Invalid Email").grid(row=5, column=6)
            label_result.config(text="Invalid Email Address Plz check it!!", fg="red")

    check(email_user, email_password, email_send)

            
   
    
    #label_result.config(text="print successfully")  
    return  
   
root = tk.Tk()  
#root.geometry('400x200+100+200')  
  
root.title('SEND MAIL')  
width = 500
height = 380
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
   
number1 = tk.StringVar()  
number2 = tk.StringVar()  
number3 = tk.StringVar()  



labelNum123 = tk.Label(root, text="Please Fill up the following", font = 14).grid(pady=20,row=1, column=3)

labelNum12 = tk.Label(root, text="").grid(pady=20,row=2, column=3)


labelNum1 = tk.Label(root, text="ADMIN MAIL ID").grid(padx=30,row=3, column=3)

labelNum2 = tk.Label(root, text="PASSWORD").grid(row=4, column=3)  

labelNum3 = tk.Label(root, text="SENDER MAIL ID").grid(row=5, column=3)  
  
labelResult = tk.Label(root)  
  
labelResult.grid(row=7, column=3)  
  
entryNum1 = tk.Entry(root, textvariable=number1, width = 30).grid(padx=30,pady=5, row=3, column=5)  
     
entryNum2 = tk.Entry(root, textvariable=number2,  show="*", width = 30).grid(padx=2,pady=5, row=4, column=5)  

entryNum3 = tk.Entry(root, textvariable=number3, width = 30).grid(padx=2,pady=5, row=5, column=5)  

call_result = partial(call_result, labelResult, number1, number2, number3)  
  
buttonCal = tk.Button(root, text=" SEND MAIL ", command=call_result, width = 30).grid(pady=20, row=6, column=5)  

root.mainloop()  
