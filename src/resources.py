__author__ = 'SJS'

resourceDef = dict( \
    Agriculture = dict(unitMax = 15000, delay = 31, ratio = 100, rate = 10),
    Chasse  = dict(unitMax = 7000, delay = 91, ratio = 100, rate = 20),
    Peche  = dict(unitMax = 8000, delay = 91, ratio = 100, rate = 30),
    BoisCom  = dict(unitMax = 10000, delay = 365, ratio = 100, rate = 40),
    BoisRare = dict(unitMax = 5000, delay = 730, ratio = 100, rate = 40),
    MetauxCom  = dict(unitMax = 10000, delay = -10000, ratio = 100, rate = 0),
    MetauxRare  = dict(unitMax = 3000, delay = -31000, ratio = 100, rate = 0),
    PierreCom  = dict(unitMax = 8000, delay = -31000, ratio = 100, rate = 0),
    PierreRare  = dict(unitMax = 1000, delay = -310000, ratio = 100, rate = 0),
    Petrole  = dict(unitMax = 2000, delay = -310000, ratio = 100, rate = 0),
    )


# # This class identify resource type available and define its behavior in the game
class Resource():

    def __init__(self, name):
        self.name = name        # Name/ID of the resource
        self.stock = 0          # Number of resource available in storage
        self.current = resourceDef[name]["unitMax"]  # Number of resource unit available for producer to extract of this zone.
        self.max = resourceDef[name]["unitMax"]      # Maximum raw resource the zone could contain
        self.regenDelay = resourceDef[name]["delay"]
        self.regenDay = 0
        self.regenRate = resourceDef[name]["rate"]
        self.regenRatio = resourceDef[name]["ratio"]

    def HourlyAdjustment(self, zoneMod):
        prod = (zoneMod.prodScience + zoneMod.prodBuilding) * (1 - zoneMod.panique)
        self.stock += prod
        self.current -= prod

    def DailyAdjustment(self):
        self.regenDay +=1;
        if self.regenDay == self.regenDelay :
            self.current = self.current + (self.current/self.regenRatio) * self.regenRate
            self.regenDay = 0

    def Unserialize(self, resDict):
            self.stock = resDict['Stock']
            self.current = resDict['Current']


    def Serialize(self):
        data = dict(
            Name = self.name,
            Stock = self.stock,
            Current = self.current,
        )
        return data