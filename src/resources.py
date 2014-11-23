# This file contains information and code to define resource found on each sector.
#  1. Dictionary of existing resources and their base value.
#  2. Dictionary of terrain type and their base value.
#  3. Resource class used to trace resource state on a specific sector
#
# import EnjeuxSurvie
# import zone
__author__ = 'SJS'


resourceDef = dict(
    Agriculture = dict(unitMax=15000, delay=31, ratio=100, rate=10),
    Chasse = dict(unitMax = 7000, delay = 91, ratio = 100, rate = 20),
    Peche = dict(unitMax = 8000, delay = 91, ratio = 100, rate = 30),  # il faut garder les trois sortes de source de nourriture pour la partie <<des choix pour une gestion durable>> du jeu, meme chose pour les trois sortes de mat/riaux qui tant qu'a eux ne devrait pas etre integre en une seule ressorce, ''materiax''.
    Bois = dict(unitMax = 10000, delay = 365, ratio = 100, rate = 40),
    Metaux = dict(unitMax = 10000, delay = -10000, ratio = 100, rate = 0),
    Pierre = dict(unitMax = 8000, delay = -31000, ratio = 100, rate = 0),
    Nourriture = dict(unitMax = 2000, delay = -310000, ratio = 100, rate = 0),  # nourriture prepare pour etre mangeable pour la population (ransforme)
    Materiaux = dict(unitMax = 2000, delay = -310000, ratio = 100, rate = 0),  # il va vraiment falloir utuliser les ressouces decrite plus haut, sinon perte de l'ampleur des catastrophes
    Energie = dict(unitMax = 2000, delay = -310000, ratio = 100, rate = 0),  # il n'y a pas vraiment de maximun d'energie produit. Devrait etre ailleurs, avec l'argent
    TestResA = dict(unitMax = 1000, delay = 31, ratio = 100, rate = 1),  # Should not be modified, used to valid internal mechanic of the game
    TestResB = dict(unitMax = 5000, delay = 31, ratio = 100, rate = 10)  # Should not be modified, used to valid internal mechanic of the game
    )


terrainType = dict(
    Plaine = dict(Agriculture = 5.0, Chasse  = 1.0, Peche  =  0, Bois = 0.75, Metaux = 0.25 , Pierre = 0.35 ),
    Foret = dict(Agriculture = 0.75, Chasse  = 2.0, Peche  =  0, Bois = 4.0, Metaux = 0.1 , Pierre = 0.1  ),
    Collines = dict(Agriculture = 0.5, Chasse  = 0.75, Peche  =  0, Bois = 0.5, Metaux = 4.0 , Pierre = 5.0 ),
    Volcan = dict(Agriculture = 0, Chasse  = 0.1, Peche  =  0, Bois = 0.1, Metaux = 5.0 , Pierre = 5.0 ),
    Marecage = dict(Agriculture = 0.4, Chasse  = 1.0, Peche  =  1.0, Bois = 0.5, Metaux = 0.1 , Pierre = 0.1 ),
    EauxDouces = dict(Agriculture = 0, Chasse  = 0, Peche  =  6.0, Bois = 0, Metaux = 0 , Pierre = 0 ),
    EauxSalees = dict(Agriculture = 0, Chasse  = 0, Peche  =  8.0, Bois = 0 , Metaux = 0 , Pierre = 0 )
    )


# # This class identify resource type available and define its behavior in the game
class Resource(object):

    def __init__(self, name):
        self.name = name        # Name/ID of the resource
        self.stock = 0          # Number of resource available in storage
        self.current = resourceDef[name]["unitMax"]  # Number of resource unit available for producer to extract of this zone.
        self.max = resourceDef[name]["unitMax"]      # Maximum raw resource the zone could contain
        self.regenDelay = resourceDef[name]["delay"]
        self.regenDay = 0
        self.regenRate = resourceDef[name]["rate"]
        self.regenRatio = resourceDef[name]["ratio"]

    def HourlyAdjustment(self, prod):
        self.stock += prod
        self.current -= prod

    def DailyAdjustment(self):
        self.regenDay +=1;
        if self.regenDay == self.regenDelay:
            self.current = self.current + (self.current/self.regenRatio) * self.regenRate
            self.current = self.current if(self.current <= self.max) else self.max
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