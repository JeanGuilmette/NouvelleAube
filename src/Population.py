__author__ = 'SJS'



class Population():
    def __init__(self, popMax, croissance):
        self.popMax = popMax            # Maximum of population supported by the island
        self.croissance = croissance    # Number of new people by unit of time.
        self.sante= 50                  #
        self.influence = 0              #
        self.bonheur = 50               #
        self.recherche = 0              # 
        self.education =  50            #
        self.panique = 50               #
        self.paniquedecatastrophe = 50  #
        self.criminalite = 50           #
        self.current = 0                #
        self.counter = 0                # Count number of day passed
        self.workerCurrent = 0
        self.workerIdle = 0
        self.workerMax = self.current * 0.8

    
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
        neg = self.criminalite + self.panique + self.paniquedecatastrophe 
        self.croissance += float(pos - neg)/100.0
        print("Croissant: %f" % self.croissance)
        
    def UpdateMaxWorker(self):
        self.workerMax = self.current * 0.80
    
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