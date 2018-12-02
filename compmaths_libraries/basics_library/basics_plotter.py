import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import gridspec
from IPython.display import display, HTML
import copy

# custom plot for spiffing up plot of a single mathematical function
def single_plot(table,**kwargs):
    xlabel = '$w_1$'
    ylabel = '$w_2$'
    zlabel = '$g(w_1,w_2)$'
    plot_type = 'continuous'
    fontsize = 15
    guides = 'off'
    rotate_ylabel = 90
    label_fontsize = 15
    if 'xlabel' in kwargs:
        xlabel = kwargs['xlabel']
    if 'ylabel' in kwargs:
        ylabel = kwargs['ylabel']
    if 'zlabel' in kwargs:
        zlabel = kwargs['zlabel']
    if 'fontsize' in kwargs:
        fontsize = kwargs['fontsize']
        
    if 'plot_type' in kwargs:
        plot_type = kwargs['plot_type']
    if 'rotate_ylabel' in kwargs:
        rotate_ylabel = kwargs['rotate_ylabel']   
    if 'label_fontsize' in kwargs:
        label_fontsize = kwargs['label_fontsize']
    if 'guides' in kwargs:
        guides = kwargs['guides']       
       
    # is the function 2-d or 3-d?
    dim = np.shape(table)[1]
    
    # single two dimensonal plot
    if dim == 2:
        fig = plt.figure(figsize = (7,3))

        # create subplot with 3 panels, plot input function in center plot
        gs = gridspec.GridSpec(1, 3, width_ratios=[1,3, 1]) 
        fig.subplots_adjust(bottom = 0.25)

        ax1 = plt.subplot(gs[0]); ax1.axis('off');
        ax3 = plt.subplot(gs[2]); ax3.axis('off');

        # plot input function
        ax2 = plt.subplot(gs[1])
        
        # choose plot type
        if plot_type == 'continuous':
            ax2.plot(table[:,0], table[:,1], c='k', linewidth=2,zorder = 3)
        if plot_type == 'scatter':
            ax2.scatter(table[:,0], table[:,1], c='r', s=50,edgecolor='k',linewidth=1)
            
            # if the guides are turned on, plot them
            if guides == 'on':
                ax2.plot(table[:,0], table[:,1], c='r', linewidth=2,zorder = 2,alpha = 0.25)

        # plot x and y axes, and clean up
        ax2.grid(True, which='both')
        ax2.axhline(y=0, color='k', linewidth=1)
        ax2.axvline(x=0, color='k', linewidth=1)
        
        # set viewing limits
        w = table[:,0]
        wrange = max(w) - min(w)
        wgap = wrange*0.15
        wmax = max(w) + wgap
        wmin = min(w) - wgap
        ax2.set_xlim([wmin,wmax])
        
        g = table[:,1]
        grange = max(g) - min(g)
        ggap = grange*0.25
        gmax = max(g) + ggap
        gmin = min(g) - ggap
        ax2.set_ylim([gmin,gmax])

        ax2.set_xlabel(xlabel,fontsize = label_fontsize)
        ax2.set_ylabel(ylabel,fontsize = label_fontsize,rotation = rotate_ylabel,labelpad = 20)
        plt.show()
    
    # single 3-d function plot
    if dim == 3:    
        # plot the line
        fig = plt.figure(figsize = (15,6))

        # create subplot with 3 panels, plot input function in center plot
        gs = gridspec.GridSpec(1, 3, width_ratios=[1,2, 1]) 
        ax1 = plt.subplot(gs[0]); ax1.axis('off');
        ax3 = plt.subplot(gs[2]); ax3.axis('off');

        # plot input function
        ax2 = plt.subplot(gs[1],projection='3d')
        ax2.plot_surface(table[:,0], table[:,1], table[:,2], alpha = 0.3,color = 'r',rstride=10, cstride=10,linewidth=2,edgecolor = 'k')

        # plot x and y axes, and clean up
        ax2.set_xlabel(xlabel,fontsize = fontsize)
        ax2.set_ylabel(ylabel,fontsize = fontsize,rotation = 0)
        ax2.set_zlabel(zlabel,fontsize = fontsize)

        # clean up plot and set viewing angle
        ax2.view_init(10,30)
        plt.show()
        
# custom plot for spiffing up plot of a two mathematical functions
def double_plot(table1,table2,**kwargs): 
    # get labeling arguments
    xlabel = '$w_1$'
    ylabel_1 = '$g$'
    ylabel_2 = '$g$'
    fontsize = 15
    if 'xlabel' in kwargs:
        xlabel = kwargs['xlabel']
    if 'ylabel_1' in kwargs:
        ylabel_1 = kwargs['ylabel_1']
    if 'ylabel_2' in kwargs:
        ylabel_2 = kwargs['ylabel_2']
    if 'fontsize' in kwargs:
        fontsize = kwargs['fontsize']
        
    # plot the functions 
    fig = plt.figure(figsize = (12,4))
    gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1]) 
    ax1 = plt.subplot(gs[0]); 
    ax2 = plt.subplot(gs[1]); 
    plot_type = 'continuous'
    if 'plot_type' in kwargs:
        plot_type = kwargs['plot_type']
    if plot_type == 'scatter':
        ax1.scatter(table1[:,0], table1[:,1], c='r', s=20,zorder = 3)
        ax2.scatter(table2[:,0], table2[:,1], c='r', s=20,zorder = 3)
    if plot_type == 'continuous':
        ax1.plot(table1[:,0], table1[:,1], c='r', linewidth=2,zorder = 3)
        ax2.plot(table2[:,0], table2[:,1], c='r', linewidth=2,zorder = 3)

    # plot x and y axes, and clean up
    ax1.set_xlabel(xlabel,fontsize = fontsize)
    ax1.set_title(ylabel_1,fontsize = fontsize+3,y=1.04)
    ax2.set_xlabel(xlabel,fontsize = fontsize)
    ax2.set_title(ylabel_2,fontsize = fontsize+3,y=1.04)
    
    ax1.grid(True, which='both'), ax2.grid(True, which='both')
    ax1.axhline(y=0, color='k', linewidth=1), ax2.axhline(y=0, color='k', linewidth=1)
    ax2.axvline(x=0, color='k', linewidth=1), ax2.axvline(x=0, color='k', linewidth=1)
    plt.show()
    
    
# custom plot for spiffing up plot of a two mathematical functions
def triple_plot(**kwargs): 
    # get labeling arguments
    xlabel = '$x$'
    ylabel = []
    if 'ylabel' in kwargs:
        ylabel = kwargs['ylabel']
    func_in = kwargs['func_in']
    f1 = kwargs['f1']
    f2 = kwargs['f2']
    f3 = kwargs['f3']
    title1 = kwargs['title1']
    title2 = kwargs['title2']
    title3 = kwargs['title3']
    axes = False
    if 'axes' in kwargs:
        axes = kwargs['axes']
    
    # plot the functions 
    fig = plt.figure(figsize = (15,4))
    plt.style.use('ggplot')
    ax1 = fig.add_subplot(131); ax2 = fig.add_subplot(132); ax3 = fig.add_subplot(133);
    
    # plot
    ax1.plot(func_in, f1, c='r', linewidth=2,zorder = 3)
    ax2.plot(func_in, f2, c='r', linewidth=2,zorder = 3)
    ax3.plot(func_in, f3, c='r', linewidth=2,zorder = 3)

    # plot x and y axes, and clean up
    ax1.set_xlabel(xlabel,fontsize = 14)
    ax2.set_xlabel(xlabel,fontsize = 14)
    ax3.set_xlabel(xlabel,fontsize = 14)
 
    # plot x and y axes, and clean up
    ax1.set_title(title1,fontsize = 14)
    ax2.set_title(title2,fontsize = 14)
    ax3.set_title(title3,fontsize = 14)
    
    # clean up plots
    ax1.grid(True, which='both'), ax2.grid(True, which='both'),  ax3.grid(True, which='both')
    
    if axes == True:
        ax1.axhline(y=0, color='k', linewidth=1), ax2.axhline(y=0, color='k', linewidth=1), ax3.axhline(y=0, color='k', linewidth=1)
        ax1.axvline(x=0, color='k', linewidth=1), ax2.axvline(x=0, color='k', linewidth=1), ax3.axvline(x=0, color='k', linewidth=1)

    plt.show()
    

# custom plot for spiffing up plot of a two mathematical functions
def triple_plot_in_two(**kwargs): 
    # get labeling arguments
    xlabel = '$x$'
    ylabel = []
    if 'ylabel' in kwargs:
        ylabel = kwargs['ylabel']
    func_in = kwargs['func_in']
    f1 = kwargs['f1']
    f2 = kwargs['f2']
    f3 = kwargs['f3']
    f4 = kwargs['f4']
    legend1 = kwargs['legend1']
    legend2 = kwargs['legend2']
    axes = False
    if 'axes' in kwargs:
        axes = kwargs['axes']
    
    # plot the functions 
    fig = plt.figure(figsize = (15,4))
    plt.style.use('ggplot')
    ax1 = fig.add_subplot(121); ax2 = fig.add_subplot(122);
    
    # plot
    ax1.plot(func_in, f1, c='r', linewidth=2, zorder = 3)
    ax1.plot(func_in, f2, c='b', linewidth=2, zorder = 3)
    ax2.plot(func_in, f3, c='r', linewidth=2, zorder = 3)
    ax2.plot(func_in, f4, c='g', linewidth=2, zorder = 3)

    # plot x and y axes, and clean up
    ax1.set_xlabel(xlabel,fontsize = 14)
    ax2.set_xlabel(xlabel,fontsize = 14)
   
    
    # clean up plots
    ax1.grid(True, which='both'), ax2.grid(True, which='both')
    
    if axes == True:
        ax1.axhline(y=0, color='k', linewidth=1), ax2.axhline(y=0, color='k', linewidth=1)
        ax1.axvline(x=0, color='k', linewidth=1), ax2.axvline(x=0, color='k', linewidth=1)
        
    # add legend
    ax1.legend(legend1,loc='center left', bbox_to_anchor=(0.13, 1.15),fontsize=18,ncol=2)
    ax2.legend(legend2,loc='center left', bbox_to_anchor=(0.13, 1.15),fontsize=18,ncol=2)
    
    plt.show()      
    
# plot pandas to html table centered in notebook
def table_plot(table):
    # display table mcdonalds revenue values
    display(HTML('<center>' + table.to_html(index=False) + '</center>'))
    
# custom plot for spiffing up plot of a two mathematical functions
def step_plot(table1,table2,**kwargs): 
    # get labeling arguments
    xlabel = '$w_1$'
    ylabel_1 = '$g$'
    ylabel_2 = '$g$'
    table_3 = []
    fontsize = 15
    if 'xlabel' in kwargs:
        xlabel = kwargs['xlabel']
    if 'ylabel_1' in kwargs:
        ylabel_1 = kwargs['ylabel_1']
    if 'ylabel_2' in kwargs:
        ylabel_2 = kwargs['ylabel_2']
    if 'fontsize' in kwargs:
        fontsize = kwargs['fontsize']
    if 'table_3' in kwargs:
        table_3 = kwargs['table_3']
        
    # plot the functions 
    fig = plt.figure(figsize = (15,4))
    plt.style.use('ggplot')
    ax1 = fig.add_subplot(121); ax2 = fig.add_subplot(122); 
    
    # plot step function with continuous guider in left panel 
    ax2.plot(table1[:,0], table1[:,1], c='r', linewidth=2,zorder = 3)
    
    # plot step function in true discontinuous fashion on the right
    v = table2[:,1]
    b = np.unique(v)
    for unique_val in b:
        quant2 = copy.deepcopy(v)
        ind = np.argwhere(quant2 != unique_val)
        ind = [a[0] for a in ind]
        for a in ind:
            quant2[a] = np.nan
        ax1.plot(table2[:,0], quant2, c='r', linewidth=2,zorder = 3)
    
    # if original function given, plot that too
    if np.size(table_3) > 0:
        ax1.plot(table_3[:,0], table_3[:,1], c='b', linewidth=2,zorder = 2)
        ax2.plot(table_3[:,0], table_3[:,1], c='b', linewidth=2,zorder = 2)

    # plot x and y axes, and clean up
    ax1.set_xlabel(xlabel,fontsize = fontsize)
    ax1.set_ylabel(ylabel_1,fontsize = fontsize,rotation = 0,labelpad = 20)
    ax2.set_xlabel(xlabel,fontsize = fontsize)
    ax2.set_ylabel(ylabel_2,fontsize = fontsize,rotation = 0,labelpad = 20)
    
    ax1.grid(True, which='both'), ax2.grid(True, which='both')
    ax1.axhline(y=0, color='k', linewidth=1), ax2.axhline(y=0, color='k', linewidth=1)
    ax1.axvline(x=0, color='k', linewidth=1), ax2.axvline(x=0, color='k', linewidth=1)
    plt.show()
    
# 3d poly plotter
def general_3d_plotter(func):
    # generate input values
    s = np.linspace(-2,2,100)
    x_1,x_2 = np.meshgrid(s,s)
    x_1.shape = (100**2,1)
    x_2.shape = (100**2,1)
    x = np.concatenate((x_1,x_2),axis=1)
    f = func(x)
    print (np.shape(x))
    print (np.shape(f))
    # reshape for plotting
    x_1.shape = (100,100)
    x_2.shape = (100,100)
    f.shape = (100,100)

    # build 4 polynomial basis elements
    fig = plt.figure(num=None, figsize = (16,5), dpi=80, facecolor='w', edgecolor='k')
    ax1 = plt.subplot(1,1,1,projection = '3d')
    ax1.plot_surface(x_1,x_2,f,alpha = 0.1,color = 'b',zorder = 0,shade = True,linewidth=0.5,antialiased = True,cstride = 20, rstride = 15)
        
    # clean up plot
    ax1.view_init(10,20)    
    ax1.set_title('$f$',fontsize = 18)
    ax1.set_xlabel('$x_1$',fontsize = 15)
    ax1.set_ylabel('$x_2$',fontsize = 15)

    fig.subplots_adjust(left=0,right=1,bottom=0,top=1)   # remove whitespace around 3d figure

    plt.show()
    
    
# 3d poly plotter
def poly_3d_plotter():
    # generate input values
    s = np.linspace(-2,2,100)
    x_1,x_2 = np.meshgrid(s,s)
    degree_dict = {}

    # build 4 polynomial basis elements
    fig = plt.figure(num=None, figsize = (16,5), dpi=80, facecolor='w', edgecolor='k')

    ### plot regression surface ###
    p =  [0,1,1,2]
    q = [1,2,1,3]
    for m in range(4):
        ax1 = plt.subplot(1,4,m+1,projection = '3d')
        f_m = (x_1**p[m])*(x_2**q[m])
        ax1.plot_surface(x_1,x_2,f_m,alpha = 0.1,color = 'b',zorder = 0,shade = True,linewidth=0.5,antialiased = True,cstride = 20, rstride = 15)
        ax1.view_init(10,20)  
        deg1 = ''
        if p[m] == 1:
            deg1 = 'x_1^{\,}'
        if p[m] >=2:
            deg1 = 'x_1^' + str(p[m])
        deg2 = ''
        if q[m] == 1:
            deg2 = 'x_2^{\,}'
        if q[m] >=2:
            deg2 = 'x_2^' + str(q[m])
        ax1.set_title('$f_'+str(m+1) + ' = ' + deg1 + deg2 + '$',fontsize = 18)
        ax1.set_xlabel('$x_1$',fontsize = 15)
        ax1.set_ylabel('$x_2$',fontsize = 15)

    fig.subplots_adjust(left=0,right=1,bottom=0,top=1)   # remove whitespace around 3d figure

    plt.show()

# plot first few reciprocal functions
def poly_2d_plotter():
    ### plot the first four polynomials
    # make a fine sampling of input values over the range [-5,5]
    x = np.linspace(-5,5,100)
    fig = plt.figure(figsize = (16,5))

    for m in range(1,5):
        # make next polynomial element
        fm = x**m
        fm_table = np.stack((x,fm),axis = 1)

        # plot the current element
        ax = fig.add_subplot(1,4,m)
        ax.plot(fm_table[:,0],fm_table[:,1],color = [1 - 1/float(m),1/float(m),m/float(m)],linewidth = 5,zorder = 3)
        ax.set_title('$f_'+str(m) + ' = x^' + str(m) + '$',fontsize = 18)

        # clean up plot
        ax.grid(True, which='both')
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')
        ax.set_xlabel('$x$',fontsize = 14)

    plt.show()
   
# plot first few reciporical functions
def recip_plotter():
    fig = plt.figure(figsize = (16,5))

    for m in range(1,5):
        # make next polynomial element
        ax = fig.add_subplot(1,4,m)

        # plot the left side
        x = np.linspace(-0.5,-0.05,100)
        fm = 1/x**m
        ax.plot(x,fm,color = [1 - 1/float(m),1/float(m),m/float(m)],linewidth = 5,zorder = 3)

        # plot the right side
        x = np.linspace(0.05,0.5,100)
        fm = 1/x**m
        ax.plot(x,fm,color = [1 - 1/float(m),1/float(m),m/float(m)],linewidth = 5,zorder = 3)

        # clean up plot
        ax.set_title('$f_'+str(m) + ' = x^{-' + str(m) + '}$',fontsize = 18)
        ax.grid(True, which='both')
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')
        ax.set_xlabel('$x$',fontsize = 14)

    plt.show()
    
# composition demonstration number 1
def composition_demo1():
    # create functions
    x = np.linspace(-3,3,500)
    f1 = x**3
    f2 = np.sin(x)
    f2_f1 = np.sin(x**3)
    f1_f2 = (np.sin(x))**3

    # plot the functions 
    fig = plt.figure(figsize = (15,4))
    plt.style.use('ggplot')
    ax1 = fig.add_subplot(131); ax2 = fig.add_subplot(132); ax3 = fig.add_subplot(133);

    # plot
    ax1.plot(x, f1, c='k', linewidth=2,zorder = 3)
    ax2.plot(x, f2, c='k', linewidth=2,zorder = 3)
    ax3.plot(x, f2_f1, c='r', linewidth=2,zorder = 3)
    ax3.plot(x, f1_f2, c='b', linewidth=2,zorder = 3)

    # plot x and y axes, and clean up
    xlabel='$x$'
    ax1.set_xlabel(xlabel,fontsize = 14)
    ax2.set_xlabel(xlabel,fontsize = 14)
    ax3.set_xlabel(xlabel,fontsize = 14)

    ax1.set_title('$x^3$', rotation = 0, fontsize = 14)
    ax2.set_title('$sin(x)$', rotation = 0, fontsize = 14)
    ax3.legend(['$sin(x^3)$','$(sin(x))^3$'], loc='center left', bbox_to_anchor=(0, 1.15),fontsize=14,ncol=2)

    # clean up plots
    ax1.grid(True, which='both'), ax2.grid(True, which='both'),  ax3.grid(True, which='both')

    ax1.axhline(y=0, color='k', linewidth=1), ax2.axhline(y=0, color='k', linewidth=1), ax3.axhline(y=0, color='k', linewidth=1)
    ax1.axvline(x=0, color='k', linewidth=1), ax2.axvline(x=0, color='k', linewidth=1), ax3.axvline(x=0, color='k', linewidth=1)

    plt.show()
    
# second demonstration of composition of 3 functions
def composition_demo2():
    # create functions
    x = np.linspace(-2,1.1,500)
    f1 = np.exp(np.sin(x**3))
    f2 = np.exp((np.sin(x))**3)
    f3 = np.sin(np.exp(x**3))
    f4 = np.sin((np.exp(x))**3)
    f5 = (np.exp(np.sin(x)))**3
    f6 = (np.sin(np.exp(x)))**3

    # plot the functions 
    fig = plt.figure(figsize = (15,9))
    plt.style.use('ggplot')
    ax1 = fig.add_subplot(231); ax2 = fig.add_subplot(232); ax3 = fig.add_subplot(233);
    ax4 = fig.add_subplot(234); ax5 = fig.add_subplot(235); ax6 = fig.add_subplot(236);

    # plot
    ax1.plot(x, f1, c='r', linewidth=2,zorder = 3)
    ax2.plot(x, f2, c='r', linewidth=2,zorder = 3)
    ax3.plot(x, f3, c='r', linewidth=2,zorder = 3)
    ax4.plot(x, f4, c='r', linewidth=2,zorder = 3)
    ax5.plot(x, f5, c='r', linewidth=2,zorder = 3)
    ax6.plot(x, f6, c='r', linewidth=2,zorder = 3)

    ax1.set_title('$e^{sin(x^3)}$', rotation = 0, fontsize = 14)
    ax2.set_title('$e^{(sin(x))^3}$', rotation = 0, fontsize = 14)
    ax3.set_title('$sin(e^{x^3})$', rotation = 0, fontsize = 14)
    ax4.set_title('$sin((e^x)^3)$', rotation = 0, fontsize = 14)
    ax5.set_title('$(e^{sin(x)})^3$', rotation = 0, fontsize = 14)
    ax6.set_title('$(sin(e^x))^3$', rotation = 0, fontsize = 14)

    # clean up plots
    ax1.grid(True, which='both'), ax2.grid(True, which='both'),  ax3.grid(True, which='both')
    ax4.grid(True, which='both'), ax5.grid(True, which='both'),  ax6.grid(True, which='both')

    ax1.axhline(y=0, color='k', linewidth=1), ax2.axhline(y=0, color='k', linewidth=1), ax3.axhline(y=0, color='k', linewidth=1)
    ax1.axvline(x=0, color='k', linewidth=1), ax2.axvline(x=0, color='k', linewidth=1), ax3.axvline(x=0, color='k', linewidth=1)
    ax4.axhline(y=0, color='k', linewidth=1), ax5.axhline(y=0, color='k', linewidth=1), ax6.axhline(y=0, color='k', linewidth=1)
    ax4.axvline(x=0, color='k', linewidth=1), ax5.axvline(x=0, color='k', linewidth=1), ax6.axvline(x=0, color='k', linewidth=1)

    plt.show()   
    
# plotter for our recursive function
def recursive_plotter(f,n,**kwargs):
    plot_type = 'continuous'
    if 'plot_type' in kwargs:
        plot_type = kwargs['plot_type']
        
    x = np.linspace(-3,3,500)
    if 'x' in kwargs:
        x = kwargs['x']
        
    legend = 'on'
    if 'legend' in kwargs:
        legend = kwargs['legend']
        
    plot_all = True
    if 'plot_all' in kwargs:
        plot_all = kwargs['plot_all']
        
    ### loop over compositions desired and plot each level, or just plot final composition ###
    if plot_all == True:
        for i in range(1,n+1):
            # evaluate desired composition
            f_evals = f(x,i)

            # plot = choose plot type    
            label = '$f^{(' + str(i) + ')}(x)$'
            if plot_type == 'continuous':
                plt.plot(x, f_evals, linewidth=2,zorder = 3,label = label)
            if plot_type == 'scatter':
                plt.scatter(x, f_evals, c='r', s=50,edgecolor='k',linewidth=1,label = label)
         
    else:  # plot deepest composition
        f_evals = f(x,n)
        label = '$f^{(' + str(n) + ')}(x)$'
        if plot_type == 'continuous':
            plt.plot(x, f_evals, linewidth=2,zorder = 3,label = label)
        if plot_type == 'scatter':
            plt.scatter(x, f_evals, c='r', s=50,edgecolor='k',linewidth=1,label = label)
        
    # plot x and y axes, and clean up
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k', linewidth=1)
    plt.axvline(x=0, color='k', linewidth=1)
       
    # print legend too?
    if legend == 'on':
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), shadow=True,prop={'family':'cursive','weight':'roman','size':'medium'})

    plt.show()