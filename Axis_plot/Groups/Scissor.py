import pyglet
from pyglet.gl import glDisable, glScissor,glEnable ,GL_SCISSOR_TEST

class Scissor(pyglet.graphics.Group):
    def __init__(self,x,y,width,height,order=0):
        super().__init__(order = order)
        self.x = int(x)
        self.y =int( y)
        self.width = int(width)
        self.height = int(height)

    def set_state(self):
        print("SCISSOR ENABLED:", self.x, self.y, self.width, self.height)
        glEnable(GL_SCISSOR_TEST)
        glScissor(self.x,self.y,self.width,self.height)

    def unset_state(self):
        print("Scissor disabled")
        glDisable(GL_SCISSOR_TEST)
