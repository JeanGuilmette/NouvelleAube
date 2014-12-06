__author__ = 'SJS'

# import pygame
# import resources
# import Population
# import Building
import zone
# from defines import COLORS

secteurDef = dict(
    Region = dict(terType = "Foret", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Metaux", "Pierre") ),
    Saguenay = dict(terType = "Foret", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Metaux", "Pierre") ),
    Gaspesis = dict(terType = "Plaine", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Metaux", "Pierre") ),    
    )

class Island(object):
    def __init__(self, filename):
        self.secteur = dict()
        self.__activeZone = None                      # Which zone player currently examine or work with
        if(filename == "new"):
            self.__create()
        else:
            self.__load(filename)

    # load game information from saved file
    def __load(self, filename):
        pass

    # Create new game with inital value
    def __create(self):
        for sectorName in secteurDef:
            self.secteur[sectorName] = zone.Secteur(sectorName, secteurDef[sectorName]["terType"], secteurDef[sectorName]["resList"])
        self.__activeZone = "Region"

    def GetActiveZone(self):
        return self.secteur[self.__activeZone]
    
    def SetActiveZone(self, zoneName):
        self.__activeZone = zoneName
        
    def GetCurrentPopulation(self):
        pop = 0
        for zone in self.secteur:
            if(zone != "Region"):            
                pop += self.secteur[zone].GetCurrentPopulation()
        return pop 

    def GetPopulationMax(self):
        popMax = 0
        for zone in self.secteur:
            if(zone != "Region"):
                popMax += self.secteur[zone].GetMaxPopulation()
        return popMax 

    def AddBuilding(self, zoneName, buildingName, pos):
        self.secteur[zoneName].AddBuilding(buildingName, pos)
        
    def UpdateProd(self):
        for zone in self.secteur:
            if(zone != "Region"):
                self.secteur[zone].UpdateProd()