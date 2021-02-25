import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import cm

def plot_fit_projections_3D(im, ax):
    """Plots a surface based on input data as well as projections of the data along the x- and y-axis
    
    Parameters
    ----------
    im : iterable object
        Gaussian function evaulated with the given parameters
    ax : axes 3D subplot object
        axes to plot the surface in 
        
    """
    X, Y = np.meshgrid(np.linspace(0, im.shape[0], im.shape[0]), np.linspace(0, im.shape[1], im.shape[1]))
    p = ax.plot_surface(X, Y, im, rstride=1, cstride=1, cmap=cm.viridis, linewidth=0, antialiased=False)
    fig.colorbar(p, shrink=0.5, orientation='horizontal')

    cset = ax.contour(X, Y, im, zdir='x', offset=-1, cmap=cm.viridis)
    cset = ax.contour(X, Y, im, zdir='y', offset=im.shape[0]+1, cmap=cm.viridis)
    ax.set_zlim(top=im.max())
    
    
