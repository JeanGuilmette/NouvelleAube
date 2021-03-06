__author__ = 'SJS'


class Population():
    def __init__(self, popMax, croissance):
        self.popMax = popMax            # Maximum of population supported by the island
        self.croissance = croissance    # Number of new people by unit of time.
        self.sante= 50 
        self.influence = 50
        self.bonheur = 50
        self.education =  50 
        self.panique = 0 
        self.criminalite = 10
        self.current = 0
        self.counter = 0                # Count number of day passed
        self.workerCurrent = 0
        self.workerIdle = 0
        self.workerMax = 0
        self.pollution = 0
    
    def PopulationAdjustment(self):
        if(self.counter >= 30):
            self.UpdateCroissance()
            self.current += (self.current * self.croissance)
            self.counter = 0
        else:
            self.counter += 1
        self.UpdateMaxWorker()            
        newPanic = self.panique - (self.influence * 0.05) 
        self.panique = newPanic if(newPanic>0) else 0
            
    def UpdateCroissance(self):
        pos = self.sante + self.bonheur + self.education
        neg = self.criminalite + self.panique 
        self.croissance += float(pos - neg)/100.0
        
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