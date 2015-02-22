__author__ = 'SJS'
import Zone
from Building import GENERAL, SOUSTERRAIN, RIVE, AERIEN
import Musique
import StoryTelling

OVERVIEW_ZONE_NAME = "Region"
LANDING_REGION_NAME = "RegionA"


secteurDef = dict(
    Region = dict(terType = "Foret", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/map/Man'ana'toura .png", name = "Man'ana'toura" ),
    RegionA = dict(terType = "Foret", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/map/Man'ana'toura_foest.png", name = "La Forêt Boisée" ),
    RegionB = dict(terType = "Plaine", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/map/Man'ana'toura_North_Plains.png", name = "La Prairie Nord" ),
    RegionC = dict(terType = "Plaine", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/map/Man'ana'toura_South_Plains.png", name = "La Prairie Sud" ),
    RegionD = dict(terType = "Lac", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/map/Man'ana'toura_Lac.png", name = "Le Lac Mouillé" ),
    RegionE = dict(terType = "Collines", resList = ( "Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/map/Man'ana'toura_Collines.png", name = "LES Collines" ),
    RegionF = dict(terType = "Volcan", resList = ( "Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/map/Man'ana'toura_volcano.png", name = "Le Volcan Délavé" ),
    RegionG = dict(terType = "Marecage", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/map/Man'ana'toura_marecage.png", name = "Les Marécages" ),
    RegionH = dict(terType = "Collines", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/map/Man'ana'toura_ile_sud.png", name = "L'île aux Mouettes " ),
    RegionI = dict(terType = "Foret", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/map/Man'ana'toura_ileNord.png", name = "L'île du Nord" ),
    RegionJ = dict(terType = "EauxSalees", resList = ( "Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole" ), image = "image/map/Man'ana'toura_peninsule_ile_sud.png", name = "La Pointe aux Crabes" ),
    RegionK = dict(terType = "EauxSalees", resList = ( "Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole" ), image = "image/map/Man'ana'toura_Plage_Sud.png", name = "Le Littoral Sud" ),
    RegionL = dict(terType = "EauxSalees", resList = ( "Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole" ), image = "image/map/Man'ana'toura_peninsule_Nord.png", name = "Le Littoral Nord" ),
    )



secteurSpaceDef = dict(
    Region  = [],                       
    RegionA = [(155,125,GENERAL), (28,566,GENERAL),(292,629,GENERAL), (390,282,GENERAL), (515,153,GENERAL),(484,411,GENERAL),(584,580,GENERAL), (842,248,GENERAL),(904,568,GENERAL)],
    RegionB = [(66,53,GENERAL), (160,246,GENERAL),(62,597,GENERAL),(289,438,GENERAL),(384,591,GENERAL),(449,311,GENERAL),(417,86,GENERAL),(643,433,GENERAL),(706,55,GENERAL),(866,279,GENERAL) ],
    RegionC = [(124,117,GENERAL), (192,440,GENERAL), (128,623,GENERAL),(318,20,GENERAL),(413,335,GENERAL),(479,625,GENERAL),(543,55,GENERAL),(672,272,GENERAL),(800,528,GENERAL),(838,60,AERIEN) ],
    RegionD = [(159,431,GENERAL),(224,326,AERIEN), (637,0,GENERAL),(764,180,GENERAL),(631,400,GENERAL),(607,630,GENERAL), (833,600,GENERAL)],
    RegionE = [(7,170,SOUSTERRAIN), (135,47,SOUSTERRAIN),(167,230,SOUSTERRAIN), (153,520,GENERAL), (327,145,SOUSTERRAIN),(400,565,GENERAL),(454,110,SOUSTERRAIN), (567,497,AERIEN),(615,145,SOUSTERRAIN),(774,40,SOUSTERRAIN), (775,236,SOUSTERRAIN),(900,139,SOUSTERRAIN),(890,598,AERIEN)],
    RegionF = [(470,115,AERIEN),(702,0,AERIEN),(680,363,SOUSTERRAIN),(915,172,AERIEN),(745,363,SOUSTERRAIN),(888,431,AERIEN),(773,525,SOUSTERRAIN),(710,620,SOUSTERRAIN),(809,620,SOUSTERRAIN)],
    RegionG = [(256,24,GENERAL), (451,17,GENERAL),(130,118,GENERAL),(285,243,GENERAL),(65,410,GENERAL),(96,592,GENERAL),(930,183,GENERAL),(897,442,GENERAL),(860,634,GENERAL)],
    RegionH = [(70,74,SOUSTERRAIN),(132,74,SOUSTERRAIN),(49,215,GENERAL),(185,595,GENERAL),(265,360,GENERAL),(355,10,SOUSTERRAIN),(380,500,SOUSTERRAIN),(519,104,SOUSTERRAIN),(646,10,SOUSTERRAIN),(744,10,SOUSTERRAIN),(636,500,GENERAL),(824,210,GENERAL),(816,595,GENERAL),(903,70,SOUSTERRAIN)],
    RegionI = [(96,334,GENERAL),(190,560,GENERAL),(320,180,GENERAL),(410,395,GENERAL),(510,632,GENERAL),(640,237,GENERAL),(767,500,GENERAL),(864,24,GENERAL)],
    RegionJ = [(352,0,GENERAL),(368,206,GENERAL),(580,24,GENERAL),(514,430,RIVE)],
    RegionK = [(160,75,GENERAL),(480,90,GENERAL),(700,0,GENERAL),(770,155,GENERAL),(160,279,RIVE),(290,285,RIVE),(411,282,RIVE),(628,333,RIVE)],
    RegionL = [(0,494,GENERAL),(190,627,GENERAL),(172,399,RIVE),(366,474,RIVE),(459,474,RIVE),(622,447,RIVE),(848,547,RIVE)],
    )

class Island(object):
    def __init__(self, filename):
        Musique.StartMusic("Soundtrack/Mananatoura-days.ogg")
        self.secteur = dict()
        self.__activeZone = None                      # Which zone player currently examine or work with
        if(filename == "new"):
            self.__create()
        else:
            self.__load(filename)

    # load game information from saved file
    def __load(self, filename):
        pass

    # Create new game with inital value
    def __create(self):
        for sectorName in sorted(secteurDef):
            self.secteur[sectorName] = Zone.Secteur(sectorName, secteurDef[sectorName]["terType"], secteurDef[sectorName]["resList"], secteurDef[sectorName]["image"], secteurSpaceDef[sectorName])
        self.secteur[LANDING_REGION_NAME].Initialize(StoryTelling.Ressources_depart)
        self.__activeZone = OVERVIEW_ZONE_NAME

    def GetActiveZone(self):
        return self.secteur[self.__activeZone]
    
    def SetActiveZone(self, zoneName):
        self.__activeZone = zoneName
        
    def GetCurrentPopulation(self, zoneName="Active"):
        pop = 0
        if(zoneName == "Active"):
            zoneName = self.__activeZone
        if(zoneName == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):            
                    pop += self.secteur[zone].GetCurrentPopulation()
        else:
            pop = self.secteur[zoneName].GetCurrentPopulation()
        return pop 

    def GetPopulationMax(self, zoneName="Active"):
        popMax = 0
        if(zoneName == "Active"):
            zoneName = self.__activeZone        
        if(zoneName == OVERVIEW_ZONE_NAME):        
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):
                    popMax += self.secteur[zone].GetMaxPopulation()
        else:
            popMax = self.secteur[zoneName].GetMaxPopulation()                    
        return popMax 

    def GetCurrentWorker(self, zoneName="Active"):
        pop = 0
        if(zoneName == "Active"):
            zoneName = self.__activeZone         
        if(zoneName == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):            
                    pop += self.secteur[zone].GetCurrentWorker()
        else:
            pop = self.secteur[zoneName].GetCurrentWorker()
        return pop 

    def GetAvailableWorker(self, zoneName="Active"):
        popMax = 0
        if(zoneName == "Active"):
            zoneName = self.__activeZone         
        if(zoneName == OVERVIEW_ZONE_NAME):        
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):
                    popMax += self.secteur[zone].GetAvailableWorker()
        else:
            popMax = self.secteur[zoneName].GetAvailableWorker()                    
        return popMax 
 
    def GetMaxWorker(self, zoneName="Active"):
        popMax = 0
        if(zoneName == "Active"):
            zoneName = self.__activeZone         
        if(zoneName == OVERVIEW_ZONE_NAME):        
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):
                    popMax += self.secteur[zone].GetMaxWorker()
        else:
            popMax = self.secteur[zoneName].GetMaxWorker()                    
        return popMax     
    
    
    def GetSante(self, zoneName="Active"):
        retval = 0
        if(zoneName == "Active"):
            zoneName = self.__activeZone         
        if(zoneName == OVERVIEW_ZONE_NAME):
            nbrZone = 0
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):
                    if(self.secteur[zone].GetCurrentPopulation() > 0):            
                        retval += self.secteur[zone].GetSante()
                        nbrZone += 1
            retval /= float(nbrZone)
        else:
            retval = self.secteur[zoneName].GetSante()
        return retval 
    
    def GetBonheur(self, zoneName="Active"):
        retval = 0
        if(zoneName == "Active"):
            zoneName = self.__activeZone         
        if(zoneName == OVERVIEW_ZONE_NAME):
            nbrZone = 0
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):
                    if(self.secteur[zone].GetCurrentPopulation() > 0):            
                        retval += self.secteur[zone].GetBonheur()
                        nbrZone += 1
            retval /= float(nbrZone)            
        else:
            retval = self.secteur[zoneName].GetBonheur()
        return retval     
    
    def GetRecherche(self, zoneName="Active"):
        retval = 0
        if(zoneName == "Active"):
            zoneName = self.__activeZone         
        if(zoneName == OVERVIEW_ZONE_NAME):
            nbrZone = 0
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):
                    if(self.secteur[zone].GetCurrentPopulation() > 0):            
                        retval += self.secteur[zone].GetRecherche()
                        nbrZone += 1
            retval /= float(nbrZone)                      
        else:
            retval = self.secteur[zoneName].GetRecherche()
        return retval  
    
    def GetEducation(self, zoneName="Active"):
        retval = 0
        if(zoneName == "Active"):
            zoneName = self.__activeZone         
        if(zoneName == OVERVIEW_ZONE_NAME):
            nbrZone = 0
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):
                    if(self.secteur[zone].GetCurrentPopulation() > 0):            
                        retval += self.secteur[zone].GetEducation()
                        nbrZone += 1
            retval /= float(nbrZone)                    
        else:
            retval = self.secteur[zoneName].GetEducation()
        return retval    
    
    def GetPanique(self, zoneName="Active"):
        retval = 0
        if(zoneName == "Active"):
            zoneName = self.__activeZone         
        if(zoneName == OVERVIEW_ZONE_NAME):
            nbrZone = 0
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):
                    if(self.secteur[zone].GetCurrentPopulation() > 0):            
                        retval += self.secteur[zone].GetPanique()
                        nbrZone += 1
            retval /= float(nbrZone)                         
        else:
            retval = self.secteur[zoneName].GetPanique()
        return retval   
    
    def GetCriminalite(self, zoneName="Active"):
        retval = 0
        if(zoneName == "Active"):
            zoneName = self.__activeZone         
        if(zoneName == OVERVIEW_ZONE_NAME):
            nbrZone = 0
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):
                    if(self.secteur[zone].GetCurrentPopulation() > 0):            
                        retval += self.secteur[zone].GetCriminalite()
                        nbrZone += 1
            retval /= float(nbrZone)                         
        else:
            retval = self.secteur[zoneName].GetCriminalite()
        return retval   
    
    def GetInfluence(self, zoneName="Active"):
        retval = 0
        if(zoneName == "Active"):
            zoneName = self.__activeZone         
        if(zoneName == OVERVIEW_ZONE_NAME):
            nbrZone = 0
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):
                    if(self.secteur[zone].GetCurrentPopulation() > 0):            
                        retval += self.secteur[zone].GetInfluence()
                        nbrZone += 1
            retval /= float(nbrZone)                         
        else:
            retval = self.secteur[zoneName].GetInfluence()
        return retval   
    
    def GetPollution(self, zoneName="Active"):
        retval = 0
        if(zoneName == "Active"):
            zoneName = self.__activeZone         
        if(zoneName == OVERVIEW_ZONE_NAME):
            nbrZone = 0
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):
                    if(self.secteur[zone].GetCurrentPopulation() > 0):            
                        retval += self.secteur[zone].GetPollution()
                        nbrZone += 1
            retval /= float(nbrZone)                        
        else:
            retval = self.secteur[zoneName].GetPollution()
        return retval  

    
    def GetRessourceInfo(self, resName, zoneName="Active"):
        stock = 0
        available = 0
        stockMax = 0
        if(zoneName == "Active"):
            zoneName = self.__activeZone         
        if(zoneName == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):            
                    a, b, c = self.secteur[zone].GetRessourceInfo(resName)
                    stock += a
                    available += b
                    stockMax += c
        else:
            stock, available, stockMax = self.secteur[zoneName].GetRessourceInfo(resName)
        return  stock, available, stockMax 

    def AddBuilding(self, zoneName, buildingName):
        self.secteur[zoneName].AddBuilding(buildingName)

        
    def UpdateProd(self):
        for zone in self.secteur:
            if(zone != OVERVIEW_ZONE_NAME):
                self.secteur[zone].UpdateProd()
                
    def UpdatePopulation(self):
        for zone in self.secteur:
            if(zone != OVERVIEW_ZONE_NAME):
                self.secteur[zone].UpdatePopulation()       
                
    def UpdateExpandRessource(self):
        for zone in self.secteur:
            if(zone != OVERVIEW_ZONE_NAME):
                self.secteur[zone].UpdateExpandRessource()

    
    def ModifyPopulation(self, zoneName, newVal):
        if(zoneName == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):
                    self.secteur[zone].ModifyPopulation(newVal)   
        else:
            self.secteur[zoneName].ModifyPopulation(newVal)                  

    def ModifySante(self, zoneName, newVal):
        if(zoneName == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):
                    self.secteur[zone].ModifySante(newVal)   
        else:
            self.secteur[zoneName].ModifySante(newVal) 
            
    def ModifyBonheur(self, zoneName, newVal):
        if(zoneName == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):
                    self.secteur[zone].ModifyBonheur(newVal)   
        else:
            self.secteur[zoneName].ModifyBonheur(newVal)  
            
    def ModifyInfluence(self, zoneName, newVal):
        if(zoneName == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):
                    self.secteur[zone].ModifyInfluence(newVal)   
        else:
            self.secteur[zoneName].ModifyInfluence(newVal)  
            
    def ModifyRecherche(self, zoneName, newVal):
        if(zoneName == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):
                    self.secteur[zone].ModifyRecherche(newVal)   
        else:
            self.secteur[zoneName].ModifyRecherche(newVal)                                      
                              
    def ModifyEducation(self, zoneName, newVal):
        if(zoneName == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):
                    self.secteur[zone].ModifyEducation(newVal)   
        else:
            self.secteur[zoneName].ModifyEducation(newVal)
            
    def ModifyCriminalite(self, zoneName, newVal):
        if(zoneName == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):
                    self.secteur[zone].ModifyCriminalite(newVal)   
        else:
            self.secteur[zoneName].ModifyCriminalite(newVal)

    def ModifyPollution(self, zoneName, newVal):
        if(zoneName == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):
                    self.secteur[zone].ModifyPollution(newVal)
        else:
            self.secteur[zoneName].ModifyPollution(newVal)

    def ModifyPanic(self, zoneName, newVal):
        if(zoneName == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):
                    self.secteur[zone].ModifyPanic(newVal)   
        else:
            self.secteur[zoneName].ModifyPanic(newVal)  

    def ModifyCroissance(self, zoneName, newVal):
        if(zoneName == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):
                    self.secteur[zone].ModifyCroissance(newVal)   
        else:
            self.secteur[zoneName].ModifyCroissance(newVal)  
            
    def ModifyPopulationMax(self, zoneName, newVal):
        if(zoneName == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):
                    self.secteur[zone].ModifyPopulationMax(newVal)   
        else:
            self.secteur[zoneName].ModifyPopulationMax(newVal)  
                                    
    def ModifyRessource(self, zoneName, resName, newVal):
        if(zoneName == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):
                    self.secteur[zone].ModifyRessource(resName, newVal)   
        else:
            self.secteur[zoneName].ModifyRessource(resName, newVal)          
            
            