from time import sleep
__author__ = 'SJS'

import pygame
from defines import COLORS, FPS
import Building

import sys; sys.path.append("../lib")
from pgu import gui

class BuildingLabel(gui.Label):
    def __init__(self, zone, BuildingName):
        self.BuildingName = BuildingName
        self.zone = zone
        resString = ("%d" % (self.zone.batiments[self.BuildingName].numberBuilding))
        gui.Label.__init__(self, value=resString)              
        
    def paint(self, surf):
        self.value = ("%d" % (self.zone.batiments[self.BuildingName].numberBuilding))
        gui.Label.paint(self, surf)
        
        
class WorkerLabel(gui.Label):
    def __init__(self, zone, BuildingName):
        self.BuildingName = BuildingName
        self.zone = zone
        resString = ("%d" % (self.zone.batiments[self.BuildingName].worker))
        gui.Label.__init__(self, value=resString)

        
    def paint(self, surf):
        self.value = ("%d" % (self.zone.batiments[self.BuildingName].worker))
        gui.Label.paint(self, surf)
        self.resize()
              
        
class BuildMenu(gui.Dialog):
    def __init__(self, display, zone, pos):
        title = gui.Label("Building management")
        self.zone = zone
        t = gui.Table()
        self.value = gui.Form()
        
        t.tr()
        t.td(gui.Label("Building: "))
        t.td(gui.Label("Current"))
        for index, item in enumerate(Building.buildingDef):
            t.tr()
            t.td(gui.Label(item))
            t.td(BuildingLabel(zone, item))
            b = gui.Button("Add")
            b.connect(gui.CLICK, self.action_addBuilding, item)
            t.td(b)
            b = gui.Button("Delete")
            b.connect(gui.CLICK, self.action_deleteBuilding, item)
            t.td(b)
             

            t.td(WorkerLabel(zone, item))           
            b = gui.Button("Add")
            b.connect(gui.CLICK, self.action_addWorker, item)
            t.td(b)  
            
            b = gui.Button("Remove")
            b.connect(gui.CLICK, self.action_removeWorker, item)
            t.td(b) 

        gui.Dialog.__init__(self,title,t)
        
    def action_addBuilding(self, Value):
        self.zone.AddBuilding(Value, (10,340))
        
    def action_deleteBuilding(self, Value):
        self.zone.RemoveBuilding(Value)
    
    def action_addWorker(self, Value):
        self.zone.AddWorker(Value)
    
    def action_removeWorker(self, Value):
        self.zone.RemoveWorker(Value)