# Base de jeu. Code central pour le faire fonctionner.
# Principalement des variables globales pour faire fonctionner
# toutes les autres parties du programmes.
# Ce fichier permet donc de faire le lien entre elles.

import pygame
pygame.init()
import Musique
import EnjeuxSurvieEngine
import Introduction
import MenuPrincipale
import EndGame
import StoryTelling
import EventAdvancement

def CreateMainWindows():
        pygame.display.set_caption('Nouvelle Aube')
        pygame.display.set_icon(pygame.image.load("image/Nouvelle_Aube.jpg"))
        disp = pygame.display.set_mode((1027, 768), 0, 32)
        disp.convert_alpha()
        return disp
    
    
if __name__ == "__main__":
    # Create main windows
    disp = CreateMainWindows()

    # Display introduction splash screen
    Introduction.Introduction(disp)
  
    # Create and display Start menu
    mainMenu = MenuPrincipale.MenuPrincipale(disp)
    action = mainMenu.showMenuScreen()
    
    game = EnjeuxSurvieEngine.EnjeuxSurvieEngine(disp) 
    if(action.lower() == "start"):
        Musique.PlaySound(EventAdvancement.sound_validation)
        #StoryTelling.StoryTelling(disp)
        game.run()
    elif(action.lower() == "continue"):
        Musique.PlaySound(EventAdvancement.sound_validation)
        game.run()
    elif(action.lower() == "option"):
        Musique.PlaySound(EventAdvancement.sound_validation)
        game.run()

    # Game Over
    #EndGame.EndGame(disp, game.score)
    EndGame.EndGame(disp, game.island)