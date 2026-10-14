import pyglet
import numpy as np

class Rendering_Engine():
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.window = pyglet.window.Window(width,height)
        self.label_batch = pyglet.graphics.Batch()
        self.ticks_batch = pyglet.graphics.Batch()
        self.shapes = pyglet.graphics.Batch()
        self.object_list = []
        self.graphs = []


    

    def draw_points(self,point_x , point_y):
        point_x = np.array(point_x)
        point_y = np.array(point_y)

        for x,y in zip(point_x,point_y):
            circle = pyglet.shapes.Circle(x,y,6,batch=self.shapes)
            self.object_list.append(circle)

    

    def draw_graph(self,graph):
        self.graphs.append(graph)
        tick_x,tick_y,tick_x_coor,tick_y_coor = graph.generate_nice_ticks()
        print(tick_x_coor)
        print(tick_y_coor)
        for x,y,t_x,t_y in zip(tick_x_coor,tick_y_coor,tick_x,tick_y):
            line_y = pyglet.shapes.Line( x,0,x,graph.height,batch=self.shapes,color=(255,255,255,70) )
            line_x = pyglet.shapes.Line( 0,y,graph.width,y,batch=self.shapes ,color=(255,255,255,70))

            label_y = pyglet.text.Label(
                f"{t_y}",
                x = graph.width //2,
                y = y,
                batch=self.ticks_batch,
                anchor_x="right",
                anchor_y="center",
                color=(255,255,255,125)
            )

            label_x = pyglet.text.Label(
                f"{t_x}",
                x= x,
                y = graph.height//2 ,
                batch=self.ticks_batch,
                anchor_x="center",
                anchor_y="top",
                color=(255,255,255,125)
            )
            self.object_list.append(label_x)
            self.object_list.append(label_y)
            self.object_list.append(line_x)
            self.object_list.append(line_y)
        
        



    def draw(self):
        self.window.clear()
        self.label_batch.draw()
        self.ticks_batch.draw()
        self.shapes.draw()
        for graph in self.graphs:
            graph.batch.draw()

    def update(self,dt):
        pass


    def run(self):
        @self.window.event
        def on_draw():
            self.draw()
        
        
        
        pyglet.clock.schedule_interval(self.update,1/60)
        pyglet.app.run()

        

    







