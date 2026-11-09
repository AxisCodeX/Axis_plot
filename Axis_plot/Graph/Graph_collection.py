from Graph_page import GraphPage
from pyglet import graphics

class GraphCollection:
    def __init__(self):
            self.graphs = []
            pass


    def create_collection(self,no_of_graph,orientation,width,height,spacing):

        orientation = orientation.upper()
        if orientation == "Column":
            o = self.get_orientation(no_of_graph , orientation , width , height)
        else:
            o = self.get_orientation(no_of_graph , orientation , width , height,spacing)


        return o


    def get_orientation(self,no_of_graph,orientation,width,height,spacing=10):
        if orientation == "COLUMN":
            layout=[]
            graph_height = (height - (no_of_graph - 1)*spacing )/no_of_graph
            for n in range(no_of_graph):
                x = 0
                y= n * (graph_height + spacing)
                layout.append([x , y, width , graph_height])
        else:
            layout=[]
            graph_width = (width - (no_of_graph - 1)*spacing )/no_of_graph
            for n in range(no_of_graph):
                x = n *(graph_width + spacing)
                y = 0
                layout.append([x,y,graph_width , height])

        return layout

if __name__ == "__main__":
    graph_collection =  GraphCollection()
    orientations = graph_collection.create_collection(3,"ROW",800,800)
    print(orientations)
