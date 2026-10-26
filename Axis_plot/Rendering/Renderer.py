import numpy as np
import pyglet 
from pyglet.gl import glEnable,glBlendFunc,glPointSize
from pyglet.gl import GL_LINES,GL_BLEND,GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA,GL_PROGRAM_POINT_SIZE,GL_POINTS
from  .Shaders.Shader import Shader_Program#custom shader program
from .Shaders.PointShader import Point_Shader
from core.coordinate_conversion import convert_to_screen_coordinate,convert_to_graph_coordinate
from core.generate_grid_line_pair import generate_grid_line_pair_x,generate_grid_line_pair_y
from objects.Scatter_plot import ScatterPlot
from objects.Grid_line import GridLine
class Renderer:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.window = pyglet.window.Window(width,height)
        self.graph = None

        #shader_programs
        self.shader_program = Shader_Program(width,height)
        self.point_shader = Point_Shader(width,height)


        ##batches
        self.x_tick_batches = pyglet.graphics.Batch()
        self.x_ticks = []

        self.graph_grids = pyglet.graphics.Batch()
        self.grids = []


        self.y_tick_batches = pyglet.graphics.Batch()
        self.y_ticks = [] 

        self.line_batch = pyglet.graphics.Batch()
        self.lines = []

        self.scatter_plot_batch = pyglet.graphics.Batch()
        self.scatter_plots = []



    def draw_graph(self,graph):
        self.graph = graph
        graph.generate_ticks()
        x_ticks = graph.x_ticks
        y_ticks = graph.y_ticks

        x_coordinate = convert_to_screen_coordinate(x_ticks,graph.xlim,graph.width)
        y_coordinate = convert_to_screen_coordinate(y_ticks,graph.ylim,graph.height)
        grid_line =  GridLine(x_coordinate,y_coordinate,graph)
        lines_v = self.shader_program.vertex_list(
                len(grid_line.lines_v),
                GL_LINES,
                position = ('f',grid_line.lines_v.flatten()),
                batch = self.line_batch
            )
        lines_h = self.shader_program.vertex_list(
                len(grid_line.lines_h),
                GL_LINES,
                position = ('f',grid_line.lines_h.flatten()),
                batch = self.line_batch
            )
        grid_line.lines_v_vertex = lines_v
        grid_line.lines_h_vertex = lines_h
        
        
        self.grids.append(grid_line)
        self.update_graph(graph)

    def update_graph(self,graph):
        
        for tick_y in self.y_ticks:
            tick_y.delete()
        self.y_ticks.clear()

        for tick_x in self.x_ticks:
            tick_x.delete()
        
        self.x_ticks.clear()

        for line in self.lines:
            line.delete()
        self.lines.clear()
        graph.generate_ticks()
        x_ticks = graph.x_ticks
        y_ticks = graph.y_ticks

        x_axis = convert_to_screen_coordinate(0,graph.xlim,graph.width)
        y_axis = convert_to_screen_coordinate(0,graph.ylim,graph.height)

        x_coordinate = convert_to_screen_coordinate(x_ticks,graph.xlim,graph.width)
        y_coordinate = convert_to_screen_coordinate(y_ticks,graph.ylim,graph.height)


        

        for x_t , x in zip(x_ticks,x_coordinate):
            label = pyglet.text.Label(
                f"{x_t}",
                x=x,
                y = y_axis,
                batch=self.x_tick_batches,
                anchor_x="center",
                anchor_y="center"
            )
            self.x_ticks.append(label)
        
        for y_t,y in zip(y_ticks,y_coordinate):
            label = pyglet.text.Label(
                f"{y_t}",
                x=x_axis,
                y=y,
                batch=self.y_tick_batches,
                anchor_x="center",
                anchor_y="center"
            )
            self.y_ticks.append(label)

        for grid in self.grids:
            grid.update_grid(x_coordinate,y_coordinate)
            lines_v = self.shader_program.vertex_list(
                len(grid.lines_v),
                GL_LINES,
                position = ('f',grid.lines_v.flatten()),
                batch = self.line_batch
            )
            lines_h = self.shader_program.vertex_list(
                len(grid.lines_h),
                GL_LINES,
                position = ('f',grid.lines_h.flatten()),
                batch = self.line_batch
            )
            grid.lines_v_vertex = lines_v
            grid.lines_h_vertex = lines_h
        self.update_scatter_plots(graph.xlim,graph.ylim)

    def plot_points(self,x,y):
        x = np.array(x)
        y  = np.array(y)
        scatter_plot = ScatterPlot(x,y,self.graph)

        points = self.point_shader.vertex_list(
            len(scatter_plot.points),
            GL_POINTS,
            position = ('f',scatter_plot.points.flatten()),
            batch = self.scatter_plot_batch
        )
        
        scatter_plot.vertex_list = points
        self.scatter_plots.append(scatter_plot)


    def update_scatter_plots(self,xlim,ylim):
        for s_p in self.scatter_plots:
            s_p.update_vertex_list(xlim,ylim)

    def draw(self):
        self.line_batch.draw()
        self.x_tick_batches.draw()
        self.y_tick_batches.draw()
        self.scatter_plot_batch.draw()

    def run(self):
        @self.window.event
        def on_draw():
            glEnable(GL_PROGRAM_POINT_SIZE)
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)
            self.window.clear()
            self.draw()
        

        @self.window.event
        def on_mouse_scroll(x,y,scroll_x ,scroll_y):
            
                if scroll_y == 0:
                    return
                factor = 1.1 if scroll_y > 0 else 1 / 1.1
                
                x_n = convert_to_graph_coordinate(x,self.graph.xlim,self.graph.width)
                y_n = convert_to_graph_coordinate(y,self.graph.ylim,self.graph.height)

                new_x_range = (self.graph.xlim[1] - self.graph.xlim[0])/factor

                new_y_range = (self.graph.ylim[1] - self.graph.ylim[0])/factor

                new_x_min = x_n  - (x/self.graph.width)* new_x_range
                new_y_min = y_n - (y/self.graph.height) * new_y_range

                self.graph.xlim = (new_x_min,new_x_min + new_x_range)
                self.graph.ylim = (new_y_min, new_y_min + new_y_range)
                self.update_graph(self.graph)


        @self.window.event
        def on_mouse_drag(x,y,dx,dy,buttons,modifiers):
            
            self.graph.xlim =  np.array(self.graph.xlim ) - (dx/self.graph.width) * ((self.graph.xlim[1] - self.graph.xlim[0]))
            self.graph.ylim =  np.array(self.graph.ylim) - ((dy/self.graph.height) * (self.graph.ylim[1] - self.graph.ylim[0]))
            self.update_graph(self.graph)
        def update(dt):
            pass
        pyglet.clock.schedule_interval(update,1/60)
        pyglet.app.run()