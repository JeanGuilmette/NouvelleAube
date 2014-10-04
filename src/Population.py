__author__ = 'SJS'



class Population():
    def __init__(self, popMax, croissance):
        self.pop_max = popMax
        self.croissance = croissance
        self.santé = 0
        self.influence = 0
        self.bonheur = 0
        self.recherche = 0
        self.éducation = 0
        self.panique = 0
        self.paniquedecatastrophe = 0
        self.criminalité = 0


    def valeur_de_panique(self):
    ##    Calcule la valeur de panique
        self.panique = (self.panique + self.paniquedecatastrophe)
        if unJourPasse == True:
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

    def valeur_de_santé(self):
    ##calcule valeur de santé
        self.santé = (self.effetsantébâtiment + self.effetsantéscience)-self.panique
        if self.santé > 100:
            self.santé =100


    ##-----------------------------------------------------------------------

    def valeur_de_croissance_humaine(self):
        self.croissancepophumaine = (self.santé*self.population*(self.bonheur/10))/(100*self.panique*(self.polution/10)

    def valeur_de_population(self):
        if unJourPasse == True:
            self.pop_secteur += self.croissancepophumaine
            self.population = self.population - (self.population/10)

    #--------------------------------------------------------------------------

    def valeur_de_criminalité(self):
        self.criminalité = ((self.population/100*(self.panique+1))/self.bonheur)+ self.effetcriminalitébâtiment + effetcriminalitéscience

    #--------------------------------------------------------------------------

    def valeurinfluence(self):
        self.influence = ((50*self.santé + 50*self.bonheur)/(500*self.panique + 50*self.criminalité + 1)) + effetinfluencebâtiment + effetinfluencescience

    #--------------------------------------------------------------------------

    def valeur_de_polution(self):
        self.polution= ((self.impactsurpolutiondeschoix+self.effetpolutionbâtiment)*(self.population/500)) + effetpolutionbâtiment + effetpolutionscience

    #--------------------------------------------------------------------------

    def valeuréducation(self):
        self.éducation = (self.effetéducationbâtiment + self.effetéducationscience)/self.panique
    #---------------------------------------------------------------------------

    def valeur_de_recherche(self):
        self.recherche = (self.effetrecherchebâtiment + self.effetrecherchescience)/self.panique
    #----------------------------------------------------------------------------
