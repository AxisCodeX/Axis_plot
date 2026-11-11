import numpy as np
from core.coordinate_conversion import convert_to_screen_coordinate
class VertexPlot:
    def __init__(self,graph,x,y,mode="POINT",line_joined=False,looped = False):
        self.graph = graph
        self.mode = mode
        self.x =  x
        self.y =  y
        self.line_joined = line_joined
        self.looped = looped
        self.points = None
        self.vertex_list = None
        self.initialize()

    def initialize(self):
        if self.mode == "POINT" or self.mode == 0:
            self.plot_mode = 0
        elif self.mode == "LINE" or self.mode == 1:
            self.plot_mode = 1
        screen_x =self.graph.x + convert_to_screen_coordinate( self.x,self.graph.xlim,self.graph.width)
        screen_y =self.graph.y + convert_to_screen_coordinate(self.y,self.graph.ylim,self.graph.height)
        points = np.column_stack((screen_x , screen_y))
        self.points = points

    def update_vertex_list(self,xlim,ylim):
        screen_x =self.graph.x +  convert_to_screen_coordinate(self.x,xlim,self.graph.width)
        screen_y =self.graph.y +  convert_to_screen_coordinate(self.y,ylim,self.graph.height)
        points = np.column_stack((screen_x , screen_y))
        self.vertex_list.position[:] = points.flatten()

    
