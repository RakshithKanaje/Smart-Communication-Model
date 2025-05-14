
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import os

app = Tk()
app.title("Welcome")
app.geometry('1550x850')

img=Image.open("bg image.jpg")
img=img.resize((1550,850))
bg=ImageTk.PhotoImage(img)
a=tk.Label(app,image=bg)
a.place(x=0,y=0)

# Add image
label = Label(app, image=bg)
label.place(x = 0,y = 0)

# Add text
label2 = Label(app, text = "SMART COMMUNICATION SYSTEM FOR PHYSICALLY IMPAIRED",bg="#3db7bf",
               font=("Times New Roman", 24))

label2.pack(pady = 50)


def button1():
    os.system('python text_to_speech.py')
    
def button2():
    os.system('python gesture_to_voice.py')

def button3():
    os.system('python voice_to_text.py')
    
def button4():
    os.system('python image_to_voice.py')

def button5():
    os.system('python detect.py')


def Submit():
    pass
    
b1=tk.Button(app,text="text_to_speech",command=button1,bg="#3db7bf",activebackground="#c21d54",fg="black",font=('Arial',16),height=2,width=20)
b1.place(x=100,y=200)

b1=tk.Button(app,text="gesture_to_voice",command=button2,bg="#3db7bf",activebackground="#c21d54",fg="black",font=('Arial',16),height=2,width=20)
b1.place(x=400,y=200)

b1=tk.Button(app,text="voice_to_text",command=button3,bg="#3db7bf",activebackground="#c21d54",fg="black",font=('Arial',16),height=2,width=20)
b1.place(x=700,y=200)

b1=tk.Button(app,text="image_to_voice",command=button4,bg="#3db7bf",activebackground="#c21d54",fg="black",font=('Arial',16),height=2,width=20)
b1.place(x=1000,y=200)

b1=tk.Button(app,text="Object Detection",command=button5,bg="#3db7bf",activebackground="#c21d54",fg="black",font=('Arial',16),height=2,width=20)
b1.place(x=1300,y=200)


app.mainloop()

