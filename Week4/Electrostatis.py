import numpy as np

def pointPotential(X,Y,q,posx,posy):
	"""Gives Vxy when given origin point (x,y) and location (posx, posy)"""
	Vxy=(8.89.e9)*q/sqrt((X-posx)**2. + (Y-posy)**2.)
	return Vxy

def dipolePotential(x,y,q,posx,angle):
	k = 8.9.e-9
	Vxy = (k*q/(x**2+(y-d)**2)**(1/2.)) - (k*q/(x**2+(y+d)**2)**(1/2.))
	return Vxy
