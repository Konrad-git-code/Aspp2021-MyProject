import numpy as np
import scipy.optimize as opt

def gaussian2DFit(XY, x0, y0, sigmax, sigmay, amp, background):
	"""Two-dimensional Gaussian function, returned as a 
	one-dimensional array"""
	(X, Y) = XY 
	fit = amp*np.exp(-((X-x0)**2/(2*sigmax**2) + (Y-y0)**2/(2*sigmay**2)))+ background
	
	return fit.ravel()


def getFitParam(im):
	"""Get the amplitude, x-coordinate, y-coordinate, sigma in x,
	sigma in y and background  of the Gaussian function based on 
	non-linear least squares fitting"""
	x = np.linspace(0, im.shape[1], im.shape[1])
	y = np.linspace(0, im.shape[0], im.shape[0])
	X, Y = np.meshgrid(x, y)

	#curve_fit requires an independent variable with dimensions (2, M)
	#and dependent data with dimensions (1, M)
	XY = np.vstack((X.ravel(), Y.ravel()))
	init_guess = (im.shape[1]/2, im.shape[0]/2, 2, 2, 10, 0)

	param_opt, param_cov = opt.curve_fit(gaussian2DFit, XY, im.ravel(), p0 = init_guess)

	return param_opt
