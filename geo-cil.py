#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 14:15:30 2019

@author: waves
"""

from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
#%% For Cylinder
r   = 1 
v   = np.linspace(0, np.pi*2, 50)
w   = np.linspace(0, 3, 50)
v,w = np.meshgrid(v,w)

x = r * np.cos(v)
y = r * np.sin(v)
z = w
#%% For Geodesic
V = np.linspace(0, np.pi, 50)
V = np.array(np.meshgrid(V))

X = r * np.cos(V)
Y = r * np.sin(V)
Z = (3./np.pi)*V
#%%

plt.figure().gca
ax = plt.axes(projection='3d')
ax.grid(False)
ax.plot_surface(x, y, z, rstride=1, cstride=1, color='orange', alpha=0.7)
#ax.plot_wireframe(x, y, z, rcount=5, ccount=5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');
ax.scatter(1,0,0,s=30,c='r') #Punto muestra con v=0, w=0
ax.scatter(-1,0,3,s=30,c='r') #Punto muestra con v=pi, w= 3
ax.plot_wireframe(X,Y,Z, 3, color='b')
ax.set_axis_off()
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
plt.show()