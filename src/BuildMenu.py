# from time import sleep
# from pygame.tests import surflock_test
__author__ = 'SJS'

import pygame
import Building
import CustomWidget
import Island
import Resources
import EventEffectAnalyse


import sys; sys.path.append("../lib"); sys.path.append("../src")
from pgu import gui

##########################################################
#
##########################################################
class BuildingLabel(gui.Label):
    def __init__(self, island, activeZone, buildingName):
        self.buildingName = buildingName
        self.island = island
        self.zoneCtl = activeZone
        resString = ("%d" % (self.island.secteur[self.zoneCtl.value].batiments[self.buildingName].numberBuilding))
        gui.Label.__init__(self, value=resString)     
        
    def paint(self, surf):
        self.value = ("%d" % (self.island.secteur[self.zoneCtl.value].batiments[self.buildingName].numberBuilding))
        gui.Label.paint(self, surf)
        
 
 ##########################################################
#
##########################################################       
class WorkerLabel(gui.Label):
    def __init__(self, island, activeZone, buildingName):
        self.island = island
        self.buildingName = buildingName
        self.zoneCtl = activeZone
        resString = (" %4d  " % (self.island.secteur[self.zoneCtl.value].batiments[self.buildingName].worker))
        gui.Label.__init__(self, value=resString)
        
    def paint(self, surf):
        self.value = (" %4d  " % (self.island.secteur[self.zoneCtl.value].batiments[self.buildingName].worker))
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
        workermax = self.island.secteur[self.zoneCtl.value].batiments[self.buildingName].GetMaxWorker() 
        gui.HSlider.__init__(self, value=actual,min=0,max=workermax,size=32,width=128,height=15) 
            
    def paint(self, surf):
        self.value = self.island.secteur[self.zoneCtl.value].batiments[self.buildingName].worker
        self.max =  self.island.secteur[self.zoneCtl.value].batiments[self.buildingName].GetMaxWorker()
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
    def __init__(self, island, zone):
        title = gui.Label("Building management")
        self.island = island
        self.ActiveZone = gui.Select(value=Island.LANDING_REGION_NAME , width=160, height=20)
        self.ImpactAnalyse = EventEffectAnalyse.EventImpact(island)
        
        t1 = gui.Table()
        
        self.value = gui.Form()
        t1.tr()
        for item in sorted(Island.secteurDef):
            if(item != Island.OVERVIEW_ZONE_NAME):
                self.ActiveZone.add(Island.secteurDef[item]["name"], item)
        t1.td(self.ActiveZone, align=-1)
        if(zone == Island.OVERVIEW_ZONE_NAME) : zone = Island.LANDING_REGION_NAME
        self.ActiveZone.value = zone
        
        t1.tr()
        buildingName = gui.Select(value="Ferme" , width=160, height=20)
        t = gui.Table()   
        t.tr()
        t.td(gui.Label("Bâtiment:"))
        t.td(gui.Label("   "))        
        for item in sorted(Building.buildingDef):
            buildingName.add(item, item)
            t.tr()
            l = gui.Label(item)
            t.td(gui.Label(item), align = 1)
            t.td(gui.Label("   "))            
            # Remove building
            b = gui.Button("-")
            b.connect(gui.CLICK, self.action_deleteBuilding, item)
            t.td(b, align =1)     
            # Number of building       
            t.td(BuildingLabel(self.island, self.ActiveZone, item), algin=0)
            # add Building
            b = gui.Button("+")
            b.connect(gui.CLICK, self.action_addBuilding, item)
            t.td(b)
             
            #Number of worker
            e = WorkerSlider(self.island, self.ActiveZone, item)
            e.connect(gui.CHANGE,self.adjustWorker,e, item) 
            t.td(e)
            t.td(WorkerLabel(self.island, self.ActiveZone, item), align =-1)    
            b = gui.Button(" ? ")   
            b.connect(gui.CLICK, self.action_info, item)   
            t.td(b)   

        t1.td(t)
#         t2 = gui.Table()
#         t2.tr()
#         t2.td(buildingName)
#         buildingName.connect(gui.CHANGE, self.actionBuildingDesc, buildingName)
        
#         t2.tr()
#         doc =  CreateDescription("Ferme", 400)
#         self.displayDesc = gui.ScrollArea(doc, 400, 300, hscrollbar=False,  vscrollbar=True)
#         t2.td(self.displayDesc)
        
#         t1.td(t2)
                
#         s = pygame.image.load("image/Nouvelle_Aube.jpg")
#         gui.Dialog.__init__(self,title,t, background=gui.Image(s))
        gui.Dialog.__init__(self,title, t1)        
        
    def actionBuildingDesc(self, ctl):
        self.displayDesc.widget = CreateDescription(ctl.value, 400)
        
        
    def action_addBuilding(self, Value):
        result = self.island.secteur[self.ActiveZone.value].AddBuilding(Value)
        if(result != True):
            msgbox = CustomWidget.MessageBox("Add Building", result)
            msgbox.open()
        self.ImpactAnalyse.ApplyBuildingEffect("Add Building", self.ActiveZone.value, Building.buildingEffect[Value]["add"])
        
    def action_deleteBuilding(self, Value):
        self.island.secteur[self.ActiveZone.value].RemoveBuilding(Value)
        self.ImpactAnalyse.ApplyBuildingEffect("Remove Building", self.ActiveZone.value, Building.buildingEffect[Value]["remove"])        
    
    def adjustWorker(self, ctl, building):
        zone = self.island.secteur[self.ActiveZone.value]
        if(zone.batiments[building].numberBuilding == 0):
            ctl.value = 0
            return
            
        if(ctl.value < 0):
            ctl.value = 0
        if(ctl.value > zone.batiments[building].GetMaxWorker()):
            ctl.value = zone.batiments[building].GetMaxWorker()
        if(ctl.value >= zone.GetAvailableWorker()):
            ctl.value = zone.GetAvailableWorker()
          
        a = ctl.value            
        while( a != zone.batiments[building].worker):
            if(a < zone.batiments[building].worker):
                zone.RemoveWorker(building)
            else:
                zone.AddWorker(building)   
                
    def action_info(self, buildingName):
        db = BuildingInfo(buildingName)
        db.open()

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
                self.ZoneSrc.add(Island.secteurDef[item]["name"], item)
                self.ZoneDst.add(Island.secteurDef[item]["name"], item)
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



class BuildingInfo(gui.Dialog):
    def __init__(self, buildingName): 
        
        title = gui.Label(buildingName)
        t = gui.Table()
        t.tr()
        doc = CreateDescription(buildingName, 400)
        t.td(gui.ScrollArea(doc, 400, 300, hscrollbar=False,  vscrollbar=True))
        
        t.tr()
        b = gui.Button("Close")
        b.connect(gui.CLICK, self.action_quit)  
        t.td(b)  
            
        gui.Dialog.__init__(self, title, t, background=( 128, 128, 128, 10) )
     
          
    def action_quit(self):
        pygame.event.post(pygame.event.Event(pygame.QUIT))  
                                  
    def open(self, w=None, x=None, y=None):
        gui.Dialog.open(self)
        done = False
        while not done:
            pygame.time.wait(5)             
            self.get_toplevel().update()
            pygame.display.update()
            # Process events
            for ev in pygame.event.get():
                if (ev.type == pygame.QUIT or 
                    ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE):
                    done = True
                else:
                    # Pass the event off to pgu
                    self.get_toplevel().event(ev)
        self.close()
                        
#///////////////////////////////////////////////////////////////////////////////////////////
#///
#/// 
def CreateDescription(buildingName, width, align=-1, fontName=None, fontSize=30):
    font = pygame.font.SysFont(fontName, fontSize)        
    space = font.size(" ")      
    text =Building.buildingDesc[buildingName]
    doc = gui.Document(width=width) 
    doc.block(align=align)
    doc.add(gui.Image(Building.buildingDef[buildingName]["imgName"]),align=1)    
    for word in text.split(" "): 
        doc.add(gui.Label(word))
        doc.space(space)
    return doc