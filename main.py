'''
    Object-oriented framework for pyOpenGL wrapper.

    @date: May 23, 2011
    @author: Shao-Chuan Wang (shaochuan.wang AT gmail.com)
'''
__version__ = '1.0'

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

from component import Ball
from app import App


window_size = (640, 480)
window_name = 'Animation'
app = App()
app.drawDelegate = TwoDRenderer(window_size)

def initialization():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(*window_size)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow(window_name)
    glutDisplayFunc(app.onDraw)
    glutIdleFunc(app.onIdle)
    glutReshapeFunc(app.onResize)
    glutKeyboardFunc(app.onKey)

def main():
    initialization()
    glutMainLoop()

if __name__ == '__main__':
    main()
