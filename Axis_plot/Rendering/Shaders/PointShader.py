import numpy as np
from pyglet.graphics.shader import Shader,ShaderProgram




vertex_shader = Shader(
    """
        #version 330 core

        in vec2 position;
        uniform mat4 transformation; 

        uniform int mode;
        flat out int plot_mode;
        void main(){
            gl_Position  = transformation * vec4(position , 0 , 1);
            if (mode == 0){
                gl_PointSize = 6;
            }
            plot_mode = mode;
        }
    ""","vertex"
)

fragment_shader = Shader(
    """
        #version 330 core
        flat in int plot_mode;
        out vec4 color; 
        void main(){
            color = vec4(0,1,0,1);

            vec2 coord = gl_PointCoord - vec2(0.5);

            if (plot_mode == 0){
                if (dot(coord,coord) > 0.25 ){
                    discard;
                }
            }
        }
    ""","fragment"
)




def Point_Shader(width,height):
    transformation_matrix = np.array([
            2/width ,0,0,0,
            0,  2/height,0,0,
            0,0,1,0,
            -1,-1,0,1
        ],dtype= np.float32)
    shader_program = ShaderProgram(vertex_shader,fragment_shader)
    shader_program.use()
    shader_program["transformation"] = transformation_matrix
    shader_program["mode"] = 1
    return shader_program
