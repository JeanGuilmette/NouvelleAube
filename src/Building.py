__author__ = 'SJS'

buildingDef = dict( \
    TestA = dict(resType = "Agriculture", imgName = "testA.jpg", workerMax = 10, secteur = "primaire", space = 4, buildcost = dict( bois = 345, metaux = 6), buildTime = 5, entretient = 0.1, prerequis = "" ),
    Farm = dict(resType = "Agriculture", imgName = "farm.jpg", workerMax = 10, secteur = "primaire", space = 4, buildcost = dict( bois = 345, metaux = 6), buildTime = 5, entretient = 0.1, prerequis = "" ),
    Mines  =  dict(resType = "Metaux", imgName = "mine.jpg", workerMax = 100, secteur = "primaire", space = 2, buildcost = dict( bois = 345, metaux = 6), buildTime = 5, entretient = 0.1, prerequis = "" ),
    Moulin = dict(resType = "Agriculture", imgName = "moulin.jpg", workerMax = 100, secteur = "secondaire", space = 1, buildcost = dict( bois = 345, metaux = 6), buildTime = 5, entretient = 0.1, prerequis = "" ),
    Boulangerie = dict(resType = "Agriculture", imgName = "boulangerie.jpg", workerMax = 100, secteur = "tertiaire", space = 1, buildcost = dict( bois = 345, metaux = 6), buildTime = 5, entretient = 0.1, prerequis = "" )
    )


class Batiment(object):
    def __init__(self, name, pos):
        self.name = name                                 # Name to identify building
        self.image = buildingDef[name]["imgName"]        # Filename of image to represent building on map (on zoom information?)
        self.resType = buildingDef[name]["resType"]      # 
        self.position = pos                              # Position of building on map (zone)
        self.worker = 0                                  # Current number of worker affected to building
        self.workerMax = buildingDef[name]["workerMax"]  # Maximum number of worker that could work in this building
        self.secteur = buildingDef[name]["secteur"]      # Activity sector of the building
        self.space = buildingDef[name]["space"]          # Space used by the building
        self.buildCost = buildingDef[name]["buildcost"]  # Resource needed to build the building
        self.buildTime = buildingDef[name]["buildTime"]  # Time needed to complete construction of the building
        self.maintain = buildingDef[name]["entretient"]  # Resource needed to maintain the building operational
        self.prerequis = buildingDef[name]["prerequis"]  # Science or Building require before building this building
        self.energyNeeded = 0                            # Unit of energy to operate the building
        self.waterAvailable = 0                          # Acces to water to operate the building
        self.accessToRoad = 0                            # Acces to transportation network
        self.Communication = 0                           # Access to internet, radio, TV, onde courte
        self.bonusproduction = 1.0                       # Bonus multiplicatif de la production de batiments du secteur.

    def ComputeProductivity(self, terrainBonus, moralBonus):
        return self.bonusproduction * self.worker * terrainBonus * moralBonus

    def Maintenance(self):
        pass

    def isOperational(self):
        return True if (self.worker > 0) else False
    
    def AssignWorker(self, nbrWorker):
        self.worker = (self.worker + nbrWorker) if( (self.worker + nbrWorker) <= self.workerMax) else self.workerMax
        self.worker = self.worker if (self.worker >= 0) else 0