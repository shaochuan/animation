from env import Environment

class ExplicitEuler(object):
    def step(self, xx, vv, aa, dt):
        xp = []
        vp = []
        for x, v, a in zip(xx,vv,aa):
            xp.append( x + dt*v )
            vp.append( v + dt*a )
        return xp, vp

class SemiImplicitEuler(object):
    def step(self, xx, vv, aa, dt):
        xp = []
        vp = []
        for x, v, a in zip(xx,vv,aa):
            vp.append( v + dt*a )
            xp.append( x + dt*v )
        return xp, vp


def getIntegrator():
    if Environment.integrator == 'ExplicitEuler':
        return ExplicitEuler()
    elif Environment.integrator == 'SemiImplicitEuler':
        return SemiImplicitEuler()
