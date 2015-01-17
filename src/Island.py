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
