from tkinter import *

root = Tk()
root.title("Operator Calculator")

e= Entry(root,width=40,borderwidth=20,relief=FLAT,justify=CENTER)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def myButton(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0,str(current)+str(number))

def myButton_clear():
    e.delete(0, END)

def myButton_add():
    first_num=e.get()
    global f_num
    f_num=int(first_num)
    e.delete(0,END)
    e.insert(0,"+")

def myButton_sub():
    first_num=e.get()
    global f_num
    f_num=int(first_num)
    e.delete(0,END)
    e.insert(0,"-")

def myButton_multiply():
    first_num=e.get()
    global f_num
    f_num=int(first_num)
    e.delete(0,END)
    e.insert(0,"*")

def myButton_divide():
    first_num=e.get()
    global f_num
    f_num=int(first_num)
    e.delete(0,END)
    e.insert(0,"/")

def myButton_equal():
    here=list(e.get())
    e.delete(0)
    second_num=e.get()
    e.delete(0,END)
    if(here[0]=="+"):
        answer=f_num + int(second_num)
        e.insert(0,str(f_num)+"+"+str(second_num)+"="+str(answer))
    if(here[0]=="-"):
        answer=f_num - int(second_num)
        e.insert(0,str(f_num)+"-"+str(second_num)+"="+str(answer))
    if(here[0]=="*"):
        answer=f_num * int(second_num)
        e.insert(0,str(f_num)+"*"+str(second_num)+"="+str(answer))
    if(here[0]=="/"):
        answer=f_num / int(second_num)
        e.insert(0,str(f_num)+"/"+str(second_num)+"="+str(answer))


b1=Button(root,text = "1",padx=40,pady=20,command=lambda : myButton(1))
b2=Button(root,text = "2",padx=40,pady=20,command=lambda : myButton(2))
b3=Button(root,text = "3",padx=40,pady=20,command=lambda : myButton(3))
b4=Button(root,text = "4",padx=40,pady=20,command=lambda : myButton(4))
b5=Button(root,text = "5",padx=40,pady=20,command=lambda : myButton(5))
b6=Button(root,text = "6",padx=40,pady=20,command=lambda : myButton(6))
b7=Button(root,text = "7",padx=40,pady=20,command=lambda : myButton(7))
b8=Button(root,text = "8",padx=40,pady=20,command=lambda : myButton(8))
b9=Button(root,text = "9",padx=40,pady=20,command=lambda : myButton(9))
b0=Button(root,text = "0",padx=40,pady=20,command=lambda : myButton(0))

b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)

b0.grid(row=4,column=0)

button_add=Button(root,text="+",padx=39,pady=20,command=myButton_add)
button_add.grid(row=5,column=0)
button_sub=Button(root,text="-",padx=40,pady=20,command=myButton_sub)
button_sub.grid(row=6,column=0)
button_multiply=Button(root,text="*",padx=40,pady=20,command=myButton_multiply)
button_multiply.grid(row=6,column=1)
button_divide=Button(root,text="/",padx=40,pady=20,command=myButton_divide)
button_divide.grid(row=6,column=2)
button_equals=Button(root,text="=",bg="Light Green",padx=88,pady=20,command=myButton_equal)
button_equals.grid(row=5,column=1,columnspan=2)
button_clr=Button(root,text="Clear",bg="Light Pink",padx=78,pady=20,command= myButton_clear)
button_clr.grid(row=4,column=1,columnspan=2)

root.mainloop()