import Island
import Events
import EventGenerator
import EnjeuxSurvieEngine
import EventDef
import EventAdvancement
class EventImpact(object):
    def __init__(self, island):
        self.island = island


    def Apply(self, evt):
        if(len(evt.regions) > 0 and len(evt.effects) > 0):
            for s in evt.regions:
                for item in evt.effects: 
                    self.Analyze(evt.name, s, item)          
    
    def Analyze(self, evtName, secteur, effect):
        t = effect.split('=')
        token = t[0]
        value = t[1]
        
        if(token == "population"):
            self.island.ModifyPopulation(secteur, value)
            print("%s modify %s population by %s" % (evtName, secteur, value))
        elif(token == "panic"):
            self.island.ModifyPanic(secteur, value)
            print("%s modify %s panic by %s" % (evtName, secteur, value) )               
        elif(token == "MultiplyPop"):
            pop = self.island.GetCurrentPopulation(secteur)
            mod = pop * float(value)
            self.island.ModifyPopulation(secteur, (mod-pop))
            print("%s modify %s population multiplied by %s" % (evtName, secteur, value) )

        elif(token == "influence"):
            self.island.ModifyInfluence(secteur, value)
            print("%s modify %s Influence by %s" % (evtName, secteur, value) )

        elif(token == "bonheur"):
            self.island.ModifyBonheur(secteur, value)
            print("%s modify %s Bonheur by %s" % (evtName, secteur, value) )

        elif(token == "MultiplyResStock"):
            Ress = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole")
            for Name in Ress:

                t,m,z = self.island.GetRessourceInfo(Name,secteur)
                mod = t * float(value)
                self.island.ModifyRessource(secteur,Name, (mod-t))

        elif(token == "Déplacement de ressources"):
            Ress = ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole")
            Name = "Petrole"

            t,m,z = self.island.GetRessourceInfo(Name,secteur)
            mod = t * float(value)
            self.island.ModifyRessource(secteur,Name, (mod-t))

        #
        # elif(token == "WasteLand"):
        #     secteur.TypeTerrain == Ressources.terrainType["WasteLand"]


        elif(token == "criminalite"):
            self.island.ModifyCriminalite(secteur, value)
            print("%s modify %s criminalite by %s" % (evtName, secteur, value) )

        elif(token == "sante"):
            self.island.ModifySante(secteur, value)
            print("%s modify %s sante by %s" % (evtName, secteur, value) )

        # elif(token == "pollution"):
        #     self.island.Modify(secteur, value)
        #     print("%s modify %s panic by %s" % (evtName, secteur, value) )



        elif(token == "Nego"):
            EventAdvancement.BradvaNegociation = True

        elif(token == "War"):
            EventAdvancement.BradvaWar = True

        elif(token == "Karma"):
            EventAdvancement.KarmaVesuve = True
            