# explore small change to a chaotic sistem

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib

import Calculate

data1 = Calculate.Alogrithim(8.6, 8.5, 28, 100, 80, 10, 8 / 3, 0)
data2 = Calculate.Alogrithim(8.6, 8.6, 28, 100, 80, 10, 8 / 3, 0)

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection="3d")

# Determine the edges of plots
edges = []
for i in range(3):
    ax_min = np.min(data1[i])
    ax_max = np.max(data1[i])
    gap = (ax_max - ax_min) / 20
    edges.append([ax_min - gap, ax_max + gap])

ax.set_xlim3d(edges[0])
ax.set_xlabel('X')

ax.set_ylim3d(edges[1])
ax.set_ylabel('Y')

ax.set_zlim3d(edges[2])
ax.set_zlabel('Z')

# label fixed points

fix = Calculate.fix_point(R = 80, P = 10, B = 8/3)
print(fix)

ax.scatter(fix[0, 0], fix[0, 1], fix[0, 2], lw=0.8,  color='black', label="fixed point")
ax.scatter(fix[1, 0], fix[1, 1], fix[1, 2], lw=0.8, color='black', label="fixed point")

# plot 3D graph

ax.plot(data1[0], data1[1], data1[2], lw=0.3, color = 'g', label = 'data1')
ax.plot(data2[0], data2[1], data2[2], lw=0.3, color = 'b', label = 'data2')
ax.legend(loc = 'best')
plt.savefig("butterfly_effect.png")

# calculate chaotic behavior after long enough time, the last 5000 steps

plt.figure(2)
plt.plot(range(5000), data1[0][-5000:], lw = 0.6)
plt.plot(range(5000), data2[0][-5000:], lw = 0.6)
plt.xlabel("steps")
plt.ylabel("X")
plt.legend(["data1", "data2"])
plt.savefig("X_final.png")

plt.figure(3)
plt.plot(range(5000), data1[1][-5000:], lw = 0.6)
plt.plot(range(5000), data2[1][-5000:], lw = 0.6)
plt.xlabel("steps")
plt.ylabel("Y")
plt.legend(["data1", "data2"])
plt.savefig("Y_final.png")

plt.figure(4)
plt.plot(range(5000), data1[2][-5000:], lw = 0.6)
plt.plot(range(5000), data2[2][-5000:], lw = 0.6)
plt.xlabel("steps")
plt.ylabel("Z")
plt.legend(["data1", "data2"])
plt.savefig("Z_final.png")

