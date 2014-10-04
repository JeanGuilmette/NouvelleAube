# This is the main class for the game. It's the glue and control to execute and play the game.
__author__ = 'SJS'

import pygame
import test.test_itertools
import MainScreen
import DockingMenu
import ZoneDisplay
import ZoneStatusDisplay

from defines import COLORS
from zone import Secteur, ZoneModifier


class EnjeuxSurvie:
    FPS = 30 # frames per second setting
       
    def __init__(self):
        self.display = MainScreen.MainScreen()      # Main screen  to display the game
        self.fpsClock = pygame.time.Clock()         # Timer to calculate time elapsed by turn
        
        # Reference to menu and screen area
        self.buildMenu = None                       # Menu allowing action
        self.zoneMenu = None                        # Menu to select active Zone
        self.resourceMenu = None                    # Show status of resource
        
        # Internal structure to control game
        self.secteur = []                           # List of zone present for on island
        self.quitFlag = False                       # Player want to leave game?
        self.activeZone = None                      # Which zone player currently examine or work with
        self.counter = 0                            # 


    # Build initial island at beginning of a new game
    def ConstructZone(self, nbrZone):
        resList = ("Agriculture", "Chasse", "Peche", "BoisCom", "Petrole")
        resList2 = ("PierreCom", "PierreRare", "MetauxCom", "MetauxRare", "Petrole")        
        for index in range (0, nbrZone):
            zoneName = "Zone %2d" % (index+1)
            if(test.test_itertools.isEven(index)):
                zone = Secteur(zoneName, resList)
            else:
                zone = Secteur(zoneName, resList2)                
            self.secteur.append([zoneName, zone])
        self.activeZone = self.secteur[0]


    # Build reference to all menu
    def CreateAllMenu(self):
        # create build menu
        menu_items = ('Overview', 'Zone', 'Building', 'Resources', 'Options', 'Quit')
        self.buildMenu = DockingMenu.DockingMenu(self.display.GetScreen(), menu_items, [650, 400, 150, 200] )
        
        # Create zone menu
        self.zoneMenu = ZoneDisplay.ZoneDisplay(self.display.GetScreen(), self.secteur, [0, 0, 150, 400] )   
        
        self.resourceMenu = ZoneStatusDisplay.ZoneStatusDisplay(self.display.GetScreen(), self.secteur[0], [0, 400, 650, 200])     
        

    #
    def InitDisplay(self):
        self.display.CreateScreen()


    def DrawWorld(self):
        if (self.display.GetScreen() is not None):
            self.display.GetScreen().fill((COLORS.BLACK)) # Erase entire screen

            # Now re-open the window to display everything
            self.display.SetWindow(0,0,self.display.GetScreenWidth(), self.display.GetScreenHeight())

            #self.display.drawGrid()
            self.zoneMenu.draw()  
            self.buildMenu.draw()
            self.resourceMenu.ShowStatus(self.activeZone)
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
                        continue
                    # If no button pressed, check for button in ZoneMenu
                    zone = self.zoneMenu.validSelectedMenu(event)
                    if(zone[0].lower() != "none"):        
                        print("Zone menu action: %s" % (zone[0]))  
                        if(zone[0].lower() == "quit"):
                            self.quitFlag = True
                        else:
                            #self.resourceMenu.SetSector(zone)
                            #self.resourceMenu.ShowStatus(zone)
                            self.activeZone = zone


    def run(self):
        self.ConstructZone(20)
        self.CreateAllMenu()
        self.DrawWorld()        
        while self.quitFlag == False:
            self.fpsClock.tick(self.FPS)

            # Valid player input
            self.ValidPlayerInput()

            self.UpdateWorld()
            self.DrawWorld()
            pygame.display.flip()


    def GetMainWindow(self):
        return self.display.GetScreen()

    def UpdateWorld(self):
        if(self.counter > (self.FPS * 1)):  #update ressource every 5 secondes
            zoneMod = ZoneModifier("building")
            for zone in self.secteur:
                for res in zone[1].resources.values():
                    res.HourlyAdjustment(zoneMod)
                    res.DailyAdjustment()
            self.counter = 0
        else:
            self.counter =  self.counter + 1
            
        

