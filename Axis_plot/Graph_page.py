import pyglet
import numpy as np

class Graph_Page:
    def __init__(self,Renderer):
        self.batch = pyglet.graphics.Batch()
        self.xlim = ( -5, 5 )
        self.ylim = ( -5 ,5  )
        self.grid_spacing = 50
        self.Renderer = Renderer

    


    def initialize(self,width,height):
        self.width = width
        self.height = height
    

    def generate_nice_ticks(self):
        tick_x = self.nice_num(self.xlim,self.width)
        tick_y = self.nice_num(self.ylim,self.height)
        screen_x = self.convert_to_screen_coordinate(self.xlim,tick_x,self.width)
        screen_y = self.convert_to_screen_coordinate(self.ylim,tick_y,self.height)
        return tick_x ,tick_y ,screen_x,screen_y


    def convert_to_screen_coordinate(self,limit,coordinates,dimension):
        rng = limit[1] - limit[0]
        screen_coordinates = ((coordinates - limit[0])/rng) * (dimension)
        return screen_coordinates
        
    def nice_num(self,limit,dimension):
        rng = limit[1] - limit[0]
        no_of_ticks = dimension//self.grid_spacing
        raw_interval = rng / no_of_ticks

        exponent = np.floor(np.log10(raw_interval))
        fraction = raw_interval / (10 ** exponent)
        if fraction < 1.5:
            m = 1
        elif fraction <3:
            m = 2
        elif fraction < 7:
            m = 5
        else : 
            m = 10
        interval = m * (10 ** exponent)

        ticks = np.arange(limit[0]*10**np.abs(exponent),(limit[1]*10**np.abs(exponent) +1) , interval*10**np.abs(exponent))/10**np.abs(exponent) 

        return ticks
    
    def set_xlimit(self,xmin , xmax):
        self.xlim = (xmin,xmax)

    def set_ylimit(self,ymin , ymax):
        self.ylim = (ymin,ymax)

    def plot_points(self,x,y):
        x = np.array(x)
        y = np.array(y)
        screen_x = self.convert_to_screen_coordinate(self.xlim,x,self.width)
        screen_y = self.convert_to_screen_coordinate(self.ylim,x,self.height)

        self.Renderer.add_points(screen_x,screen_y)

if __name__ =="__main__":
    pass