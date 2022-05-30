'''
Pollutant transport in Water model using finite difference method
with an explicit scheme

  C_t + vC_x - EC_xx + kC = S,    0<x<L, t>0

initial condition
  C(x,t=0) = 0

boundary conditions x=0, x=L
  C_x = 0
'''
# Imports
import numpy as np
from numba import jit
import scipy.stats as stats
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Auxiliar functions
def courant_condition(u,L,M,st,N):
  # Tsakiris p.144
  criterion = u*st*M/(N*L)

  if (0<criterion and criterion <= 1):
    print(f'The model is stable\n\t 0<{criterion} <= 1')
    return True
  if criterion == 0:
    print('StabilityError: Increase M and/or decrease N')
  else:
    print('StabilityError: Decrease M and/or increase N')
    print(f'\tSuggestion: N>={u*st*M/L}')
  return False
def plotSolution(x,t,C):
  # 3D plot
  tt,xx = np.meshgrid(t,x)
  fig = plt.figure(figsize=(9,6))
  ax = fig.add_subplot(111, projection='3d')
  ax.plot_surface(xx,tt, C, cmap='viridis')
  ax.set_xlabel('$x$')
  ax.set_ylabel('$t$')
  ax.set_zlabel('$C(x,t)$')

  plt.show()

  # Contour plot
  fig,ax=plt.subplots(1,1)
  cp = ax.contourf(xx, tt, C.T)
  fig.colorbar(cp) # Add a colorbar to a plot
  ax.set_title('Transporte de contaminante')
  ax.set_xlabel('x (m)')
  ax.set_ylabel('t (s)')
  plt.show()

# Finite Difference Method
@jit()
def main():
  # Model constants
  E = 0.06             # Dispersion coefficient [m^2/s] (from Tsakiris p.145) 70. 5
  k = 0                # Decay constant [1/s] (Conservative pollutan thus 0)

  # Pullutant injection
  alpha = 0.07*1006050                    # Total pollutant injection [kg/day] daily_per_person*population
  xp = 4000                              # Center of the pollutant injection [m]
  S = alpha*stats.norm.pdf(x, xp, 700) # Size, mean, variance. Vector de descarga total
  S_n = S/N                              # Vector de descarga para cada tiempo n

  # Initialize solution matrix
  C = np.zeros((M+1+2,N+1+2))  # Solution (pollutant concentration) matrix
  # Initial condition
  C[:,1] = 0

  # Model
  for n in range(1,N-1): # FTime loop     
    if n%500 == 0: print('Step: ', n,'/',N)
    for i in range(1,M-1): # For every spatial step
      C[i,n+1] = dt*(S_n[i] + E/(dx**2)*(C[i+1,n]-2*C[i,n]+C[i-1,n]) - u/(2*dx)*(C[i+1,n]-C[i-1,n]) - k*C[i,n]) + C[i,n]

  # Neumann boundary conditions
  C[1,:] = C[0,:]
  C[i-1,:] = C[i+1,:]
  
  return C


if __name__ == '__main__':
  # Model parameters
  L = 8000     # River length [m]
  st = 3600*1   # Simulation time [s] (24 hours) 86400
  u = 8         # Average velocity [m/s]  (from Manning formula) 8.03
  M = 320      # Spatial resolution 800 320
  N = 28000    # Time resolution 70,000 28,000
  dx = L/M     # Space step [m]
  dt = st/N    # Time step [s]

  x = np.linspace(0,L,M+1+2)  # For plotting
  t = np.linspace(0,st,N+1+2) # For plotting

  if courant_condition(u,L,M,st,N):
    C = main()
    C = np.nan_to_num(C, nan=0, posinf=0, neginf=0)
    
    plotSolution(x,t,C)