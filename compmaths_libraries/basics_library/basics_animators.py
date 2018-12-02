# import custom JS animator
from compmaths_libraries.JSAnimation_slider_only import IPython_display_slider_only

# import standard plotting and animation
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import clear_output
import time
from matplotlib import gridspec

# import autograd functionality
import numpy as np
import math

# animator for recursive function
def recursive_animator(f,n,**kwargs):
    plot_type = 'continuous'
    if 'plot_type' in kwargs:
        plot_type = kwargs['plot_type']
        
    x = np.linspace(-3,3,500)
    if 'x' in kwargs:
        x = kwargs['x']
        
    notation = 'supscript'
    if 'notation' in kwargs:
        notation = kwargs['notation']
    
    # initialize figure
    fig = plt.figure(figsize = (16,8))
    artist = fig
    
    # create subplot with 3 panels, plot input function in center plot
    gs = gridspec.GridSpec(1, 3, width_ratios=[1,2, 1]) 
    ax1 = plt.subplot(gs[0]); ax1.axis('off');
    ax3 = plt.subplot(gs[2]); ax3.axis('off');
    
    # plot input function
    ax = plt.subplot(gs[1])
    
    # define x and y viewing limits
    f_evals = f(x,1)
    fmax = max(f_evals)
    fmin = min(f_evals)
    fgap = (fmax - fmin)*0.25
    fmax+=fgap
    fmin-=fgap

    # animate
    def animate(k):
        # clear the panel
        ax.cla()
        
        # print rendering update
        if np.mod(k+1,25) == 0:
            print ('rendering animation frame ' + str(k+1) + ' of ' + str(n))
        if k == n - 1:
            print ('animation rendering complete!')
            time.sleep(1.5)
            clear_output()
            
        # compute 
        f_evals = f(x,k+1)
            
        # draw
        label = '$f^{(' + str(k+1) + ')}(x)$'
        if notation == 'subscript':
            label = '$f_{' + str(k+1) + '}(x)$'
   
        color = np.random.rand(3,1).tolist()
        color = [c[0] for c in color]
        ax.plot(x, f_evals, color =color, linewidth=4,zorder = 3,label = label)
        ax.plot(x, f_evals, color ='k', linewidth=6,zorder = 2)
        
        # plot x and y axes, and clean up
        plt.grid(True, which='both')
        plt.axhline(y=0, color='k', linewidth=1)
        plt.axvline(x=0, color='k', linewidth=1)
    
        # set limits and legend
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), shadow=True,fontsize = 25)
        
        # return artist to render
        ax.set_xlim([min(x),max(x)])
        ax.set_ylim([fmin,fmax])
                
        return artist,
        
    anim = animation.FuncAnimation(fig, animate,frames=n, interval=n, blit=True)
        
    return(anim)
        