# import custom JS animator
from compmaths_libraries.JSAnimation_slider_only import IPython_display_slider_only

# import standard plotting and animation
import matplotlib.pyplot as plt
from matplotlib import gridspec
import matplotlib.animation as animation
import math
import numpy as np
from IPython.display import clear_output
import time

# animate the method
def sin_cos(**kwargs):
    # set number of frames for animation
    num_frames = 300                          # number of slides to create - the input range [-3,3] is divided evenly by this number
    if 'num_frames' in kwargs:
        num_frames = kwargs['num_frames']

    # initialize figure
    fig = plt.figure(figsize = (16,8))
    artist = fig

    # create subplot with 3 panels, plot input function in center plot
    gs = gridspec.GridSpec(1, 2, width_ratios=[1,1],wspace=0.3, hspace=0.05) 
    ax1 = plt.subplot(gs[0]);
    ax2 = plt.subplot(gs[1]); 

    # create dataset for unit circle
    v = np.linspace(0,2*np.pi,100)
    s = np.sin(v)
    s.shape = (len(s),1)
    t = np.cos(v)
    t.shape = (len(t),1)
    
    # create span of angles to plot over
    v = np.linspace(0,4*np.pi,num_frames)
    y = 0.87*np.sin(v)
    x = 0.87*np.cos(v)
    
    # create linspace for sine/cosine plots
    w = np.linspace(0,4*np.pi,300)
    
    # define colors for sine / cosine
    colors = ['salmon','cornflowerblue']
    
    # print update
    print ('starting animation rendering...')
    
    # animation sub-function
    def animate(k):
        # clear panels for next slide
        ax1.cla()
        ax2.cla()
        
        # print rendering update
        if np.mod(k+1,25) == 0:
            print ('rendering animation frame ' + str(k+1) + ' of ' + str(num_frames))
        if k == num_frames - 1:
            print ('animation rendering complete!')
            time.sleep(1.5)
            clear_output()
        
        ### setup left panel ###
        # plot circle with lines in left panel
        ax1.plot(s,t,color = 'k',linewidth = 3)
        
        # plot arrow
        ax1.arrow(0, 0, x[k], y[k], head_width=0.1, head_length=0.1, fc='k', ec='k',linewidth=3,zorder = 3)

        # plot width 
        ax1.plot([np.cos(v[k]),np.cos(v[k])],[0,np.sin(v[k])],color = colors[0],linewidth = 3,linestyle = '--')
       
        # plot height 
        ax1.plot([0,np.cos(v[k])],[np.sin(v[k]),np.sin(v[k])],color = colors[1],linewidth = 3,linestyle = '--')
    
        # clean up panel
        ax1.grid(True, which='both')
        ax1.axhline(y=0, color='k')
        ax1.axvline(x=0, color='k')
        
        ### setup right panel ###
        # determine closest value in space of sine/cosine input
        current_angle = v[k]
        ind = np.argmin(np.abs(w - current_angle))
        p = w[:ind+1]
        
        # plot sine wave so far
        ax2.plot(p,np.sin(p),color = colors[0],linewidth=4,zorder = 3)
        ax2.plot(p,np.cos(p),color = colors[1],linewidth=4,zorder = 3)
        
        # cleanup plot
        ax2.grid(True, which='both')
        ax2.axhline(y=0, color='k')
        ax2.axvline(x=0, color='k')   
        ax2.set_xlim([-0.1,4*np.pi + 0.1])
        ax2.set_ylim([-1.1,1.1])
        
        # add legend
        ax2.legend(['cos$(x)$','sin$(x)$'],loc='center left', bbox_to_anchor=(0.13, 1.05),fontsize=18,ncol=2)

        return artist,

    anim = animation.FuncAnimation(fig, animate ,frames=num_frames, interval=num_frames, blit=True)

    return(anim)


# animate the method
def sinh_cosh(**kwargs):
    # set number of frames for animation
    num_frames = 300                          # number of slides to create - the input range [-3,3] is divided evenly by this number
    if 'num_frames' in kwargs:
        num_frames = kwargs['num_frames']

    # initialize figure
    fig = plt.figure(figsize = (16,8))
    artist = fig

    # create subplot with 3 panels, plot input function in center plot
    gs = gridspec.GridSpec(1, 2, width_ratios=[1,1],wspace=0.3, hspace=0.05) 
    ax1 = plt.subplot(gs[0]);
    ax2 = plt.subplot(gs[1]); 

    # create dataset for unit hyperbola
    lim = 2
    limgap = 0.2
    v = np.linspace(-lim,lim,100)
    s = np.sinh(v)
    s.shape = (len(s),1)
    t = np.cosh(v)
    t.shape = (len(t),1)
    
    # create span of angles to plot over
    v = np.linspace(-lim,lim,num_frames)
    y = np.sinh(v)
    x = np.cosh(v)
    
    # create linspace for sine/cosine plots
    w = np.linspace(-lim,lim,300)
    
    # define colors for sine / cosine
    colors = ['salmon','cornflowerblue']
    
    # print update
    print ('starting animation rendering...')
    
    # animation sub-function
    def animate(k):
        # clear panels for next slide
        ax1.cla()
        ax2.cla()
        
        # print rendering update
        if np.mod(k+1,25) == 0:
            print ('rendering animation frame ' + str(k+1) + ' of ' + str(num_frames))
        if k == num_frames - 1:
            print ('animation rendering complete!')
            time.sleep(1.5)
            clear_output()
        
        ### setup left panel ###
        # plot circle with lines in left panel
        ax1.plot(t,s,color = 'k',linewidth = 3)
        ax1.plot(-t,s,color = 'k',linewidth = 3)

        # plot arrow
        head_length = 0.3
        scale = float(math.sqrt(x[k]**2 + y[k]**2) - head_length-0.1) / float(math.sqrt(x[k]**2 + y[k]**2))

        ax1.arrow(0, 0, scale*x[k], scale*y[k], head_width=0.25, head_length=head_length, fc='k', ec='k',linewidth=3,zorder = 3)

        # plot width 
        ax1.plot([np.cosh(v[k]),np.cosh(v[k])],[0,np.sinh(v[k])],color = colors[1],linewidth = 3,linestyle = '--')
       
        # plot height 
        ax1.plot([0,np.cosh(v[k])],[np.sinh(v[k]),np.sinh(v[k])],color = colors[0],linewidth = 3,linestyle = '--')
    
        # clean up panel
        ax1.grid(True, which='both')
        ax1.axhline(y=0, color='k')
        ax1.axvline(x=0, color='k')
        ax1.set_xlim([np.sinh(-lim)-limgap,np.sinh(lim)+limgap])

        
        ### setup right panel ###
        # determine closest value in space of sine/cosine input
        current_angle = v[k]
        ind = np.argmin(np.abs(w - current_angle))
        p = w[:ind+1]
        
        # plot sine wave so far
        ax2.plot(p,np.cosh(p),color = colors[0],linewidth=4,zorder = 3)
        ax2.plot(p,np.sinh(p),color = colors[1],linewidth=4,zorder = 3)
        
        # cleanup plot
        ax2.grid(True, which='both')
        ax2.axhline(y=0, color='k')
        ax2.axvline(x=0, color='k')   
        ax2.set_xlim([-lim-limgap,lim+limgap])
        #ax2.set_ylim([-1.1,1.1])
        
        # add legend
        ax2.legend(['cosh$(x)$','sinh$(x)$'],loc='center left', bbox_to_anchor=(0.13, 1.05),fontsize=18,ncol=2)

        return artist,

    anim = animation.FuncAnimation(fig, animate ,frames=num_frames, interval=num_frames, blit=True)

    return(anim)
