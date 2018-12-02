# import custom JS animator
from compmaths_libraries.JSAnimation_slider_only import IPython_display_slider_only

# import standard plotting and animation
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# import autograd functionality
from autograd import grad as compute_grad   # The only autograd function you may ever need
import autograd.numpy as np
from mpl_toolkits.mplot3d import Axes3D

# import autograd functionality
from autograd import grad as compute_grad   # The only autograd function you may ever need
import autograd.numpy as np
import math
from matplotlib import gridspec
from IPython.display import clear_output
import time

class visualizer:
    '''
    This file illlustrates the convex sum of two functions in 3d.  Both functions are defined by the user.
    ''' 

    # animate the method
    def draw_it(self,**kwargs):
        # user input functions to add
        self.g1 = kwargs['g1']                            # input function
        self.g2 = kwargs['g2']                            # input function
        num_frames = 100
        if 'num_frames' in kwargs:
            num_frames = kwargs['num_frames']
            
        # turn axis on or off
        set_axis = 'on'
        if 'set_axis' in kwargs:
            set_axis = kwargs['set_axis']
  
        # set viewing angle on plot
        view = [20,50]
        if 'view' in kwargs:
            view = kwargs['view']
            
        # initialize figure
        fig = plt.figure(figsize = (15,5))
        artist = fig
        
        gs = gridspec.GridSpec(1, 3, width_ratios=[1,1, 1]) 
        ax1 = plt.subplot(gs[0],projection='3d');
        ax2 = plt.subplot(gs[1],projection='3d');
        ax3 = plt.subplot(gs[2],projection='3d');
        
        # generate input range for functions
        r = np.linspace(-3,3,100)
        w1_vals,w2_vals = np.meshgrid(r,r)
        w1_vals.shape = (len(r)**2,1)
        w2_vals.shape = (len(r)**2,1)
        g1_vals = self.g1([w1_vals,w2_vals])
        g2_vals = self.g2([w1_vals,w2_vals])
        
        # vals for cost surface
        w1_vals.shape = (len(r),len(r))
        w2_vals.shape = (len(r),len(r))
        g1_vals.shape = (len(r),len(r))
        g2_vals.shape = (len(r),len(r))

        # decide on number of slides
        alpha_vals = np.linspace(1,0,num_frames)

        # animation sub-function
        print ('starting animation rendering...')
        def animate(t):
            # clear panels for next slide
            ax1.cla()
            ax2.cla()
            ax3.cla()
            
            # print rendering update
            if np.mod(t+1,25) == 0:
                print ('rendering animation frame ' + str(t+1) + ' of ' + str(num_frames))
            if t == num_frames - 1:
                print ('animation rendering complete!')
                time.sleep(1.5)
                clear_output()
              
            # plot function 1
            ax1.plot_surface(w1_vals,w2_vals,g1_vals,alpha = 0.1,color = 'w',rstride=10, cstride=10,linewidth=2,edgecolor = 'k') 
            ax1.set_title("$g_1$",fontsize = 15)
            ax1.view_init(view[0],view[1])
            ax1.axis(set_axis)

            # plot function 2
            ax2.plot_surface(w1_vals,w2_vals,g2_vals,alpha = 0.1,color = 'w',rstride=10, cstride=10,linewidth=2,edgecolor = 'k') 
            ax2.set_title("$g_2$",fontsize = 15)
            ax2.view_init(view[0],view[1])
            ax2.axis(set_axis)
            
            # plot combination of both
            alpha = alpha_vals[t]
            g_combo = alpha*g1_vals + (1 - alpha)*g2_vals
            ax3.plot_surface(w1_vals,w2_vals,g_combo,alpha = 0.1,color = 'k',rstride=10, cstride=10,linewidth=2,edgecolor = 'k')             
            ax3.set_title('$\\alpha\,g_1 + (1 - \\alpha)\,g_2$',fontsize = 15)
            ax3.view_init(view[0],view[1])
            ax3.axis(set_axis)
            
            return artist,

        anim = animation.FuncAnimation(fig, animate ,frames=num_frames, interval=num_frames, blit=True)

        return(anim)