£READ README FIRST

import tkinter

tictactoe=tkinter.Tk()
tictactoe.title('Tic-Tac-Toe')
tictactoe.geometry('240x260')

f=1

def det1():
    global f
    if(f==1):
        b1.configure(text='X')
        f=f*(-1)
    elif(f==-1):
        b1.configure(text='O') 
        f=f*(-1)
        
def det2():
    global f
    if(f==1):
        b2.configure(text='X')
        f=f*(-1)
    elif(f==-1):
        b2.configure(text='O') 
        f=f*(-1)

def det3():
    global f
    if(f==1):
        b3.configure(text='X')
        f=f*(-1)
    elif(f==-1):
        b3.configure(text='O') 
        f=f*(-1)

def det4():
    global f
    if(f==1):
        b4.configure(text='X')
        f=f*(-1)
    elif(f==-1):
        b4.configure(text='O') 
        f=f*(-1)

def det5():
    global f
    if(f==1):
        b5.configure(text='X')
        f=f*(-1)
    elif(f==-1):
        b5.configure(text='O') 
        f=f*(-1)
        
def det6():
    global f
    if(f==1):
        b6.configure(text='X')
        f=f*(-1)
    elif(f==-1):
        b6.configure(text='O') 
        f=f*(-1)
        
def det7():
    global f
    if(f==1):
        b7.configure(text='X')
        f=f*(-1)
    elif(f==-1):
        b7.configure(text='O') 
        f=f*(-1)

def det8():
    global f
    if(f==1):
        b8.configure(text='X')
        f=f*(-1)
    elif(f==-1):
        b8.configure(text='O') 
        f=f*(-1)

def det9():
    global f
    if(f==1):
        b9.configure(text='X')
        f=f*(-1)
    elif(f==-1):
        b9.configure(text='O') 
        f=f*(-1)


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
