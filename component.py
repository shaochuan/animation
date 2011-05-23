
from OpenGL.GL import *
from math import sin, cos, pi


class Component(object):
    def draw(self):
        raise NotImplementedError

class Ball(Component):
    resolution = 64
    circle_points = [(cos(t*2*pi/resolution), sin(t*2*pi/resolution)) for t in xrange(0, resolution)]
    def __init__(self, center=(0.0,0.0),
                       radius=1,
                       is_solid=True,
                       color = (1.0,0.0,0.0)
                       ):
        self.center = center
        self.radius = radius
        self.color = color
        self.is_solid = is_solid

    @property
    def xyz(self):
        return self.center[0], self.center[1], 0.0
    @property
    def x(self):
        return self.center[0]
    @property
    def y(self):
        return self.center[1]

    def draw(self):
        if self.is_solid:
            self.draw_solid()
        else:
            self.draw_hollow()

    def draw_solid(self):
        selfx = self.x
        selfy = self.y

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(*self.color)
        glVertex3f(*self.xyz)
        for x,y in self.circle_points:
            glVertex3f(self.radius*x+selfx, self.radius*y+selfy, 0.0)
        firstx = self.circle_points[0][0]
        firsty = self.circle_points[0][1]
        glVertex3f(self.radius*firstx + selfx, self.radius*firsty+selfy,0.0)
        glEnd()

    def draw_hollow(self):
        selfx = self.x
        selfy = self.y
        glBegin(GL_LINE_LOOP)
        glColor3f(*self.color)
        for x,y in self.circle_points:
            glVertex3f(self.radius*x+selfx, self.radius*y+selfy, 0.0)
        glEnd()

