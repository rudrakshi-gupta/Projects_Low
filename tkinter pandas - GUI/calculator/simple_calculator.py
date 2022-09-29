from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.configure(background="Light Yellow")#set bg col of window
# root.geometry()can also be assigned

e= Entry(root,width=37,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def myButton(number):
    # variable=username.get()
    current=e.get()

    # delete(0, END) which aims to clear all the content in the range.(syntax--> delete(first index, last index))
    e.delete(0, END)#actually deletes the last digit backwards, eg. 2--> only 2 as no current, then 5--> cureent 2 + 5 ==> 252 as the 2 was the previous one in 252(it deleted the right side 2)
    
    #  insert ( index, 'name') : Inserts string 'name' before the character at the given index
    e.insert(0,str(current)+str(number))

def myButton_clear():
    e.delete(0, END)

def myButton_add():
    first_num=e.get()
    global f_num
    f_num=int(first_num)
    e.delete(0,END)
    e.insert(0,"+")# why not first num + ---> length of first num unknown so dk how much to delete

def myButton_equal():
    e.delete(0)
    second_num=e.get()
    e.delete(0,END)
    answer=f_num + int(second_num)
    e.insert(0,str(f_num)+"+"+str(second_num)+"="+str(answer))


b1=Button(root,text = "1",padx=40,pady=20,command=lambda : myButton(1))
b2=Button(root,text = "2",padx=40,pady=20,command=lambda : myButton(2))
b3=Button(root,text = "3",padx=40,pady=20,command=lambda : myButton(3))
b4=Button(root,text = "4",padx=40,pady=20,command=lambda : myButton(4))
b5=Button(root,text = "5",padx=40,pady=20,command=lambda : myButton(5))
b6=Button(root,text = "6",padx=40,pady=20,command=lambda : myButton(6))
b7=Button(root,text = "7",padx=40,pady=20,command=lambda : myButton(7))
b8=Button(root,text = "8",padx=40,pady=20,command=lambda : myButton(8))
b9=Button(root,text = "9",padx=40,pady=20,command=lambda : myButton(9))
b0=Button(root,text = "0",padx=40,pady=20,state=DISABLED,command=lambda : myButton(0))

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

button_add=Button(root,text="+",bg="Light Blue",padx=39,pady=20,command=myButton_add)
button_add.grid(row=5,column=0)
button_equals=Button(root,text="=",padx=91,pady=20,command=myButton_equal)
button_equals.grid(row=5,column=1,columnspan=2)
button_clr=Button(root,text="Clear",padx=79,pady=20,command= myButton_clear)#works as well --> lambda : myButton_clear()
button_clr.grid(row=4,column=1,columnspan=2)

root.mainloop()