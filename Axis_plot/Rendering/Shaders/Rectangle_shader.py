import pyglet
from pyglet.graphics.shader import ShaderProgram,Shader

vertex_shader = """
    #version 330 core

    in vec2 position;
    in vec3 color;

    out vec4 final_color;

    void main(){
        gl_Position = transformation * vec4(position,0,1);
        final_color = color;
    }
"""

fragment_shader = """
    #version 330 core

    in vec3 final_color;
    out vec4 vertex_color;
    void main(){
        vertex_color = vec4(color , 1);
    }

"""

vertex_shader = Shader(vertex_shader , "vertex")
fragment_shader = Shader(fragment_shader , "fragment")



def RectangleShader(width,height):
    transformation_matrix = np.array([
            2/width ,0,0,0,
            0,  2/height,0,0,
            0,0,1,0,
            -1,-1,0,1
        ],dtype= np.float32)
    shader_program = ShaderProgram(vertex_shader,fragment_shader)
    shader_program["transformation"] = transformation_matrix
    return shader_program

