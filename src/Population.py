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


    def HourlyPanicAdlustment(self):
    ##    Calcule la valeur de panique
        self.panique = (self.panique + self.paniquedecatastrophe)
        if self.panique > 0:
            self.panique = (self.panique/10) -1
        if self.panique < 0:
            self.panique = 0

    #----------------------------------------------------------------------


    def valeur_de_bonheur(self):
    ##calcule valeur de bonheur
        self.bonheur = (self.effetbonheurbâtiment + self.effetbonheurscience)-self.panique
        if self.bonheur >100:
            self.bonheur = 100

    #----------------------------------------------------------------------

    def valeur_de_sante(self):
    ##calcule valeur de santé
        self.sante = (self.effetsantébâtiment + self.effetsantéscience)-self.panique
        if self.sante > 100:
            self.sante =100


    ##-----------------------------------------------------------------------

    def valeur_de_croissance_humaine(self):
        self.croissancepophumaine = (self.sante*self.population*(self.bonheur/10))/(100*self.panique*(self.polution/10))


    def valeur_de_population(self):
        #if unJourPasse == True:
        self.pop_secteur += self.croissancepophumaine
        self.population = self.population - (self.population/10)

    #--------------------------------------------------------------------------

    def valeur_de_criminalite(self):
        self.criminalite = ((self.population/100*(self.panique+1))/self.bonheur) #+ self.effetcriminalitebatiment + effetcriminalitescience

    #--------------------------------------------------------------------------

    def valeurinfluence(self):
        self.influence = ((50*self.sante + 50*self.bonheur)/(500*self.panique + 50*self.criminalite + 1)) #+ effetinfluencebâtiment + effetinfluencescience

    #--------------------------------------------------------------------------

    def valeur_de_polution(self):
        self.polution= ((self.impactsurpolutiondeschoix+self.effetpolutionbâtiment)*(self.population/500)) # + effetpolutionbâtiment + effetpolutionscience

    #--------------------------------------------------------------------------

    def valeurEducation(self):
        pass #self.éducation = (self.effetéducationbâtiment + self.effetéducationscience)/self.panique
    #---------------------------------------------------------------------------

    def valeur_de_recherche(self):
        pass #self.recherche = (self.effetrecherchebâtiment + self.effetrecherchescience)/self.panique
    #----------------------------------------------------------------------------
