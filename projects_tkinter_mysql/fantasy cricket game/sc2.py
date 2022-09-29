from tkinter import *

# create a GUI window

root = Tk()

# set the background colour of GUI window

root.configure(background="red")

# set the title of GUI window

root.title("Simple Calculator")

# set the configuration of GUI window

# root.geometry("500x500")



expression = ""

equation = StringVar()



def button_click(num):

  global expression

  expression = expression + str(num)

  equation.set(expression)



def equalpress():

  try:

    global expression

    total = str(eval(expression))

    equation.set(total)

    expression = ""

  except:

    equation.set(" error ")

    expression = ""

 

def clear():

  global expression

  expression = ""

  equation.set("")

   

expression_field = Entry(root, textvariable=equation)

expression_field.grid(columnspan=3, ipadx=70)



button_1= Button(root, text='1', padx= 40, pady=20, command= lambda: button_click(1))

button_2= Button(root, text='2', padx= 40, pady=20, command= lambda: button_click(2))

button_3= Button(root, text='3', padx= 40, pady=20, command= lambda: button_click(3))

button_4= Button(root, text='4', padx= 40, pady=20, command= lambda: button_click(4))

button_5= Button(root, text='5', padx= 40, pady=20, command= lambda: button_click(5))

button_6= Button(root, text='6', padx= 40, pady=20, command= lambda: button_click(6))

button_7= Button(root, text='7', padx= 40, pady=20, command= lambda: button_click(7))

button_8= Button(root, text='8', padx= 40, pady=20, command= lambda: button_click(8))

button_9= Button(root, text='9', padx= 40, pady=20, command= lambda: button_click(9))

button_0= Button(root, text='0', padx= 40, pady=20, command= lambda: button_click(0))



button_add= Button(root, text='+', padx= 39, pady=20, command= lambda: button_click('+'))

button_equal= Button(root, text='=', padx= 90, pady=20, command=equalpress)

button_clear= Button(root, text='clear', padx= 80, pady=20,command=clear)



button_7.grid(row=1, column= 0)

button_8.grid(row=1, column= 1)

button_9.grid(row=1, column= 2)



button_4.grid(row=2, column= 0)

button_5.grid(row=2, column= 1)

button_6.grid(row=2, column= 2)



button_1.grid(row=3, column= 0)

button_2.grid(row=3, column= 1)

button_3.grid(row=3, column= 2)



button_0.grid(row=4, column= 0)

button_clear.grid(row=4, column= 1, columnspan= 2)



button_add.grid(row=5, column= 0)

button_equal.grid(row=5, column= 1, columnspan= 2)

 

root.mainloop()