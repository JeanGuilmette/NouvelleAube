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
        self.population = Population.Population(100000, 0.05)
        self.TypeTerrain = resources.terrainType[terrain]

        self.ConstructResourcesList(resList)
        
        for buildingType in Building.buildingDef:
            pos = (0,0)
            self.batiments[buildingType] = Building.Batiment(buildingType, pos)    

    def ConstructResourcesList(self, resList):
        for resName in resList:
            self.resources[resName] = resources.Resource(resName)

    def AddBuilding(self, buildingType, pos):
        #Check if resources are availble
        for resNeeded in self.batiments[buildingType].buildCost:
            if(self.resources[resNeeded].stock >= self.batiments[buildingType].buildCost[resNeeded]):
                pass
            else:
                print("Missing ressource")
                return "No ressource"
        #Remove resources
        for resNeeded in self.batiments[buildingType].buildCost:
            self.resources[resNeeded].stock -= self.batiments[buildingType].buildCost[resNeeded]
        #Add new building        
        self.batiments[buildingType].Add(pos)

    def RemoveBuilding(self, buildingType):
        self.batiments[buildingType].Remove()
        
    def draw(self):
        if(self.name.lower() == "region"):
            return pygame.image.load("image/islandMap.jpg")

        # Create region
        surface = pygame.Surface((600, 400))
        pygame.draw.rect(surface, COLORS.GREEN, [0, 0, 600, 400], 0)

        return surface

    def GetCurrentPopulation(self):
        return self.population.current
    
    def GetMaxPopulation(self):
        return self.population.popMax 
    
    def GetSante(self):
        return self.population.sante
    
    def GetBonheur(self):
        return self.population.bonheur
    
    def GetRecherche(self):
        return self.population.recherche
    
    def GetEducation(self):
        return self.population.education
    
    def GetPanique(self):
        return self.population.panique
    
    def GetCriminalite(self):
        return self.population.criminalite
    
    def GetInfluence(self):
        return self.population.influence    
    
    def GetPollution(self):
#         return self.population.valeur_de_polution() 
        return 222   
    
    def GetProduction(self):
        return 999 
    
    def GetTresors(self):
        return 111                   
    
    def GetRessourceInfo(self, resName):
        stock = 0
        available = 0
        stockMax = 0
        if resName in self.resources:
            stock = int(self.resources[resName].stock)
            available = int(self.resources[resName].current)
            stockMax = int(self.resources[resName].max)        
        return stock, available, stockMax
    
    
    def UpdateProd(self):
        for res in self.resources:
            prod = 0            
            for b in self.batiments:
                if(self.batiments[b].resType == res):
                    prod += self.batiments[b].ComputeProductivity(self.TypeTerrain[res], 1.0)
            self.resources[res].Adjustment(prod)

    
    
    def UpdatePopulation(self):
        self.population.PopulationAdjustment()
        
    def Initialize(self):
        self.resources["Agriculture"].stock = 10000
        self.resources["Chasse"].stock = 10000
        self.resources["Peche"].stock = 10000               
        self.resources["Bois"].stock = 1000
        self.resources["Metaux"].stock = 1000
        self.population.current = 5000

    def UpdateExpandRessource(self):
        #Nourrire la population
        self.resources["Agriculture"].stock -= 0.005 * self.population.current
        self.resources["Chasse"].stock -= 0.005 * self.population.current
        self.resources["Peche"].stock -= 0.005 * self.population.current
        if(self.resources["Agriculture"].stock <= 0):
            self.resources["Agriculture"].stock = 0
            self.population.bonheur -= 5
            self.population.criminalite += 5
            self.population.sante -= 2
        if(self.resources["Chasse"].stock <= 0):
            self.resources["Chasse"].stock = 0
            self.population.bonheur -= 5
            self.population.criminalite += 5
            self.population.sante -= 2  
        if(self.resources["Peche"].stock <= 0):
            self.resources["Peche"].stock = 0
            self.population.bonheur -= 5
            self.population.criminalite += 5
            self.population.sante -= 2