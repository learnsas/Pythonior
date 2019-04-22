from tkinter import *
from tkinter import ttk
from tkinter import messagebox

Active_player=1
p1=[]
p2=[]
root=Tk()
root.title("Tic Tac Toe: Player1")
#add buttons

bu1=ttk.Button(root,text=' ')
bu1.grid(row=0,column=0,sticky='snew',ipadx=40,ipady=40)
bu1.config(command=lambda: buttonclick(1))

bu2=ttk.Button(root,text=' ')
bu2.grid(row=0,column=1,sticky='snew',ipadx=40,ipady=40)
bu2.config(command=lambda: buttonclick(2))

bu3=ttk.Button(root,text=' ')
bu3.grid(row=0,column=2,sticky='snew',ipadx=40,ipady=40)
bu3.config(command=lambda: buttonclick(3))

bu4=ttk.Button(root,text=' ')
bu4.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)
bu4.config(command=lambda: buttonclick(4))

bu5=ttk.Button(root,text=' ')
bu5.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)
bu5.config(command=lambda: buttonclick(5))

bu6=ttk.Button(root,text=' ')
bu6.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)
bu6.config(command=lambda: buttonclick(6))

bu7=ttk.Button(root,text=' ')
bu7.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
bu7.config(command=lambda: buttonclick(7))

bu8=ttk.Button(root,text=' ')
bu8.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
bu8.config(command=lambda: buttonclick(8))

bu9=ttk.Button(root,text=' ')
bu9.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
bu9.config(command=lambda: buttonclick(9))



def buttonclick(id):
    global Active_player
    global p1
    global p2
    if (Active_player==1):
        setlayout(id,"X")
        p1.append(id)
        root.title("Tic Tac Toe: Player2")
        Active_player=2
        print('p1:{}'.format(p1))
    elif(Active_player==2):
        setlayout(id, "O")
        p2.append(id)
        root.title("Tic Tac Toe: Player1")
        Active_player = 1
        print('p2:{}'.format(p2))

    checkwinner()

def setlayout(id,playersymbol):
    if id==1:
        bu1.config(text=playersymbol)
        bu1.state(['disabled'])
    elif id==2:
        bu2.config(text=playersymbol)
        bu2.state(['disabled'])
    elif id==3:
        bu3.config(text=playersymbol)
        bu3.state(['disabled'])
    elif id==4:
        bu4.config(text=playersymbol)
        bu4.state(['disabled'])
    elif id==5:
        bu5.config(text=playersymbol)
        bu5.state(['disabled'])
    elif id==6:
        bu6.config(text=playersymbol)
        bu6.state(['disabled'])
    elif id==7:
        bu7.config(text=playersymbol)
        bu7.state(['disabled'])
    elif id==8:
        bu8.config(text=playersymbol)
        bu8.state(['disabled'])
    elif id==9:
        bu9.config(text=playersymbol)
        bu9.state(['disabled'])

def checkwinner():
    winner=-1
    if ((1 in p1) (2 in p1) (3 in p1)):
        winner=1
    if ((1 in p2) (2 in p2) (3 in p2)):
        winner=2

    if ((4 in p1)(5 in p1)(6 in p1)):
        winner = 1
    if ((4 in p2)(5 in p2)(6 in p2)):
        winner = 2

    if ((7 in p1)(8 in p1)(9 in p1)):
        winner = 1
    if ((7 in p2)(8 in p2)(9 in p2)):
        winner = 2

    if ((1 in p1) (4 in p1) (7 in p1)):
        winner=1
    if ((1 in p2) (4 in p2) (7 in p2)):
        winner=2

    if ((2 in p1) (5 in p1) (8 in p1)):
        winner=1
    if ((2 in p2) (5 in p2) (8 in p2)):
        winner=2

    if ((3 in p1) (6 in p1) (9 in p1)):
        winner=1
    if ((3 in p2) (6 in p2) (9 in p2)):
        winner=2

    if ((1 in p1) (5 in p1) (9 in p1)):
        winner=1
    if ((1 in p2) (5 in p2) (9 in p2)):
        winner=2

    if ((3 in p1) (5 in p1) (7 in p1)):
        winner=1
    if ((3 in p2) (5 in p2) (7 in p2)):
        winner=2

    if (winner==1):
        messagebox.showinfo(title='Cogratulation:',message='Player 1 is the Winner')
    elif (winner==2):
        messagebox.showinfo(title='Cogratulation:',message='Player 2 is the Winner')



root.mainloop()
