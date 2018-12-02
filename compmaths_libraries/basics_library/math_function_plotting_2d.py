# import standard plotting and animation
import matplotlib.pyplot as plt
from matplotlib import gridspec

# import autograd functionality
from autograd import grad as compute_grad   # The only autograd function you may ever need
import autograd.numpy as np

class visualizer:
    '''
    A simple 2-dimensional function plotter with custom settings.
    '''

    # compute first order approximation
    def draw_it(self,**args):  
        # get user defined function
        self.g = args['function']                      # user-defined input function
        
        ### other options
        # size of figure
        set_figsize = 7
        if 'set_figsize' in args:
            set_figsize = args['set_figsize']
            
        # turn axis on or off
        set_axis = 'on'
        if 'set_axis' in args:
            set_axis = args['set_axis']
            
        # plot title
        set_title = ''
        if 'set_title' in args:
            set_title = args['set_title']
            
        # horizontal and vertical axis labels
        horiz_label = ''
        if 'horiz_label' in args:
            horiz_label = args['horiz_label']
            
        vert_label = ''
        if 'vert_label' in args:
            vert_label = args['vert_label']
            
        # set width of plot
        input_range = np.linspace(-3,3,200)                  # input range for original function
        if 'input_range' in args:
            input_range = args['input_range']
        
        # initialize figure
        fig = plt.figure(figsize = (12,5))

        # create subplot with 3 panels, plot input function in center plot
        gs = gridspec.GridSpec(1, 3, width_ratios=[1,2, 1]) 
        ax1 = plt.subplot(gs[0]); ax1.axis('off');
        ax3 = plt.subplot(gs[2]); ax3.axis('off');

        # create panel for input function
        ax2 = plt.subplot(gs[1])

        # generate a range of values over which to plot input function, and derivatives
        g_plot = self.g(input_range)
        g_range = max(g_plot) - min(g_plot)             # used for cleaning up final plot
        ggap = g_range*0.5
        ax2.plot(input_range,g_plot,color = 'k',zorder = 0)                           # plot function

        # clean up plotting area
        ax2.axis(set_axis)
        ax2.set_title(set_title,fontsize = 15)
        ax2.set_xlabel(horiz_label,fontsize = 15)
        ax2.set_ylabel(vert_label,fontsize = 15)
        plt.show()