__author__ = 'SJS'
import time
import datetime
import pygame
from Defines import COLORS, FPS, FPS_MIN, FPS_MAX, FPS_DAY
import Resources
import Island
import Zone
import sys; sys.path.append("../lib")
from pgu import gui

class RessourceLabel(gui.Label):
    def __init__(self, island, activeZone, resName):
        self.resource = resName
        self.island = island
        self.zoneCtl = activeZone
        stock, available, stockMax = self.island.GetRessourceInfo(self.resource, self.zoneCtl.value)
        resString = ("{:0>6d} / {:0>6d} / {:0>6d}".format(stock, available, stockMax ))
        gui.Label.__init__(self, value=resString)
        
    def paint(self, surf):
        stock, available, stockMax = self.island.GetRessourceInfo(self.resource, self.zoneCtl.value)
        self.value = ("{:0>6d} / {:0>6d} / {:0>6d}".format(stock, available, stockMax ))
        gui.Label.paint(self, surf)
       
class StockLabel(gui.Label):
    def __init__(self, island, activeZone, resName):
        self.resource = resName
        self.island = island
        self.zoneCtl = activeZone
        stock, available, stockMax = self.island.GetRessourceInfo(self.resource, self.zoneCtl.value)
        resString = ("{:0>6d}".format(stock))
        gui.Label.__init__(self, value=resString)
        
    def paint(self, surf):
        stock, available, stockMax = self.island.GetRessourceInfo(self.resource, self.zoneCtl.value)
        self.value = ("{:0>6d}".format(stock))
        gui.Label.paint(self, surf)
        
              
class DemographieLabel(gui.Label):
    def __init__(self, island, activeZone, popName):
        self.popName = popName
        self.island = island
        self.zoneCtl = activeZone
        resString = self.BuildString()
        gui.Label.__init__(self, value=resString)
        
    def paint(self, surf):
        self.value = self.BuildString()
        gui.Label.paint(self, surf)     
        self.resize() 
      
    def BuildString(self):  
        if(self.popName == "PopulationActive"):
            return ("%6d   " % (self.island.GetCurrentPopulation(self.zoneCtl.value)))
        if(self.popName == "Population"):
            return ("%d/%d" % (self.island.GetCurrentPopulation(self.zoneCtl.value), self.island.GetPopulationMax(self.zoneCtl.value)) )
        elif(self.popName == "Worker"):
            return ("%d/%d/%d" % (self.island.GetCurrentWorker(self.zoneCtl.value), self.island.GetAvailableWorker(self.zoneCtl.value), self.island.GetMaxWorker(self.zoneCtl.value)) )
        elif("Sante"):
            return ("%2.2f" % self.island.GetSante(self.zoneCtl.value))
        elif(self.popName == "Bonheur"):
            return ("%2.2f" % self.island.GetBonheur(self.zoneCtl.value))
        elif(self.popName == "Recherche"):
            return ("%2.2f" % self.island.GetRecherche(self.zoneCtl.value))
        elif(self.popName == "Education"):
            return ("%2,2f" % self.island.GetEducation(self.zoneCtl.value))
        elif(self.popName == "Panique"):
            return ("%2,2f" % self.island.GetPanique(self.zoneCtl.value))
        elif(self.popName == "Criminalite"):
            return ("%2.2f" % self.island.GetCriminalite(self.zoneCtl.value))
        elif(self.popName == "Influence"):
            return ("%2.2f" % self.island.GetInfluence(self.zoneCtl.value))
        elif(self.popName == "Pollution"):
            return ("%2,2f" % self.island.GetPollution(self.zoneCtl.value))
        elif(self.popName == "Production"):
            return ("%d" % self.island.GetProduction(self.zoneCtl.value))
        elif(self.popName == "Tresors"):
            return ("%d" % self.island.GetTresors(self.zoneCtl.value))        
        else:
            return "Not Applicable"  
                       
class MapDisplay(gui.Widget):
    def __init__(self, zone, width, height):
        gui.Widget.__init__(self, width=width, height=height)
        self.island = zone        
   
    def paint(self, surf):
        zone = self.island.GetActiveZone()
        scale1 = pygame.transform.smoothscale(zone.draw(), (surf.get_width(), surf.get_height()))
        surf.blit(scale1, (0, 0))
#         pygame.display.update()   
        
class GameClock(gui.Label):
    def __init__(self):
        self.counter = 0
        self.day = FPS_DAY
        self.gameTime = datetime.date(2014, 12, 29) # Fisrt day of the game
        gui.Label.__init__(self, value=self.gameTime.isoformat())       
   
    def paint(self, surf):
        self.value =   self.gameTime.isoformat()
        gui.Label.paint(self, surf)  

        
    def Tick(self):
        self.counter += 1
        if(self.counter >= self.day):        
            self.gameTime += datetime.timedelta(days=1)
            self.counter = 0
            return True
        return False
           
