import sys
sys.path.append("../src")
from unittest import TestCase
from Personnage import Personnage

__author__ = 'SJS'


class TestPersonnage(TestCase):
    def testCreation(self):
        p = Personnage('Stella', 9)
        self.assertEquals('Stella', p.name)
        self.assertEquals(True, p.vivant)
        self.assertEquals(9, p.condition_physique)


    def testDoubleCreation(self):
        p = Personnage('Stella', 9)
        q = Personnage('Francis', 99)
        self.assertEquals('Stella', p.name)
        self.assertEquals(True, p.vivant)
        self.assertEquals(9, p.condition_physique)