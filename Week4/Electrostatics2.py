import numpy as np
from math import sin, cos, pi

def pointPotential(x,y,q,posx,posy, k=8.9875e9):
	"""Returns electrial potential at x,y from point charge"""
	return (k*q)/(((x-posx)**2+(y-posy)**2)**(1/2.))

def dipolePotential(x,y,q,d,a=0):
	"""Returns electric potential at x,y from dipole centered at origin"""
	xp = (0.5)*d*cos(a); yp = (0.5)*d*sin(a)
	xn = (0.5)*d*cos(a+pi); yn = (0.5)*d*sin(a+pi)
	return pointPotential(x,y,q,xp,yp) + pointPotential(x,y,-q,xn,yn)

def pointField(x,y,q,Xq,Yq):
	"""takes arrays (x,y), charge q and position (Xq,Yq) and returns a tuple of the electric fild components (Ex, Ey)"""
	
	return ((8.98*e**9*q)(x-Xq))/((x-Xq)**2+(y-Yq)**2)**0.5
	return ((8.98*e**9*q)(y-Yq))/((x-Xq)**2+(y-Yq)**2)**0.5

