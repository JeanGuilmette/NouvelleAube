from astropy.units import day
__author__ = 'SJS'


# This is the main class for the game.
# It's the glue and control to execute and play the game.
import time
import datetime
import pygame
import yaml
import MainScreen
import DockingMenu
import ZoneDisplay
import ZoneStatusDisplay
import MapDisplay
import Island
import BuildMenu
from defines import COLORS, FPS, FPS_DELTA, FPS_MIN, FPS_MAX, FPS_DAY
import zone

import sys; sys.path.append("../pgu")
from pgu import gui

        
class EnjeuxSurvieEngine(object):
    def __init__(self, disp):
        self.display = disp                        # Main screen  to display the game
        self.fpsClock = pygame.time.Clock()         # Timer to calculate time elapsed by turn
        
#         # Reference to menu and screen area
#         self.buildMenu = None                       # Menu allowing action
#         self.zoneMenu = None                        # Menu to select active Zone
#         self.resourceMenu = None                    # Show status of resource
#         self.mapDisplay = None                      # Show map of active zone
        
        # Internal structure to control game
        self.island = None                          # Main object containing information on game
        self.technology = dict()                    # List of know technologies
        self.quitFlag = False                       # Player want to leave game?
        self.gameTime = datetime.date(2014, 12, 29) # Fisrt day of the game
        self.counter = 0
        self.tick = FPS
        self.day = FPS_DAY
        self.score = 0
        
    # Build initial island at beginning of a new game
    def ConstructZone(self, filename="new"):
        self.island = Island.Island(filename)

    # Build reference to all menu
    def CreateAllMenu(self):
        self.mainGUI = MainScreen.MainScreen(self.island, self.display)        

    def DrawWorld(self):
        self.mainGUI.update()
        pygame.display.update()

    def ValidPlayerInput(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.quitFlag = True
            else:
                self.mainGUI.event(event)

    def UpdateWorld(self):
        self.counter += 1
        if(self.counter >= self.day):
            # Update game time
            self.gameTime += datetime.timedelta(days=1)
            
            # Update production and regeneration of ressource every day
            self.island.UpdateProd()
                
            # Update Population based on natalite and mortalite
            self.island.UpdatePopulation()
                         
            # Update reserve  based on consomation and entretient
            self.island.UpdateExpandRessource()
            
            # Verify if a catastrophe occur
            # Update modifer for production/moral/natalite... science, building
            # Verify if construction is completed
            # New decovery completed
            # Histoire principal Event  
            self.counter = 0          

    def DrawGameClock(self):
        # Windows characteristic
        self.bgColor = COLORS.BLACK  
        self.font = pygame.font.SysFont(None, 25)
        self.fontColor = COLORS.WHITE
        self.borderColor = COLORS.DARKGRAY   
               
        resString = ("%s - %s dps" % (self.gameTime.isoformat(), self.day))
        label = self.font.render(resString, 1, self.fontColor, self.bgColor)
        surface = self.display
        posX =  surface.get_width() - 75 - (label.get_rect().width/2)
        posY =  surface.get_height() - label.get_rect().height 
        self.display.blit(label, (posX, posY))

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

            # Valid player input
            self.ValidPlayerInput()

#             self.UpdateWorld()
            self.DrawWorld()
#             pygame.display.flip()
#             self.isEndofGame()

    def ProcessKeyInput(self, event):
        if event.key == pygame.K_KP_PLUS:
            self.day = (self.day + FPS_DELTA) 
        elif event.key == pygame.K_KP_MINUS:
            self.day = (self.day - FPS_DELTA)
            
        if (self.day < FPS_MIN):
            self.day = FPS_MIN
        if (self.day > FPS_MAX):
            self.day = FPS_MAX

    def ProcessMouseInput(self, event):
        # First check the button of the build menu
        action = self.buildMenu.validSelectedMenu(event)
        if (action.lower() != "none"):
            print("Build menu action: %s" % (action))
            if (action.lower() == "quit"):
                self.quitFlag = True
            elif (action.lower() == "building"):
                if (self.island.GetActiveZone().name.lower() != "region"):
                    print("Show building construction menu")
                    self.buildChoiceMenu.Run(self.island.GetActiveZone())
    # If no button pressed, check for button in ZoneMenu
        zone = self.zoneMenu.validSelectedMenu(event)
        if (zone.lower() != "none"):
            print("Zone menu action: %s" % (zone))
            if (zone.lower() == "quit"):
                self.quitFlag = True
            else:
                self.island.SetActiveZone(zone) # self.resourceMenu.SetSector(zone)
    
            # self.resourceMenu.ShowStatus(zone)

    def isEndofGame(self):
        pop = self.island.GetCurrentPopulation()
        if(pop <= 0):
            print("Game Over, You have lost")
            self.score = -1
            self.quitFlag = True
        elif(pop >= self.island.GetPopulationMax()):
            print("You have Win Game over")
            self.score = 100
            self.quitFlag = True
            time.sleep(10)
