import sys
sys.path.append("../src")
from unittest import TestCase
from Island import Island

__author__ = 'SJS'


class TestIsland(TestCase):
    def testCreationNew(self):
        i = Island("new")
        nbr = 0
        for z in i.secteur:
            nbr = nbr + 1
        self.assertGreater(nbr, 0)
        self.assertEqual(0, i.GetCurrentPopulation())
        self.assertEqual(200000, i.GetPopulationMax())

    def testUpdateProduction(self):
        i = Island("new")
        nbr = 0
        for z in i.secteur:
            nbr = nbr + 1
        self.assertGreater(nbr, 0)
        self.assertEqual(0, i.GetCurrentPopulation())
        self.assertEqual(200000, i.GetPopulationMax())    
        
        i.UpdateProd()    