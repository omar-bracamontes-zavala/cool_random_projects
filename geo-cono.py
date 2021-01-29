#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 17:04:16 2019

@author: waves
"""

from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
#%% For cone
v   = np.linspace(0, 3, 50)
w   = np.linspace(0, 2*np.pi, 50)
v,w = np.meshgrid(v,w)

x = v * np.cos(w)
y = v * np.sin(w)
z = v
#%% For Geodesic
W = np.linspace(0, np.pi, 50)
W = np.array(np.meshgrid(W))
k = 0.8960189
a = 0.6506451


X = (1 + 1/np.pi * W) * np.cos(W)
Y = (1 + 1/np.pi * W) * np.sin(W)
Z = (1 + 1/np.pi * W)
#%%

plt.figure().gca
ax = plt.axes(projection='3d')
ax.grid(False)
ax.plot_surface(x, y, z, rstride=1, cstride=1, color='orange', alpha=0.7)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');
ax.scatter(1,0,1, s=30,c='r') #Punto muestra con v=1, w=0
ax.scatter(-2,0,2,s=30,c='g') #Punto muestra con v=2, w=pi
ax.plot_wireframe(X,Y,Z, 3, color='b')
ax.set_axis_off()
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
plt.show()