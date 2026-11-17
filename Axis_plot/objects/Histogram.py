import numpy as np
from core.coordinate_conversion import convert_to_graph_coordinate, convert_to_screen_coordinate
class Hist:
    def __init__(self,graph,dist,bins = 5):
        self.graph = graph
        self.dist = dist
        self.bins = bins
        self.bin_edges = None
        self.frequency = None
        self.min_value = None
        self.max_value = None
        self.initialize()
    def initialize(self):
        self.min_value = self.dist.min()
        self.max_value = self.dist.max()
        bin_boundaries = np.arange(self.min_value , self.max_value , self.bins)
        counts , bin_edges = np.histogram(self.dist , bin_boundaries)
        print("counts : ", counts)
        print("bin_edges : ", bin_edges)
        self.frequency = counts
        self.bin_edges = bin_edges

    def convert_to_rectangle(self):
        screen_coordinates_x = self.graph .x + convert_to_screen_coordinate(self.bin_edges ,self.graph.xlim , dimension  = self.graph.width )
        screen_coordinmtes_y = self.graph.y + convert_to_screen_coordinate(self.frequency , self.graph.ylim , dimension=self.graph.height)
        bin_width = self.graph.x + convert_to_screen_coordinate(self.bins , self.graph.xlim , self.graph.width)
        print("x : ",screen_coordinates_x)
        print("Y :" ,screen_coordinmtes_y)
        p1 = np.column_stack((screen_coordinates_x[1:],np.zeros(screen_coordinates_x.shape[0] - 1)))
        p2 = np.column_stack((screen_coordinates_x[1: ],np.zeros(screen_coordinates_x.shape[0] - 1)))
        h1 = np.column_stack((screen_coordinates_x[:-1], screen_coordinmtes_y))
        h2 = np.column_stack((screen_coordinates_x[1: ] , screen_coordinmtes_y))
        triangle_1 = np.column_stack((p1,p2,h1))
        triangle_2 = np.column_stack((p2,h2,h1))
        rectangles  = np.column_stack((triangle_1 , triangle_2))

        return rectangles
