from enum import Enum
#import Population
from resources import *


__author__ = 'SJS'

class ZoneModifier():
    def __init__(self, source):
        self.source = source
        self.production = 0
        self.bonheur = 0
        self.sante = 0
        self.criminalite = 0
        self.influence = 0
        self.polution = 0
        self.Education = 0
        self.recherche = 0
        self.panique = 0
        self.nourriture =0
        self.prodScience = 1
        self.prodBuilding = 1



class Secteur():
    terrain = "none"
    mod_erosion = "none"
    size = ""
    espace_entreposage = ""
    #population = Population.Population(100000, 5)
    batiments = []

    def __init__(self, name, resList):
        self.name = name
        self.resources = dict()
        self.ConstructResources(resList)
        

    def ConstructResources(self, resList):
        for resName in resList:
            self.resources[resName] =  Resource(resName)
