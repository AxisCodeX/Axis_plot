import pyglet
import numpy as np


class Rendering_Engine:
    def __init__(self,width,height):
        
        self.width = width
        self.height = height
        self.window = pyglet.window.Window(width,height)
        self.graphs = []
        self.tick_label = pyglet.graphics.Batch()
        self.tick_list = []
        self.lines = pyglet.graphics.Batch()
        self.lines_list = []
        self.points = pyglet.graphics.Batch()
        self.points_list = []


    

    def create_graph(self,graph):
        self.graphs.append(graph)
        tick_x ,tick_y,screen_x_coor,screen_y_coor = graph.generate_nice_ticks()
        for t_x,t_y,x,y, in zip(tick_x,tick_y,screen_x_coor,screen_y_coor):
            tick_x = pyglet.text.Label(
                f"{t_x}",
                x = x,
                y = graph.height//2,
                anchor_x="center",
                anchor_y="top",
                batch= self.tick_label,
            )
            tick_y = pyglet.text.Label(
                f"{t_y}",
                x = graph.width //2,
                y = y,
                anchor_x="right",
                anchor_y="center",
                batch= self.tick_label
            )

            line_x = pyglet.shapes.Line(
                0,y,graph.width,y,color=(255,255,255,70),batch=self.lines
            )
            line_y = pyglet.shapes.Line(
                x,0,x,graph.height,color=(255,255,255,70),batch=self.lines
            )

            self.tick_list.append(tick_x)
            self.tick_list.append(tick_y)
            self.lines_list.append(line_x)
            self.lines_list.append(line_y)
    
    def draw(self):
        self.tick_label.draw()
        self.lines.draw()
        self.points.draw()


    def add_points(self,x,y,size = 6):
        print(x)
        print(y)
        for xi,yi in zip(x,y):
            print("runnig add_points")
            print(xi,yi)
            circle = pyglet.shapes.Circle(xi,yi,radius=size,batch=self.points)
            self.points_list.append(circle)


    def run(self):

        @self.window.event
        def on_draw():
            self.window.clear()
            self.draw()
        
        def update(dt):
            pass
        pyglet.clock.schedule_interval(update,1/60)
        pyglet.app.run()