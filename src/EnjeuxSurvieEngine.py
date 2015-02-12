__author__ = 'SJS'

# This is the main class for the game.
# It's the glue and control to execute and play the game.
import pygame
import yaml
import MainScreen
import CustomWidget
import Island
import Zone
from Defines import COLORS, FPS
import sys; sys.path.append("../pgu")
from pgu import gui
import Events
import EventDef
import EventEffectAnalyse
import EventGenerator
import EventAdvancement
import EventAdvancement


class EnjeuxSurvieEngine(object):
    def __init__(self, disp):
        self.display = disp                        # Main screen  to display the game
        self.fpsClock = pygame.time.Clock()         # Timer to calculate time elapsed by turn
        
        # Internal structure to control game
        self.island = None                          # Main object containing information on game
        self.technology = dict()                    # List of know technologies
        self.quitFlag = False                       # Player want to leave game?
        self.tick = FPS
        self.score = 0
        self.evtMgr = Events.EventsMgr()            #List of occurred events.
        self.evtGenerator = None

    # Build initial island at beginning of a new game
    def ConstructZone(self, filename="new"):
        self.island = Island.Island(filename)
        self.evtEffect = EventEffectAnalyse.EventImpact(self.island)        
        self.evtGenerator = EventGenerator.GenerateEvents(self.island)

        #crime organise
        EventDef.evt_Aleksei_Vasilev.regions =  EventGenerator.AreaOfEffect(self.island)
        self.evtMgr.add(EventDef.evt_Aleksei_Vasilev)
        EventDef.evt_Emergence_du_crime_organise.regions =  EventGenerator.AreaOfEffect(self.island,"all")
        self.evtMgr.add(EventDef.evt_Emergence_du_crime_organise)

        #Recherche
        EventDef.evt_EnergieThermovolcanique.regions =  EventGenerator.AreaOfEffect(self.island,"all")
        self.evtMgr.add(EventDef.evt_EnergieThermovolcanique)
        EventDef.evt_SchoolAtSleep.regions =  EventGenerator.AreaOfEffect(self.island,"all")
        self.evtMgr.add(EventDef.evt_SchoolAtSleep)
        EventDef.evt_STEP3000.regions =  EventGenerator.AreaOfEffect(self.island,"all")
        self.evtMgr.add(EventDef.evt_STEP3000)
        EventDef.evt_serumUtopia.regions =  EventGenerator.AreaOfEffect(self.island,"all")
        self.evtMgr.add(EventDef.evt_serumUtopia)

        #Fin de jeu
        EventDef.evt_À_la_reconquête_du_monde.regions =  EventGenerator.AreaOfEffect(self.island,"all")
        self.evtMgr.add(EventDef.evt_À_la_reconquête_du_monde)


    # Build reference to all menu
    def CreateAllMenu(self):
        self.mainGUI = MainScreen.MainScreen(self.island, self.display)        

    def DrawWorld(self):
        self.mainGUI.paint()
        pygame.display.update()
       

    def ValidPlayerInput(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.quitFlag = True
            else:
                self.mainGUI.event(event)
    def Gameadvance(self):
        if EventAdvancement.BradvaNegociation == True:
            EventDef.evt_Negociation.regions =  EventGenerator.AreaOfEffect(self.island,"all")
            self.evtMgr.add(EventDef.evt_Negociation)
        if EventAdvancement.BradvaWar == True:
            EventDef.evt_Guerre_contre_la_Bradva.regions =  EventGenerator.AreaOfEffect(self.island,"all")
            self.evtMgr.add(EventDef.evt_Guerre_contre_la_Bradva)
        if EventAdvancement.KarmaVesuve == True:
            EventDef.evt_Éruption_vésuvienne.regions =  EventGenerator.AreaOfEffect(self.island,"all")
            self.evtMgr.add(EventDef.evt_Éruption_vésuvienne)
    def UpdateWorld(self):
        # Update game time
        if(self.mainGUI.gameTime.Tick() == True):
            # Update production and regeneration of ressource every day
            self.island.UpdateProd()
                
            # Update Population based on natalite and mortalite
            self.island.UpdatePopulation()
                         
            # Update reserve  based on consomation and entretient
            # Update modifer for production/moral/natalite... science, building
            self.island.UpdateExpandRessource()
            
            # Verify if a catastrophe occur
            # Verify if construction is completed
            # New decovery completed
            # Histoire principal Event
            moreEvent = True
            while(moreEvent == True):
                self.Gameadvance()
                evt = self.evtMgr.pop(self.mainGUI.gameTime.GetDateString())  
                if(evt == False):
                    moreEvent = False
                else:
                    evt = self.mainGUI.action_event(evt)
                    self.evtEffect.Apply(evt)      

            evt =self.evtGenerator.Generate()
            if(evt != False):
                self.evtMgr.add(evt)     

    # Build initial island at beginning of a new game
    def LoadGame(self, saveFile):
        stream = open(saveFile, 'r')
        print(yaml.load(stream))

    def run(self):
        self.ConstructZone()
        self.CreateAllMenu()
        self.DrawWorld()
        while(self.quitFlag is False):
            self.fpsClock.tick(self.tick)
            self.ValidPlayerInput()
            self.UpdateWorld()
            self.DrawWorld()
            self.isEndofGame()


    def isEndofGame(self):
        pop = self.island.GetCurrentPopulation(Island.OVERVIEW_ZONE_NAME)
        if(pop <= 0):
            EventAdvancement.TrueEnding = True
            print("Game Over, You have lost")
            EventAdvancement.Linkmessage = EventAdvancement.Extinction
            self.score = -1
            self.quitFlag = True
        sante = self.island.GetSante(Island.OVERVIEW_ZONE_NAME)
        if(sante <= 0):
            EventAdvancement.TrueEnding = True
            print("Game Over, You have lost")
            EventAdvancement.Linkmessage = EventAdvancement.LaRedDeath
            self.score = -1
            self.quitFlag = True
        bonheur = self.island.GetBonheur(Island.OVERVIEW_ZONE_NAME)
        if(bonheur <= 0):
            EventAdvancement.TrueEnding = True
            print("Game Over, You have lost")
            EventAdvancement.Linkmessage = EventAdvancement.LaRevolution
            self.score = -1
            self.quitFlag = True
        Criminalite = self.island.GetCriminalite(Island.OVERVIEW_ZONE_NAME)
        if(Criminalite >= 100):
            EventAdvancement.TrueEnding = True
            print("Game Over, You have lost")
            EventAdvancement.Linkmessage = EventAdvancement.Coup_etat
            self.score = -1
            self.quitFlag = True
        Influence = self.island.GetInfluence(Island.OVERVIEW_ZONE_NAME)
        if(Influence <= 0):
            EventAdvancement.TrueEnding = True
            print("Game Over, You have lost")
            EventAdvancement.Linkmessage = EventAdvancement.Anarchie
            self.score = -1
            self.quitFlag = True

        if EventAdvancement.KarmaVesuve == True:
            EventAdvancement.TrueEnding = True
            print("Game Over, You have WIN")
            EventAdvancement.Linkmessage = EventAdvancement.Vesuve
            self.score = -1
            self.quitFlag = True

        if EventAdvancement.WIN == True:
            EventAdvancement.TrueEnding = True
            EventAdvancement.HappyEnd = True
            print("Game Over, You have WIN")
            EventAdvancement.Linkmessage = EventAdvancement.Gagne
            self.score = -1
            self.quitFlag = True

        if self.quitFlag == True:


            EventAdvancement.Ending_Bonheur = str(int(self.island.GetBonheur(Island.OVERVIEW_ZONE_NAME)))
            EventAdvancement.Ending_Influence= str(int(self.island.GetInfluence(Island.OVERVIEW_ZONE_NAME)))
            EventAdvancement.Ending_Sante= str(int(self.island.GetSante(Island.OVERVIEW_ZONE_NAME)))
            EventAdvancement.Ending_Education = str(int(self.island.GetEducation(Island.OVERVIEW_ZONE_NAME)))
            EventAdvancement.Ending_Criminalite = str(int(self.island.GetCriminalite(Island.OVERVIEW_ZONE_NAME)))
            EventAdvancement.Ending_Population = str(int(self.island.GetCurrentPopulation(Island.OVERVIEW_ZONE_NAME)))
            EventAdvancement.Ending_Pollution = str(int(self.island.GetPollution(Island.OVERVIEW_ZONE_NAME)))
            EventAdvancement.Ending_Panique = str(int(self.island.GetPanique(Island.OVERVIEW_ZONE_NAME)))
