from numpy import arange,pi,sin,cos
import matplotlib.pyplot as plt
class moduam:
    def __init__(self,vp,vm):
        self.Vp=vp
        self.Vm=vm
    def portadora(self):
        t=arange(0.0,4*pi,0.01)
        Vp=self.Vp
        Vm=self.Vm
        f1=20
        plt.subplot(3,1,1)
        w1=2*pi*f1*t
        y1=Vp*sin(w1)
        y11=sin(w1)
        plt.plot(t,y1)
        plt.title("Señal Portadora")
    def mensaje(self):
        t=arange(0.0,4*pi,0.01)
        Vp=self.Vp
        Vm=self.Vm
        f2=1
        plt.subplot(3,1,2)
        w2=2*pi*f2*t
        y2=Vm*sin(w2)
        y21=sin(w2)
        plt.plot(t,y2)
        plt.title("Señal moduladora analogica")
    def moduamplitud(self):
        t=arange(0.0,4*pi,0.01)
        Vp=self.Vp
        Vm=self.Vm
        f1=20
        w1=2*pi*f1*t
        y1=Vp*sin(w1)
        y11=sin(w1)
        f2=1
        w2=2*pi*f2*t
        y2=Vm*sin(w2)
        y21=sin(w2)
        plt.subplot(3,1,3)
        m=Vm/Vp
        vt=Vp*(1+(m*y21))*y11
        plt.plot(t,vt)
        plt.title("Señal modulada AM")
        plt.ylabel('Am(t)')
#Algoritmo principal
Vp=float(input('Ingresar amplitud de señal portadora (V) ='))
Vm=float(input('Ingresar amplitud de señal moduladora (V) ='))
a=moduam(Vp,Vm)
a.portadora()
a.mensaje()
a.moduamplitud()
m=Vm/Vp
print("El indice de modulación es ",m*100,'%')
plt.show()
