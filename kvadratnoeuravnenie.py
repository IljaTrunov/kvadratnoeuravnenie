from tkinter import *
from math import sqrt
def sqrt_(a,b,c):
    D = b*b - 4*a*c
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        text = "Дискриминант: %s \nX1 -: %s \nX2 -: %s \n"%(D, x1, x2)        
    else:
        text = "Дискриминант: %s \n" % D 
    return text
def sqrt_(a,b,c):
    D = b*b - 4*a*c
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        text = "Дискриминант: %s \nX1 -: %s \nX2 -: %s \n"%(D, x1, x2)        
    else:
        text = "Дискриминант: %s \n  Нет корней у данного уравнения" % D 
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
        inserter("Введите 3 значения!")
aken = Tk()
aken.title("Калькулятор квадратного уравнения")
aken.minsize(400,325)
aken.resizable(width=False, height=False)
button_=Button(aken,text="Решить",font="Arial 16",width=10,bg="#458B00",fg="#000080",relief=RAISED)
button_.pack(side=RIGHT)
kvad=Label(aken,text="Решение квадратного уравнения",height=3,width=30,font="Arial 16",fg="#458B00",bg="lightblue",relief="solid")
kvad.place(x=20,y=25)
a=Entry(width=30,font="Arial 16",fg="#458B00",bg="lightblue",justify="left")

aken.mainloop()
