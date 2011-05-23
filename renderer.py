from OpenGL.GL import *
from OpenGL.GLUT import glutSwapBuffers
import draw

class TwoDRenderer(draw.DrawDelegate):
    def __init__(self, size, objs=[]):
        self.size = size
        self.objs = objs    # expect each obj has draw method

    def onDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glTranslatef(0.0, 0.0, -10.0)
        for obj in self.objs:
            obj.draw()
        glutSwapBuffers()

