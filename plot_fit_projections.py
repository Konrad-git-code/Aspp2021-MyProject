import matplotlib.pyplot as plt

def plot_fit_projections(im, ax, ax_plotx, ax_ploty):
    """Plots an image and its projects along the x- and y-axis
    
    Parameters
    ----------
    im : iterable object
        image to plot
    ax : axes object
        axes to plot the image in
    ax_plotx : axes object
        axes for the x-axis projection
    ax_ploty : axes object
        axes for the y-axis projection
    
    """
    # remove axis labels
    ax_plotx.tick_params(axis="x", labelbottom=False)
    ax_ploty.tick_params(axis="y", labelleft=False)

    # plot the image
    ax.imshow(im)
    
    #plot projections of the Gaussian fit along the x and y axes
    ax_plotx.plot(im.sum(axis=0)/im.shape[0])
    ax_ploty.plot(im.sum(axis=1)/im.shape[1], np.arange(0, im.shape[0]))
    
