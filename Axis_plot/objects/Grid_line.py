import numpy as np
from core.generate_grid_line_pair import generate_grid_line_pair_x,generate_grid_line_pair_y

class GridLine:
    def __init__(self,x,y,graph):
        self.x = x
        self.y = y
        self.graph = graph
        self.lines_v = None
        self.lines_h = None
        self.lines_v_vertex = None
        self.lines_h_vertex = None
        self.initialize()
    def initialize(self):
        self.lines_v = generate_grid_line_pair_x(self.x,self.graph.height)
        self.lines_h = generate_grid_line_pair_y(self.y, self.graph.width)


    def update_grid(self,x_coor,y_coor):
        self.lines_v_vertex.delete()
        self.lines_h_vertex.delete()
        self.x = x_coor
        self.y = y_coor
        
        self.lines_v = generate_grid_line_pair_x(x_coor,self.graph.height)
        self.lines_h = generate_grid_line_pair_y(y_coor, self.graph.width)

