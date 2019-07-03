import numpy as np
import matplotlib.pyplot as plt
v=[1,0,0,1,0,0,1,0,0,1,1]
dim=100
Vx=[]
#Ciclo para crear la trama de datos digitales
for i in range (1,11):
    f=np.ones(dim)
    x=f*v[i]
    Vx=np.concatenate((Vx,x))
plt.subplot(3,1,1)
plt.plot(Vx)
plt.title("Señal digital (Moduladora)")
plt.ylabel('Xm(t)')
dim2=len(Vx)
t=np.linspace(0,5,dim2)
f1=10
plt.subplot(3,1,2)
w1=2*np.pi*f1*t
y1=np.cos(w1)
plt.plot(t,y1)
plt.title("Señal Portadora")
plt.ylabel('Fc(t)')
plt.subplot(3,1,3)
mult=(Vx*y1)
plt.plot(t,mult)
plt.title("Señal Modulada ASK")
plt.ylabel('Ym(t)')
plt.show()
