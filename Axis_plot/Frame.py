from Rendering.Renderer import Renderer
from Graph_page import GraphPage
class Frame:
    def __init__(self,width = 800,height =800 ):
        self.width = width
        self.height = height
        self.Renderer = Renderer(width,height)
        self.graph = []

    def graph_page(self,grids = True):
        graph = GraphPage(self.width,self.height,self.Renderer,grids)
        self.Renderer.draw_graph(graph)
        return graph

    def run(self):
        self.Renderer.run()
