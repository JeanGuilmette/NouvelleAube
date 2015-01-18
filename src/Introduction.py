__author__ = 'SJS'

import pygame
from Defines import COLORS


class Introduction():
    def __init__(self, display):
        self.menuSurface =  display
        self.scr_width = self.menuSurface.get_rect().width
        self.scr_height = self.menuSurface.get_rect().height

        self.bgColor = COLORS.BLACK
        self.clock = pygame.time.Clock()
        
        self.bgImage = pygame.image.load("image/Nouvelle_Aube.jpg")

        self.font = pygame.font.SysFont(None, 30)
        self.showScreen()


    def drawPressKeyMsg(self):
        pressKeySurf =  self.font.render('Press a key to play.', True, COLORS.YELLOW)
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = ( self.scr_width - 200,  self.scr_height - 30)
        self.menuSurface.blit(pressKeySurf, pressKeyRect)


    def checkForKeyPress(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYUP: 
                return "quit"
        return "none"


    def showScreen(self):
        titleFont = pygame.font.Font('freesansbold.ttf', 100)
        titleSurf1 = titleFont.render('Nouvelle Aube', True, COLORS.BLACK)

        degrees1 = 0
        scale1 = 0.1
        while True:
            self.menuSurface.blit(self.bgImage, [0,0])
            
            rotatedSurf1 = pygame.transform.rotozoom(titleSurf1, degrees1, scale1)
            rotatedRect1 = rotatedSurf1.get_rect()
            rotatedRect1.center = ( self.scr_width / 2,  self.scr_height / 2)
            self.menuSurface.blit(rotatedSurf1, rotatedRect1)

            self.drawPressKeyMsg()

            if self.checkForKeyPress().lower() == "quit":
                pygame.event.get() # clear event queue
                self.menuSurface.fill(self.bgColor) # Redraw the background
                return
            
            pygame.display.update()
            self.clock.tick(20)
            if degrees1 < 360:
                degrees1 += 18 # rotate by 18 degrees each frame
                scale1 += 0.05 # rotate by 7 degrees each frame
            else:
                degrees1 = 360 # rotate by 18 degrees each frame
                scale1 = 1.0 # rotate by 7 degrees each frame            
                
