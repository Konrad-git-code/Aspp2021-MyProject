import numpy as np
import scipy.optimize as opt

def gaussian2DFit(XY, x0, y0, sigmax, sigmay, amp, background):
	"""Two-dimensional Gaussian function, returned as a
	one-dimensional array

	Parameters
        ----------
        XY : ndarray
            matrix to fit the Gaussian function
        x0 : int, float
            x-coordinate of a centroid
        y0 : int, float
            y-coordinate of a centroid
        sigmax : int, float
            standard deviation of the Gaussian function along the x-axis
        sigmay : int, float
            standard deviation of the Gaussian function along the y-axis
        amp : float
            amplitude of the Gaussian function
        background : float
            background signal in the matrix to be fit
        Returns
        ----------
        array_like
            Gaussian function evaluated with the given parameters
        

	"""
	X, Y = XY
	fit = amp*np.exp(-((X-x0)**2/(2*sigmax**2) + (Y-y0)**2/(2*sigmay**2)))+ background
	
	return fit.ravel()


def getFitParam(im):
	"""Get the amplitude, x-coordinate, y-coordinate, sigma in x,
	sigma in y and background  of the Gaussian function based on 
	non-linear least squares fitting

        Parameters
        ----------
        im : ndarray
            matrix to fit the Gaussian function and estimate the fit parameters for
        
        Returns
        ----------
        ndarray
            array of two-dimensional Gaussian fit parameters


	"""
	x = np.linspace(0, im.shape[1], im.shape[1])
	y = np.linspace(0, im.shape[0], im.shape[0])
	X, Y = np.meshgrid(x, y)

	#curve_fit requires an independent variable with dimensions (2, M)
	#and dependent data with dimensions (1, M)
	XY = np.vstack((X.ravel(), Y.ravel()))
	init_guess = (im.shape[1]/2, im.shape[0]/2, 2, 2, 500, 0)

	param_opt, param_cov = opt.curve_fit(gaussian2DFit, XY, im.ravel(), p0 = init_guess)

	return param_opt
