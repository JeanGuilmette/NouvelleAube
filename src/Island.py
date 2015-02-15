__author__ = 'SJS'
import Zone

OVERVIEW_ZONE_NAME = "Region"
LANDING_REGION_NAME = "RegionA"

secteurDef = dict(
    Region = dict(terType = "Foret", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/map/Man'ana'toura .png" ),
    RegionA = dict(terType = "Foret", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/map/Man'ana'toura_foest.png" ),
    RegionB = dict(terType = "Plaine", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/map/Man'ana'toura_North_Plains.png" ),
    RegionC = dict(terType = "Plaine", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/map/Man'ana'toura_South_Plains.png" ),
    RegionD = dict(terType = "Lac", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/map/Man'ana'toura_Lac.png" ),
    RegionE = dict(terType = "Collines", resList = ( "Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/map/Man'ana'toura_Collines.png" ),
    RegionF = dict(terType = "Volcan", resList = ( "Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/map/Man'ana'toura_volcano.png" ),
    RegionG = dict(terType = "Marecage", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/map/Man'ana'toura_marecage.png" ),
    RegionH = dict(terType = "Collines", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/map/Man'ana'toura_ile_sud.png" ),
    RegionI = dict(terType = "Foret", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/map/Man'ana'toura_ileNord.png" ),
    RegionJ = dict(terType = "EauxSalees", resList = ( "Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole" ), image = "image/map/Man'ana'toura_peninsule_ile_sud.png" ),
    RegionK = dict(terType = "EauxSalees", resList = ( "Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole" ), image = "image/map/Man'ana'toura_Plage_Sud.png" ),
    RegionL = dict(terType = "EauxSalees", resList = ( "Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole" ), image = "image/map/Man'ana'toura_peninsule_Nord.png" ),
    )

secteurSpaceDef = dict(
    Region  = [],                       
    RegionA = [(155,125), (28,566),(292,629), (390,282), (515,153),(484,411),(584,580), (842,248),(904,568)],
    RegionB = [(66,53), (160,246),(62,597),(289,438),(384,591),(449,311),(417,86),(643,433),(706,55),(866,279) ],
    RegionC = [(124,117), (192,440), (128,623),(318,20),(413,335),(479,625),(543,55),(672,272),(800,528),(838,60) ],
    RegionD = [(159,431),(224,326), (637,0),(764,180),(631,400),(607,630), (833,600)],
    RegionE = [(7,170), (135,47),(167,230), (153,520), (327,145),(400,565),(454,110), (567,497),(615,145),(774,40), (775,236),(900,139),(890,598)],
    RegionF = [(470,115),(702,0),(680,363),(915,172),(745,363),(888,431),(773,525),(710,620),(809,620)],
    RegionG = [(256,24), (451,17),(130,118),(285,243),(65,410),(96,592),(930,183),(897,442),(860,634)],
    RegionH = [(70,74),(132,74),(49,215),(185,595),(265,360),(355,10),(380,500),(519,104),(646,10),(744,10),(636,500),(824,210),(816,595),(903,70)],
    RegionI = [(96,334),(190,560),(320,180),(410,395),(510,632),(640,237),(767,500),(864,24)],
    RegionJ = [(352,0),(368,206),(580,24),(514,430)],
    RegionK = [(160,75),(480,90),(700,0),(770,155),(160,279),(290,285),(411,282),(628,333)],
    RegionL = [(0,494),(190,627),(172,399),(366,474),(459,474),(622,447),(848,547)],
    )

class Island(object):
    def __init__(self, filename):
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
        self.secteur[LANDING_REGION_NAME].Initialize()
        self.__activeZone = OVERVIEW_ZONE_NAME

    def GetActiveZone(self):
        return self.secteur[self.__activeZone]
    
    def SetActiveZone(self, zoneName):
        print(zoneName)        
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
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):            
                    retval += self.secteur[zone].GetSante()
            retval /= float(len(self.secteur))
        else:
            retval = self.secteur[zoneName].GetSante()
        return retval 
    
    def GetBonheur(self, zoneName="Active"):
        retval = 0
        if(zoneName == "Active"):
            zoneName = self.__activeZone         
        if(zoneName == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):            
                    retval += self.secteur[zone].GetBonheur()
            retval /= len(self.secteur)                    
        else:
            retval = self.secteur[zoneName].GetBonheur()
        return retval     
    
    def GetRecherche(self, zoneName="Active"):
        retval = 0
        if(zoneName == "Active"):
            zoneName = self.__activeZone         
        if(zoneName == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):            
                    retval += self.secteur[zone].GetRecherche()
            retval /= len(self.secteur)                    
        else:
            retval = self.secteur[zoneName].GetRecherche()
        return retval  
    
    def GetEducation(self, zoneName="Active"):
        retval = 0
        if(zoneName == "Active"):
            zoneName = self.__activeZone         
        if(zoneName == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):            
                    retval += self.secteur[zone].GetEducation()
            retval /= len(self.secteur)                    
        else:
            retval = self.secteur[zoneName].GetEducation()
        return retval    
    
    def GetPanique(self, zoneName="Active"):
        retval = 0
        if(zoneName == "Active"):
            zoneName = self.__activeZone         
        if(zoneName == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):            
                    retval += self.secteur[zone].GetPanique()
            retval /= len(self.secteur)                       
        else:
            retval = self.secteur[zoneName].GetPanique()
        return retval   
    
    def GetCriminalite(self, zoneName="Active"):
        retval = 0
        if(zoneName == "Active"):
            zoneName = self.__activeZone         
        if(zoneName == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):            
                    retval += self.secteur[zone].GetCriminalite()
            retval /= len(self.secteur)                       
        else:
            retval = self.secteur[zoneName].GetCriminalite()
        return retval   
    
    def GetInfluence(self, zoneName="Active"):
        retval = 0
        if(zoneName == "Active"):
            zoneName = self.__activeZone         
        if(zoneName == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):            
                    retval += self.secteur[zone].GetInfluence()
            retval /= len(self.secteur)                       
        else:
            retval = self.secteur[zoneName].GetInfluence()
        return retval   
    
    def GetPollution(self, zoneName="Active"):
        retval = 0
        if(zoneName == "Active"):
            zoneName = self.__activeZone         
        if(zoneName == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):            
                    retval += self.secteur[zone].GetPollution()
            retval /= len(self.secteur)                       
        else:
            retval = self.secteur[zoneName].GetPollution()
        return retval  
    
    def GetProduction(self, zoneName="Active"):
        retval = 0
        if(zoneName == "Active"):
            zoneName = self.__activeZone         
        if(zoneName == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):            
                    retval += self.secteur[zone].GetProduction()
            retval /= len(self.secteur)                       
        else:
            retval = self.secteur[zoneName].GetProduction()
        return retval  
    
    def GetTresors(self, zoneName="Active"):
        retval = 0
        if(zoneName == "Active"):
            zoneName = self.__activeZone         
        if(zoneName == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):            
                    retval += self.secteur[zone].GetTresors()
            retval /= float(len(self.secteur))                     
        else:
            retval = self.secteur[zoneName].GetTresors()
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
            
            