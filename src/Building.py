__author__ = 'SJS'
import EventAdvancement
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
    Camp_de_chasse  =  dict(resType = "Chasse", pos = GENERAL, imgName = "image/building_image/camp_de_chasse.png", workerMax = 600, secteur = "primaire", space = 1, buildcost = dict( Bois = 345, Minerais = 60), buildTime = 5, entretient = 0.05, prerequis = "" ),
    Port = dict(resType = "Peche", pos = GENERAL, imgName = "image/building_image/port.png", workerMax = 1500, secteur = "primaire", space = 1, buildcost = dict( Bois = 300, Minerais = 300), buildTime = 5, entretient = 0.15, prerequis = "" ),
    ZRLA= dict(resType = "population max", pos = GENERAL, imgName = "image/building_image/quartier_residentielle.png", workerMax = 500, secteur = "tertiaire", space = 1, buildcost = dict( Bois = 500, Minerais = 500), buildTime = 5, entretient = 0.2, prerequis = "" ),
    Ecole  =  dict(resType = "Travailleurs", pos = GENERAL, imgName = "image/building_image/ecole.png", workerMax = 400, secteur = "tertiaire", space = 1, buildcost = dict( Bois = 800, Minerais = 500), buildTime = 5, entretient = 0.1, prerequis = "" ),
    Stade = dict(resType = "Bonheur", pos = GENERAL, imgName = "image/building_image/stade.png", workerMax = 1700, secteur = "tertiaire", space = 1, buildcost = dict( Bois = 100, Minerais = 2000), buildTime = 5, entretient = 0.1, prerequis = "" ),
    CSE = dict(resType = "Pollution", pos = GENERAL, imgName = "image/building_image/centre_de_recherche.png", workerMax = 500, secteur = "tertiaire", space = 1, buildcost = dict( Bois = 300, Minerais = 2000), buildTime = 5, entretient = 0.4, prerequis = "" ),
    Prison  =  dict(resType = "Criminalite", pos = GENERAL, imgName = "image/building_image/prison.png", workerMax = 500, secteur = "tertiaire", space = 1, buildcost = dict( Bois = 600, Minerais = 800), buildTime = 5, entretient = 0.2, prerequis = "" ),
    CGA = dict(resType = "Influence", pos = GENERAL, imgName = "image/building_image/centre_journalistique.png", workerMax = 500, secteur = "tertiaire", space = 1, buildcost = dict( Bois = 700, Minerais = 400), buildTime = 5, entretient = 0.15, prerequis = "" ),
    Parc= dict(resType = "Pollution", pos = GENERAL, imgName = "image/building_image/parc.png", workerMax = 200, secteur = "tertiaire", space = 1, buildcost = dict( Bois = 1200, Minerais = 200), buildTime = 5, entretient = 0.05, prerequis = "" ),
    Hopital  =  dict(resType = "Sante", pos = GENERAL, imgName = "image/building_image/hopital.png", workerMax = 500, secteur = "tertiaire", space = 1, buildcost = dict( Bois = 500, Minerais = 500), buildTime = 5, entretient = 0.2, prerequis = "" )


    )

buildingDesc = dict( \
    Ferme = "Les exploitations agricoles permettent de fournir des produits agricoles, l'une des trois ressources permettant de nourrir la population de l'île.",
    Mine  =  "Les exploitations minières servent, vous le devinerez, à excaver diverses sortes de minerais nécessaires à la construction de bâtiments.",
    Scierie = "Aussi appelé, moins communément, usine de transformation primaire du bois, les scieries servent à produire ce matériau de construction essentielle au développement de nos infrastructure.",
    Forage_petrolier = "Ces installations permettent de récupérer le pétrole qui est dans le sol et de le raffiner pour le transformer en essence qui pourra ensuite être ré-utilisé pour faire rouler nos véhicules.",
    Camp_de_chasse  =  "Ce sont des camps remplient de chasseurs (surprise!) qui chasse (Étonnant!) des (attention, tenez-vous bien...) animaux et les apprêtent pour qu'ils prêt à être mangé par votre population.",
    Port = "C'est de là que les pêcheurs partent pour pêcher du poisson et c'est également là qu'ils les apprêtent pour qu'ils soient prêt à être consommé par la population." ,
    ZRLA = "Les ZRLA, Zone Résidentielle à Logistique Avancée, représente une zone du secteur spécifiquement résidentielle composé principalement de gratte-ciel, conçu pour pouvoir accueillir un maximum de gens dans le moins d'espace possible.",
    Ecole  = " Les institutions d'éducation permettent d'améliorer la formation d'ouvriers. Ceux-ci vous seront essentielles tout au long de votre exil pour faire fonctionner vos bâtiments.",
    Stade = "Un stade est une infrastructure gigantesque permettant l'organisation de divers événements sportifs distrayant les foules. Un stade est plutôt cher à entretenir, mais permet d'aider les habitants de secteur à retrouver le sourire. Cela n'en vaut-il pas la peine?",
    CSE = "Les Centre de surveillance environnementales (CSE) permettent une meilleure surveillance de l'émission de polluant dans la nature, tout en permettant de réduire la pollution déjà présente dans ses alentours.",
    Prison  =  "Les établissements pénitencier servent à incarcérer les criminels et font de ce fait baisser la criminalité du secteur dans lequel ils se trouvent.",
    CGA = "Les Centre de Gestion ARCHE sont les QG des employés de l'ARCHE à partir desquels se déroulent les opérations et grâce auxquels vos ordres sont exécuté. La construction d'un centre de gestion ARCHE dans un secteur augmente votre influence sur celui-ci." ,
    Parc=  "Un magnifique espace vert légèrement aménagé, protégé des dégâts de l'industrie et de l'urbanisation où tout le monde peut aller s'amuser ou encore tout simplement relaxer après une dure journée de travail. L’aménagement d'une de ces réserves naturelles dans un secteur y augmente le bonheur et y fait baisser la pollution. " ,
    Hopital  =  "Les complexes hospitaliers permettent de sensiblement améliorer la santé des habitants du secteur où ils sont construits."
    )

buildingEffect = dict( \
    Ferme = dict( add = ["pollution=6"], remove = [""]),
    Mine  = dict( add = ["pollution=10" ], remove = [""]),
    Scierie = dict( add = ["pollution=4"], remove = [""]),
    Forage_petrolier = dict( add = ["pollution=16", "bonheur=-7"], remove = [""]),
    Camp_de_chasse  =  dict( add = ["pollution=2"], remove = [""]),
    Port = dict( add = ["pollution=4"], remove = [""]),
    ZRLA = dict( add = ["pollution=8"], remove = [""]),#augmentation population
    Ecole  = dict( add = ["pollution=2"], remove = [""]),#augemntation population
    Stade = dict( add = ["pollution=8", "bonheur=20"], remove = ["bonheur=-25"]),
    CSE = dict( add = ["pollution=-15"], remove = ["pollution=18"]),
    Prison  =  dict( add = ["pollution=3","criminalite=-10"], remove = [""]),
    CGA = dict( add = ["pollution=4","influence=15"], remove = [""]),
    Parc =  dict( add = ["pollution=-40", "bonheur=10","sante=8"], remove = ["bonheur=-30"]),
    Hopital  =  dict( add = ["pollution=4","sante=17"], remove = ["bonheur=-30"])
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
        if EventAdvancement.ARNAQUED != True:
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
        
