from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
global D,t
D=-1
t="Нет решений!"
def lahenda():
    global D,t
    if (a.get()!="" and b.get()!="" and c.get()!=""):
        a_=float(a.get())
        b_=float(b.get())
        c_=float(c.get())
        D=b_*b_-4*a_*c_
        if D>0:
            x1_=round((-1*b_+sqrt(D))/(2*a_),2)
            x2_=round((-1*b_-sqrt(D))/(2*a_),2)
            t=f"X1={x1_}, \nX2={x2_}"
            flag=True
        elif D==0:
            x1_=round((-1*b_)/(2*a_),2)
            t=f"X1={x1_}"
            flag=True
        else:
            t="Корней нет"
            flag=False
        vastus.configure(text=f"D={D}\n{t}")
        a.configure(bg="lightblue")
        b.configure(bg="lightblue")
        c.configure(bg="lightblue")
    else:
        if a.get()=="":
            a.configure(bg="red")
        if b.get()=="":
            b.configure(bg="red")
        if c.get()=="":
            c.configure(bg="red")
            flag=False
    return flag,D,t
def graafik():
    flag,D,t=lahenda()
    if flag==True:
        a_=float(a.get())
        b_=float(b.get())
        c_=float(c.get())
        x0=(-b_)/(2*a_)
        y0=a_*x0*x0+b_*x0+c_
        x1 = np.arange(x0-10, x0+10, 0.5)#min max step
        y1=a_*x1*x1+b_*x1+c_
        fig = plt.figure()
        plt.plot(x0, y0, x1, y1,'r-d')
        plt.title('Квадратное уравнение')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
        text=f"Вершина параболлы ({x0},{y0})"
    else:
        text=f"График нет возможности построить"
    vastus.configure(text=f"D={D}\n{t}\n{text}")
t=0
def veel():
    global t    
    if t==0:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()+200))
        btn_veel.config(text="Уменьшить окно")
        t=1
    else:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()-200))
        btn_veel.config(text="Увеличить окно")
def kala():
    x1 = np.arange(0, 9.5, 0.5)
    y1=(2/27)*x1*x1-3
    x2 = np.arange(-10, 0.5, 0.5)
    y2=0.04*x2*x2-3
    x3 = np.arange(-9, -2.5, 0.5)
    y3=(2/9)*(x3+6)**2+1
    x4 = np.arange(-3, 9.5, 0.5)
    y4=(-1/12)*(x4-3)**2+6
    x5 = np.arange(5, 9, 0.5)
    y5=(1/9)*(x5-5)**2+2
    x6 = np.arange(5, 8.5, 0.5)
    y6=(1/8)*(x6-7)**2+1.5
    x7 = np.arange(-13, -8.5, 0.5)
    y7=(-0.75)*(x7+11)**2+6
    x8 = np.arange(-15, -12.5, 0.5)
    y8=(-0.5)*(x8+13)**2+3
    x9 = np.arange(-15, -10, 0.5)
    y9=[1]*len(x9)
    x10 = np.arange(3, 4, 0.5)
    y10=[3]*len(x10)
    fig = plt.figure()
    plt.plot(x1, y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
    plt.title('Кит')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()
def prillid():
    x1=np.arange(-9,-0.5,0.5)
    y1=-1/16*(x1+5)**2+2
    x2=np.arange(1,9.5,0.5)
    y2=-1/16*(x2-5)**2+2
    x3=np.arange(-9,-0.5,0.5)
    y3=1/4*(x3+5)**2-3
    x4=np.arange(1,9.5,0.5)
    y4=1/4*(x4-5)**2-3
    x5=np.arange(-9,-5.5,0.5)
    y5=-(x5+7)**2+5
    x6=np.arange(6,9.5,0.5)
    y6=-(x6-7)**2+5
    x7=np.arange(-1,1.5,0.5)
    y7=-0.5*x7**2+1.5
    fig = plt.figure()
    plt.plot(x1, y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
    plt.title('Oчки')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()
def babochka():
    x1 = np.arange(-9, -0.5, 0.5)
    y1=-(1/8)*(x1+9)**2+8
    x2 = np.arange(1, 9.5, 0.5)#
    y2=-(1/8)*(x2-9)**2+8
    x3 = np.arange(-9, -7.5, 0.5)
    y3=7*(x3+8)**2+1
    x4 = np.arange(8, 9.5, 0.5)
    y4=7*(x4-8)**2+1
    x5 = np.arange(-8, -0.5, 0.5)
    y5=1/49*(x5+1)**2
    x6 = np.arange(1, 8.5, 0.5)
    y6=1/49*(x6-1)**2
    x7 = np.arange(-8, -0.5, 0.5)
    y7=-4/49*(x7+1)**2
    x8=np.arange(1, 8.5, 0.5)
    y8=-4/49*(x8-1)**2
    x9=np.arange(-8, -1.5, 0.5)
    y9=1/3*(x9+5)**2-7
    x10=np.arange(2, 8.5, 0.5)
    y10=1/3*(x10-5)**2-7
    x11=np.arange(-2, -0.5, 0.5)
    y11=-2*(x11+1)**2-2
    x12=np.arange(1, 2.5, 0.5)
    y12=-2*(x12-1)**2-2
    x13=np.arange(-1, 1.5, 0.5)
    y13=-4*x13**2+2
    x14=np.arange(-1, 1.5, 0.5)
    y14=4*x14**2-6
    x15=np.arange(-2, 0.5, 0.5)
    y15=-1.5*x15+2
    x16=np.arange(0, 2.5, 0.5)
    y16=1.5*x16+2
    fig = plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x13,y13,x14,y14,x15,y15,x16,y16)
    plt.title('Бабочка')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()
def vihmavari():
    x1 = np.arange(-12, 12.5, 0.5)
    y1 = (-1/18)*x1*x1+12
    x2 = np.arange(-4, 4.5, 0.5)
    y2 = (-1/8)*x2*x2+6
    x3 = np.arange(-12, -3.5, 0.5)
    y3 = (-1/8)*(x3+8)**2+6
    x4 = np.arange(4, 12.5, 0.5)
    y4 = (-1/8)*(x4-8)**2+6
    x5 = np.arange(-4, 0.2, 0.5)
    y5 = 2*(x5+3)**2-9
    x6 = np.arange(-4, 0.7, 0.5)
    y6 = 1.5*(x6+3)**2-10
    fig = plt.figure()
    plt.plot(x1, y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
    plt.title('Зонтик')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()
def figura():
    global var
    valik=var.get()
    if valik==1:
        kala()
    elif valik==2:
        prillid()
    elif valik==3:
        vihmavari()
    elif valik==4:
        babochka()
    else:
        konn()
aken=Tk()
aken.geometry("620x200")
aken.title("Квадратные уравнения")
f1=Frame(aken,width=650,height=200)
f1.pack(side=TOP)
f2=Frame(aken,width=650,height=200)
f2.pack(side=BOTTOM)

lbl=Label(f1,text="Решение квадратного уравнения",font="Calibri 26", fg="purple",bg="blue")
lbl.pack()
vastus=Label(f1,text="Решение", height=4,width=60,bg="green")
vastus.pack(side=BOTTOM)
a=Entry(f1,font="Calibri 26", fg="green",bg="lightblue",width=3)
a.pack(side=LEFT)#,padx=10,pady=10
x2=Label(f1,text="x**2+",font="Calibri 26", fg="green", padx=10)
x2.pack(side=LEFT)
b=Entry(f1,font="Calibri 26", fg="green",bg="lightblue",width=3)
b.pack(side=LEFT)
x=Label(f1,text="x+",font="Calibri 26", fg="green")
x.pack(side=LEFT)
c=Entry(f1,font="Calibri 26", fg="green",bg="lightblue",width=3)
c.pack(side=LEFT)
y=Label(f1,text="=0",font="Calibri 26", fg="green")
y.pack(side=LEFT)

btn=Button(f1,text="Решить", font="Calibri 26",bg="green",command=lahenda)
btn.pack(side=LEFT)
btn_g=Button(f1,text="График", font="Calibri 26",bg="green",command=graafik)
btn_g.pack(side=LEFT)
btn_veel=Button(f2,text="Увеличить окно", font="Calibri 26",bg="yellow",command=veel)
btn_veel.pack(side=TOP)
var=IntVar()
r1=Radiobutton(f2,text="Кит", variable=var,var=1, font="Calibri 26",command=kala)
r2=Radiobutton(f2,text="Очки", variable=var,var=2,font="Calibri 26",command=prillid)
r3=Radiobutton(f2,text="Зонтик", variable=var,var=3,font="Calibri 26",command=vihmavari)
r4=Radiobutton(f2,text="Бабочка", variable=var,var=4, font="Calibri 26",command=babochka)
r1.pack()
r2.pack()
r3.pack()
r4.pack()
#btn.bind("<Button-1>",lahenda)
aken.mainloop()
