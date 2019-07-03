import numpy as np
import matplotlib.pyplot as plt

#Lista de N elementos
num=int(input('Ingresar el tamaño de trama de datos digitales ='))
v=[None]*num
cont=0
while (cont<num):
    print ('Ingresar bit ',cont)
    v[cont]=int(input(''))
    cont=cont+1
print ('La trama de bits es :',v,' y es de tipo', type(v))
dim=100
Vx=[]
Di=[]
#Ciclo para crear la trama de datos digitales
for i in range (1,len(v)):
    f=np.ones(dim)
    x=f*v[i]
    Vx=np.concatenate((Vx,x))
plt.subplot(4,1,1)
plt.plot(Vx)
plt.title("Señal digital (Moduladora)")
plt.ylabel('Xm(t)')
dim2=len(Vx)
t=np.linspace(0,5,dim2)
f1=5
plt.subplot(4,1,2)
w1=2*np.pi*f1*t
y1=np.cos(w1)
plt.plot(t,y1)
plt.title("Señal Portadora 1")
plt.ylabel('Fc1(t)')
f2=20
plt.subplot(4,1,3)
w2=2*np.pi*f2*t
y2=np.cos(w2)
plt.plot(t,y2)
plt.title("Señal Portadora 2")
plt.ylabel('Fc2(t)')
plt.subplot(4,1,4)
#Ciclo para concatenar bits ceros con una Fc1 y bits unos con una Fc2
for i in range(0,dim2):
    if Vx[i]==0:
        cero=np.array([y1[i]])
        Di=np.concatenate((Di,cero))
    else:
        uno=np.array([y2[i]])
        Di=np.concatenate((Di,uno))
plt.plot(t,Di)
plt.title("Señal Modulada FSK")
plt.ylabel('Ym(t)')
plt.show()
