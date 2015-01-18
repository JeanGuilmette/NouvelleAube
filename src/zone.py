__author__ = 'SJS'

import pygame
import Resources
import Population
import Building
from Defines import COLORS

########################################
class Secteur():
    __terrain = "none"
    __mod_erosion = "none"
    __size = ""
    __espace_entreposage = ""

    def __init__(self, name, terrain, resList, map):
        self.name = name               # Name of the zone
        self.spaceMax = 50             # Maximum available space on the zone
        self.currentSpace = 0          # Currently used space of the zone
        self.resources = dict()        # Available resource in the zone
        self.batiments = dict()        # List of building in the zone
        self.population = Population.Population(100000, 0.05)
        self.TypeTerrain = Resources.terrainType[terrain]
        self.map = map
        
        self.ConstructResourcesList(resList)
        
        for buildingType in Building.buildingDef:
            pos = (0,0)
            self.batiments[buildingType] = Building.Batiment(buildingType, pos)    

    def ConstructResourcesList(self, resList):
        for resName in resList:
            self.resources[resName] = Resources.Resource(resName)

    def AddBuilding(self, buildingType, pos):
        #Check if resources are availble
        for resNeeded in self.batiments[buildingType].buildCost:
            if(self.resources[resNeeded].stock >= self.batiments[buildingType].buildCost[resNeeded]):
                pass
            else:
                print("Missing ressource")
                return "No ressource"
            
        # Check space avaialble
        if( (self.currentSpace + self.batiments[buildingType].space) > self.spaceMax):
            print("Not enough space needed: %d used: %d  max: %d" % (self.batiments[buildingType].space, self.currentSpace, self.spaceMax) )
            return "No space"
        
        #Remove resources and use space
        for resNeeded in self.batiments[buildingType].buildCost:
            self.resources[resNeeded].stock -= self.batiments[buildingType].buildCost[resNeeded]
            
        self.currentSpace += self.batiments[buildingType].space  
        
        #Add new building        
        self.batiments[buildingType].Add(pos)

    def RemoveBuilding(self, buildingType):
        self.batiments[buildingType].Remove()
        self.currentSpace -= self.batiments[buildingType].space
        
    def AddWorker(self, building):
        if(self.population.ActivateWorker() == True):
            self.batiments[building].AddWorker()
      
    def RemoveWorker(self, building):
        if(self.population.Deactivateworker() == True):
            self.batiments[building].RemoveWorker()   

    def draw(self):
        surface =  pygame.image.load(self.map)
        # Create building
        size = 50
        posX = 50
        posY = 50
        for building in self.batiments:
            for index in range (0, self.batiments[building].numberBuilding):
                imgBuild = pygame.image.load(self.batiments[building].image)
                scale1 = pygame.transform.scale(imgBuild, (size, size))                
                surface.blit(scale1, (posX, posY))
                posX += size #imgBuild.get_rect().width
                if(posX > surface.get_rect().width -50):
                    posY += size
                    posX = 50
        return surface

    def GetCurrentPopulation(self):
        return self.population.current
    
    def GetMaxPopulation(self):
        return self.population.popMax 

    def GetCurrentWorker(self):
        return self.population.workerCurrent  
    
    def GetMaxWorker(self):
        return self.population.workerMax     
    
    def GetAvailableWorker(self):
        return self.population.workerIdle
    
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
        self.resources["Agriculture"].stock = 5000
        self.resources["Chasse"].stock = 1000
        self.resources["Peche"].stock = 1000               
        self.resources["Bois"].stock = 1000
        self.resources["Minerais"].stock = 1000
        self.population.SetCurrentPopulation(1000)

    def UpdateExpandRessource(self):
        if(self.population.current > 0):
            #Nourrire la population
            self.resources["Agriculture"].stock -= 0.005 * self.population.current
            self.resources["Chasse"].stock -= 0.005 * self.population.current
            self.resources["Peche"].stock -= 0.005 * self.population.current
            if(self.resources["Agriculture"].stock <= 0):
                self.resources["Agriculture"].stock = 0
                self.population.bonheur -= 0.5
                self.population.criminalite += 0.5
                self.population.sante -= 0.22
            if(self.resources["Chasse"].stock <= 0):
                self.resources["Chasse"].stock = 0
    #             self.population.bonheur -= 0.5
    #             self.population.criminalite += 0.5
    #             self.population.sante -= 0.2  
            if(self.resources["Peche"].stock <= 0):
                self.resources["Peche"].stock = 0
    #             self.population.bonheur -= 0.5
    #             self.population.criminalite += 0.5
    #             self.population.sante -= 0.2