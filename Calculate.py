# Final Project Calculation Part
import numpy as np
import matplotlib.pyplot as plt
import copy as cp
import cmath as cm

def Alogrithim(x = 20, y = 1, z = 11, T = 50, R = 28, P = 10, B = 8 / 3, t = 0):
    
    x_values = [x]
    y_values = [y]
    z_values = [z]
    #t_values = np.array([t])
    
   
    N = 100000
    # slice number and initial values

    for i in range(0, N):
        vx = P * (y -x)
        vy = R * x - y - x * z
        vz = x * y - B * z

        m1 = x + vx * T / N
        n1 = y + vy * T / N
        q1 = z + vz * T / N
        # Euler method to calculate a test value

        for j in range(0, 50):

            vx1 = P * (n1 - m1)
            vy1 = R * m1 - n1 - m1 * q1
            vz1 = m1 * n1 - B * q1
            # differential in the next point

            vx = (vx1 + vx) / 2
            vy = (vy1 + vy ) / 2
            vz = (vz1 + vz) / 2
            # average changing ratio

            m1 = x + vx * T / N
            n1 = y + vy * T / N
            q1 = z + vz * T / N

            vx = cp.copy(vx1)
            vy = cp.copy(vy1)
            vz = cp.copy(vz1)
        # iterate for 50 times

        x = m1
        y = n1
        z = q1
        t = t + T / N
        # calculate next point's values

        x_values.append(x)
        y_values.append(y)
        z_values.append(z)

    data = np.array([x_values, y_values, z_values])
    return data

#define a function to calculate the fixed points
#the results are stored in a 2D array
def fix_point(R, P ,B):
    z=R-1
    if R-1<0:
        x_y=cm.sqrt(B*(R-1))
    else:
        x_y=np.sqrt(B*(R-1))
    return np.array([[x_y,x_y,z],[-x_y,-x_y,z]])