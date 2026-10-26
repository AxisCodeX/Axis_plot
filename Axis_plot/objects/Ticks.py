import pyglet
from core.coordinate_conversion import convert_to_screen_coordinate
class Ticks:
    def __init__(self,graph,x,y):
        self.graph = graph
        self.x = x
        self.y = x
        self.ticks_x = []
        self.ticks_y = []
    def initialize(self,batch):
        x_axis = convert_to_screen_coordinate(0,self.graph.xlim,self.graph.width)
        y_axis = convert_to_screen_coordinate(0,self.graph.ylim,self.graph.height)

        x_coordinate = convert_to_screen_coordinate(self.x,self.graph.xlim,self.graph.width)
        y_coordinate = convert_to_screen_coordinate(self.y,self.graph.ylim,self.graph.height)

        for x_t , x in zip(self.x,x_coordinate):
            label = pyglet.text.Label(
                f"{x_t}",
                x=x,
                y = y_axis,
                batch=batch,
                anchor_x="center",
                anchor_y="center"
            )
            self.ticks_x.append(label)
        for y_t,y in zip(self.y,y_coordinate):
            label = pyglet.text.Label(
                f"{y_t}",
                x=x_axis,
                y=y,
                batch=batch,
                anchor_x="center",
                anchor_y="center"
            )
            self.ticks_y.append(label)

    def update_ticks(self,x_ticks,y_ticks,batch):
        self.x = x_ticks
        self.y = y_ticks

        x_axis = convert_to_screen_coordinate(0,self.graph.xlim,self.graph.width)
        y_axis = convert_to_screen_coordinate(0,self.graph.ylim,self.graph.height)

        x_coordinate = convert_to_screen_coordinate(self.x,self.graph.xlim,self.graph.width)
        y_coordinate = convert_to_screen_coordinate(self.y,self.graph.ylim,self.graph.height)

        for ticks in self.ticks_x:
            ticks.delete()
        
        self.ticks_x.clear()

        for ticks in self.ticks_y:
            ticks.delete()
        self.ticks_y.clear()

        for x_t , x in zip(self.x,x_coordinate):
            label = pyglet.text.Label(
                f"{x_t}",
                x=x,
                y = y_axis,
                batch=batch,
                anchor_x="center",
                anchor_y="center"
            )
            self.ticks_x.append(label)
        for y_t,y in zip(self.y,y_coordinate):
            label = pyglet.text.Label(
                f"{y_t}",
                x=x_axis,
                y=y,
                batch=batch,
                anchor_x="center",
                anchor_y="center"
            )
            self.ticks_y.append(label)

