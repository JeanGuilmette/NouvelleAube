__author__ = 'SJS'

import pygame
import DockingMenu
from Defines import COLORS
import Musique
class MenuPrincipale(object):
    __menu_items = ('Start', 'Continue', 'Options', 'Quit')
    
    def __init__(self, display):
        self.clock = pygame.time.Clock()
        self.bgImage = pygame.image.load("image/Nouvelle_Aube.jpg")    
        self.menuSurface = display    
        self.menuSurface.blit(self.bgImage, [0,0]) 
               
        sizeX = 100
        sizeY = 100
        X = display.get_rect().width / 2 - (sizeX / 2)
        Y = display.get_rect().height /2 - (sizeY / 2)        
        self.mainMenu = DockingMenu.DockingMenu(display, self.__menu_items, [X, Y, sizeX, sizeY], COLORS.BLACK, None, 30, COLORS.DARKGRAY )        
        #self.showStartScreen()


    def CheckMenu(self):
        while True:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                else:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        menuName = self.mainMenu.validSelectedMenu(event)
                        if(menuName != "none"):
                            print(menuName)
                            #Musique.StopMusic()
                            return menuName
                        
            self.menuSurface.blit(self.bgImage, [0,0])
            self.mainMenu.draw()
            

    def showMenuScreen(self):
        self.mainMenu.draw()
        pygame.display.flip()        
        return self.CheckMenu()
