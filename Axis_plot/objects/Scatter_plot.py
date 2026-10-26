
import numpy as np
from core.coordinate_conversion import convert_to_screen_coordinate
class ScatterPlot:
    def __init__(self,x,y,graph):
        self.graph = graph
        self.x = x
        self.y = y
        self.points = None
        self.vertex_list = None
        self.initialize()

    def initialize(self):
        screen_x = convert_to_screen_coordinate(self.x,self.graph.xlim,self.graph.width)
        screen_y = convert_to_screen_coordinate(self.y,self.graph.ylim,self.graph.height)
        points = np.column_stack((screen_x , screen_y))
        self.points = points

    def update_vertex_list(self,xlim,ylim):
        screen_x = convert_to_screen_coordinate(self.x,xlim,self.graph.width)
        screen_y = convert_to_screen_coordinate(self.y,ylim,self.graph.height)
        points = np.column_stack((screen_x , screen_y))
        self.vertex_list.position = points.flatten()

    