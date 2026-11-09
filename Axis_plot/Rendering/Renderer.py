import numpy as np
import pyglet 
from pyglet.graphics import ShaderGroup
from pyglet.gl import glEnable,glBlendFunc,glPointSize
from pyglet.gl import GL_LINES,GL_BLEND,GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA,GL_PROGRAM_POINT_SIZE,GL_POINTS
from pyglet.window import shader
from  .Shaders.Shader import Shader_Program#custom shader program
from .Shaders.PointShader import Point_Shader
from core.coordinate_conversion import convert_to_screen_coordinate,convert_to_graph_coordinate
from objects.Scatter_plot import ScatterPlot
from objects.Grid_line import GridLine
from objects.Ticks import Ticks
from Groups.Scissor import Scissor
class Renderer:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.window = pyglet.window.Window(width,height)
        self.graphs = []

        #shader_programs
        self.shader_program = Shader_Program(width,height)
        self.point_shader = Point_Shader(width,height)


        ##batches

        self.graph_grids = pyglet.graphics.Batch()

        self.tick_batches = pyglet.graphics.Batch()

        self.scatter_plot_batch = pyglet.graphics.Batch()



    def draw_graph(self,graph):
        self.graphs.append(graph)
        scissor_group = Scissor(graph.x , graph.y , graph.width , graph.height , order = len(self.graphs))
        shader_group = ShaderGroup(self.shader_program,parent = scissor_group)
        graph.scissor_group = scissor_group
        graph.shader_group = shader_group
        x_ticks , y_ticks = graph.generate_ticks()
        x_coordinate =graph.x +  convert_to_screen_coordinate(x_ticks,graph.xlim,graph.width)
        y_coordinate =graph.y +  convert_to_screen_coordinate(y_ticks,graph.ylim,graph.height)


        grid_line =  GridLine(x_coordinate,y_coordinate,graph)
        lines_v = self.shader_program.vertex_list(
                len(grid_line.lines_v),
                GL_LINES,
                position = ('f',grid_line.lines_v.flatten()),
                batch = self.graph_grids,
                group = shader_group

            )
        lines_h = self.shader_program.vertex_list(
                len(grid_line.lines_h),
                GL_LINES,
                position = ('f',grid_line.lines_h.flatten()),
                batch = self.graph_grids,
                group = shader_group

            )
        grid_line.lines_v_vertex = lines_v
        grid_line.lines_h_vertex = lines_h


        tick = Ticks(graph,x_ticks,y_ticks)
        tick.initialize(self.tick_batches)
        graph.grid_object = grid_line
        graph.tick_object = tick
        self.update_graph(graph)

    def update_graph(self,graph):
        
        x_ticks , y_ticks = graph.generate_ticks()


        x_coordinate = graph.x + convert_to_screen_coordinate(x_ticks,graph.xlim,graph.width)
        y_coordinate = graph.y + convert_to_screen_coordinate(y_ticks,graph.ylim,graph.height)

        graph.tick_object.update_ticks(x_ticks,y_ticks,self.tick_batches)


        graph.grid_object.update_grid(x_coordinate,y_coordinate,graph)
        lines_v = self.shader_program.vertex_list(
            len(graph.grid_object.lines_v),
            GL_LINES,
            position = ('f',graph.grid_object.lines_v.flatten()),
            batch = self.graph_grids,
            group = graph.shader_group

        )
        lines_h = self.shader_program.vertex_list(
            len(graph.grid_object.lines_h),
            GL_LINES,
            position = ('f',graph.grid_object.lines_h.flatten()),
            batch = self.graph_grids,
            group = graph.shader_group

        )
        graph.grid_object.lines_v_vertex = lines_v
        graph.grid_object.lines_h_vertex = lines_h


        self.update_scatter_plots(graph,graph.xlim,graph.ylim)

    def plot_points(self,graph,x,y):
        x = np.array(x)
        y  = np.array(y)
        scatter_plot = ScatterPlot(x,y,graph)

        points = self.point_shader.vertex_list(
            len(scatter_plot.points),
            GL_POINTS,
            position = ('f',scatter_plot.points.flatten()),
            batch = self.scatter_plot_batch
        )
        
        scatter_plot.vertex_list = points
        graph.scatter_plots.append(scatter_plot)

    def update_scatter_plots(self,graph,xlim,ylim):
        for scatter_plt in graph.scatter_plots:
            scatter_plt.update_vertex_list(xlim,ylim)

    def draw(self):
        self.graph_grids.draw()
        self.tick_batches.draw()

        self.scatter_plot_batch.draw()

    def zoom(self,graph,x,y,scroll_y):
        if scroll_y == 0:
            return
        factor = 1.1 if scroll_y > 0 else 1 / 1.1

        x_n =  convert_to_graph_coordinate(x - graph.x  ,graph.xlim,graph.width)
        y_n =  convert_to_graph_coordinate(y,graph.ylim,graph.height)



        new_x_range = (graph.xlim[1] - graph.xlim[0])/factor

        new_y_range = (graph.ylim[1] - graph.ylim[0])/factor

        new_x_min = x_n  - (((x - graph.x) /graph.width)* new_x_range)
        new_y_min = y_n - ((y - graph.y)/graph.height) * new_y_range

        graph.xlim = (new_x_min,new_x_min + new_x_range)
        graph.ylim = (new_y_min, new_y_min + new_y_range)

        self.update_graph(graph)

    def pan(self,graph,dx,dy):
        graph.xlim =  np.array(graph.xlim ) - (dx/graph.width) * ((graph.xlim[1] - graph.xlim[0]))
        graph.ylim =  np.array(graph.ylim) - ((dy/graph.height) * (graph.ylim[1] - graph.ylim[0]))
        self.update_graph(graph)

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
            for graph in self.graphs:
                if (x >= graph.x and x <= (graph.x + graph.width) )and (y >= graph.y and y<= (graph.y + graph.height)):
                    self.zoom(graph,x,y,scroll_y)


        @self.window.event
        def on_mouse_drag(x,y,dx,dy,buttons,modifiers):
            for graph in self.graphs:
                if (x >= graph.x and x <= (graph.x + graph.width) )and (y >= graph.y and y<= (graph.y + graph.height)):
                    self.pan(graph,dx,dy)

        def update(dt):
            pass
        pyglet.clock.schedule_interval(update,1/60)
        pyglet.app.run()
