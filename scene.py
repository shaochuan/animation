
import re

import draw
from component import *
from env import Environment
import integrator

def loadConf(string):
    ''' Parse the config file and load the environment variables.
    '''
    pat = re.compile(r'\w+:')
    attrstrs = [a.strip() for a in pat.split(string) if a.strip()]
    clses = [c.replace(':','').strip() for c in pat.findall(string)]
    components = []
    for clsn, attrs in zip(clses, attrstrs):
        attrs = [a.strip() for a in attrs.split('\n') if a.strip()]
        clsobj = globals()[clsn]
        if clsn == 'Environment':
            target_obj = clsobj    # overwrite environment setting
        else:
            target_obj = clsobj()  # new a component

        for a in attrs:
            k,v = a.split('=')
            k = k.strip()
            v = v.strip()
            setattr(target_obj, k, eval(v))
        if clsn != 'Environment':
            components.append(target_obj)
    return components

def loadSceneComponents(confFileName):
    fd = open(confFileName)
    components = loadConf(fd.read())
    fd.close()
    return components


class DummyScene(draw.DrawDelegate):
    def __init__(self):
        self.components = []

    def step(self, dt):
        pass



class Scene(draw.DrawDelegate):
    def __init__(self, components=[]):
        self.components = components

    @classmethod
    def fromConfigFile(cls, confFileName):
        scene = cls()
        scene.components = loadSceneComponents(confFileName)

    def step(self, dt):
        for c in self.components:
            c.step(dt, integrator.getIntegrator())
