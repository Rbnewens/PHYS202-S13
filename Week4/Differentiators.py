from numpy import zeros

def finiteDifference(x,y):
	"""takes the arrays x and y(x) and returns the derivative of y with respect to x."""
	dydx = zeros(y.shape, float)
	dydx[1:-1] = (y[2:]-y[:-2])/(x[2:]-x[:-2])
    	dydx[0] = (y[1]-y[0])/(x[1]-x[0])
    	dydx[-1] = (y[-1]-y[-2])/(x[-1]-x[-2])
   	return dydx

def fourPtFiniteDiff(x,y):
    """returns derivative of y with respect to x using finite difference method"""
    dydx = zeros(y.shape,float)
    for i in range(2,len(y)-2):
        dydx[i] = (y[i-2]-8*y[i-1]+8*y[i+1]-y[i+2])/(12*(x[1]-x[0]))
    dydx[0] = (y[1]-y[0])/(x[1]-x[0])
    dydx[-1] = (y[-1]-y[-2])/(x[-1]-x[-2])
    dydx[1] = (y[2]-y[1])/(x[2]-x[1])
    dydx[-2] = (y[-2]-y[-3])/(x[-2]-x[-3])
    return dydx

