import pyglet
from Graph_page import Graph_Page
from Rendering.Renderer import Rendering_Engine
from core.Geomertry_Engine import geometry_engine
from Groups.Scissor import Scissor
class Frame:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.graphs = []
        self.Renderer = Rendering_Engine(width,height)
        

    
    def create_graph_pages(self,no_of_graphs=1,orientation="ROW",grid_spacing=10):
        coors = geometry_engine.orientation(no_of_graphs,width=self.width,height = self.height,grid_spacing=grid_spacing,orientation=orientation)
        print(coors)
        
        

        for idx,coordinates in enumerate(coors):
            xmin,xmax,ymin,ymax = coordinates
            scissor_group = Scissor(xmin,ymin,(xmax-xmin),(ymax-ymin),order=idx)
            graph = Graph_Page((xmin,xmax),(ymin,ymax),Renderer=self.Renderer,scissor_group=scissor_group)
            graph.initialize()
            self.graphs.append(graph)
            self.Renderer.create_graph(graph,order = idx)
            
        
        return self.graphs

    
    def run(self):
        self.Renderer.run()
        




if __name__ =="__main__":
    pass
    









