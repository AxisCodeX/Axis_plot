from core.generate_interval import interval
from core.generate_ticks import generate_ticks
from core.coordinate_conversion import convert_to_screen_coordinate

class GraphPage:
    def __init__(self,width,height,Renderer):
        self.width = width
        self.height = height
        self.Renderer = Renderer
        self.grid_spacing = 200
        self.zoom = 1
        self.xlim = (-10,10)
        self.ylim = (-10,10)
        self.x_ticks = []
        self.y_ticks = []
        self.generate_ticks()


    
    
    def generate_ticks(self):
        print("xlim : ",self.xlim)
        print("ylim : ",self.ylim)
        interval_x = interval(self.xlim,self.width,self.grid_spacing)
        interval_y = interval(self.ylim,self.height,self.grid_spacing)
        
        self.x_ticks = generate_ticks(self.xlim,interval_x)
        self.y_ticks = generate_ticks(self.ylim , interval_y)
        print("interval_x : ", interval_x)
        print("interval_y : ", interval_y)

        print("x_ticks : ", self.x_ticks)
        print("y_ticks : ", self.y_ticks)

