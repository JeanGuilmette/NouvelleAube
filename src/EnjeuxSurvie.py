# This is the main class for the game.
# It's the glue and control to execute and play the game.
__author__ = 'SJS'

import zone
import pygame
import MainScreen
import DockingMenu
import ZoneDisplay
import ZoneStatusDisplay
import MapDisplay
import yaml
import Island
import BuildMenu
from time import sleep
from defines import COLORS, FPS
# from zone import ZoneModifier, Secteur


class EnjeuxSurvie:

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
        self.counter = 0

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
        self.resourceMenu = ZoneStatusDisplay.ZoneStatusDisplay(self.GetMainWindow(), self.island.GetActiveZone(), [0, 400, 650, 200])
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
            self.resourceMenu.ShowStatus(self.island.GetActiveZone())
            self.mapDisplay.draw(self.island.GetActiveZone())
            pygame.display.flip()

    def ValidPlayerInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quitFlag = True
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # First check the button of the build menu
                    action = self.buildMenu.validSelectedMenu(event)
                    if(action.lower() != "none"):
                        print("Build menu action: %s" % (action))
                        if(action.lower() == "quit"):
                            self.quitFlag = True
                        elif(action.lower() == "building"):
                        	if(self.island.GetActiveZone().name.lower() != "region"):
	                            print("Show building construction menu")
	                            # Now re-open the window to display everything
	                            self.display.SetWindow(0, 0, self.display.GetScreenWidth(), self.display.GetScreenHeight())
	                            self.buildChoiceMenu.Run(self.island.GetActiveZone())
                    # If no button pressed, check for button in ZoneMenu
                    zone = self.zoneMenu.validSelectedMenu(event)
                    if(zone.lower() != "none"):
                        print("Zone menu action: %s" % (zone))
                        if(zone.lower() == "quit"):
                            self.quitFlag = True
                        else:
                            # self.resourceMenu.SetSector(zone)
                            # self.resourceMenu.ShowStatus(zone)
                            self.island.SetActiveZone(zone)

    def GetMainWindow(self):
        return self.display.GetScreen()

    def UpdateWorld(self):
        # Update production and regeneration of ressource
        # Update Population based on natalite and mortalite
        # Update reserve  based on consomation and entretient
        # Verify if a catastrophe occur
        # Update modifer for production/moral/natalite... science, building
        # Verify if construction is completed
        # New decovery completed^
        # Histoire principal Event

        if(self.counter > (FPS * 1)):  # update ressource every 5 secondes
            zoneMod = zone.ZoneModifier("building")
            zoneMod.prodBuilding = 1
            zoneMod.prodScience = 1
            self.island.UpdateProd()
            self.counter = 0
        else:
            self.counter = self.counter + 1

    # Build initial island at beginning of a new game
    def LoadGame(self, saveFile):
        stream = open(saveFile, 'r')
        print(yaml.load(stream))

    def run(self):
        self.ConstructZone()
        self.CreateAllMenu()
        self.DrawWorld()
        while(self.quitFlag is False):
            self.fpsClock.tick(FPS)

            # Valid player input
            self.ValidPlayerInput()

            self.UpdateWorld()
            self.DrawWorld()
            pygame.display.flip()
