
import re

import draw
from component import Ball

def parseConf(string):
    pat = re.compile(r'\w+:')
    attrstrs = [a.strip() for a in pat.split(string) if a.strip()]
    clses = [c.replace(':','').strip() for c in pat.findall(string)]
    components = []
    for clsn, attrs in zip(clses, attrstrs):
        attrs = attrs.split()
        clsobj = globals()[clsn]
        comp = clsobj()
        for a in attrs:
            k,v = a.split('=')
            k = k.strip()
            v = v.strip()
            setattr(comp, k, eval(v))
        components.append(comp)
    return components

def loadSceneComponents(confFileName):
    fd = open(confFileName)
    components = parseConf(fd.read())
    fd.close()
    return components


class DummyScene(draw.DrawDelegate):
    def __init__(self):
        self.components = []

class Scene(draw.DrawDelegate):
    def __init__(self, components=[]):
        self.components = components

    @classmethod
    def fromConfigFile(cls, confFileName):
        scene = cls()
        scene.components = loadSceneComponents(confFileName)
