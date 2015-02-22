__author__ = 'SJS'

import StoryTelling

class Population():
    def __init__(self, popMax, croissance):
        self.popMax = popMax            # Maximum of population supported by the island
        self.croissance = croissance    # Number of new people by unit of time.
        self.sante= StoryTelling.Ressources_depart.Effects ["Sante"]                  #
        self.influence = StoryTelling.Ressources_depart.Effects ["Influence"]             #
        self.bonheur = StoryTelling.Ressources_depart.Effects ["Bonheur"]               #
        self.recherche = 0              # 
        self.education =  StoryTelling.Ressources_depart.Effects ["Education"]            #
        self.panique = StoryTelling.Ressources_depart.Effects ["Panique"]               #
        #self.paniquedecatastrophe = 50  #
        self.criminalite = StoryTelling.Ressources_depart.Effects ["Criminalite"]           #
        self.current = StoryTelling.Ressources_depart.Effects ["Population"]                #
        self.counter = 0                # Count number of day passed
        self.workerCurrent = 0
        self.workerIdle = 0
        self.workerMax = self.current * 0.8
        self.pollution = 0
    
    def PopulationAdjustment(self):
        if(self.counter >= 30):
            self.UpdateCroissance()
            self.current += (self.current * self.croissance)
            if(self.current > self.popMax):
                self.current = self.popMax
            self.counter = 0
            self.UpdateMaxWorker()
        else:
            self.counter += 1
            
    def UpdateCroissance(self):
        pos = self.sante + self.bonheur + self.education
        neg = self.criminalite + self.panique 
        self.croissance += float(pos - neg)/100.0
        print("Croissant: %f" % self.croissance)
        
    def UpdateMaxWorker(self):
        self.workerMax = self.current * 0.80
        self.workerIdle = self.workerMax * (self.education/100.0)
    
    def ActivateWorker(self):
        if( ((self.workerCurrent + 1) <= self.workerMax) or (self.workerIdle > 0)):
            self.workerCurrent += 1  
            self.workerIdle -= 1
            return True
        return False
             
    def Deactivateworker(self):
        if(self.workerCurrent >= 1):        
            self.workerCurrent -= 1
            self.workerIdle += 1 
            return True
        return False
            
    def AddAvailableWorker(self):
        if( (self.workerIdle + 1) <= self.workerMax):
            self.workerIdle += 1
       
    def SetCurrentPopulation(self, val): 
        self.current = val
        self.UpdateMaxWorker()    
        self.workerIdle = val * 0.25    