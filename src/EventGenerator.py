import random
import EventDef
import Island
import EventAdvancement
import Events

class GenerateEvents(object):

    def __init__(self, Island):
        self.Island = Island
        self.evtmgr = Events.EventsMgr()

        pass
    
    def Generate(self):
        # qui arrive si l'une des varibles est inférieure ou supérieure à:
        TheList = ["RegionA","RegionB","RegionC", "RegionD","RegionE","RegionF","RegionG", "RegionH","RegionI","RegionJ","RegionK", "RegionL"]
        for secteur in TheList:
            i,b,c=self.Island.GetRessourceInfo("Agriculture", secteur)
            if (b==0):
                EventDef.evt_Guerre_contre_la_Bradva.regions = [secteur]
                return EventDef.evt_Guerre_contre_la_Bradva

        for secteur in TheList:
            i,b,c=self.Island.GetRessourceInfo("Petrole", secteur)
            if(b)==0:
                EventDef.evt_Épuisement_du_pétrole.regions = [secteur]
                return EventDef.evt_Épuisement_du_pétrole
        for secteur in TheList:
            i,b,c=self.Island.GetRessourceInfo("Chasse", secteur)
            if(b)==0:
                EventDef.evt_Épuisement_du_gibier.regions = [secteur]
                return EventDef.evt_Épuisement_du_gibier
        for secteur in TheList:
            i,b,c=self.Island.GetRessourceInfo("Bois", secteur)
            if(b)==0:
                EventDef.evt_Déforestation_totale.regions = [secteur]
                return EventDef.evt_Déforestation_totale
        for secteur in TheList:
            i,b,c=self.Island.GetRessourceInfo("Peche", secteur)
            if(b)==0:
                EventDef.evt_Épuisement_de_la_faune_aquatique.regions = [secteur]
                return EventDef.evt_Épuisement_de_la_faune_aquatique

        # for secteur in TheList:
        #     if(self.Island.GetCurrentPopulation(secteur)==self.Island.GetPopulationMax(secteur)):
        #         EventDef.evt_Surpopulation.regions = [secteur]
        #         return EventDef.evt_Surpopulation
        #
        # for secteur in TheList:
        #     if(self.Island.GetCriminalite(secteur)>80) and (self.Island.GetCriminalite(secteur)<100):
        #         EventDef.evt_Vague_de_crime.regions = [secteur]
        #         return EventDef.evt_Vague_de_crime
        #
        # for secteur in TheList:
        #     if(self.Island.GetBonheur(secteur)<30) and (self.Island.GetCriminalite(secteur)>10):
        #         EventDef.evt_Revolte.regions = [secteur]
        #         return EventDef.evt_Revolte
        #
        # for secteur in TheList:
        #     if(self.Island.GetSante(secteur)<30) and (self.Island.GetCriminalite(secteur)>10):
        #         EventDef.evt_epidemie.regions = [secteur]
        #         return EventDef.evt_epidemie


        # Events au hasard
        a = random.random()
        if (a< 0.2):



            a = random.random()
            if(a > 0.88):
                EventDef.evt_Feu_de_forêt.regions = AreaOfEffect(self.Island)
                return EventDef.evt_Feu_de_forêt
            a = random.random()
            if(a > 0.90):
                EventDef.evt_Tornade.regions = AreaOfEffect(self.Island,"all")
                return EventDef.evt_Tornade

            a = random.random()#+ ((self.Island.GetPollution("Region")/100))
            print("random: %f"% a)

            if(a > 0.95):
                EventDef.evt_seisme.regions = AreaOfEffect(self.Island,"all")
                return EventDef.evt_seisme
            a = random.random()
            if(a > 0.99):
                EventDef.evt_Eruption.regions = AreaOfEffect(self.Island,"volcan")
                return EventDef.evt_Eruption

            a = random.random()
            if(a > 0.97):
                EventDef.evt_Fausse_Eruption.regions = AreaOfEffect(self.Island,"volcan")
                return EventDef.evt_Fausse_Eruption





            if True == True:
                if EventAdvancement.wait != True:

                    a = random.random()
                    c= random.randrange(1,12)
                    b=TheList[c]
                    if(a < self.Island.GetCriminalite(b)):
                        EventAdvancement.wait = True
                        EventDef.evt_Arnaque.regions = [b]
                        return EventDef.evt_Arnaque

                    a = random.random()
                    c= random.randrange(1,12)
                    b=TheList[c]
                    if(a > self.Island.GetSante(b)):
                        EventAdvancement.wait = True
                        EventDef.evt_epidemie.regions = [b]
                        return EventDef.evt_epidemie

                    a = random.random()
                    c= random.randrange(1,12)
                    b=TheList[c]
                    if(a < self.Island.GetCriminalite(b)):
                        EventAdvancement.wait = True
                        EventDef.evt_Vague_de_crime.regions = [b]
                        return EventDef.evt_Vague_de_crime

                    a = random.random()
                    c= random.randrange(1,12)
                    b=TheList[c]
                    if(a > self.Island.GetBonheur(b)):
                        EventAdvancement.wait = True
                        EventDef.evt_Revolte.regions = [b]
                        return EventDef.evt_Revolte


                else:
                    if EventAdvancement.daynumber == 3:
                        EventAdvancement.wait = False
                    else:
                        EventAdvancement.daynumber +=1
        return False






def AreaOfEffect( Island,specification = "none"):
    # A=Foret sud
    # b=prairie nord
    # c=prairie sud
    # d=lac et berge
    # e=collines
    # f=volcan
    # g=marecage
    # h=ile sud-est
    # i=ile nord-ouest
    # j=peninsule sud ile nord ouest
    # k=plage sud
    # l=peninsule(plage) nord

    if specification == "volcan": #partout sauf les deux iles secondaires
        a = []

        if Island.GetCurrentPopulation("RegionA") >0:
            a.append("RegionA")

        if Island.GetCurrentPopulation("RegionB") >0:
            a.append("RegionB")

        if Island.GetCurrentPopulation("RegionC") >0:
            a.append("RegionC")

        if Island.GetCurrentPopulation("RegionD") >0:
            a.append("RegionD")

        if Island.GetCurrentPopulation("RegionE") >0:
            a.append("RegionE")

        if Island.GetCurrentPopulation("RegionF") >0:
            a.append("RegionF")

        if Island.GetCurrentPopulation("RegionG") >0:
            a.append("RegionG")

        if Island.GetCurrentPopulation("RegionH") >0:
            a.append("RegionH")

        if Island.GetCurrentPopulation("RegionK") >0:
            a.append("RegionK")

        if Island.GetCurrentPopulation("RegionL") >0:
            a.append("RegionL")

        return a
    elif specification == "none":
        a=random.randrange(1,12)
        if a==1:
            if Island.GetCurrentPopulation("RegionA") >0:
                return ["RegionA"]
        elif a==2:
            if Island.GetCurrentPopulation("RegionB") >0:
                return ["RegionB"]
        elif a==3:
            if Island.GetCurrentPopulation("RegionC") >0:
                return ["RegionC"]
        elif a==4:
            if Island.GetCurrentPopulation("RegionD") >0:
                return ["RegionD"]
        elif a==5:
            if Island.GetCurrentPopulation("RegionE") >0:
                return ["RegionE"]
        elif a==6:
            if Island.GetCurrentPopulation("RegionF") >0:
                return ["RegionF"]
        elif a==7:
            if Island.GetCurrentPopulation("RegionG") >0:
                return ["RegionG"]
        elif a==8:
            if Island.GetCurrentPopulation("RegionH") >0:
                return ["RegionH"]
        elif a==9:
            if Island.GetCurrentPopulation("RegionI") >0:
                return ["RegionI"]
        elif a==10:
            if Island.GetCurrentPopulation("RegionJ") >0:
                return ["RegionJ"]
        elif a==11:
            if Island.GetCurrentPopulation("RegionK") >0:
                return ["RegionK"]
        elif a==12:
            if Island.GetCurrentPopulation("RegionL") >0:
                return ["RegionL"]


    elif specification == "all":
        a = []

        if Island.GetCurrentPopulation("RegionA") >0:
            a.append("RegionA")

        if Island.GetCurrentPopulation("RegionB") >0:
            a.append("RegionB")

        if Island.GetCurrentPopulation("RegionC") >0:
            a.append("RegionC")

        if Island.GetCurrentPopulation("RegionD") >0:
            a.append("RegionD")

        if Island.GetCurrentPopulation("RegionE") >0:
            a.append("RegionE")

        if Island.GetCurrentPopulation("RegionF") >0:
            a.append("RegionF")

        if Island.GetCurrentPopulation("RegionG") >0:
            a.append("RegionG")

        if Island.GetCurrentPopulation("RegionH") >0:
            a.append("RegionH")

        if Island.GetCurrentPopulation("RegionI") >0:
            a.append("RegionI")

        if Island.GetCurrentPopulation("RegionJ") >0:
            a.append("RegionJ")

        if Island.GetCurrentPopulation("RegionK") >0:
            a.append("RegionK")

        if Island.GetCurrentPopulation("RegionL") >0:
            a.append("RegionL")

        return a







    return ["RegionA"]