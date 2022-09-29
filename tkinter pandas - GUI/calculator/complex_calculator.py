from tkinter import *

root = Tk()
root.title("Complex Calculator")

e= Entry(root,width=53,borderwidth=25,justify=RIGHT,relief=FLAT)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10,rowspan=2)

def myButton(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0,str(current)+str(number))

def myButton_clear():
    e.delete(0, END)

def myButton_back():
    # e.delete(-1)#dosen't work
    length=len(e.get())
    e.delete(length-1)

def myButton_add():
    first_num=e.get()
    global f_num
    f_num=float(first_num)
    e.delete(0,END)
    e.insert(0,"+")

def myButton_sub():
    first_num=e.get()
    global f_num
    f_num=float(first_num)
    e.delete(0,END)
    e.insert(0,"-")

def myButton_multiply():
    first_num=e.get()
    global f_num
    f_num=float(first_num)
    e.delete(0,END)
    e.insert(0,"*")

def myButton_divide():
    first_num=e.get()
    global f_num
    f_num=float(first_num)
    e.delete(0,END)
    e.insert(0,"/")

def myButton_expo():
    first_num=e.get()
    global f_num
    f_num=float(first_num)
    e.delete(0,END)
    e.insert(0,"^")

def myButton_mod():
    first_num=e.get()
    global f_num
    f_num=float(first_num)
    e.delete(0,END)
    e.insert(0,"%")

def myButton_equal():
    here=list(e.get())
    e.delete(0)
    second_num=e.get()
    e.delete(0,END)
    if(here[0]=="+"):
        answer=f_num + float(second_num)
        e.insert(0,float(answer))
    if(here[0]=="-"):
        answer=f_num - float(second_num)
        e.insert(0,float(answer))
    if(here[0]=="*"):
        answer=f_num * float(second_num)
        e.insert(0,float(answer))
    if(here[0]=="/"):
        answer=f_num / float(second_num)
        e.insert(0,float(answer))
    if(here[0]=="^"):
        answer=f_num ** float(second_num)
        e.insert(0,float(answer))
    if(here[0]=="%"):
        answer=f_num % float(second_num)
        e.insert(0,float(answer))


b1=Button(root,text = "1",padx=40,pady=20,bg="Grey",relief=GROOVE,fg="white",activebackground="White",command=lambda : myButton(1))
b2=Button(root,text = "2",padx=40,pady=20,bg="Grey",relief=GROOVE,fg="white",activebackground="White",command=lambda : myButton(2))
b3=Button(root,text = "3",padx=40,pady=20,bg="Grey",relief=GROOVE,fg="white",activebackground="White",command=lambda : myButton(3))
b4=Button(root,text = "4",padx=40,pady=20,bg="Grey",relief=GROOVE,fg="white",activebackground="White",command=lambda : myButton(4))
b5=Button(root,text = "5",padx=40,pady=20,bg="Grey",relief=GROOVE,fg="white",activebackground="White",command=lambda : myButton(5))
b6=Button(root,text = "6",padx=40,pady=20,bg="Grey",relief=GROOVE,fg="white",activebackground="White",command=lambda : myButton(6))
b7=Button(root,text = "7",padx=40,pady=20,bg="Grey",relief=GROOVE,fg="white",activebackground="White",command=lambda : myButton(7))
b8=Button(root,text = "8",padx=40,pady=20,bg="Grey",relief=GROOVE,fg="white",activebackground="White",command=lambda : myButton(8))
b9=Button(root,text = "9",padx=40,pady=20,bg="Grey",relief=GROOVE,fg="white",activebackground="White",command=lambda : myButton(9))
b0=Button(root,text = "0",padx=40,pady=20,bg="Grey",relief=GROOVE,fg="white",activebackground="White",command=lambda : myButton(0))
b=Button(root,text = ".",padx=41,pady=20,bg="white",relief=GROOVE,activebackground="Dark Grey",command=lambda : myButton("."))

b1.grid(row=4,column=0)
b2.grid(row=4,column=1)
b3.grid(row=4,column=2)

b4.grid(row=3,column=0)
b5.grid(row=3,column=1)
b6.grid(row=3,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

b0.grid(row=5,column=0)
b.grid(row=6,column=0)

button_add=Button(root,text="+",padx=40,pady=20,bg="white",relief=GROOVE,activebackground="Dark Grey",command=myButton_add)
button_add.grid(row=2,column=3)
button_sub=Button(root,text="-",padx=40,pady=20,bg="white",relief=GROOVE,activebackground="Dark Grey",command=myButton_sub)
button_sub.grid(row=3,column=3)
button_multiply=Button(root,text="*",padx=40,pady=20,bg="white",relief=GROOVE,activebackground="Dark Grey",command=myButton_multiply)
button_multiply.grid(row=4,column=3)
button_divide=Button(root,text="/",padx=40,pady=20,bg="white",relief=GROOVE,activebackground="Dark Grey",command=myButton_divide)
button_divide.grid(row=5,column=3)
button_expo=Button(root,text="^",padx=40,pady=20,bg="white",relief=GROOVE,activebackground="Dark Grey",command=myButton_expo)
button_expo.grid(row=6,column=3)
button_mod=Button(root,text="mod",padx=31,pady=20,bg="white",relief=GROOVE,activebackground="Dark Grey",command=myButton_mod)
button_mod.grid(row=7,column=3)
button_equals=Button(root,text="=",padx=87.4,pady=20,relief=GROOVE,activebackground="Light Blue",bg="Light Grey",fg="Black",command=myButton_equal)
button_equals.grid(row=6,column=1,columnspan=2)
button_clr=Button(root,text="Back",padx=79,relief=GROOVE,pady=20,activebackground="Light Pink",bg="Light Grey",fg="Black",command= myButton_back)
button_clr.grid(row=5,column=1,columnspan=2)
button_clr=Button(root,text="{ CLEAR }",relief=RAISED,padx=115,pady=20,activebackground="Brown",bg="Orange",command= myButton_clear)
button_clr.grid(row=7,column=0,columnspan=3)

root.mainloop()