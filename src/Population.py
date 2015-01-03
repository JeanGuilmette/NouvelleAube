__author__ = 'SJS'



class Population():
    def __init__(self, popMax, croissance):
        self.popMax = popMax            # Maximum of population supported by the island
        self.croissance = croissance    # Number of new people by unit of time.
        self.sante= 0                   #
        self.influence = 0              #
        self.bonheur = 0                #
        self.recherche = 0              # 
        self.education =  0             #
        self.panique = 0                #
        self.paniquedecatastrophe = 0   #
        self.criminalite = 0            #
        self.current = 0                #
        self.counter = 0                # Count number of day passed

    
    def PopulationAdjustment(self):
        if(self.counter >= 30):
            self.current += (self.current * self.croissance)
            if(self.current > self.popMax):
                self.current = self.popMax
            self.counter = 0
        else:
            self.counter += 1
