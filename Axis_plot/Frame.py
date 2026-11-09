from Rendering.Renderer import Renderer
from Graph.Graph_collection import GraphCollection
from Graph_page import GraphPage

class Frame:
    def __init__(self,width = 800,height =800 ):
        self.width = width
        self.height = height
        self.Renderer = Renderer(width,height)
        self.graph_collection = None

    def graph_page(self,grids = True):
        graph = GraphPage(0,0,self.width,self.height,self.Renderer,grids)
        self.graphs.append(graph)
        self.Renderer.draw_graph(graph)
        return graph


    def collection(self,n,orientation="ROWS",spacing= 40):
        graph_collection= GraphCollection()
        self.graph_collection = graph_collection
        layout = graph_collection.create_collection(n,orientation,self.width,self.height,spacing)  # pyright: ignore[reportUnknownArgumentType]
        for orent in layout:
            x,y,width,height = orent
            graph = GraphPage(x,y,width,height,self.Renderer,grids = True)
            graph_collection.graphs.append(graph)
            self.Renderer.draw_graph(graph)
        return graph_collection.graphs

    def run(self):
        self.Renderer.run()
