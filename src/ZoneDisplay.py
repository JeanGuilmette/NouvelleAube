__author__ = 'SJS'

import pygame
from defines import COLORS


class ZoneDisplay(object):
    
    def __init__(self, display, zones, pos):
        # Windows characteristic
        self.bgColor = COLORS.BLACK  
        self.font = pygame.font.SysFont(None, 25)
        self.fontColor = COLORS.DARKGREEN
        self.borderColor = COLORS.DARKGRAY        
              
        self.menuSurface = pygame.Surface( (pos[2], pos[3]) )
        self.screen = display
        self.menuPos = pos
        self.menuCoord = [0, 0, pos[2], pos[3]]

        # Object game data
        self.secteur = zones

        self.quitFlag = 0
        
        # Build menu display
        self.items = []
        for index, item in enumerate(self.secteur):
            label = self.font.render(item[0], 1, self.fontColor)
            width = label.get_rect().width
            height = label.get_rect().height
            posx = 5
            posy = (index * height) + 5
            self.items.append([item, label, (width, height), (posx, posy)])


    def draw(self):
        # Redraw the background
        pygame.draw.rect(self.menuSurface, self.bgColor, self.menuCoord, 0)
        pygame.draw.rect(self.menuSurface, self.borderColor, self.menuCoord, 3)

        for name, label, (width, height), (posx, posy) in self.items:
            self.menuSurface.blit(label, (posx, posy))

        self.screen.blit(self.menuSurface, (self.menuPos[0], self.menuPos[1]) )


    def validSelectedMenu(self, event):
        # Read location and which buttons are down...
        buttonPressed = event.dict["button"]
        posX = event.dict["pos"][0]
        posY = event.dict["pos"][1]

        # First: Check Menus. Menus trump all.
        for name, label, (width, height), (posx, posy) in self.items:
            if( (posY > posy) and (posY < (posy+height)) and (posX > posx) and (posX < (posx + width)) ):                    
                return name
        return "none"