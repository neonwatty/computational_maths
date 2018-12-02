# import custom JS animator
from compmaths_libraries.JSAnimation_slider_only import IPython_display_slider_only
import numpy as np
import time

# import standard plotting and animation
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import gridspec
from IPython.display import clear_output

# import patches
from matplotlib.patches import Rectangle, PathPatch
import mpl_toolkits.mplot3d.art3d as art3d
#import cv2 
from PIL import Image

# convert a color image to grayscale and plot both for visual comparison
def show_color_gray(**kwargs):
    img_path = kwargs['img_path']
    shrink_factor = 1
    if 'shrink_factor' in kwargs:
        shrink_factor = kwargs['shrink_factor']
       
    img = Image.open(img_path)
    gray = np.array(img.convert('L'))
    img = img.resize((round(shrink_factor*np.shape(gray)[1]),round(shrink_factor*np.shape(gray)[0])), Image.ANTIALIAS)
    gray = np.array(img.convert('L'))
    
    # create figure to plot
    fig = plt.figure(num=None, figsize=(12,5), dpi=80, facecolor='w', edgecolor='k')

    # make subplots
    gs = gridspec.GridSpec(1, 2, width_ratios=[1,1]) 
    gs.update(wspace=0.005, hspace=0.005) # set the spacing between axes.
    ax1 = plt.subplot(gs[0]); ax1.grid(False); ax1.axis('off');
    ax2 = plt.subplot(gs[1]); ax2.grid(False); ax2.axis('off');

    # plot images
    ax1.imshow(img)
    ax2.imshow(gray,cmap = 'gray')
    plt.show()
    
# Draw an input image as a 3d surface
# compute first order approximation
def grayimg_as_function(**kwargs):  
    img_path = kwargs['img_path']
        
    # get viewing angle and num_slides args
    num_frames = 100
    if 'num_frames' in kwargs:
        num_frames = kwargs['num_frames']
    start_view = [90,90]
    end_view = [-90,270]
    if 'end_view' in kwargs:
        end_view = kwargs['end_view']
    plot_type = 'scatter'
    if 'plot_type' in kwargs:
        plot_type = kwargs['plot_type']
    shrink_factor = 0.1
    if 'shrink_factor' in kwargs:
        shrink_factor = kwargs['shrink_factor']
            
    # construct viewing angles
    view1 = np.linspace(start_view[0],end_view[0],num_frames)
    view2 = np.linspace(start_view[1],end_view[1],num_frames)
        
    img = Image.open(img_path)
    orig_img = img.copy() 
    gray = np.array(img.convert('L'))
    img = img.resize((round(shrink_factor*np.shape(gray)[1]),round(shrink_factor*np.shape(gray)[0])), Image.ANTIALIAS)
    gray = np.array(img.convert('L'))
  
    # create figure to plot
    fig = plt.figure(num=None, figsize=(7,7), dpi=80, facecolor='w', edgecolor='k')
    artist = fig
        
    ### create 3d plot in left panel
    ax2 = plt.subplot(111,projection = '3d'); ax2.axis('off');
    fig.subplots_adjust(left=0,right=1,bottom=0,top=1)   # remove whitespace around 3d figure

    # setup 3d ground to plot over
    s = np.shape(gray)[0]
    t = np.shape(gray)[1]
    s = np.arange(0,s,1)
    t = np.arange(0,t,1)
    xpos, ypos = np.meshgrid(t,s)
    zpos = np.ones((np.shape(xpos)))

    # plot 3d surface
    if plot_type == 'continuous':
        ax2.plot_surface(xpos,ypos,gray,cmap = 'gray', antialiased=True,edgecolor = 'w',linewidth=0.15)
    if plot_type == 'scatter':
        ax2.scatter(xpos,ypos,gray.astype(float),marker = 's',s = 20,c = 1-gray.astype(float)/float(255),cmap=plt.cm.Greys,alpha = 1,edgecolor = 'w',linewidth=0.5)
        ax2.set_facecolor((1, 0.8, 1))
        ax2.set_aspect('auto')

        ax2.set_xlim(10,np.shape(gray)[1] - 0)
        ax2.set_ylim(10,np.shape(gray)[0] - 10)
        
    if plot_type == 'proto':
        ### plot surface in right panel
        max_color = max(gray.flatten())
        for i in range(gray.shape[1]):
            for j in range(gray.shape[0]):
                level = gray[j,gray.shape[1]- i - 1]
                col = float(level)/float(max_color)
                rec = Rectangle((i-1,j-1), 1, 1,color = [col,col,col],linewidth = 0)
                ax2.add_patch(rec)
                art3d.pathpatch_2d_to_3d(rec, z=level, zdir='z')    
    
        ax2.set_xlim([-8,gray.shape[0]+8])
        ax2.set_ylim([-8,gray.shape[1]+8])
        ax2.set_zlim([0,max_color + 1])

    print ('starting animation rendering...')

    # animation sub-function
    def animate(k):
        # print rendering update
        if np.mod(k+1,25) == 0:
            print ('rendering animation frame ' + str(k+1) + ' of ' + str(num_frames))
        if k == num_frames - 1:
            print ('animation rendering complete!')
            time.sleep(1.5)
            clear_output()
                
        ax2.view_init(view1[k],view2[k])
        ax2.set_facecolor('white')
 
        return artist,

    anim = animation.FuncAnimation(fig, animate ,frames=num_frames, interval=num_frames, blit=True)
    return(anim)
        
 # show multipole views of an image patch
def reveal_imgpatch(**kwargs):
    # grab user defined args
    img_path = kwargs['img_path']
    shrink_factor = 1
    if 'shrink_factor' in kwargs:
        shrink_factor = kwargs['shrink_factor']
        
    img = Image.open(img_path)
    gray = np.array(img.convert('L'))
    img = img.resize((round(shrink_factor*np.shape(gray)[1]),round(shrink_factor*np.shape(gray)[0])), Image.ANTIALIAS)
    gray = np.array(img.convert('L'))
    
    # setup figure
    fig = plt.figure(figsize = (18,5))
    gs = gridspec.GridSpec(1, 3, width_ratios=[1,1,1],wspace=0.0, hspace=0.0) 
    ax1 = plt.subplot(gs[0]); ax1.axis('off');
    ax2 = plt.subplot(gs[1]);
    ax3 = plt.subplot(gs[2],projection='3d');

    ### plot raw image in left panel
    ax1.imshow(gray, cmap=plt.cm.gray)
    ax1.grid(False)
    ax1.axis('off')

    ### plot image with pixel numbering in middle panel
    ax2.imshow(gray, cmap=plt.cm.gray)

    # plot pixel values as numbers on top
    min_val, max_val = 0, gray.shape[0]
    diff = 1
    ind_array1 = np.arange(min_val, max_val, diff)
    min_val, max_val = 0, gray.shape[1]
    ind_array2 = np.arange(min_val, max_val, diff)

    x, y = np.meshgrid(ind_array1, ind_array2)

    for x_val, y_val in zip(x.flatten(), y.flatten()):
        c = int(gray[x_val,y_val])
        ax2.text(y_val, x_val, c, va='center', ha='center',color = 'red',fontsize=13)

    # set tickmarks and grid correctly
    ax2.set_xticks(np.arange(np.shape(gray)[1]),minor=False)
    ax2.set_yticks(np.arange(np.shape(gray)[0]),minor=False)
    ax2.set_xticks(np.arange(np.shape(gray)[1])-0.5,minor=True)
    ax2.set_yticks(np.arange(np.shape(gray)[0])-0.5,minor=True)
    ax2.grid(which='minor', color='w', linestyle='-', linewidth=2)

    ### plot surface in right panel
    max_color = max(gray.flatten())
    for i in range(gray.shape[1]):
        for j in range(gray.shape[0]):
            level = gray[j,gray.shape[1]- i - 1]
            col = float(level)/float(max_color)
            rec = Rectangle((i-1,j-1), 1, 1,color = [col,col,col],linewidth = 0)
            ax3.add_patch(rec)
            art3d.pathpatch_2d_to_3d(rec, z=level, zdir='z')
    ax3.set_xlim([-1,gray.shape[0]])
    ax3.set_ylim([-1,gray.shape[1]])
    ax3.set_zlim([0,max_color + 1])
    ax3.view_init(20,-290)

    # set tickmarks correctly
    ax3.set_xticks(np.arange(np.shape(gray)[1]))
    ax3.set_xticklabels(np.flipud(np.arange(np.shape(gray)[1])),ha = 'center')
    ax3.set_yticks(np.arange(np.shape(gray)[0]))
    ax3.set_yticklabels(np.arange(np.shape(gray)[0]),ha = 'center')

    plt.show()
    