import numpy as np
from core.generate_interval import interval
from core.generate_ticks import generate_ticks
from core.coordinate_conversion import convert_to_screen_coordinate

class GraphPage:
    def __init__(self,width,height,Renderer,grids):
        self.width = width
        self.height = height
        self.Renderer = Renderer
        self.grid_spacing = 200
        self.zoom = 1
        self.xlim = (-10,10)
        self.ylim = (-10,10)
        self.x_ticks = []
        self.y_ticks = []
        self.grids = grids
        self.generate_ticks()


    
    
    def generate_ticks(self):
        interval_x = interval(self.xlim,self.width,self.grid_spacing)
        interval_y = interval(self.ylim,self.height,self.grid_spacing)
        
        self.x_ticks = generate_ticks(self.xlim,interval_x)
        self.y_ticks = generate_ticks(self.ylim , interval_y)

    def scatter_plot(self,x,y):
        self.Renderer.plot_points(x,y)



