import numpy as np
from core.generate_interval import interval
from core.generate_ticks import generate_ticks
from core.coordinate_conversion import convert_to_screen_coordinate

class GraphPage:
    def __init__(self,x,y,width,height,Renderer,grids,scissor_group=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.Renderer = Renderer
        self.grid_spacing = 200
        self.zoom = 1
        self.xlim = (-10,10)
        self.ylim = (-10,10)

        self.grids = grids
        self.scatter_plots = []
        self.scissor_group = scissor_group
        self.generate_ticks()



    
    
    def generate_ticks(self):
        interval_x = interval(self.xlim,self.width,self.grid_spacing)
        interval_y = interval(self.ylim,self.height,self.grid_spacing)
        
        x_ticks = generate_ticks(self.xlim,interval_x)
        y_ticks = generate_ticks(self.ylim , interval_y)
        return x_ticks,y_ticks

    def scatter_plot(self,x,y):
        self.Renderer.plot_points(self,x,y)



