import matplotlib.pyplot as plt

def plot_fit_projections(im, ax, ax_plotx, ax_ploty):
    """Plots an image and its projections along the x- and y-axis
    
    Parameters
    ----------
    im : ndarray
        image to plot
    ax : `~matplotlib.axes.Axes`
        axes to plot the image in
    ax_plotx : `~matplotlib.axes.Axes`
        axes for the x-axis projection
    ax_ploty : `~matplotlib.axes.Axes`
        axes for the y-axis projection
    
    """
    # remove axis labels
    ax_plotx.tick_params(axis="x", labelbottom=False)
    ax_ploty.tick_params(axis="y", labelleft=False)

    # plot the image
    ax.imshow(im)
    
    # plot projections of the Gaussian fit along the x and y axes
    ax_plotx.plot(im.sum(axis=0)/im.shape[0])
    ax_ploty.plot(im.sum(axis=1)/im.shape[1], np.arange(0, im.shape[0]))
    
