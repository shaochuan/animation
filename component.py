
from OpenGL.GL import *
from math import sin, cos, atan2, pi


class Component(object):
    def draw(self):
        raise NotImplementedError
    def step(self, dt):
        raise NotImplementedError

class Ball(Component):
    resolution = 64
    circle_points = [(cos(t*2*pi/resolution), sin(t*2*pi/resolution)) for t in xrange(0, resolution)]
    def __init__(self, center=(0.0,0.0),
                       velocity=(0.0,0.0),
                       radius=1,
                       mass=1.0,
                       is_solid=True,
                       color = (1.0,0.0,0.0)
                       ):
        self.center = center
        self.velocity = velocity
        self.radius = radius
        self.mass = mass
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

    def step(self, dt, integrator=None):
        self.center, self.velocity = integrator.step(self.center,
                self.velocity, (0,0,0), dt)

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


class Halfplane(object):
    def __init__(self, intercept=(0.0,0.0),
                       normal=(0.0,1.0),
                       color = (1.0,0.0,0.0)
                       ):
        self.intercept = intercept
        self.normal = normal
        self.color = color

    def step(self, *args):
        pass

    def draw(self):
        x = self.intercept
        n = self.normal
        glPushMatrix()
        theta = -360.0 * atan2(n[0], n[1])/(2.0*pi)

        glTranslated(x[0], x[1], 0)
        glRotated(theta, 0, 0, 1.0)

        glBegin(GL_TRIANGLES)
        glColor3f(*self.color)
        glVertex4d(0.0, 0.0, 0.0, 1.0)
        glVertex4d(1.0, 0.0, 0.0, 0.0)
        glVertex4d(0.0,-1.0, 0.0, 0.0)
        glVertex4d(0.0, 0.0, 0.0, 1,0)
        glVertex4d(-1.0,0.0, 0.0, 0.0)
        glVertex4d(0.0,-1.0, 0.0, 0.0)
        glEnd()

        glPopMatrix()
