#Final Project Calculation Part
import math as m
import cmath as cm
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import copy as cp
#import all the possible packages for convenience

x=20
y=1
z=11
t=0
T=100
#initial values of x,y,t and total time T

P=10
R=28
B=8/3
#parameters

x_values=[x]
y_values=[y]
z_values=[z]
t_values=[t]

dx_values=[P*(y-x)]
dy_values=[R*x-y-x*z]
dz_values=[x*y-B*z]
#establish some lists to store values

N=200000
#slice number and initial values

for i in range(0,N):
    vx0=P*(y-x)
    vy0=R*x-y-x*z
    vz0=x*y-B*z
    
    m1=x+vx0*T/N
    n1=y+vy0*T/N
    q1=z+vz0*T/N
    #Euler method to calculate a test value
    
    for j in range(0,50):
    
        vx1=P*(n1-m1)
        vy1=R*m1-n1-m1*q1
        vz1=m1*n1-B*q1
        #differential in the next point
    
        vx=(vx1+vx0)/2
        vy=(vy1+vy0)/2
        vz=(vz1+vz0)/2
        #average changing ratio
    
        m1=x+vx*T/N
        n1=y+vy*T/N
        q1=z+vz*T/N
        
        vx0=cp.copy(vx1)
        vy0=cp.copy(vy1)
        vz0=cp.copy(vz1)
    #iterate for 50 times
    
    x=m1
    y=n1
    z=q1
    t=t+T/N
    #calculate next point's values
    
    x_values.append(x)
    y_values.append(y)
    z_values.append(z)
    t_values.append(t)
    dx_values.append(vx)
    dy_values.append(vy)
    dz_values.append(vz)
    #store the values

#for testing the results
plt.plot(y_values,z_values,'g',label="I am your father")
plt.title("Do you desire power?")
plt.legend(loc='best')
plt.show()
    
plt.plot(x_values,z_values,'b',label="Grandfather Wei")
plt.title("Do you desire power?")
plt.legend(loc='best')
plt.show()
       
plt.plot(x_values,y_values,'silver',label="Leader Wei")
plt.title("Do you desire power?")
plt.legend(loc='best')
plt.show()
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    