# -*- coding: utf-8 -*-
"""
Created on Sun May 19 13:17:39 2019

@author: Pedro Henrique
"""
" Preparatorio PII"
# NBR-5422 #
# Rota de 2,5 Km 230KV #
# Estrada rural (0,8 e 1,3)Km #
# Mata (1,4-1,9)Km #
# Ferrovia eletrificada (0,3 e 2,2) Km #
# Restantes das areas acessiveis somente para pedestres #
# Torres de 20 m #
# Tipo de cabo : PARROT #

import numpy as np
import matplotlib.pyplot as plt
from lib import equation
from scipy.optimize import fsolve
import math
plt.close('all')


M = np.loadtxt(open("route_estudo.csv","r"),delimiter=",",skiprows=1,usecols=(3,2))
M[:,0]=M[:,0]*1000

plt.figure(1) 
plt.xlabel("x [m]")
plt.ylabel("y [m]")

rmin = 6.83
R = np.array([[300,12.83],[800,8.83],[1300,8.83],[2200,12.83]])

y_min = M[:,1] + rmin

numlinhasR = np.shape(R)[0]

for i in range(0,numlinhasR):
    indice = np.where(M[:,0]>=R[i,0])[0][0]
    y_min[indice-2:indice+2] = M[indice-2:indice+2,1]+R[i,1]


plt.plot(M[:,0],M[:,1],'b',M[:,0] ,y_min, 'r') ## linha limite da catenaria pronta ##
 

        ## alocação das torres ##
  

xt1 = 0
xt2 = 370
xt3 = 780
xt4 = 1380
xt5 = 1700
xt6 = 2080
H = 20

i_t1 = np.where(M[:,0]>=xt1)[0][0] 
i_t2 = np.where(M[:,0]>=xt2)[0][0]
i_t3 = np.where(M[:,0]>=xt3)[0][0] 
i_t4 = np.where(M[:,0]>=xt4)[0][0]
i_t5 = np.where(M[:,0]>=xt5)[0][0]
i_t6 = np.where(M[:,0]>=xt6)[0][0]  

yt1 = M[i_t1,1] + H 
yt2 = M[i_t2,1] + H 
yt3 = M[i_t3,1] + H
yt4 = M[i_t4,1] + H
yt5 = M[i_t5,1] + H
yt6 = M[i_t6,1] + H


T1 = np.array([[xt1,M[i_t1,1]],[xt1,yt1]])
T2 = np.array([[xt2,M[i_t2,1]],[xt2,yt2]])
T3 = np.array([[xt3,M[i_t3,1]],[xt3,yt3]])
T4 = np.array([[xt4,M[i_t4,1]],[xt4,yt4]])
T5 = np.array([[xt5,M[i_t5,1]],[xt5,yt5]])
T6 = np.array([[xt6,M[i_t6,1]],[xt6,yt6]])

plt.figure(1)
plt.plot(T1[:,0],T1[:,1],'k')
plt.plot(T2[:,0],T2[:,1],'k') 
plt.plot(T3[:,0],T3[:,1],'k')
plt.plot(T4[:,0],T4[:,1],'k') 
plt.plot(T5[:,0],T5[:,1],'k')
plt.plot(T6[:,0],T6[:,1],'k')    
 
         
         
Tnom = 230.50e3
Tmax = 0.25*Tnom
ms = 2894*9.81/1000   


        ## catenaria 0 ##
        
        
T0 = 0.98*Tmax
        
param = (xt1,xt2,yt1,yt2,T0,ms)
x0 = fsolve(equation,xt1,args=param)[0]
y0 = yt1 - T0/ms*(math.cosh(ms/T0*(xt1-x0))-1)

catenaria1_x = np.arange(xt1-x0,xt2-x0,1) 
catenaria1_y = np.array([T0/ms*(math.cosh(ms/T0*x)-1) for x in catenaria1_x])

catenaria1_x_real = catenaria1_x + x0
catenaria1_y_real = catenaria1_y + y0

plt.figure(1)
plt.plot(catenaria1_x_real,catenaria1_y_real,'m')


T = T0 + catenaria1_y*ms
Vtmax = Tmax*np.ones(len(catenaria1_x_real))

plt.figure(2)

plt.xlabel("x [m]")
plt.ylabel("Tração [N]")

plt.plot(catenaria1_x_real,T,'b',catenaria1_x_real,Vtmax,'r')


S = T0/ms*(math.sinh(ms/T0*(xt2-x0))-math.sinh(ms/T0*(xt1-x0)))


        ## catenaria 1 ##
         # poderia ser ajustada melhor mas tem a estrada, pgt sobre isso #
        
T01 = 0.98*Tmax
        
param1 = (xt2,xt3,yt2,yt3,T01,ms)
x01 = fsolve(equation,xt2,args=param1)[0]
y01 = yt2 - T01/ms*(math.cosh(ms/T01*(xt2-x01))-1)

catenaria1_x1 = np.arange(xt2-x01,xt3-x01,1) 
catenaria1_y1 = np.array([T01/ms*(math.cosh(ms/T01*x)-1) for x in catenaria1_x1])

catenaria1_x1_real = catenaria1_x1 + x01
catenaria1_y1_real = catenaria1_y1 + y01

plt.figure(1)
plt.plot(catenaria1_x1_real,catenaria1_y1_real,'m')


T1 = T01 + catenaria1_y1*ms
Vtmax1 = Tmax*np.ones(len(catenaria1_x1_real))


plt.figure(3)

plt.xlabel("x [m]")
plt.ylabel("Tração [N]")

plt.plot(catenaria1_x1_real,T1,'b',catenaria1_x1_real,Vtmax1,'r')


S1 = T01/ms*(math.sinh(ms/T01*(xt3-x01))-math.sinh(ms/T01*(xt2-x01)))


   ## catenaria 2 ## 
       
        
T02 = 0.96*Tmax
        
param2 = (xt3,xt4,yt3,yt4,T02,ms)
x02 = fsolve(equation,xt3,args=param2)[0]
y02 = yt3 - T02/ms*(math.cosh(ms/T02*(xt3-x02))-1)

catenaria1_x2 = np.arange(xt3-x02,xt4-x02,1) 
catenaria1_y2 = np.array([T02/ms*(math.cosh(ms/T02*x)-1) for x in catenaria1_x2])

catenaria1_x2_real = catenaria1_x2 + x02
catenaria1_y2_real = catenaria1_y2 + y02

plt.figure(1)
plt.plot(catenaria1_x2_real,catenaria1_y2_real,'m')


T2 = T02 + catenaria1_y2*ms
Vtmax2 = Tmax*np.ones(len(catenaria1_x2_real))


plt.figure(4)

plt.xlabel("x [m]")
plt.ylabel("Tração [N]")

plt.plot(catenaria1_x2_real,T2,'b',catenaria1_x2_real,Vtmax2,'r')


S2 = T02/ms*(math.sinh(ms/T02*(xt4-x02))-math.sinh(ms/T02*(xt3-x02)))



   ## catenaria 3 ## 
   # torre na mata ?? ##
       
        
T03 = 0.96*Tmax
        
param3 = (xt4,xt5,yt4,yt5,T03,ms)
x03 = fsolve(equation,xt4,args=param3)[0]
y03 = yt4 - T03/ms*(math.cosh(ms/T03*(xt4-x03))-1)

catenaria1_x3 = np.arange(xt4-x03,xt5-x03,1) 
catenaria1_y3 = np.array([T03/ms*(math.cosh(ms/T03*x)-1) for x in catenaria1_x3])

catenaria1_x3_real = catenaria1_x3 + x03
catenaria1_y3_real = catenaria1_y3 + y03

plt.figure(1)
plt.plot(catenaria1_x3_real,catenaria1_y3_real,'m')


T3 = T03 + catenaria1_y3*ms
Vtmax3 = Tmax*np.ones(len(catenaria1_x3_real))


plt.figure(5)

plt.xlabel("x [m]")
plt.ylabel("Tração [N]")

plt.plot(catenaria1_x3_real,T3,'b',catenaria1_x3_real,Vtmax3,'r')


S3 = T03/ms*(math.sinh(ms/T03*(xt5-x03))-math.sinh(ms/T03*(xt4-x03)))




   ## catenaria 4 ## 
   
       
        
T04 = 0.99*Tmax
        
param4 = (xt5,xt6,yt5,yt6,T04,ms)
x04 = fsolve(equation,xt4,args=param4)[0]
y04 = yt5 - T04/ms*(math.cosh(ms/T04*(xt5-x04))-1)

catenaria1_x4 = np.arange(xt5-x04,xt6-x04,1) 
catenaria1_y4 = np.array([T04/ms*(math.cosh(ms/T04*x)-1) for x in catenaria1_x4])

catenaria1_x4_real = catenaria1_x4 + x04
catenaria1_y4_real = catenaria1_y4 + y04

plt.figure(1)
plt.plot(catenaria1_x4_real,catenaria1_y4_real,'m')


T4 = T04 + catenaria1_y4*ms
Vtmax4 = Tmax*np.ones(len(catenaria1_x4_real))


plt.figure(6)

plt.xlabel("x [m]")
plt.ylabel("Tração [N]")

plt.plot(catenaria1_x4_real,T4,'b',catenaria1_x4_real,Vtmax4,'r')


S4 = T04/ms*(math.sinh(ms/T04*(xt6-x04))-math.sinh(ms/T04*(xt5-x04)))











      
         

 
        
        


    
