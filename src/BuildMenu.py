from time import sleep
from pygame.tests import surflock_test
__author__ = 'SJS'

import pygame
import Building
import CustomWidget
import Island
import Resources

import sys; sys.path.append("../lib")
from pgu import gui

##########################################################
#
##########################################################
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
        
 
 ##########################################################
#
##########################################################       
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
     
 
##########################################################
#
##########################################################        
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
 
 
##########################################################
#
##########################################################
class PopulationSlider(gui.HSlider):
    def __init__(self, island, zoneSrc, zoneDst): 
        self.island = island
        self.zoneCtlSrc = zoneSrc
        self.zoneCtlDst = zoneDst 
        gui.HSlider.__init__(self, value=0,min=0,max=100,size=32,width=128,height=15) 
        self.SetInternalValue()        
        self.connect(gui.CHANGE, self.adjustPopulation)
            
    def paint(self, surf):
        self.value = self.populationToMove
        gui.HSlider.paint(self, surf)
        
    def adjustPopulation(self):
        self.populationToMove = self.value
        self.island.secteur[self.zoneCtlSrc.value].population.current =  self.src - self.populationToMove
        self.island.secteur[self.zoneCtlDst.value].population.current =  self.dst + self.populationToMove        
          
    def Refresh(self):
        self.SetInternalValue()   
        
    def SetInternalValue(self): 
        self.populationToMove = 0        
        self.src = self.island.GetCurrentPopulation(self.zoneCtlSrc.value)
        self.dst = self.island.GetCurrentPopulation(self.zoneCtlDst.value)  
        self.max = self.src     
      
       
##########################################################
#
##########################################################
class ResourcesSlider(gui.HSlider):
    def __init__(self, island, zoneSrc, zoneDst, resName): 
        self.island = island
        self.zoneCtlSrc = zoneSrc
        self.zoneCtlDst = zoneDst 
        self.resName = resName
        gui.HSlider.__init__(self, value=0,min=0,max=100,size=32,width=128,height=15) 
        self.SetInternalValue()        
        self.connect(gui.CHANGE, self.adjusResource)
            
    def paint(self, surf):
        self.value = self.resourceToMove
        gui.HSlider.paint(self, surf)
        
    def adjusResource(self):
        self.resourceToMove = self.value
        self.island.secteur[self.zoneCtlSrc.value].resources[self.resName].stock =  self.src - self.resourceToMove
        self.island.secteur[self.zoneCtlDst.value].resources[self.resName].stock =  self.dst + self.resourceToMove        
          
    def Refresh(self):
        self.SetInternalValue()   
        
    def SetInternalValue(self): 
        self.resourceToMove = 0        
        self.src, a, m = self.island.GetRessourceInfo(self.resName, self.zoneCtlSrc.value)
        self.dst, a, m = self.island.GetRessourceInfo(self.resName, self.zoneCtlDst.value)  
        self.max = self.src   


##########################################################
#
##########################################################
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

##########################################################
#
##########################################################                                                        
class TransferMenu(gui.Dialog):  
    def __init__(self, island):
        title = gui.Label("Resources Management")
        self.island = island
        self.ZoneSrc = gui.Select(value=Island.LANDING_REGION_NAME , width=160, height=20)
        self.ZoneDst = gui.Select(value="RegionB" , width=160, height=20)        
        t = gui.Table()
        self.value = gui.Form()
        self.widgetList = []
        
        # Origin and destination zone
        t.tr()
        for item in sorted(Island.secteurDef):
            if(item != Island.OVERVIEW_ZONE_NAME):
                self.ZoneSrc.add(item, item)
                self.ZoneDst.add(item, item)
        self.ZoneSrc.connect(gui.CHANGE, self.action_ChangeZone, "src")
        self.ZoneDst.connect(gui.CHANGE, self.action_ChangeZone, "dst")        
        t.td(self.ZoneSrc)
        t.td(gui.Label("Origine"))
        t.td(gui.Label(""))   
        t.td(gui.Label("Destination"))
        t.td(self.ZoneDst)
        
        # Population
        t.tr()
        t.td(gui.Label("Population"))
        t.td(CustomWidget.DemographieLabel(self.island, self.ZoneSrc, "PopulationActive"))
        s = PopulationSlider(self.island, self.ZoneSrc, self.ZoneDst)
        self.widgetList.append(s)
        t.td(s)
        t.td(CustomWidget.DemographieLabel(self.island, self.ZoneDst, "PopulationActive"))     

        
        # Resources
        for item in sorted(Resources.resourceDef):         
            t.tr()
            t.td(gui.Label(item))
            t.td(CustomWidget.StockLabel(self.island, self.ZoneSrc, item))
            s = ResourcesSlider(self.island, self.ZoneSrc, self.ZoneDst, item)
            self.widgetList.append(s)
            t.td(s)
            t.td(CustomWidget.StockLabel(self.island, self.ZoneDst, item))     

        gui.Dialog.__init__(self,title,t)

    def action_TransferPopulation(self, slider):
        slider.populationToMove
        self.island.secteur[self.ZoneSrc.value].population.current -=  slider.populationToMove
        self.island.secteur[self.ZoneDst.value].population.current +=  slider.populationToMove
    
    def action_ChangeZone(self, origin):
        if(self.ZoneSrc.value == self.ZoneDst.value):
            zoneCtl = self.ZoneDst if(origin == "src") else self.ZoneSrc  
            i =  zoneCtl.values.index(zoneCtl.top_selected.value)
            i = 0 if(i+1 >= len(zoneCtl.values)) else (i+1)
            zoneCtl.value =  zoneCtl.values[i].value 
        for w in self.widgetList:
            w.Refresh()
 