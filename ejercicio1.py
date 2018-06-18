# Ejercicio 1 (10 puntos)
# Calcule integral de exp(x) entre 0 y 1 con el método de trapecio y de Simpson.
# Haga una grafica (error.png) del error fraccional entre la solución numérica y 
# analítica como funcion del numero de puntos (desde N=10 hasta N=10^8). 
# Tanto el error como el numero de puntos deben variar en escala logaritmica.

import math
import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def simpson(a,b,n):
    dx=(b-a)/n
    integral=0.0
    for i in range(n):
        integral+=(dx/6)*(f(a+i*dx)+f(a+(i+1)*dx)+4*f(a+(i+0.5)*dx))
    return integral

def trapeze(a,b,n):
    dx=(b-a)/n
    integral=0.0
    for i in range(n):
        integral+=(dx*0.5)*(f(a+i*dx)+f(a+(i+1)*dx))
    return integral

def f(x):
    return math.exp(x)
def exact():
    return math.exp(1)-1


powers=np.logspace(1,8,8)
#powers=np.logspace(1,4,4)
errorSimpson=[]
errorTrapeze=[]
for i in powers:
    errorSimpson.append(abs(simpson(0,1,i.astype(int)))-exact())
    errorTrapeze.append(abs(trapeze(0,1,i.astype(int)))-exact())
#mini=min(min(np.absolute(errorSimpson)),min(np.absolute(errorTrapeze)))
#maxi=max(max(errorSimpson),max(errorTrapeze))
#print(errorSimpson)
#print(errorTrapeze)
plt.figure()
plt.yscale('log')
plt.xscale('log')
plt.scatter(powers,np.absolute(errorSimpson),label="Simpson")
plt.scatter(powers,np.absolute(errorTrapeze),label="Trapecio")     
plt.legend()
#plt.ylim(mini, maxi)
plt.xlabel("numero de puntos")
plt.ylabel("error")    
plt.savefig("error.png")
