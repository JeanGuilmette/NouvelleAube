__author__ = 'SJS'
import time
import datetime
import pygame
from defines import COLORS, FPS, FPS_MIN, FPS_MAX, FPS_DAY
import resources
import Island
import zone
import sys; sys.path.append("../lib")
from pgu import gui

class RessourceLabel(gui.Label):
    def __init__(self, island, resName):
        self.resource = resName
        self.island = island
        stock, available, stockMax = self.island.GetRessourceInfo(self.resource)
        resString = ("{:0>6d} / {:0>6d} / {:0>6d}".format(stock, available, stockMax ))
        gui.Label.__init__(self, value=resString)
        
    def paint(self, surf):
        stock, available, stockMax = self.island.GetRessourceInfo(self.resource)
        self.value = ("{:0>6d} / {:0>6d} / {:0>6d}".format(stock, available, stockMax ))
        gui.Label.paint(self, surf)
       
class DemographieLabel(gui.Label):
    def __init__(self, island, popName):
        self.popName = popName
        self.island = island
        resString = self.BuildString()
        gui.Label.__init__(self, value=resString)
        
    def paint(self, surf):
        self.value = self.BuildString()
        gui.Label.paint(self, surf)      
      
    def BuildString(self):  
        if(self.popName == "Population"):
            return ("%d/%d" % (self.island.GetCurrentPopulation(), self.island.GetPopulationMax()) )
        elif(self.popName == "Worker"):
            return ("%d/%d/%d" % (self.island.GetCurrentWorker(), self.island.GetAvailableWorker(), self.island.GetMaxWorker()) )
        elif("Sante"):
            return ("%d" % self.island.GetSante())
        elif(self.popName == "Bonheur"):
            return ("%d" % self.island.GetBonheur())
        elif(self.popName == "Recherche"):
            return ("%d" % self.island.GetRecherche())
        elif(self.popName == "Education"):
            return ("%d" % self.island.GetEducation())
        elif(self.popName == "Panique"):
            return ("%d" % self.island.GetPanique())
        elif(self.popName == "Criminalite"):
            return ("%d" % self.island.GetCriminalite())
        elif(self.popName == "Influence"):
            return ("%d" % self.island.GetInfluence())
        elif(self.popName == "Pollution"):
            return ("%d" % self.island.GetPollution())
        elif(self.popName == "Production"):
            return ("%d" % self.island.GetProduction())
        elif(self.popName == "Tresors"):
            return ("%d" % self.island.GetTresors())        
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