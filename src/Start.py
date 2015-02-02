# Base de jeu. Code central pour le faire fonctionner.
# Principalement des variables globales pour faire fonctionner
# toutes les autres parties du programmes.
# Ce fichier permet donc de faire le lien entre elles.

import pygame
pygame.init()
import EnjeuxSurvieEngine
import Introduction
import MenuPrincipale
import EndGame
import StoryTelling


def CreateMainWindows():
        pygame.display.set_caption('Enjeux-Survie')        
        pygame.display.set_icon(pygame.image.load("image/pygame.bmp"))
        disp = pygame.display.set_mode((1027, 768), 0, 32)
        disp.convert_alpha()
        return disp
    
    
if __name__ == "__main__":
    # Create main windows
    disp = CreateMainWindows()

    # Display introduction splash screen
#     Introduction.Introduction(disp)
  
    # Create and display Start menu
    mainMenu = MenuPrincipale.MenuPrincipale(disp)
    action = mainMenu.showMenuScreen()
    
    game = EnjeuxSurvieEngine.EnjeuxSurvieEngine(disp) 
    if(action.lower() == "start"):
#         StoryTelling.StoryTelling(disp)        
        game.run()
    elif(action.lower() == "continue"):
        game.run()
    elif(action.lower() == "option"):
        game.run()

    # Game Over
    EndGame.EndGame(disp, game.score)
