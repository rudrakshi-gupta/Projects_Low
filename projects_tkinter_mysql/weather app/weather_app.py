from cProfile import label
from email.mime import image
from tkinter import *
from tkinter import font
from turtle import color
from PIL import Image,ImageTk

window=Tk()
window.title("Weather App;)")
window.geometry('800x600')

img=Image.open('weather.jpg')
img=img.resize((800,600),Image.ANTIALIAS)
photobg=ImageTk.PhotoImage(img)

img_l=Label(window,image=photobg).place(x=0,y=0)

city=Entry(window,width=44,borderwidth=25,font=("Calibri",12),relief=FLAT)
city.place(x=130,y=70)
city.insert(0,"eg:CHENNAI")
submit=Button(window,height=4, width=17,text="SUBMIT;)", background="green").place(x=548,y=70)


window.mainloop()