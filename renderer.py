from OpenGL.GL import *
from OpenGL.GLUT import glutSwapBuffers

class DrawDelegate(object):
    def onDraw(self):
        raise NotImplementedError


class TwoDRenderer(DrawDelegate):
    def __init__(self, size):
        self.size = size
        self.objs = [Ball((0,0)), Ball((1,0))]    # expect each obj has draw method

    def onDraw(self):
        # Clear The Screen And The Depth Buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glTranslatef(0.0, 0.0, -10.0)
        for obj in self.objs:
            obj.draw()
        glutSwapBuffers()

