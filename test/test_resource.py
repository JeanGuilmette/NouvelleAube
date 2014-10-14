import sys
from unittest import TestCase
sys.path.append("../src")
from resources import *
from zone import ZoneModifier

class TestResource(TestCase):

    def testCreation(self):
        r = Resource('TestResA')
        self.assertEquals('TestResA', r.name)
        self.assertEquals(0, r.stock)
        self.assertEquals(1000, r.current)
        self.assertEquals(1000, r.max)
        self.assertEquals(31, r.regenDelay)
        self.assertEquals(0, r.regenDay)
        self.assertEquals(1, r.regenRate)
        self.assertEquals(100, r.regenRatio)


    def testDoubleCreation(self):
        r1 =  Resource('TestResB')
        r = Resource('TestResA')
        self.assertEquals('TestResA', r.name)
        self.assertEquals(0, r.stock)
        self.assertEquals(1000, r.current)
        self.assertEquals(1000, r.max)
        self.assertEquals(31, r.regenDelay)
        self.assertEquals(0, r.regenDay)
        self.assertEquals(1, r.regenRate)
        self.assertEquals(100, r.regenRatio)

    def testHourlyAdjustementNoProd(self):
        r = Resource('TestResB')
        zoneMod = ZoneModifier("Science")

        # Check if initial value of resource are valid
        self.assertEquals(0, r.stock)
        self.assertEquals(5000, r.current)
        self.assertEquals(5000, r.max)

        # Apply hourly production without any production modifier
        r.HourlyAdjustment(zoneMod)
        self.assertEquals(0, r.stock)
        self.assertEquals(5000,r.current)
        self.assertEquals(5000, r.max)

    def testHourlyAdjustementScienceProd(self):
        r = Resource('TestResB')
        zoneMod = ZoneModifier("Science")
        zoneMod.prodScience = 10

        # Apply hourly production with science production modifier
        r.HourlyAdjustment(zoneMod)
        self.assertEquals(10, r.stock)
        self.assertEquals(4990,r.current)
        self.assertEquals(5000, r.max)


    def testHourlyAdjustementBuildingProd(self):
        r = Resource('TestResB')
        zoneMod = ZoneModifier("Science")
        zoneMod.prodBuilding = 10

        # Apply hourly production with science production modifier
        r.HourlyAdjustment(zoneMod)
        self.assertEquals(10, r.stock)
        self.assertEquals(4990,r.current)
        self.assertEquals(5000, r.max)


    def testHourlyAdjustementProdWithPanic(self):
        r = Resource('TestResB')
        zoneMod = ZoneModifier("Science")
        zoneMod.prodBuilding = 25
        zoneMod.prodScience = 15
        zoneMod.panique = 0.5

        # Apply hourly production with panic modifier
        r.HourlyAdjustment(zoneMod)
        self.assertEquals(20, r.stock)
        self.assertEquals(4980,r.current)
        self.assertEquals(5000, r.max)