#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk,messagebox
import matplotlib.pyplot as plt
from numpy import arange,sin,pi,cos,tan


def graficar():
    t=arange(0.0,4*pi,0.01)
    Vp=numero1.get()
    Vm=numero2.get()
    #Vp=2
    f1=20
    plt.subplot(3,1,1)
    w1=2*pi*f1*t
    y1=Vp*sin(w1)
    y11=sin(w1)
    plt.plot(t,y1)
    #plt.title("Señal Portadora")
    plt.ylabel('Fc(t)')
    #Vm=1
    f2=1
    plt.subplot(3,1,2)
    w2=2*pi*f2*t
    y2=Vm*sin(w2)
    y21=sin(w2)
    plt.plot(t,y2)
    #plt.title("Señal moduladora analogica")
    plt.ylabel('Y(t)')
    plt.subplot(3,1,3)
    #Indice de modulación
    m=Vm/Vp
    if m>1:
        men="Sobremodulación de señal AM"
    if m<=1:
        men="Modulación normal de señal AM"
    #Ecuación de señal modulada
    vt=Vp*(1+(m*y21))*y11
    plt.plot(t,vt)
    #plt.title("Señal modulada AM")
    plt.ylabel('Am(t)')
    print("El indice de modulación es ",m*100,'%')
    print("Y éxiste ",men)
    m2=m*100
    a=str(Vp)
    f=str(Vm)
    m3=str(m2)
    messagebox.showinfo("NIVEL DE MODULACIÓN ","El índice de Modulación es "+(m3+" %"  )+"  Y éxiste "+men)
    plt.show()
    
ventana=Tk()
numero1=DoubleVar()
numero2=DoubleVar()
#nombre.set("Escribe tu nombre")
ventana.title("Entradas en tkinter")
ventana.geometry("430x100")
etiqueta=Label(ventana,text="MODULACIÓN AM").place(x=170,y=5)
etiqueta1=Label(ventana,text="Amplitud de Portadora(V)= ").place(x=10,y=30)
nombreCaja=Entry(ventana,textvariable=numero1).place(x=180,y=30)
etiqueta2=Label(ventana,text="Amplitud de Moduladora (V)= ").place(x=10,y=50)
nombreCaja=Entry(ventana,textvariable=numero2).place(x=180,y=50)
boton=Button(ventana,text="GRAFICAR",command=graficar).place(x=340,y=30)
ventana.mainloop()

