import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

ax = plt.axes(projection='3d')

zline = np.linspace(0,15,1000)
xline = np.sin(zline)
yline = np.cos(zline)

ax.plot(xline,yline,zline,'grey')

zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)

ax.scatter3D(xdata,ydata,zdata,c=zdata, cmap='Blues')




#Contour plot

def f(x,y):
    return np.sin(np.sqrt(x**2 + y**2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X,Y = np.meshgrid(x,y)
Z = f(X,Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()



#Surface Triangulation

theta = 2 * np.pi * np.random.random(1000)
r = 6 * np.random.random(1000)
x = np.ravel(r * np.sin(theta))
y = np.ravel(r * np.cos(theta))
z = f(x, y)

ax = plt.axes(projection='3d')
ax.scatter(x, y, z, c=z, cmap='viridis', linewidth=0.5)

plt.show()