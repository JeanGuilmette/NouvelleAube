__author__ = 'SJS'

import pygame
import resources
import Population
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


class Island(object):
    def __init__(self, filename):
        self.secteur = []
        self.activeZone = None                      # Which zone player currently examine or work with
        if(filename == "new"):
            self.create()
        else:
            self.load(filename)

    # load game information from saved file
    def load(self, filename):
        pass

    # Create new game with inital value
    def create(self):
        resList = ("Nourriture", "Materiaux", "Energie")
        zone = Secteur("Region", resList)
        self.secteur.append(["Region", zone])
        zone = Secteur("Saguenay", resList)
        self.secteur.append(["Saguenay", zone])
        zone = Secteur("Gaspesis", resList)
        self.secteur.append(["Gaspesis", zone])
        self.activeZone = self.secteur[0]

    def get_current_population(self):
        pass

    def get_max_population(self):
        pass


########################################
########################################
class Secteur():
    __terrain = "none"
    __mod_erosion = "none"
    __size = ""
    __espace_entreposage = ""

    def __init__(self, name, resList):
        self.name = name               # Name of the zone
        self.spaceMax = 50             # Maximum available space on the zone
        self.currentSpace = 0          # Currently used space of the zone
        self.resources = dict()        # Available resource in the zone
        self.batiments = dict()        # List of building in the zone
        self.__population = Population.Population(100000, 5)

        self.ConstructResourcesList(resList)

    def ConstructResourcesList(self, resList):
        for resName in resList:
            self.resources[resName] = resources.Resource(resName)

    def AddBuilding(self, building):
        pass

    def draw(self):
        if(self.name.lower() == "region"):
            return pygame.image.load("image/islandMap.jpg")

        # Create region
        surface = pygame.Surface((600, 400))
        pygame.draw.rect(surface, COLORS.GREEN, [0, 0, 600, 400], 0)
        
        return surface
