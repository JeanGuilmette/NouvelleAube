__author__ = 'SJS'

import pygame
from defines import COLORS


class EndGame():
    def __init__(self, display, score):
        self.menuSurface =  display
        self.scr_width = self.menuSurface.get_rect().width
        self.scr_height = self.menuSurface.get_rect().height

        self.bgColor = COLORS.BLACK
        self.clock = pygame.time.Clock()
        
        self.bgImage = pygame.image.load("image/Nouvelle_Aube.jpg")        

        self.font = pygame.font.SysFont(None, 30)
        
        self.score = score
        self.showScreen()


    def drawPressKeyMsg(self):
        pressKeySurf =  self.font.render('Press a key to exit.', True, COLORS.YELLOW)
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
        titleSurf1 = titleFont.render('Game Over!', True, COLORS.DARKGRAY)
        resString = ("Your Score: %d" % (self.score))
        scoreSurf = titleFont.render(resString, True, COLORS.BLACK)
 
        centerX = (self.menuSurface.get_rect().width/2) - (scoreSurf.get_rect().width/2)
        centerY = (self.menuSurface.get_rect().height/2) - (scoreSurf.get_rect().height/2)
        posX = 50
        posY = 50
        dirY = -1
        dirX = 1
        while True:
            self.menuSurface.blit(self.bgImage, [0,0])
            self.menuSurface.blit(titleSurf1, ( posX, posY) )
            self.menuSurface.blit(scoreSurf, (centerX, centerY))

            self.drawPressKeyMsg()

            if self.checkForKeyPress().lower() == "quit":
                pygame.event.get() # clear event queue
                self.menuSurface.fill(self.bgColor) # Redraw the background
                return
            
            pygame.display.update()
            self.clock.tick(60)
            
            expX = posX + dirX + titleSurf1.get_rect().width
            expY = posY + dirY + titleSurf1.get_rect().height
            dirX =  dirX if( ( expX < self.scr_width) and (posX + dirX > 0)) else -dirX
            posX += dirX
            dirY =  dirY if( ( expY < self.scr_height) and (posY + dirY > 0)) else -dirY
            posY += dirY                 

       
            