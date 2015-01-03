import sys
from unittest import TestCase
sys.path.append("../src")
import resources


class TestResource(TestCase):

    def testCreation(self):
        r = resources.Resource('TestResA')
        self.assertEquals('TestResA', r.name)
        self.assertEquals(0, r.stock)
        self.assertEquals(1000, r.current)
        self.assertEquals(1000, r.max)
        self.assertEquals(31, r.regenDelay)
        self.assertEquals(0, r.regenDay)
        self.assertEquals(1, r.regenRate)
        self.assertEquals(100, r.regenRatio)


    def testDoubleCreation(self):
        r1 = resources.Resource('TestResB')
        r = resources.Resource('TestResA')
        self.assertEquals('TestResA', r.name)
        self.assertEquals(0, r.stock)
        self.assertEquals(1000, r.current)
        self.assertEquals(1000, r.max)
        self.assertEquals(31, r.regenDelay)
        self.assertEquals(0, r.regenDay)
        self.assertEquals(1, r.regenRate)
        self.assertEquals(100, r.regenRatio)
        
        self.assertEquals('TestResB', r1.name)
        self.assertEquals(0, r1.stock)
        self.assertEquals(5000, r1.current)
        self.assertEquals(5000, r1.max)
        self.assertEquals(31, r1.regenDelay)
        self.assertEquals(0, r1.regenDay)
        self.assertEquals(10, r1.regenRate)
        self.assertEquals(100, r1.regenRatio)      

    def testHourlyAdjustementNoProd(self):
        r = resources.Resource('TestResB')
        # Check if initial value of resource are valid
        self.assertEquals(0, r.stock)
        self.assertEquals(5000, r.current)
        self.assertEquals(5000, r.max)

        # Apply hourly production without any production modifier
        r.Adjustment(0)
        self.assertEquals(0, r.stock)
        self.assertEquals(5000,r.current)
        self.assertEquals(5000, r.max)

    def testHourlyAdjustementScienceProd(self):
        r = resources.Resource('TestResB')
        # Apply hourly production with science production modifier
        r.Adjustment(10)
        self.assertEquals(10, r.stock)
        self.assertEquals(4990,r.current)
        self.assertEquals(5000, r.max)


    def testHourlyAdjustementBuildingProd(self):
        r = resources.Resource('TestResB')
        # Apply hourly production with science production modifier
        r.Adjustment(10)
        self.assertEquals(10, r.stock)
        self.assertEquals(4990,r.current)
        self.assertEquals(5000, r.max)


    def testHourlyAdjustementProdWithPanic(self):
        r = resources.Resource('TestResB')
        # Apply hourly production with panic modifier
        r.Adjustment(20)
        self.assertEquals(20, r.stock)
        self.assertEquals(4980,r.current)
        self.assertEquals(5000, r.max)