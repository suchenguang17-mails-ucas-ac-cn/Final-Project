#Fixed Point Calculator
import numpy as np
import math as m
import cmath as cm
import matplotlib.pyplot as plt
#import all the packages

def fix_point(R, P ,B):
    z=R-1
    if R-1<0:
        x_y=cm.sqrt(B*(R-1))
    else:
        x_y=np.sqrt(B*(R-1))
    return ([x_y,x_y,z],[-x_y,-x_y,z])
    
#define a function to calculate the fixed points
#the results are stored in a 2D array
'''
R=np.linspace(0,168,10000)
P=10
B=8/3

fix1=[]
fix2=[]

for i in R:
    fix1.append(fix_point(i,P,B)[0])
    fix2.append(fix_point(i,P,B)[1])
#calculate the fixed point

print(fix1)
'''