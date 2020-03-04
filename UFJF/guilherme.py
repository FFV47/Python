# -*- coding: utf-8 -*-
"""
Created on Fri May 10 09:55:00 2019

@author: Guilherme Márcio
"""

import numpy as np
import matplotlib.pyplot as plt
from lib import equation
from scipy.optimize import fsolve
import math


plt.close('all')

M = np.loadtxt(open("route.csv", "r"), delimiter=",",
               skiprows=1, usecols=(3, 2))
M[:, 0] = M[:, 0]*1000

rmin = 6  # Local. ac. pedestres (69 kV)
R = np.array([[200, 8], [400, 8]])


y_min = M[:, 1] + rmin

numlinhasR = np.shape(R)[0]

for i in range(0, numlinhasR):
    indice = np.where(M[:, 0] >= R[i, 0])[0][0]
    y_min[indice-2:indice+2] = M[indice-2:indice+2, 1]+R[i, 1]

plt.figure(1)  # Repres. relevo, torres e catenária
plt.xlabel("x [m]")
plt.ylabel("y [m]")

plt.plot(M[:, 0], M[:, 1], 'b', M[:, 0], y_min, 'r')


xt1 = 0
xt2 = 330
H = 20

i_t1 = np.where(M[:, 0] >= xt1)[0][0]  # indice da torre 1
i_t2 = np.where(M[:, 0] >= xt2)[0][0]  # indice da torre 2

yt1 = M[i_t1, 1] + H  # coordenada y do ponto mais alto da T1
yt2 = M[i_t2, 1] + H  # coordenada y do ponto mais alto da T2

# Representação das torres
T1 = np.array([[xt1, M[i_t1, 1]], [xt1, yt1]])
T2 = np.array([[xt2, M[i_t2, 1]], [xt2, yt2]])

plt.figure(1)
plt.plot(T1[:, 0], T1[:, 1], 'k')
plt.plot(T2[:, 0], T2[:, 1], 'k')

# Parâmetros da catenária

Tnom = 140e3
Tmax = 0.25*Tnom
T0 = 0.96*Tmax
ms = 1350*9.81/1000

param = (xt1, xt2, yt1, yt2, T0, ms)
x0 = fsolve(equation, xt1, args=param)[0]
y0 = yt1 - T0/ms*(math.cosh(ms/T0*(xt1-x0))-1)

# Gráfico da catenária

catenaria1_x = np.arange(xt1-x0, xt2-x0, 1)
catenaria1_y = np.array([T0/ms*(math.cosh(ms/T0*x)-1) for x in catenaria1_x])

catenaria1_x_real = catenaria1_x + x0
catenaria1_y_real = catenaria1_y + y0

plt.figure(1)
plt.plot(catenaria1_x_real, catenaria1_y_real, 'm')

# Gráfico da tração

T = T0 + catenaria1_y*ms
Vtmax = Tmax*np.ones(len(catenaria1_x_real))

plt.figure(2)

plt.xlabel("x [m]")
plt.ylabel("Tração [N]")

plt.plot(catenaria1_x_real, T, 'b', catenaria1_x_real, Vtmax, 'r')

# Cálculo do comprimento

S = T0/ms*(math.sinh(ms/T0*(xt2-x0))-math.sinh(ms/T0*(xt1-x0)))

np.array
