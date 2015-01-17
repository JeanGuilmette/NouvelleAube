__author__ = 'SJS'
import zone

OVERVIEW_ZONE_NAME = "Region"
LANDING_REGION_NAME = "RegionA"

secteurDef = dict(
    Region = dict(terType = "Foret", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/map/Man'ana'toura .png" ),
    RegionA = dict(terType = "Foret", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/map/Man'ana'toura_foest.png" ),
    RegionB = dict(terType = "Plaine", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/region2.jpg" ), 
    RegionC = dict(terType = "Plaine", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/region2.jpg" ),   
    RegionD = dict(terType = "Plaine", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/region2.jpg" ),
    RegionE = dict(terType = "Plaine", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/region2.jpg" ),       
    RegionF = dict(terType = "Plaine", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/region2.jpg" ),   
    RegionG = dict(terType = "Plaine", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/region2.jpg" ),       
    RegionH = dict(terType = "Plaine", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/region2.jpg" ),   
    RegionI = dict(terType = "Plaine", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/region2.jpg" ),   
    RegionJ = dict(terType = "Plaine", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/region2.jpg" ),   
    RegionK = dict(terType = "Plaine", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/region2.jpg" ),   
    RegionL = dict(terType = "Plaine", resList = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), image = "image/region2.jpg" ),   
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
            self.secteur[sectorName] = zone.Secteur(sectorName, secteurDef[sectorName]["terType"], secteurDef[sectorName]["resList"], secteurDef[sectorName]["image"])
        self.secteur[LANDING_REGION_NAME].Initialize()
        self.__activeZone = OVERVIEW_ZONE_NAME

    def GetActiveZone(self):
        return self.secteur[self.__activeZone]
    
    def SetActiveZone(self, zoneName):
        print(zoneName)        
        self.__activeZone = zoneName
        
    def GetCurrentPopulation(self):
        pop = 0
        if(self.__activeZone == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):            
                    pop += self.secteur[zone].GetCurrentPopulation()
        else:
            pop = self.secteur[self.__activeZone].GetCurrentPopulation()
        return pop 

    def GetPopulationMax(self):
        popMax = 0
        if(self.__activeZone == OVERVIEW_ZONE_NAME):        
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):
                    popMax += self.secteur[zone].GetMaxPopulation()
        else:
            popMax = self.secteur[self.__activeZone].GetMaxPopulation()                    
        return popMax 

    def GetCurrentWorker(self):
        pop = 0
        if(self.__activeZone == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):            
                    pop += self.secteur[zone].GetCurrentWorker()
        else:
            pop = self.secteur[self.__activeZone].GetCurrentWorker()
        return pop 

    def GetAvailableWorker(self):
        popMax = 0
        if(self.__activeZone == OVERVIEW_ZONE_NAME):        
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):
                    popMax += self.secteur[zone].GetAvailableWorker()
        else:
            popMax = self.secteur[self.__activeZone].GetAvailableWorker()                    
        return popMax 
 
    def GetMaxWorker(self):
        popMax = 0
        if(self.__activeZone == OVERVIEW_ZONE_NAME):        
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):
                    popMax += self.secteur[zone].GetMaxWorker()
        else:
            popMax = self.secteur[self.__activeZone].GetMaxWorker()                    
        return popMax     
    
    
    def GetSante(self):
        retval = 0
        if(self.__activeZone == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):            
                    retval += self.secteur[zone].GetSante()
        else:
            retval = self.secteur[self.__activeZone].GetSante()
        return retval 
    
    def GetBonheur(self):
        retval = 0
        if(self.__activeZone == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):            
                    retval += self.secteur[zone].GetBonheur()
        else:
            retval = self.secteur[self.__activeZone].GetBonheur()
        return retval     
    
    def GetRecherche(self):
        retval = 0
        if(self.__activeZone == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):            
                    retval += self.secteur[zone].GetRecherche()
        else:
            retval = self.secteur[self.__activeZone].GetRecherche()
        return retval  
    
    def GetEducation(self):
        retval = 0
        if(self.__activeZone == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):            
                    retval += self.secteur[zone].GetEducation()
        else:
            retval = self.secteur[self.__activeZone].GetEducation()
        return retval    
    
    def GetPanique(self):
        retval = 0
        if(self.__activeZone == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):            
                    retval += self.secteur[zone].GetPanique()
        else:
            retval = self.secteur[self.__activeZone].GetPanique()
        return retval   
    
    def GetCriminalite(self):
        retval = 0
        if(self.__activeZone == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):            
                    retval += self.secteur[zone].GetCriminalite()
        else:
            retval = self.secteur[self.__activeZone].GetCriminalite()
        return retval   
    
    def GetInfluence(self):
        retval = 0
        if(self.__activeZone == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):            
                    retval += self.secteur[zone].GetInfluence()
        else:
            retval = self.secteur[self.__activeZone].GetInfluence()
        return retval   
    
    def GetPollution(self):
        retval = 0
        if(self.__activeZone == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):            
                    retval += self.secteur[zone].GetPollution()
        else:
            retval = self.secteur[self.__activeZone].GetPollution()
        return retval  
    
    def GetProduction(self):
        retval = 0
        if(self.__activeZone == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):            
                    retval += self.secteur[zone].GetProduction()
        else:
            retval = self.secteur[self.__activeZone].GetProduction()
        return retval  
    
    def GetTresors(self):
        retval = 0
        if(self.__activeZone == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):            
                    retval += self.secteur[zone].GetTresors()
        else:
            retval = self.secteur[self.__activeZone].GetTresors()
        return retval              
                
    
    def GetRessourceInfo(self, resName):
        stock = 0
        available = 0
        stockMax = 0
        if(self.__activeZone == OVERVIEW_ZONE_NAME):
            for zone in self.secteur:
                if(zone != OVERVIEW_ZONE_NAME):            
                    a, b, c = self.secteur[zone].GetRessourceInfo(resName)
                    stock += a
                    available += b
                    stockMax += c
        else:
            stock, available, stockMax = self.secteur[self.__activeZone].GetRessourceInfo(resName)
        return  stock, available, stockMax 

    def AddBuilding(self, zoneName, buildingName, pos):
        self.secteur[zoneName].AddBuilding(buildingName, pos)
        
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
