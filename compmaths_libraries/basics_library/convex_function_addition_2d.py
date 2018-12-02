# import custom JS animator
from compmaths_libraries.JSAnimation_slider_only import IPython_display_slider_only

# import standard plotting and animation
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# import autograd functionality
from autograd import grad as compute_grad   # The only autograd function you may ever need
import autograd.numpy as np
import math
from IPython.display import clear_output
import time

class visualizer:
    '''
    This file illlustrates the convex sum of two functions in 2d.  Both functions are defined by the user.
    ''' 

    # animate the method
    def draw_it(self,**args):
        # user input functions to add
        self.g1 = args['g1']                            # input function
        self.g2 = args['g2']
        # input function
        num_frames = 100
        if 'num_frames' in args:
            num_frames = args['num_frames']
        min_range = -3
        if 'min_range' in args:
            min_range = args['min_range']
        max_range = -3
        if 'max_range' in args:
            max_range = args['max_range']
        if 'mode' in args:
            mode = args['mode']
        else:
            mode = 'convex_combo'
            
        if 'alpha_range' in args:
            alpha_range = args['alpha_range']
        else:
            alpha_range = [0,1]
           
            
        if 'title1' in args:
            title1 = args['title1']
        else:
            title1 = '$g_1$'
        if 'title2' in args:
            title2 = args['title2']
        else:
            title2 = '$g_2$'
        if 'title3' in args:
            title3 = args['title3']
        else:
            title3 = '$(1 - \\alpha)\,g_1 + \\alpha\,g_2$'    
            
      
        # initialize figure
        fig = plt.figure(figsize = (15,5))
        artist = fig
        ax1 = fig.add_subplot(131)
        ax2 = fig.add_subplot(132)
        ax3 = fig.add_subplot(133)

        # generate base function for plotting on each slide
        w_plot = np.linspace(min_range,max_range,200)
        g1_plot = self.g1(w_plot)
        g2_plot = self.g2(w_plot)
        
        # set vertical limit markers
        g1_min = np.amin(g1_plot)
        g2_min = np.amin(g2_plot)
        g1_max = np.amax(g1_plot)
        g2_max = np.amax(g2_plot)
        g1_gap = 0.2*(g1_max - g1_min)
        g2_gap = 0.2*(g2_max - g2_min)
        
        g1_min = np.amin(g1_plot) - g1_gap
        g2_min = np.amin(g2_plot) - g2_gap
        g1_max = np.amax(g1_plot) + g1_gap
        g2_max = np.amax(g2_plot) + g2_gap
       
        # decide on number of slides
        alpha_vals = np.linspace(alpha_range[0], alpha_range[1], num_frames)
        print ('starting animation rendering...')

        # animation sub-function
        def animate(k):
            # clear panels for next slide
            ax1.cla()
            ax2.cla()
            ax3.cla()
            
            # print rendering update
            if np.mod(k+1,25) == 0:
                print ('rendering animation frame ' + str(k+1) + ' of ' + str(num_frames))
            if k == num_frames - 1:
                print ('animation rendering complete!')
                time.sleep(1.5)
                clear_output()
                                                
            # plot function 1
            ax1.plot(w_plot,g1_plot,color = 'k',zorder = 1)                           
            ax1.set_title(title1,fontsize = 22)

            # plot function 2
            ax2.plot(w_plot,g2_plot,color = 'k',zorder = 1)                
            ax2.set_title(title2,fontsize = 22)

            # plot combination of both
            alpha = alpha_vals[k]
            
            if mode == 'regularization': 
                g_combo = g1_plot + alpha*g2_plot
            else:
                g_combo = (1-alpha)*g1_plot + alpha*g2_plot
            
            ax3.plot(w_plot,g_combo,color = 'k',zorder = 1) 
            ax3.set_title(title3,fontsize = 22)
            
            # set vertical limits
            ax1.set_ylim([g1_min,g1_max])
            ax2.set_ylim([g2_min,g2_max])
            
            # set vertical limit markers
            gmin = np.amin(g_combo)
            gmax = np.amax(g_combo)
            g_gap = 0.2*(gmax - gmin)
            gmin = gmin - g_gap
            gmax = gmax + g_gap
            ax3.set_ylim([gmin,gmax])
        
            return artist,

        anim = animation.FuncAnimation(fig, animate ,frames=num_frames, interval=num_frames, blit=True)

        return(anim)