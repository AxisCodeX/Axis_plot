import pyglet
import numpy as np
from core.Geomertry_Engine import geometry_engine
class Graph_Page:
    def __init__(self,x_range,y_range,Renderer,scissor_group):
        self.batch = pyglet.graphics.Batch()
        self.x_range = x_range
        self.y_range = y_range
        self.xlim = ( -5, 5 )
        self.ylim = ( -5 ,5  )
        self.grid_spacing = 50
        self.Renderer = Renderer
        self.scissor_group = scissor_group

    


    def initialize(self):
        self.width = self.x_range[1] - self.x_range[0]
        self.height = self.y_range[1] - self.y_range[0]
    

    def generate_nice_ticks(self):
        tick_x = geometry_engine.nice_num(self.xlim,self.width,grid_spacing=self.grid_spacing)
        tick_y = geometry_engine.nice_num(self.ylim,self.height,grid_spacing=self.grid_spacing)
        screen_x = geometry_engine.convert_to_screen_coordinate(tick_x,self.xlim,self.width,self.x_range)
        screen_y = geometry_engine.convert_to_screen_coordinate(tick_y,self.ylim,self.height,self.y_range)
        return tick_x ,tick_y ,screen_x,screen_y

    
    def set_xlimit(self,xmin , xmax):
        self.xlim = (xmin,xmax)

    def set_ylimit(self,ymin , ymax):
        self.ylim = (ymin,ymax)


    def plot_points(self,x,y,radius=6):
        x = np.array(x)
        y = np.array(y)

        screen_x = geometry_engine.convert_to_screen_coordinate(coordinates=x,limit=self.xlim,dimension=self.width,d_range=self.x_range)
        screen_y = geometry_engine.convert_to_screen_coordinate(
            coordinates=y,limit=self.ylim,dimension=self.height,d_range=self.y_range
        )
        self.Renderer.add_points(screen_x,screen_y,self.scissor_group,size=radius )

if __name__ =="__main__":
    pass