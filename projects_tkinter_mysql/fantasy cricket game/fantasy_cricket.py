from tkinter import *
from tkinter import ttk
import random
from tkinter.messagebox import showinfo
import mysql.connector as connector

#GUI-frontend
class fantasy_cricket:
    def __init__(self,window):
        self.window = window
        self.window.title("Fantasy Cricket")
        self.window.geometry('1200x1080+0+0')
        con = connector.connect(host='localhost',port='3306',user='root',passwd='PINK33', database='teams')
        cur=con.cursor()

        #menu


        def new():
            def submt():
                """ callback when the login button clicked"""
                msg = f'You entered Team name: {teamnamenew.get()} successfully!!'
                showinfo(
                    title='Information',
                    message=msg
                )
            news=Tk()
            teamnamenew=Tk.StringVar()
            n1 = Label(news, text = "Enter team name :").grid(row=0,column=0)
            n2 = Entry(news, width=40,textvariable=teamnamenew)
            n2.grid(row=0,column=1)
            submit=Button(news, text="Submit Here!",width=15,height=2,bg='pink',command=submt)
            submit.grid(row=1,column=1)

        def menu():
            menu=Tk()
            New = Button(menu, text="NEW Teams", width=13, height=2, foreground="black",background="grey",command=new).grid(row=1,column=1,)
            Open = Button(menu, text="OPEN Teams", width=13, height=2, foreground="black",background="grey").grid(row=2,column=1,)
            Save = Button(menu, text="SAVE Teams", width=13, height=2, foreground="black",background="grey").grid(row=3,column=1,)
            Evaluate = Button(menu, text="EVALUATE Teams", width=13, height=2, foreground="black",background="grey").grid(row=4,column=1,)
        manageTeams=Button(self.window, text="ManageTeams",relief=RAISED, width=15, height=3, foreground="black",background="grey",command=menu).grid(row=0,column=0)

        

        #Board
        Boardframe = LabelFrame(self.window,bd=20,bg="grey",text="Your Selection",relief=FLAT,font=('calibri',12))
        Boardframe.place(x=120,y=80,width=900,height=150)
        Board1=Label(Boardframe,text="Batsman(BAT)",background="grey",foreground="black",padx=2,pady=35,font=('calibri',16,'bold')).grid(row=0,column=0)
        e1=Entry(Boardframe,width=5,relief=FLAT,borderwidth=8,font=1,justify=CENTER)
        e1.insert(0,"##")
        e1.grid(row=0,column=1)
        Board2=Label(Boardframe,text="Bowler(BOW)",background="grey",foreground="black",padx=2,pady=35,font=('calibri',16,'bold')).grid(row=0,column=3)
        e2=Entry(Boardframe,width=5,relief=FLAT,borderwidth=8,font=1,justify=CENTER)
        e2.insert(0,"##")
        e2.grid(row=0,column=4)
        Board3=Label(Boardframe,text="Allrounder(AR)",background="grey",foreground="black",padx=2,pady=35,font=('calibri',16,'bold')).grid(row=0,column=5)
        e3=Entry(Boardframe,width=5,relief=FLAT,borderwidth=8,font=1,justify=CENTER)
        e3.insert(0,"##")
        e3.grid(row=0,column=6)
        Board4=Label(Boardframe,text="Wicket-keeper(WK)",background="grey",foreground="black",padx=2,pady=35,font=('calibri',16,'bold')).grid(row=0,column=7)
        e4=Entry(Boardframe,width=5,relief=FLAT,borderwidth=8,font=1,justify=CENTER)
        e4.insert(0,"##")
        e4.grid(row=0,column=8)

        #Points Available
        PointAvaFrame = Frame(self.window,bd=20,bg="grey",relief=FLAT)
        PointAvaFrame.place(x=120,y=320,width=400,height=500)
        pavf=Label(PointAvaFrame,text="Points Available",background="grey",foreground="black",padx=2,font=('calibri',16,'bold')).grid(row=0,column=0,columnspan=2)
        pav=Entry(PointAvaFrame,width=8,relief=FLAT,borderwidth=5,font=1,justify=CENTER)
        pav.insert(0,"##")
        pav.grid(row=0,column=2,columnspan=2)

        blank=Label(PointAvaFrame,bg="grey").grid(row=1)


        #sub-menu
        player_selected=[]
        def team_player(list):
            l=Listbox(PointUsedFrame,font=('Calibri',14),width=32,height=15,selectmode=MULTIPLE)
            l.grid(row=5,column=0,columnspan=4)
            for j in range(len(list)):
                l.insert(j,list[j])

        def clicked_r(i):
            blank=Label(PointAvaFrame,bg="grey").grid(row=4)
            lb=Listbox(PointAvaFrame,font=('Calibri',14),width=32,height=15,selectmode=MULTIPLE)
            lb.grid(row=5,column=0,columnspan=4)
            for j in range(len(i)):
                lb.insert(j,i[j])
            bb=Button(PointAvaFrame,text="Done",background="grey",command=lambda: selected_items(lb))
            bb.grid(row=4,column=3)

        def selected_items(lb):
            for k in lb.curselection():
                player_selected.append(lb.get(k))

            selected_checkboxs = lb.curselection()
            for selected_checkbox in selected_checkboxs[::-1]:
                lb.delete(selected_checkbox)
            
            team_player(player_selected)
            
            # print(player_selected)
        
        selected = list()

        bat_values=["Kohli","Yuvraj","Rahane","Dhoni","Rohit"]
        Bat = ttk.Radiobutton(PointAvaFrame, text='BAT', value=bat_values, variable=selected,command=lambda: clicked_r(bat_values))
        Bat.grid(row=2,column=0)

        bow_values=["Axar","Pandya","Jadeja","Kedar"]
        Bow = ttk.Radiobutton(PointAvaFrame, text='BOW', value=bow_values, variable=selected,command=lambda: clicked_r(bow_values))
        Bow.grid(row=2,column=1)

        ar_values=["Dhawan","Ashwin", "Kartik", "Bhuwneshwar"]
        Ar = ttk.Radiobutton(PointAvaFrame, text='AR', value=ar_values, variable=selected,command=lambda : clicked_r(ar_values))
        Ar.grid(row=2,column=2)

        wk_values=["Umesh","Bumrah"]
        Wk = ttk.Radiobutton(PointAvaFrame, text='WK', value=wk_values, variable=selected,command=lambda: clicked_r(wk_values))
        Wk.grid(row=2,column=3)


        blank=Label(PointAvaFrame,bg="grey").grid(row=4)
        lb1=Listbox(PointAvaFrame,font=('Calibri',12),width=40,height=18,selectmode=SINGLE)
        lb1.grid(row=5,column=0,columnspan=4)


        #Points Used
        PointUsedFrame = LabelFrame(self.window,bd=20,bg="grey",relief=FLAT)
        PointUsedFrame.place(x=620,y=320,width=400,height=500)
        puf=Label(PointUsedFrame,text="Points Used",background="grey",foreground="black",padx=2,font=('calibri',16,'bold')).grid(row=0,column=1)
        pu=Entry(PointUsedFrame,width=8,relief=FLAT,borderwidth=5,font=1,justify=CENTER)
        pu.insert(0,"##")
        pu.grid(row=0,column=3)

        teamname = Label(PointUsedFrame,text="Team name : ",background="grey",foreground="black",pady=10,font=('calibri',16)).grid(row=1, column=1)
        etn=ttk.Combobox(PointUsedFrame, font=('calibri',16))
        # Bat=ttk.Combobox(PointAvaFrame,width=15,font=('calibri',16))
        etn.grid(row=1, column=3)

        blank=Label(PointUsedFrame,bg="grey").grid(row=4)
        lb2=Listbox(PointUsedFrame,font=('Calibri',12),width=40,height=18,selectmode=SINGLE)
        lb2.grid(row=5,column=0,columnspan=4)

        #DB
        # def fc(self):
        #     con = connector.connect(host='localhost',port='3306',user='root',passwd='PINK33', database='teams')
        #     cur=con.cursor()
        #     cur.execute('insert into teams values (%s,%s,%d)'),(self.teamnamenew.get)





#main program
#GUI
window = Tk()
ob=fantasy_cricket(window)
window.mainloop()



# window.title("Fantasy Cricket")

# teamnamenew='\0'
# def new():
#     news=Tk()
#     n1 = Label(news, text = "Enter team name :").grid(row=0,column=0)
#     n2 = Entry(news, width=40).grid(row=0,column=1)
#     teamnamenew=n2.get()

# def menu():
#     menu=Tk()
#     New = Button(menu, text="NEW Teams", width=13, height=2, foreground="black",background="grey",command=new).grid(row=1,column=1,)
#     Open = Button(menu, text="OPEN Teams", width=13, height=2, foreground="black",background="grey").grid(row=2,column=1,)
#     Save = Button(menu, text="SAVE Teams", width=13, height=2, foreground="black",background="grey").grid(row=3,column=1,)
#     Evaluate = Button(menu, text="EVALUATE Teams", width=13, height=2, foreground="black",background="grey").grid(row=4,column=1,)

# manageTeams=Button(window, text="ManageTeams", width=15, height=3, foreground="black",background="grey",command=menu).grid(row=0,column=0)

# Selection=Label(window,text="Your Selection",background="grey",foreground="black",width=143,height=1,anchor='w').grid(row=2,column=1,columnspan=8)

# # def Batsmen():
# #     return(3)
# # def Bowler():
# #     return(3)
# # def Allrounder():
# #     return(3)
# # def Wicketkeeper():
# #     return8


# Board1=Label(window,text="Batsman(BAT)",background="grey",foreground="black",width=15,height=2).grid(row=3,column=1)
# e1=Entry(window,width=10,relief=FLAT,borderwidth=8,font=1,justify=CENTER)
# e1.insert(0,"##")
# e1.grid(row=3,column=2)
# Board2=Label(window,text="Bowler(BOW)",background="grey",foreground="black",width=15,height=2).grid(row=3,column=3)
# e2=Entry(window,width=10,relief=FLAT,borderwidth=8,font=1,justify=CENTER)
# e2.insert(0,"##")
# e2.grid(row=3,column=4)
# Board3=Label(window,text="Allrounder(AR)",background="grey",foreground="black",width=15,height=2).grid(row=3,column=5)
# e3=Entry(window,width=10,relief=FLAT,borderwidth=8,font=1,justify=CENTER)
# e3.insert(0,"##")
# e3.grid(row=3,column=6)
# Board4=Label(window,text="Wicket-keeper(WK)",background="grey",foreground="black",width=15,height=2).grid(row=3,column=7)
# e4=Entry(window,width=10,relief=FLAT,borderwidth=8,font=1,justify=CENTER)
# e4.insert(0,"##")
# e4.grid(row=3,column=8)

# blank=Label(window).grid(row=4)
# pav=Label(window,text="Points Available",background="grey",foreground="black",width=35,justify=RIGHT,height=2).grid(row=5,column=1,columnspan=2)
# pav1=Entry(window,width=20,relief=FLAT,borderwidth=8,font=1,justify=CENTER)
# pav1.insert(0,"##")
# pav1.grid(row=5,column=3,columnspan=2)
# puse=Label(window,text="Points Used",background="grey",foreground="black",width=35,justify=RIGHT,height=2).grid(row=5,column=5,columnspan=2)
# puse1=Entry(window,width=22,relief=FLAT,borderwidth=8,font=1,justify=CENTER)
# puse1.insert(0,"##")
# puse1.grid(row=5,column=7,columnspan=2)

# def bat_names():
#     bats=Tk()
#     b1 = Button(bats, text="Kohli", width=13, height=2, foreground="black",background="yellow").grid(row=1,column=1,)
#     b2 = Button(bats, text="Yuvraj", width=13, height=2, foreground="black",background="yellow").grid(row=2,column=1,)
#     b3 = Button(bats, text="Rahane", width=13, height=2, foreground="black",background="yellow").grid(row=3,column=1,)
#     b4 = Button(bats, text="Dhoni", width=13, height=2, foreground="black",background="yellow").grid(row=4,column=1,)
#     b5 = Button(bats, text="Rohit", width=13, height=2, foreground="black",background="yellow").grid(row=5,column=1,)
# def bow_names():
#     bows=Tk()
#     w1 = Button(bows, text="Axar", width=13, height=2, foreground="black",background="yellow").grid(row=1,column=1,)
#     w2 = Button(bows, text="Pandya", width=13, height=2, foreground="black",background="yellow").grid(row=2,column=1,)
#     w3 = Button(bows, text="Jadeja", width=13, height=2, foreground="black",background="yellow").grid(row=3,column=1,)
#     w4 = Button(bows, text="Kedar", width=13, height=2, foreground="black",background="yellow").grid(row=4,column=1,)
# def ar_names():
#     ars=Tk()
#     a1 = Button(ars, text="Dhawan", width=13, height=2, foreground="black",background="yellow").grid(row=1,column=1,)
#     a2 = Button(ars, text="Ashwin", width=13, height=2, foreground="black",background="yellow").grid(row=2,column=1,)
#     a3 = Button(ars, text="Kartik", width=13, height=2, foreground="black",background="yellow").grid(row=3,column=1,)
#     a4 = Button(ars, text="Bhuwaneshwar", width=13, height=2, foreground="black",background="yellow").grid(row=4,column=1,)
# def wk_names():
#     wks=Tk()
#     k1 = Button(wks, text="Umesh", width=13, height=2, foreground="black",background="yellow").grid(row=1,column=1,)
#     k2 = Button(wks, text="Bumrah", width=13, height=2, foreground="black",background="yellow").grid(row=2,column=1,)

# bat=Button(window,text="BAT",background="blue",command=bat_names,width=16).grid(row=6,column=1)
# bow=Button(window,text="BOW",background="cyan",command=bow_names,width=16).grid(row=6,column=2)
# ar=Button(window,text="AR",background="blue",command=ar_names,width=16).grid(row=6,column=3)
# wk=Button(window,text="WK",background="cyan",command=wk_names,width=16).grid(row=6,column=4)

# def tnames():
#     tnns=Tk()
#     for i in range(2):
#         create=Button(tnns,text=teamnamenew,width=10,height=2).grid(row=i,column=0)

# pave=Entry(window,width=36,relief=FLAT,borderwidth=50,font=1,justify=CENTER)
# pave.insert(0,"Click the above buttons to display!!")
# pave.grid(row=7,rowspan=7,column=1,columnspan=4)
# tnl=Button(window, text="Team name displayed here", background="White",foreground="black",width=73,command=tnames).grid(row=6,column=5,columnspan=4)
# teamnames=Entry(window,width=38,relief=FLAT,borderwidth=50,font=1,justify=CENTER)
# teamnames.insert(0,"Click the above buttons to display!!")
# teamnames.grid(row=7,rowspan=6,column=5,columnspan=4)

# blank=Label(window,width=5).grid(column=9)

# window.mainloop()