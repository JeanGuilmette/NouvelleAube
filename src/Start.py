# Base de jeu. Code central pour le faire fonctionner.
# Principalement des variables globales pour faire fonctionner
# toutes les autres parties du programmes.
# Ce fichier permet donc de faire le lien entre elles.

import pygame
pygame.init()
import EnjeuxSurvie
import Introduction
import MenuPrincipale
import EndGame
import StoryTelling

if __name__ == "__main__":
    # Create main windows
    game = EnjeuxSurvie.EnjeuxSurvie()

    # Display introduction splash screen
    Introduction.Introduction(game.GetMainWindow())
  
    # Create and display Start menu
    mainMenu = MenuPrincipale.MenuPrincipale(game.GetMainWindow())
    action = mainMenu.showMenuScreen()
    if(action.lower() == "start"):
        StoryTelling.StoryTelling(game.GetMainWindow())        
        game.run()
    elif(action.lower() == "continue"):
        game.run()
    elif(action.lower() == "option"):
        game.run()

    # Game Over
    EndGame.EndGame(game.GetMainWindow(), game.score)
