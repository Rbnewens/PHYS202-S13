import numpy as np

def pointPotential(X,Y,q,posx,posy):
	"""Gives Vxy when given origin point (x,y) and location (posx, posy)"""
	k = 9*10**9
	return(k*q/((X-posx)**2+(Y-posy)**2)**(1/2.))

def dipolePotential(x,y,q1,q2,d1,d2):
	return (pointPotential(X,Y,q1,-d1/2,-d2/2) + pointPotential(X,Y,q2,d1/2,d2/2))

