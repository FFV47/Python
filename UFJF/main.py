import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
from lib import equation
import math

plt.close('all')

# "r" na função open eh pra permitir somente leitura
# delimiter >> mostra como ler os argumentos separados no arquivo
# skiprows >> linhas a pular
# usecols >> quais colunas usar, a ordem importa

M = np.loadtxt(open("route.csv", "r"), delimiter=",",
               skiprows=1, usecols=(3, 2))
M[:, 0] = M[:, 0]*1000

rmin = 6  # Local acessivel a pedestres (69kV)

y_min = M[:, 1] + rmin

R = np.array([[200, 8], [400, 8]])

numlinhasR = np.shape(R)[0]

for i in range(0, numlinhasR):
    indice = np.where(M[:, 0] >= R[i, 0])[0][0]
    y_min[indice-2:indice+2] = M[indice-2:indice+2, 1]+R[i, 1]

plt.figure(1, figsize=(9, 9))
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.plot(M[:, 0], M[:, 1], "b", M[:, 0], y_min, "r")

xt1 = 0
xt2 = 330
H = 20

i_t1 = np.where(M[:, 0] >= xt1)[0][0]
i_t2 = np.where(M[:, 0] >= xt2)[0][0]


yt1 = M[i_t1, 1] + H  # coordenada Y do ponto mais alto da torre 1
yt2 = M[i_t2, 1] + H  # coordenada Y do ponto mais alto da torre 2

"""REPRESENTAÇÃO DAS TORRES"""

T1 = np.array([[xt1, M[i_t1, 1]], [xt1, yt1]])
T2 = np.array([[xt2, M[i_t2, 1]], [xt2, yt2]])

plt.figure(1)
plt.plot(T1[:, 0], T1[:, 1], "k")
plt.plot(T2[:, 0], T2[:, 1], "k")

"""PARAMETROS DA CATENARIA"""

Tnom = 140e3
Tmax = 0.25*Tnom
T0 = 0.96*Tmax
ms = 1350*9.81/1000

param = (xt1, xt2, yt1, yt2, T0, ms)

x0 = fsolve(equation, xt1, args=param)[0]
y0 = yt1-T0/ms*(math.cosh(ms/T0*(xt1-x0))-1)

"""Grafico da Catenaria"""

catenaria_x = np.arange(xt1-x0, xt2-x0, 1)
catenaria_y = np.array([T0/ms*(math.cosh(ms/T0*x)-1) for x in catenaria_x])

catenaria_real_x = catenaria_x + x0
catenaria_real_y = catenaria_y + y0

plt.figure(1)
plt.plot(catenaria_real_x, catenaria_real_y, 'm')

"""Grafico da Tensão"""

T = T0 + catenaria_y*ms
Vtmax = Tmax*np.ones(len(catenaria_real_x))

plt.figure(2, figsize=(9, 9))
plt.xlabel("x[m]")
plt.ylabel("Tração [N]")

plt.plot(catenaria_real_x, T, 'b', catenaria_real_x, Vtmax, 'r')
plt.show()

"""Calculo do Comprimento"""

S = T0/ms*(math.sinh(ms/T0*(xt2-x0)) - math.sinh(ms/T0*(xt1-x0)))
print(S)
