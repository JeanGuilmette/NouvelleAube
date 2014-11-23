__author__ = 'SJS'

import pygame
import resources
import Population
import Building
from defines import COLORS


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
        self.nourriture = 0
        self.prodScience = 0
        self.prodBuilding = 0





########################################
########################################
class Secteur():
    __terrain = "none"
    __mod_erosion = "none"
    __size = ""
    __espace_entreposage = ""

    def __init__(self, name, terrain, resList):
        self.name = name               # Name of the zone
        self.spaceMax = 50             # Maximum available space on the zone
        self.currentSpace = 0          # Currently used space of the zone
        self.resources = dict()        # Available resource in the zone
        self.batiments = dict()        # List of building in the zone
        self.__population = Population.Population(100000, 5)
        self.TypeTerrain = resources.terrainType[terrain]

        self.ConstructResourcesList(resList)

    def ConstructResourcesList(self, resList):
        for resName in resList:
            self.resources[resName] = resources.Resource(resName)

    def AddBuilding(self, buildingType, pos):
        self.batiments[buildingType] = Building.Batiment(buildingType, pos)

    def draw(self):
        if(self.name.lower() == "region"):
            return pygame.image.load("image/islandMap.jpg")

        # Create region
        surface = pygame.Surface((600, 400))
        pygame.draw.rect(surface, COLORS.GREEN, [0, 0, 600, 400], 0)

        return surface
    
    def GetCurrentPopulation(self):
        return self.__population.current
    
    def GetMaxPopulation(self):
        return self.__population.popMax  
    
    def UpdateProd(self):
        for res in self.resources:
            prod = 0            
            for b in self.batiments:
                if(self.batiments[b].resType == res):
                    a = self.TypeTerrain[res]
                    c = self.batiments[b]
                    d = c.ComputeProductivity(a, 1.0)  
                    prod += d                  
#                     prod += self.batiments[b].ComputeProductivity(self.TypeTerrain[res], 1.0)
            self.resources[res].HourlyAdjustment(prod)
            
    def ComputeProduction(self, resource):
        pass

