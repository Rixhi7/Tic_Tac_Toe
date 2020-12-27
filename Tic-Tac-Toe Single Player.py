#read README file

import tkinter
import random

tictactoe=tkinter.Tk()
tictactoe.title('Tic-Tac-Toe')
tictactoe.geometry('240x260')


but1=but2=but3=but4=but5=but6=but7=but8=but9=0

#Function to Place 'O' on computer's turn
def chk(x):
    global but1,but2,but3,but4,but5,but6,but7,but8,but9
    if x==1:
        b1.configure(text='0')
        but1=1
    elif x==2:
        b2.configure(text='0')
        but2=1
    elif x==3:
        b3.configure(text='0')
        but3=1
    elif x==4:
        b4.configure(text='0')
        but4=1
    elif x==5:
        b5.configure(text='0')
        but5=1
    elif x==6:
        b6.configure(text='0')
        but6=1
    elif x==7:
        b7.configure(text='0')
        but7=1
    elif x==8:
        b8.configure(text='0')
        but8=1
    elif x==9:
        b9.configure(text='0')
        but9=1


#To be used for Computer's Turn
def comp():
    n=random.randint(1,9)
    if(n==1 and but1==0):
        chk(1)            
    elif(n==2 and but2==0):
        chk(2)
    elif(n==3 and but3==0):
        chk(3)
    elif(n==4 and but4==0):
        chk(4)
    elif(n==5 and but5==0):
        chk(5)
    elif(n==6 and but6==0):
        chk(6)
    elif(n==7 and but7==0):
        chk(7)
    elif(n==8 and but8==0):
        chk(8)
    elif(n==9 and but9==0):
        chk(9)
    else:
        comp()
   
#Functions to place 'X' on user's turn (det1-det9)
def det1():
    global but1
    but1=1
    b1.configure(text='X')
    comp()
      
def det2():
    global but2
    but2=1
    b2.configure(text='X')
    comp()
    
def det3():
    global but3
    but3=1
    b3.configure(text='X')
    comp()   

def det4():
    global but4
    but4=1
    b4.configure(text='X')
    comp()

def det5():
    global but5
    but5=1
    b5.configure(text='X')
    comp()
    
def det6():
    global but6
    but6=1
    b6.configure(text='X')
    comp()    
        
def det7():
    global but7
    but7=1
    b7.configure(text='X')
    comp()     

def det8():
    global but8
    but8=1
    b8.configure(text='X')
    comp()
    
def det9():
    global but9
    but9=1
    b9.configure(text='X')
    comp()

b1=tkinter.Button(tictactoe,text='GRID 1',height=5,width=10,command=det1)
b1.grid(row=1,column=1)

b2=tkinter.Button(tictactoe,text='GRID 2',height=5,width=10,command=det2)
b2.grid(row=1,column=2)

b3=tkinter.Button(tictactoe,text='GRID 3',height=5,width=10,command=det3)
b3.grid(row=1,column=3)

b4=tkinter.Button(tictactoe,text='GRID 4',height=5,width=10,command=det4)
b4.grid(row=2,column=1)

b5=tkinter.Button(tictactoe,text='GRID 5',height=5,width=10,command=det5)
b5.grid(row=2,column=2)

b6=tkinter.Button(tictactoe,text='GRID 6',height=5,width=10,command=det6)
b6.grid(row=2,column=3)

b7=tkinter.Button(tictactoe,text='GRID 7',height=5,width=10,command=det7)
b7.grid(row=3,column=1)

b8=tkinter.Button(tictactoe,text='GRID 8',height=5,width=10,command=det8)
b8.grid(row=3,column=2)

b9=tkinter.Button(tictactoe,text='GRID 9',height=5,width=10,command=det9)
b9.grid(row=3,column=3)


tictactoe.mainloop()

