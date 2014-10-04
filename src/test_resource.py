from unittest import TestCase
from resources import *
from zone import ZoneModifier

class TestResource(TestCase):

    def testCreation(self):
        r = Resource('Chasse')
        self.assertEquals('Chasse', r.name)
        self.assertEquals(0, r.stock)
        self.assertEquals(1000, r.current)
        self.assertEquals(1000, r.max)
        self.assertEquals(31, r.regenDelay)
        self.assertEquals(0, r.regenDay)
        self.assertEquals(1, r.regenRate)
        self.assertEquals(100, r.regenRatio)


    def testDoubleCreation(self):
        r1 =  Resource('Agriculture')
        r = Resource('Chasse')
        self.assertEquals('Chasse', r.name)
        self.assertEquals(0, r.stock)
        self.assertEquals(1000, r.current)
        self.assertEquals(1000, r.max)
        self.assertEquals(31, r.regenDelay)
        self.assertEquals(0, r.regenDay)
        self.assertEquals(1, r.regenRate)
        self.assertEquals(100, r.regenRatio)

    def testHourlyAdjustementNoProd(self):
        r = Resource('Agriculture')
        zoneMod = ZoneModifier()

        # Check if initial value of resource are valid
        self.assertEquals(0, r.stock)
        self.assertEquals(5000, r.current)
        self.assertEquals(5000, r.max)

        # Apply hourly production without any production modifier
        r.HourlyAdjustment(100, zoneMod)
        self.assertEquals(0, r.stock)
        self.assertEquals(5000,r.current)
        self.assertEquals(5000, r.max)

    def testHourlyAdjustementScienceProd(self):
        r = Resource('Agriculture')
        zoneMod = ZoneModifier()
        zoneMod.prodScience = 10

        # Apply hourly production with science production modifier
        r.HourlyAdjustment(100, zoneMod)
        self.assertEquals(10, r.stock)
        self.assertEquals(4990,r.current)
        self.assertEquals(5000, r.max)


    def testHourlyAdjustementBuildingProd(self):
        r = Resource('Agriculture')
        zoneMod = ZoneModifier()
        zoneMod.prodBuilding = 10

        # Apply hourly production with science production modifier
        r.HourlyAdjustment(100, zoneMod)
        self.assertEquals(10, r.stock)
        self.assertEquals(4990,r.current)
        self.assertEquals(5000, r.max)


    def testHourlyAdjustementProdWithPanic(self):
        r = Resource('Agriculture')
        zoneMod = ZoneModifier()
        zoneMod.prodBuilding = 25
        zoneMod.prodScience = 15
        zoneMod.panique = 50

        # Apply hourly production with panic modifier
        r.HourlyAdjustment(100, zoneMod)
        self.assertEquals(20, r.stock)
        self.assertEquals(4980,r.current)
        self.assertEquals(5000, r.max)