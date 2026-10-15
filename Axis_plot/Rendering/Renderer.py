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
        self.rectangles = pyglet.graphics.Batch()
        self.rectangles_list = []
        self.graph_borders = pyglet.graphics.Batch()
        self.graph_borders_list = []


    

    def create_graph(self,graph,order):
        self.graphs.append(graph)

        x_min,x_max = graph.x_range
        y_min , y_max = graph.y_range
        top = pyglet.shapes.Line(
            x_min,y_min,x_max,y_min,batch=self.graph_borders,group=graph.scissor_group
        )
        bottom = pyglet.shapes.Line(
            x_min,y_max,x_max,y_max,batch=self.graph_borders,group=graph.scissor_group
        )
        left = pyglet.shapes.Line(
            x_min,y_min,x_min,y_max,batch=self.graph_borders,group=graph.scissor_group
        )
        right = pyglet.shapes.Line(
            x_max,y_min,x_max,y_max,batch=self.graph_borders,group=graph.scissor_group
        )
        self.graph_borders_list.extend([top,bottom,left,right])
        
        tick_x ,tick_y,screen_x_coor,screen_y_coor = graph.generate_nice_ticks()
 
        for t_x,x in zip(tick_x,screen_x_coor):
            tick_x = pyglet.text.Label(
                f"{t_x}",
                x = x,
                y = (graph.y_range[0] + graph.y_range[1])//2,
                anchor_x="center",
                anchor_y="top",
                batch= self.tick_label,
                group=graph.scissor_group
            )
            self.tick_list.append(tick_x)
            
        for y in (screen_y_coor):
            line = pyglet.shapes.Line(
                graph.x_range[0],y,graph.x_range[1],y,color=(255,255,255,70),batch=self.lines,group=graph.scissor_group
            )
            self.lines_list.append(line)
        for x in screen_x_coor:
            line = pyglet.shapes.Line(
                x,graph.y_range[0],x,graph.y_range[1],color=(255,255,255,70),batch=self.lines,group=graph.scissor_group
            )
            self.lines_list.append(line)
        for t_y,y in zip(tick_y,screen_y_coor):
            tick_y = pyglet.text.Label(
                f"{t_y}",
                x = (graph.x_range[0] + graph.x_range[1]) //2,
                y = y,
                anchor_x="right",
                anchor_y="center",
                batch= self.tick_label,group=graph.scissor_group
            )
            
            self.tick_list.append(tick_y)
            
        
    
    def draw(self):
        self.tick_label.draw()
        self.lines.draw()
        self.points.draw()
        self.rectangles.draw()
        self.graph_borders.draw()


    def add_points(self,x,y,scissor_group,size = 6):
        for xi,yi in zip(x,y):
            print(xi,yi)
            circle = pyglet.shapes.Circle(xi,yi,radius=size,batch=self.points,group=scissor_group)
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