__author__ = 'SJS'
from enum import Enum

buildingDef = dict( \
    Farm = dict(imgName = "farm.jpg", workerMax = 100),
    Mines  =  dict(imgName = "mine.jpg", workerMax = 100)
    )


class BatimentTypes(Enum):
    Mine = 0
    Moulin = 1
    Entrepot = 2
    Forge = 3


class Batiment(object):
    def __init__(self, buildingType, img, pos, wkMax):
        self.name = BatimentTypes(buildingType).name
        self.image = img
        self.position = pos
        self.worker = 0
        self.workerMax = wkMax