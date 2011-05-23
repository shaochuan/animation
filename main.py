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
import scene
from renderer import TwoDRenderer

def printHelp():
    print '''
    Usage:
        $ python main.py -i scene_filename
    '''

def getSceneFileName():
    if '-i' in sys.argv:
        ind = sys.argv.index('-i')
        return sys.argv[ind+1]
    else:
        print >> sys.stderr, "Scene File Not Found!"
        printHelp()
        sys.exit(1)

window_size = (640, 480)
window_name = 'Animation'
app = App()
components = scene.loadSceneComponents(getSceneFileName())
app.scene = scene.Scene(components)
app.drawDelegate = TwoDRenderer(window_size, components)


def initialization():
    glutInit([])
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
