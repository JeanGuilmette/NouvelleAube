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

    def __init__(self, name, terrain, resList, map, posList):
        self.name = name               # Name of the zone
        self.spaceList = posList       # Maximum available space on the zone
#         self.currentSpace = 0          # Currently used space of the zone
        self.resources = dict()        # Available resource in the zone
        self.batiments = dict()        # List of building in the zone
        self.population = Population.Population(100000, 0.05)
        self.TypeTerrain = Resources.terrainType[terrain]
        self.map = map
        
        self.ConstructResourcesList(resList)
        
        for buildingType in Building.buildingDef:
            self.batiments[buildingType] = Building.Batiment(buildingType)    

    def ConstructResourcesList(self, resList):
        for resName in resList:
            self.resources[resName] = Resources.Resource(resName)

    def AddBuilding(self, buildingType):
        #Check if resources are available
        for resNeeded in self.batiments[buildingType].buildCost:
            if(self.resources[resNeeded].stock >= self.batiments[buildingType].buildCost[resNeeded]):
                pass
            else:
                print("Missing ressource")
                return "No ressource"
            
        # Check space avaialble
        pos = "Not Found"
        for t in self.spaceList:
            if(t[2] == Building.buildingDef[buildingType]["pos"]):
                pos = (t[0], t[1])
                self.spaceList.remove(t)
                break
        
        if( pos == "Not Found"):
            msg = "Not enough space used: %d  max: %d" % (len(self.spaceList), self.batiments[buildingType].numberBuilding )
            print(msg)
            return "No space"
               
        #Add new building        
        self.batiments[buildingType].Add(pos)
        
        #Remove resources and use space
        for resNeeded in self.batiments[buildingType].buildCost:
            self.resources[resNeeded].stock -= self.batiments[buildingType].buildCost[resNeeded]
        return True
    
    def RemoveBuilding(self, buildingType):
        pos = self.batiments[buildingType].Remove()
        t = (pos[0], pos[1], Building.buildingDef[buildingType]["pos"])
        self.spaceList.insert(0, t) 
        
    def AddWorker(self, building):
        if(self.population.ActivateWorker() == True):
            self.batiments[building].AddWorker()
      
    def RemoveWorker(self, building):
        if(self.population.Deactivateworker() == True):
            self.batiments[building].RemoveWorker()   

    def draw(self):
        surface =  pygame.image.load(self.map)
        # Create building
        size = 100
        for building in self.batiments:
            imgBuild = pygame.image.load(self.batiments[building].image)
            scale1 = pygame.transform.scale(imgBuild, (size, size))  
            for index in range (0, self.batiments[building].numberBuilding):
                surface.blit(scale1, self.batiments[building].position[index] )
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
    
    def ModifyRessource(self, resName, newVal):
        if resName in self.resources:
            stock = int(self.resources[resName].stock) + int(newVal)
            stockMax = int(self.resources[resName].max)  
        if(stock < 0): stock = 0
        if(stock > stockMax): stock = stockMax
        self.resources[resName].stock = stock

    def ModifyPopulation(self, newVal):
        newPop = self.population.current + int(newVal)
        if(newPop < 0): newPop = 0
        if(newPop > self.population.popMax): newPop = self.population.popMax
        self.population.SetCurrentPopulation(newPop)
        
    def ModifySante(self, newVal):
        self.population.sante += int(newVal)
        
    def ModifyBonheur(self, newVal):
        self.population.bonheur += int(newVal)       
        
    def ModifyInfluence(self, newVal):
        self.population.influence += int(newVal) 
        
    def ModifyRecherche(self, newVal):
        self.population.recherche += int(newVal) 
        
    def ModifyEducation(self, newVal):
        self.population.education += int(newVal) 
        
    def ModifyCriminalite(self, newVal):
        self.population.criminalite += int(newVal) 
        
    def ModifyCroissance(self, newVal):
        self.population.croissance += int(newVal)  
        
    def ModifyPopulationMax(self, newVal):
        self.population.popMax += int(newVal)  
                                                                        
    def ModifyPanic(self, newVal):
        self.population.panique += int(newVal)
        
    
        