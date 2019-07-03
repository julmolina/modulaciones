import numpy as np
import matplotlib.pyplot as plt
v=[1,0,1,1,0,1,1,0,0,1,0]
dim=100
Vx=[]
Di=[]
#Ciclo para crear la trama de datos digitales
for i in range (1,11):
    f=np.ones(dim)
    x=f*v[i]
    Vx=np.concatenate((Vx,x))
plt.subplot(4,1,1)
plt.plot(Vx)
plt.title("Señal digital (Moduladora)")
plt.ylabel('Xm(t)')
dim2=len(Vx)
t=np.linspace(0,5,dim2)
f1=3
plt.subplot(4,1,2)
w1=2*np.pi*f1*t
y1=np.cos(w1)
plt.plot(t,y1)
plt.title("Señal Portadora")
plt.ylabel('Fc1(t)')
plt.subplot(4,1,3)
w2=2*np.pi*f1*t
y2=np.sin(w2)
plt.plot(t,y2)
plt.title("Señal Portadora desfasada")
plt.ylabel('Fc1d(t)')
plt.subplot(4,1,4)
res=((y2*Vx)-(y1*Vx)+(y1))
plt.plot(t,res)
plt.title("Señal Modulada PSK")
plt.ylabel('Ym(t)')
plt.show()
