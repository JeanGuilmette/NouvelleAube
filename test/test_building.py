import sys
sys.path.append("../src")
from unittest import TestCase
from Building import buildingDef, Batiment

__author__ = 'SJS'


class TestBuilding(TestCase):
    def testCreation(self):
        name = "TestA"
        pos = (10, 34)
        b = Batiment(name, pos)
        
        # Valid fixed value at construction
        self.assertEqual(name, b.name)
        self.assertEqual(pos, b.position)  
        self.assertEqual(0, b.worker)       
        self.assertEqual(0, b.energyNeeded)  
        self.assertEqual(0, b.waterAvailable)     
        self.assertEqual(0, b.accessToRoad)  
        self.assertEqual(0, b.Communication)  
        self.assertEqual(1.0, b.bonusproduction)                  
                
        # Valid value set from dictionnary                        
        self.assertEqual(buildingDef[name]["imgName"], b.image) 
        self.assertEqual(buildingDef[name]["resType"], b.resType)        
        self.assertEqual(buildingDef[name]["workerMax"], b.workerMax)  
        self.assertEqual(buildingDef[name]["secteur"], b.secteur)         
        self.assertEqual(buildingDef[name]["space"], b.space) 
        self.assertEqual(buildingDef[name]["buildcost"], b.buildCost) 
        self.assertEqual(buildingDef[name]["buildTime"], b.buildTime) 
        self.assertEqual(buildingDef[name]["entretient"], b.maintain)
        self.assertEqual(buildingDef[name]["prerequis"], b.prerequis)        
        
        self.assertEqual(False, b.isOperational()) 
        
    def testAssisgnWorker(self):
        # Create  building
        b = Batiment("TestA", (10, 34))     
        self.assertEqual(False, b.isOperational()) 
        #add 4 worker 
        b.AssignWorker(4)
        self.assertEqual(True, b.isOperational())  
        self.assertEqual(4, b.worker)   
        # assign 4 more 
        b.AssignWorker(4)
        self.assertEqual(True, b.isOperational())  
        self.assertEqual(8, b.worker)          
        # Assign more worker than maximum allowed           
        b.AssignWorker(4)
        self.assertEqual(True, b.isOperational())  
        self.assertEqual(b.workerMax, b.worker)   
        # Remove worker
        b.AssignWorker(-4)
        self.assertEqual(True, b.isOperational())  
        self.assertEqual(6, b.worker)  
        b.AssignWorker(-4)
        self.assertEqual(True, b.isOperational())  
        self.assertEqual(2, b.worker)
        b.AssignWorker(-4)
        self.assertEqual(False, b.isOperational())  
        self.assertEqual(0, b.worker)             
                        
    def testComputeProductivityNoWorker(self):
        b = Batiment("TestA", (10, 34))     
        self.assertEqual(False, b.isOperational())        
        self.assertEqual(0, b.ComputeProductivity(0.5, 1.0))   
        self.assertEqual(0, b.ComputeProductivity(-0.5, 100.0))  
        
    def testComputeProductivityWithWorker(self):
        b = Batiment("TestA", (10, 34))  
        b.AssignWorker(5)       
        self.assertEqual(True, b.isOperational())
        self.assertEqual(2.5, b.ComputeProductivity(0.5, 1.0))   
  