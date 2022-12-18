#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: joseangelcidaraujo
"""

import numpy as np
from sympy import Symbol,Derivative,simplify,lambdify,sin
import math
import matplotlib.pyplot as plt

#Definimos a función cuxas raíces queremos aproximar:

z=Symbol('z')
f=z**2-0.59255*z**-1 # Julia set of z^2 - 0.59255z^-1 (http://usefuljs.net/fractals/docs/rational_maps.html)

#Definimos a derivada da función anterior:

derf=Derivative(f,z,1).doit()

#Definimos tamén a segunda derivada:

der2f=Derivative(f,z,2).doit()

#Método de Chebyshev
g=z-(1+(f*der2f/(derf**2))/2)*(f/derf)

#Os seguintes parámetros poden ser modificados co obxetivo de 
#conseguir os mellores gráficos posibles: 

#Número máximo de iteracións para o método elexido:

maxiter=30

#O fractal representarase no rectángulo [a,b]x[c,d]: 

a=-1.6
b=1.5
c=-1.6
d=1.5

#Número de puntos usados nos eixos OX e OY para representar o fractal: canto
#maior sexa o número de puntos mais preciso sera o gráfico, pero tamén mais
#tempo se necesitará para levar a cabo os cálculos.

npuntos=900

################### NON MODIFICAR ESTA PARTE DO PROGRAMA #####################
##############################################################################

ff=lambdify(z,f,"numpy")
gg=lambdify(z,g,"numpy")
fractal = np.zeros((npuntos+1,npuntos+1))
x = np.zeros(npuntos+1)
y = np.zeros(npuntos+1)
hx=(b-a)/npuntos
hy=(d-c)/npuntos
tol=1.0e-6

for i in range(0,npuntos):
    x[i] = a+i*hx
    for j in range(0,npuntos):
        y[j] = c+j*hy
        z = complex(x[i],y[j])
        n=0
        # while (n<maxiter and abs(ff(z))>tol):
        while (n<maxiter and abs(z)!=0  and abs(ff(z))>tol):
            if abs(z.real)>tol and abs(z.imag)>tol and abs(gg(z))<1/tol:   
               z=gg(z)
               n=n+1
            else:
               break
        fractal[npuntos-j,i]=float(n)  

##############################################################################
##############################################################################

print('') 
print('MÉTODO DE CHEBYSHEV')       
print('A función utilizada é: f(z)=',f)
print('A súa derivada é: derf(z)=',derf)
print('A súa segunda derivada é: der2f(z)=',der2f)
print('A función do método de Chebyshev é: g(z)=',g)

#A continuación represéntase a imaxen fractal: recoméndase buscar unha gama de 
#cores atractiva. 

plt.imshow(fractal,cmap='coolwarm', extent=(a, b, c, d))
plt.colorbar()
plt.xlabel("x")
plt.ylabel("y")

#A continuación gárdase a imaxen do fractal nun ficheiro: cambiar o nome do 
#ficheiro según o método usado 

plt.savefig('fractal_Chebyshev.png', dpi=2000)
plt.show()