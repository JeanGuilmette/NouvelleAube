import sys
sys.path.append("../src")
from unittest import TestCase
from zone import Secteur

__author__ = 'SJS'


class TestSecteur(TestCase):
    def __createTestSector(self):
        self.secName = "TestA"
        self.terrain = "Plaine"
        self.resList = ("TestResA", "TestResB")
        self.sectorA = Secteur(self.secName, self.terrain, self.resList)
        
        self.secName = "TestB"
        self.terrain = "Foret"
        self.sectorB = Secteur(self.secName, self.terrain, self.resList)
                
    def testCreation(self):
        secName = "TestA"
        terrain = "Plaine"
        resList = ("Agriculture", "Chasse", "Peche", "Bois", "Metaux", "Pierre")
        s = Secteur(secName, terrain, resList)
        self.assertEqual(secName, s.name)
        self.assertEqual(50, s.spaceMax) 
        self.assertEqual(0, s.currentSpace)  
        self.assertEqual(5.0, s.TypeTerrain["Agriculture"])  
        self.assertEqual(0, s.GetCurrentPopulation())                             
        self.assertEqual(100000, s.GetMaxPopulation()) 

        # Check no building are create
        nbr = 0
        for z in s.batiments:
            nbr = nbr + 1
        self.assertEqual(nbr, 0) 
        
        # Check resource
#         found = 0
        for res in resList:
            self.assertIsNotNone(s.resources[res])

    def testUpdateProductionNoWorker(self):
        self.__createTestSector()
        self.sectorA.AddBuilding("TestA", (10,340))
        
        self.sectorA.UpdateProd()
        self.assertEqual(0, self.sectorA.resources["TestResA"].stock)
        self.assertEqual(1000, self.sectorA.resources["TestResA"].current)
        self.assertEqual(1000, self.sectorA.resources["TestResA"].max)  
                
        self.sectorB.UpdateProd()
        self.assertEqual(0, self.sectorA.resources["TestResB"].stock)
        self.assertEqual(5000, self.sectorA.resources["TestResB"].current)
        self.assertEqual(5000, self.sectorA.resources["TestResB"].max)        
        
    def testUpdateProductionWithWorker(self):
        self.__createTestSector()
        self.sectorA.AddBuilding("TestA", (10,340))
        self.sectorA.batiments["TestA"].AssignWorker(4)
        
        self.sectorA.UpdateProd()
        self.assertEqual(0, self.sectorA.resources["TestResA"].stock)
        self.assertEqual(1000, self.sectorA.resources["TestResA"].current)
        self.assertEqual(1000, self.sectorA.resources["TestResA"].max)  
                
        self.sectorB.UpdateProd()
        self.assertEqual(0, self.sectorB.resources["TestResB"].stock)
        self.assertEqual(5000, self.sectorB.resources["TestResB"].current)
        self.assertEqual(5000, self.sectorB.resources["TestResB"].max)    