from time import sleep
from pygame.tests import surflock_test
__author__ = 'SJS'

import pygame
from defines import COLORS, FPS
import Building
import CustomWidget
import Island

import sys; sys.path.append("../lib")
from pgu import gui


class BuildingLabel(gui.Label):
    def __init__(self, island, activeZone, buildingName):
        self.buildingName = buildingName
        self.island = island
        self.zoneCtl = activeZone
        resString = ("%2d  " % (self.island.secteur[self.zoneCtl.value].batiments[self.buildingName].numberBuilding))
        gui.Label.__init__(self, value=resString)     
        
    def paint(self, surf):
        self.value = ("%2d  " % (self.island.secteur[self.zoneCtl.value].batiments[self.buildingName].numberBuilding))
        gui.Label.paint(self, surf)
        
        
class WorkerLabel(gui.Label):
    def __init__(self, island, activeZone, buildingName):
        self.island = island
        self.buildingName = buildingName
        self.zoneCtl = activeZone
        resString = ("%3d  " % (self.island.secteur[self.zoneCtl.value].batiments[self.buildingName].worker))
        gui.Label.__init__(self, value=resString)
        
    def paint(self, surf):
        self.value = ("%3d  " % (self.island.secteur[self.zoneCtl.value].batiments[self.buildingName].worker))
        gui.Label.paint(self, surf)
     
        
class WorkerSlider(gui.HSlider):
    def __init__(self, island, activeZone, buildingName): 
        self.island = island
        self.buildingName = buildingName
        self.zoneCtl = activeZone
        actual = self.island.secteur[self.zoneCtl.value].batiments[self.buildingName].worker  
        workermax = self.island.secteur[self.zoneCtl.value].batiments[self.buildingName].workerMax 
        gui.HSlider.__init__(self, value=actual,min=0,max=workermax,size=32,width=128,height=15) 
            
    def paint(self, surf):
        self.value = self.island.secteur[self.zoneCtl.value].batiments[self.buildingName].worker
        gui.HSlider.paint(self, surf)
  
class PopulationSlider(gui.HSlider):
    def __init__(self, island, zoneSrc, zoneDst): 
        self.island = island
        self.zoneCtlSrc = zoneSrc
        self.zoneCtlDst = zoneDst   
        maxVal = self.island.GetCurrentPopulation(self.zoneCtlSrc.value) + self.island.GetCurrentPopulation((self.zoneCtlDst.value))
        actual = maxVal - self.island.GetCurrentPopulation(self.zoneCtlSrc.value)

        gui.HSlider.__init__(self, value=actual,min=0,max=maxVal,size=32,width=128,height=15) 
        self.connect(gui.CHANGE, self.adjustPopulation)
            
    def paint(self, surf):
        self.max =  self.island.GetCurrentPopulation(self.zoneCtlSrc.value) + self.island.GetCurrentPopulation((self.zoneCtlDst.value))        
        self.value = self.max - self.island.GetCurrentPopulation(self.zoneCtlSrc.value)

        gui.HSlider.paint(self, surf)
        
    def adjustPopulation(self):
        self.island.secteur[self.zoneCtlSrc.value].population.current = self.value
        self.island.secteur[self.zoneCtlDst.value].population.current = (self.max - self.value)
                

class BuildMenu(gui.Dialog):
    def __init__(self, island):
        title = gui.Label("Building management")
        self.island = island
        self.ActiveZone = gui.Select(value=Island.LANDING_REGION_NAME , width=160, height=20)
        t = gui.Table()
        self.value = gui.Form()
        
        t.tr()
        for item in sorted(Island.secteurDef):
            if(item != Island.OVERVIEW_ZONE_NAME):
                self.ActiveZone.add(item, item)
        t.td(self.ActiveZone)
       
        t.tr()
        t.td(gui.Label("Building: "))
        t.td(gui.Label("Current"))
        for item in sorted(Building.buildingDef):
            t.tr()
            t.td(gui.Label(item))
            t.td(BuildingLabel(self.island, self.ActiveZone, item))
            b = gui.Button("Add")
            b.connect(gui.CLICK, self.action_addBuilding, item)
            t.td(b)
            b = gui.Button("Delete")
            b.connect(gui.CLICK, self.action_deleteBuilding, item)
            t.td(b)
             
            t.td(WorkerLabel(self.island, self.ActiveZone, item), colspan=3)
 
            e = WorkerSlider(self.island, self.ActiveZone, item)
            e.connect(gui.CHANGE,self.adjustWorker,e, item) 
            t.td(e)

        gui.Dialog.__init__(self,title,t)
        
    def action_addBuilding(self, Value):
        self.island.secteur[self.ActiveZone.value].AddBuilding(Value, (10,340))
        
    def action_deleteBuilding(self, Value):
        self.island.secteur[self.ActiveZone.value].RemoveBuilding(Value)
    
    def adjustWorker(self, ctl, building):
        zone = self.island.secteur[self.ActiveZone.value]
        if(zone.batiments[building].numberBuilding == 0):
            ctl.value = 0
            return
            
        if(ctl.value < 0):
            ctl.value = 0
        if(ctl.value > zone.batiments[building].workerMax):
            ctl.value = zone.batiments[building].workerMax
        if(ctl.value >= zone.GetAvailableWorker()):
            ctl.value = zone.GetAvailableWorker()
          
        a = ctl.value            
        while( a != zone.batiments[building].worker):
            if(a < zone.batiments[building].worker):
                zone.RemoveWorker(building)
            else:
                zone.AddWorker(building)   

                                                        
class TransferMenu(gui.Dialog):  
    def __init__(self, island):
        title = gui.Label("Resources Management")
        self.island = island
        self.ZoneSrc = gui.Select(value=Island.LANDING_REGION_NAME , width=160, height=20)
        self.ZoneDst = gui.Select(value="RegionB" , width=160, height=20)        
        t = gui.Table()
        self.value = gui.Form()
        
        # Origin and destination zone
        t.tr()
        for item in sorted(Island.secteurDef):
            if(item != Island.OVERVIEW_ZONE_NAME):
                self.ZoneSrc.add(item, item)
                self.ZoneDst.add(item, item)
        t.td(self.ZoneSrc)
        t.td(gui.Label("Origine"))
        t.td(gui.Label(""))   
        t.td(gui.Label("Destination"))
        t.td(self.ZoneDst)
        
        # Population
        t.tr()
        t.td(gui.Label("Population"))
        t.td(CustomWidget.DemographieLabel(self.island, self.ZoneSrc, "PopulationActive"))
        t.td(PopulationSlider(self.island, self.ZoneSrc, self.ZoneDst))
        t.td(CustomWidget.DemographieLabel(self.island, self.ZoneDst, "PopulationActive"))     
        

        gui.Dialog.__init__(self,title,t)
