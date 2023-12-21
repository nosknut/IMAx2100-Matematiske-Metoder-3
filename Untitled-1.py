import numpy as np
import math as m
import sympy as sp
import sympy.plotting as spl

x, y, z, t = sp.symbols('x y z t')
r, theta = sp.symbols('r theta', positive=True)

# theta = sp.atan2(y, x)
# r = sp.sqrt(x**2 + y**2)

# spl.plot3d(2*x + 35, (x, -10, 10), (y, -10, 10))

spl.plot3d_parametric_surface(r*sp.cos(theta),r*sp.sin(theta),2*r*sp.cos(theta)+35, (theta, 0, sp.pi * 2), (r,0,20))
x = sp.sqrt(49)*sp.cos(theta)
y = sp.sqrt(49)*sp.sin(theta)
spl.plot3d_parametric_surface(x,y,z, (theta, 0, sp.pi * 2), (z,0,10))




