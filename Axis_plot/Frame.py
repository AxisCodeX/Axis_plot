import pyglet
from Graph_page import Graph_Page
from Rendering.Renderer import Rendering_Engine

class Frame:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.graphs = []
        self.Renderer = Rendering_Engine(width,height)
        

    
    def create_graph_page(self):
        graph = Graph_Page(self.Renderer)
        graph.initialize(self.width,self.height)
        self.graphs.append(graph)
        self.Renderer.create_graph(graph)
        return graph
    

    
    def run(self):
        self.Renderer.run()
        




if __name__ =="__main__":
    pass
    









