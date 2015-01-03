from astropy.units import day
__author__ = 'SJS'


# This is the main class for the game.
# It's the glue and control to execute and play the game.

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
from defines import COLORS, FPS, FPS_DELTA, FPS_MIN, FPS_MAX
import zone

        
class EnjeuxSurvie(object):
    def __init__(self):
        self.display = MainScreen.MainScreen()      # Main screen  to display the game
        self.fpsClock = pygame.time.Clock()         # Timer to calculate time elapsed by turn
        
        # Reference to menu and screen area
        self.buildMenu = None                       # Menu allowing action
        self.zoneMenu = None                        # Menu to select active Zone
        self.resourceMenu = None                    # Show status of resource
        self.mapDisplay = None                      # Show map of active zone
        
        # Internal structure to control game
        self.island = None                          # Main object containing information on game
        self.technology = dict()                    # List of know technologies
        self.quitFlag = False                       # Player want to leave game?
        self.gameTime = datetime.date(2014, 12, 29) # Fisrt day of the game
        self.counter = 0
        self.tick = FPS
        
        # Initialize display
        self.display.CreateScreen()

    # Build initial island at beginning of a new game
    def ConstructZone(self, filename="new"):
        self.island = Island.Island(filename)

    # Build reference to all menu
    def CreateAllMenu(self):
        # create build menu
        menu_items = ('Zone', 'Building', 'Resources', 'Options', 'Quit')
        self.buildMenu = DockingMenu.DockingMenu(self.GetMainWindow(), menu_items, [650, 400, 150, 200])

        # Create zone menu
        self.zoneMenu = ZoneDisplay.ZoneDisplay(self.GetMainWindow(), self.island.secteur, [0, 0, 150, 400])
        self.resourceMenu = ZoneStatusDisplay.ZoneStatusDisplay(self.GetMainWindow(), self.island, [0, 400, 650, 200])
        self.mapDisplay = MapDisplay.MapDisplay(self.GetMainWindow(), self.island.GetActiveZone(), [150, 0, 650, 400])
        
        # Create build menu
        self.buildChoiceMenu = BuildMenu.BuildMenu(self.GetMainWindow(), self.island.GetActiveZone(), [50, 50, 550, 300])

    def DrawWorld(self):
        if (self.display.GetScreen() is not None):
            self.display.GetScreen().fill((COLORS.BLACK))  # Erase entire screen

            # Now re-open the window to display everything
            self.display.SetWindow(0, 0, self.display.GetScreenWidth(), self.display.GetScreenHeight())

            self.display.drawGrid()
            self.zoneMenu.draw()
            self.buildMenu.draw()
            self.resourceMenu.ShowStatus()
            self.mapDisplay.draw(self.island.GetActiveZone())
            self.DrawGameClock()
            pygame.display.flip()
            

    def ValidPlayerInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quitFlag = True
            elif event.type == pygame.KEYDOWN:
                self.ProcessKeyInput(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.ProcessMouseInput(event)

    def GetMainWindow(self):
        return self.display.GetScreen()

    def UpdateWorld(self):
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

    def DrawGameClock(self):
        # Windows characteristic
        self.bgColor = COLORS.BLACK  
        self.font = pygame.font.SysFont(None, 25)
        self.fontColor = COLORS.WHITE
        self.borderColor = COLORS.DARKGRAY   
              
        resString = ("%s - %s dps" % (self.gameTime.isoformat(), self.tick))
        label = self.font.render(resString, 1, self.fontColor, self.bgColor)
        surface = self.display.GetScreen()
        posX =  surface.get_width() - 75 - (label.get_rect().width/2)
        posY =  surface.get_height() - label.get_rect().height 
        self.display.GetScreen().blit(label, (posX, posY))

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

            self.UpdateWorld()
            self.DrawWorld()
            pygame.display.flip()

    def ProcessKeyInput(self, event):
        if event.key == pygame.K_KP_PLUS:
            self.tick = (self.tick + FPS_DELTA) 
        elif event.key == pygame.K_KP_MINUS:
            self.tick = (self.tick - FPS_DELTA)
            
        if (self.tick < FPS_MIN):
            self.tick = FPS_MIN
        if (self.tick > FPS_MAX):
            self.tick = FPS_MAX

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
                    # Now re-open the window to display everything
                    self.display.SetWindow(0, 0, self.display.GetScreenWidth(), self.display.GetScreenHeight())
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


