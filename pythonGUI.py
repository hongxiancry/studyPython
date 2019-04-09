

from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry('800x200')
def helloCallBack():
	msg = messagebox.showinfo("Hello,user","Hello,Guest")
	B = Button(top,text="register",command=helloCallBack)
	B.place(x=300,y=100)
