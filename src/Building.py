__author__ = 'SJS'

buildingDef = dict( \
    Farm = dict(resType = "Agriculture", imgName = "image/farm.jpg", workerMax = 10, secteur = "primaire", space = 40, buildcost = dict( Bois = 345, Minerais = 6), buildTime = 5, entretient = 0.1, prerequis = "" ),
    Mines  =  dict(resType = "Metaux", imgName = "image/mine.jpg", workerMax = 100, secteur = "primaire", space = 2, buildcost = dict( Bois = 345, Minerais = 6), buildTime = 5, entretient = 0.1, prerequis = "" ),
    Moulin = dict(resType = "Agriculture", imgName = "image/moulin.jpg", workerMax = 100, secteur = "secondaire", space = 1, buildcost = dict( Bois = 345, Minerais = 6), buildTime = 5, entretient = 0.1, prerequis = "" ),
    Boulangerie = dict(resType = "Agriculture", imgName = "image/boulangerie.jpg", workerMax = 100, secteur = "tertiaire", space = 1, buildcost = dict( Bois = 345, Minerais = 6), buildTime = 5, entretient = 0.1, prerequis = "" ),
    Bucheron = dict(resType = "Bois", imgName = "image/Camp.jpg", workerMax = 20, secteur = "primaire", space = 5, buildcost = dict( Bois = 0, Minerais = 6), buildTime = 5, entretient = 0.1, prerequis = "" )
    )


class Batiment(object):
    def __init__(self, name, pos):
        self.name = name                                 # Name to identify building
        self.image = buildingDef[name]["imgName"]        # Filename of image to represent building on map (on zoom information?)
        self.resType = buildingDef[name]["resType"]      # 
        self.position = pos                              # Position of building on map (zone)
        self.numberBuilding = 0                          # Number of building constructed in zone
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
        limitMaxWorker = (self.workerMax * self.numberBuilding)
        self.worker = (self.worker + nbrWorker) if( (self.worker + nbrWorker) <= limitMaxWorker ) else limitMaxWorker
        self.worker = self.worker if (self.worker >= 0) else 0
        
    def Add(self, pos):
        self.numberBuilding = self.numberBuilding + 1 
        
    def Remove(self):
        self.numberBuilding = self.numberBuilding - 1
        self.numberBuilding = self.numberBuilding if (self.numberBuilding >= 0) else 0    
        self.AssignWorker(0)    
        
    def AddWorker(self):
        val = self.worker + 1
        limitMaxWorker = self.workerMax * self.numberBuilding
        self.worker = val if( val <= limitMaxWorker ) else limitMaxWorker
        
    def RemoveWorker(self):
        self.worker = self.worker - 1
        self.worker = self.worker if (self.worker >= 0) else 0  
        
