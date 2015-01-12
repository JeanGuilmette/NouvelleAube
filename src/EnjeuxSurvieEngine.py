__author__ = 'SJS'

# This is the main class for the game.
# It's the glue and control to execute and play the game.
import pygame
import yaml
import MainScreen
import CustomWidget
import Island
import zone
from defines import COLORS, FPS
import sys; sys.path.append("../pgu")
from pgu import gui

        
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
        
    # Build initial island at beginning of a new game
    def ConstructZone(self, filename="new"):
        self.island = Island.Island(filename)

    # Build reference to all menu
    def CreateAllMenu(self):
        self.mainGUI = MainScreen.MainScreen(self.island, self.display)        

    def DrawWorld(self):
        self.mainGUI.paint()
#         self.mainGUI.update()
        pygame.display.update()
        pygame.display.flip()        

    def ValidPlayerInput(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.quitFlag = True
            else:
                self.mainGUI.event(event)

    def UpdateWorld(self):
        # Update game time
        if(self.mainGUI.gameTime.Tick() == True):
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
