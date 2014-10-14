__author__ = 'SJS'

buildingDef = dict( \
    Farm = dict(imgName = "farm.jpg", workerMax = 10, secteur = "primaire", space = 4, buildcost = dict(argent = 1000, bois = 345, metaux = 6), buildTime = 5, entretient = 0.1, prerequis = "" ),
    Mines  =  dict(imgName = "mine.jpg", workerMax = 100, secteur = "primaire", space = 2, buildcost = dict(argent = 1000, bois = 345, metaux = 6), buildTime = 5, entretient = 0.1, prerequis = "" ),
    Moulin = dict(imgName = "moulin.jpg", workerMax = 100, secteur = "secondaire", space = 1, buildcost = dict(argent = 1000, bois = 345, metaux = 6), buildTime = 5, entretient = 0.1, prerequis = "" ),
    Boulangerie = dict(imgName = "boulangerie.jpg", workerMax = 100, secteur = "tertiaire", space = 1, buildcost = dict(argent = 1000, bois = 345, metaux = 6), buildTime = 5, entretient = 0.1, prerequis = "" )
    )


class Batiment(object):
    def __init__(self, name, pos):
        self.name = name                                # Name to identify building
        self.image = buildingDef[name]["imgName"]       # Filename of image to represent building on map (on zoom information?)
        self.position = pos                             # Position of building on map (zone)
        self.worker = 0                                 # Current number of worker affected to building
        self.workerMax = buildingDef[name]["workerMax"] # Maximum number of worker that could work in this building
        self.secteur = buildingDef[name]["secteur"]     # Activity sector of the building
        self.space = buildingDef[name]["space"]         # Space used by the building
        self.buildCost = buildingDef[name]["buildcost"] # Resource needed to build the building
        self.buildTime = buildingDef[name]["buildTime"] # Time needed to complete construction of the building
        self.maintain = buildingDef[name]["entretient"] # Resource needed to maintain the building operational
        self.prerequis = buildingDef[name]["prerequis"] # Science or Building require before building this building        
        self.energyNeeded = 0                           # Unit of energy to operate the building
        self.waterAvailable = 0                         # Acces to water to oparate the building
        self.accessToRoad = 0                           # Acces to transportation network
        self.Communication = 0                          # Access to internet, radio, TV, onde courte
        
        
    def ComputeProductivity(self):
        pass
    
    def Maintenance(self):
        pass
    
    def isOperational(self):
        pass