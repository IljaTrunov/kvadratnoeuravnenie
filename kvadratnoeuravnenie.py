
from tkinter import *
from math import sqrt
def sqrt_(a,b,c):
    D = b*b - 4*a*c
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        text = "Discriminant: %s \nX1 -: %s \nX2 -: %s \n"%(D, x1, x2)        
    else:
        text = "Discriminant: %s \n There are no solutions for this!" % D 
    return text
def numbers(value):
    otvet.delete("0.0","end")
    otvet.insert("0.0",value)
def values():
    try:
        a_val = float(a.get())
        b_val = float(b.get())
        c_val = float(c.get())
        numbers(sqrt_(a_val, b_val, c_val))
    except ValueError:
        inserter("3 meanings!")
aken = Tk()
aken.title("discriminant calculator")
aken.minsize(400,325)
aken.resizable(width=False, height=False)
lbl=Label(aken,text="Discriminant solver",height=3,width=30,font="Arial 20",fg="green",bg="lightblue",relief=FLAT)#.pack()
lbl.pack()
txt=Entry(aken,width=4,font="Arial 20",fg="green",bg="lightblue",justify=CENTER)
txt.pack(side=LEFT)
lb2=Label(aken,text="  x**2+  ",height=3,width=6,font="Arial 20",fg="green",relief=FLAT)#.pack()
lb2.pack(side=LEFT)
txt2=Entry(aken,width=4,font="Arial 20",fg="green",bg="lightblue",justify=CENTER)
txt2.pack(side=LEFT)
lb3=Label(aken,text="  x+  ",height=3,width=6,font="Arial 20",fg="green",relief=FLAT)#.pack()
lb3.pack(side=LEFT)
txt3=Entry(aken,width=4,font="Arial 20",fg="green",bg="lightblue",justify=CENTER)
txt3.pack(side=LEFT)
lb4=Label(aken,text="  =0  ",height=3,width=6,font="Arial 20",fg="green",relief=FLAT)#.pack()
lb4.pack(side=LEFT)
nupp=Button(aken,text="Solve!",font="Arial 20",width=15,bg="green",fg="black",relief=RAISED)
nupp.pack(side=LEFT)
nupp.bind("<Button-1>",sqrt_)
lb5=Label(aken,text="Get",height=3,width=40,font="Arial 20",fg="black",bg="yellow",relief="solid")#.pack()
lb5.place(x=80,y=360)
aken.mainloop()
