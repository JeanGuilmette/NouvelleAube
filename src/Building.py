__author__ = 'SJS'
# Available position type
GENERAL = 0
RIVE = 1
SOUSTERRAIN = 2
AERIEN = 3

buildingDef = dict( \
    Ferme = dict(resType = "Agriculture", pos = GENERAL, imgName = "image/building_image/ferme.png", workerMax = 10, secteur = "primaire", space = 40, buildcost = dict( Bois = 345, Minerais = 6), buildTime = 5, entretient = 0.1, prerequis = "" ),
    Mine  =  dict(resType = "Metaux", pos = GENERAL, imgName = "image/building_image/mine.png", workerMax = 100, secteur = "primaire", space = 2, buildcost = dict( Bois = 345, Minerais = 6), buildTime = 5, entretient = 0.1, prerequis = "" ),
    Scierie = dict(resType = "Bois", pos = GENERAL, imgName = "image/building_image/usine_de_transformation_du_bois.png", workerMax = 20, secteur = "primaire", space = 5, buildcost = dict( Bois = 0, Minerais = 6), buildTime = 5, entretient = 0.1, prerequis = "" ),

    Forage_petrolier = dict(resType = "Petrole", pos = GENERAL, imgName = "image/building_image/Station_de_forage.png", workerMax = 3000, secteur = "primaire", space = 1, buildcost = dict( Bois = 0, Minerais = 800), buildTime = 5, entretient = 0.1, prerequis = "gisement" ),
    camp_de_chasse  =  dict(resType = "Chasse", pos = GENERAL, imgName = "image/building_image/camp_de_chasse.png", workerMax = 600, secteur = "primaire", space = 1, buildcost = dict( Bois = 345, Minerais = 60), buildTime = 5, entretient = 0.05, prerequis = "" ),
    port = dict(resType = "Peche", pos = GENERAL, imgName = "image/building_image/port.png", workerMax = 1500, secteur = "primaire", space = 1, buildcost = dict( Bois = 300, Minerais = 300), buildTime = 5, entretient = 0.15, prerequis = "" ),
    Zone_residentielle_importante= dict(resType = "population max", pos = GENERAL, imgName = "image/building_image/quartier_residentielle.png", workerMax = 500, secteur = "tertiaire", space = 1, buildcost = dict( Bois = 500, Minerais = 500), buildTime = 5, entretient = 0.2, prerequis = "" ),
    Ecole  =  dict(resType = "Travailleurs", pos = GENERAL, imgName = "image/building_image/ecole.png", workerMax = 400, secteur = "tertiaire", space = 1, buildcost = dict( Bois = 800, Minerais = 500), buildTime = 5, entretient = 0.1, prerequis = "" ),
    Stade = dict(resType = "Bonheur", pos = GENERAL, imgName = "image/building_image/stade.png", workerMax = 1700, secteur = "tertiaire", space = 1, buildcost = dict( Bois = 100, Minerais = 2000), buildTime = 5, entretient = 0.1, prerequis = "" ),
    Centrale_de_surveillance = dict(resType = "Panique", pos = GENERAL, imgName = "image/building_image/centre_de_recherche.png", workerMax = 500, secteur = "tertiaire", space = 1, buildcost = dict( Bois = 300, Minerais = 2000), buildTime = 5, entretient = 0.4, prerequis = "" ),
    Prison  =  dict(resType = "Criminalite", pos = GENERAL, imgName = "image/building_image/prison.png", workerMax = 500, secteur = "tertiaire", space = 1, buildcost = dict( Bois = 600, Minerais = 800), buildTime = 5, entretient = 0.2, prerequis = "" ),
    Bureaux_journalistiques = dict(resType = "Influence", pos = GENERAL, imgName = "image/building_image/centre_journalistique.png", workerMax = 500, secteur = "tertiaire", space = 1, buildcost = dict( Bois = 700, Minerais = 400), buildTime = 5, entretient = 0.15, prerequis = "" ),
    Parc= dict(resType = "Pollution", pos = GENERAL, imgName = "image/building_image/parc.png", workerMax = 200, secteur = "tertiaire", space = 1, buildcost = dict( Bois = 1200, Minerais = 200), buildTime = 5, entretient = 0.05, prerequis = "" ),
    Hopital  =  dict(resType = "Sante", pos = GENERAL, imgName = "image/building_image/hopital.png", workerMax = 500, secteur = "tertiaire", space = 1, buildcost = dict( Bois = 500, Minerais = 500), buildTime = 5, entretient = 0.2, prerequis = "" ),

    Entrepot = dict(resType = "Stockage", pos = GENERAL, imgName = "image/building_image/entrepot.png", workerMax = 1000000, secteur = "tertiaire", space = 1, buildcost = dict( Bois = 800, Minerais = 500), buildTime = 5, entretient = (0.15), prerequis = "" ), # ajouter +2% par 100 worker
    Centre_de_logistique_routiere = dict(resType = "Transport", pos = GENERAL, imgName = "image/building_image/centre_logistique_routier.png", workerMax = 4000, secteur = "tertiaire", space = 1, buildcost = dict( Bois = 300, Minerais = 500), buildTime = 5, entretient = 0.15, prerequis = "" ), #PRIX PETROLE
    Centre_de_logistique_aeroportee  =  dict(resType = "Tranport", pos = GENERAL, imgName = "image/building_image/aeroport.png", workerMax = 500, secteur = "tertiaire", space = 1, buildcost = dict( Bois = 1000, Minerais = 2300), buildTime = 5, entretient = 0.35, prerequis = "centre_de_logistique_routière" )
    )

buildingDesc = dict( \
    Ferme = "Ferme est pour",
    Mine  =  "Mine est pour",
    Scierie = "Scierie",
    Forage_petrolier = "Forage pétrolier",
    camp_de_chasse  =  "Camp de chasse",
    port = "Port" ,
    Zone_residentielle_importante = "Zone residentielle",
    Ecole  = "Ecole",
    Stade = "Stade",
    Centrale_de_surveillance = "Centrale de surveillance",
    Prison  =  "Prison",
    Bureaux_journalistiques = "Bureau journalistique" ,
    Parc=  "Parc" ,
    Hopital  =  "Hopital",
    Entrepot = "Entrepot",
    Centre_de_logistique_routiere = "Centre logistique routière",
    Centre_de_logistique_aeroportee  = "Centre de logistique aeroporte"
    )

buildingEffect = dict( \
    Ferme = dict( add = ["panic=15"], remove = ["panic=-5"]),
    Mine  = dict( add = "", remove = ""),
    Scierie = dict( add = "", remove = ""),
    Forage_petrolier = dict( add = "", remove = ""),
    camp_de_chasse  =  dict( add = "", remove = ""),
    port = dict( add = "", remove = ""),
    Zone_residentielle_importante = dict( add = "", remove = ""),
    Ecole  = dict( add = "", remove = ""),
    Stade = dict( add = "", remove = ""),
    Centrale_de_surveillance = dict( add = "", remove = ""),
    Prison  =  dict( add = "", remove = ""),
    Bureaux_journalistiques = dict( add = "", remove = ""),
    Parc =  dict( add = "", remove = ""),
    Hopital  =  dict( add = "", remove = ""),
    Entrepot = dict( add = "", remove = ""),
    Centre_de_logistique_routiere = dict( add = "", remove = ""),
    Centre_de_logistique_aeroportee  = dict( add = "", remove = ""),
    )

class Batiment(object):
    def __init__(self, name):
        self.name = name                                 # Name to identify building
        self.image = buildingDef[name]["imgName"]        # Filename of image to represent building on map (on zoom information?)
        self.resType = buildingDef[name]["resType"]      # 
        self.position = []                              # Position of building on map (zone)
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
        limitMaxWorker =  self.GetMaxWorker()
        self.worker = (self.worker + nbrWorker) if( (self.worker + nbrWorker) <= limitMaxWorker ) else limitMaxWorker
        self.worker = self.worker if (self.worker >= 0) else 0
        
    def Add(self, pos):
        self.numberBuilding = self.numberBuilding + 1 
        self.position.append(pos)
        
    def Remove(self):
        self.numberBuilding = self.numberBuilding - 1
        self.numberBuilding = self.numberBuilding if (self.numberBuilding >= 0) else 0    
        self.AssignWorker(0)  
        return self.position.pop()  
        
    def AddWorker(self):
        val = self.worker + 1
        limitMaxWorker = self.GetMaxWorker()
        self.worker = val if( val <= limitMaxWorker ) else limitMaxWorker
        
    def RemoveWorker(self):
        self.worker = self.worker - 1
        self.worker = self.worker if (self.worker >= 0) else 0  
        
    def GetMaxWorker(self):
        return self.workerMax * self.numberBuilding
        
