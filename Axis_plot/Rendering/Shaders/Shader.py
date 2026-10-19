import pyglet
from pyglet.graphics import ShaderGroup
from pyglet.graphics.shader import Shader,ShaderProgram
import numpy as np

vertex_shader = Shader(
    """
        #version 330 core

        in vec2 position;
        uniform mat4 transformation;

        void main(){
            gl_Position = transformation * vec4(position , 0,1);
        }
    ""","vertex"
)

fragment_shader = Shader(
    """
        #version 330 core

        out vec4 color;

        void main(){
            color = vec4(0,1,0,0.5);
        }
    ""","fragment"
)




def Shader_Program(width,height):
    transformation_matrix = np.array([
            2/width ,0,0,0,
            0,  2/height,0,0,
            0,0,1,0,
            -1,-1,0,1
        ],dtype= np.float32)
    shader_program = ShaderProgram(vertex_shader,fragment_shader)
    shader_program["transformation"] = transformation_matrix
    return shader_program
