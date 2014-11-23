__author__ = 'SJS'

import pygame
from defines import COLORS
import resources


class ZoneStatusDisplay(object):
    
    def __init__(self, display, zone, pos):
        # Windows characteristic
        self.bgColor = COLORS.BLACK  
        self.font = pygame.font.SysFont(None, 20)
        self.fontColor = COLORS.WHITE
        self.borderColor = COLORS.DARKGRAY        
              
        self.menuSurface = pygame.Surface( (pos[2], pos[3]) )
        self.screen = display
        self.menuPos = pos
        self.menuCoord = [0, 0, pos[2], pos[3]]

        # Object game data
        self.resources = resources

        self.quitFlag = 0
        
        # Build menu display
        self.items = []
        
        # Each column have 150 pixel so 5 column of 9 row.
        #self.labelCol1 = ("Nourriture", "Materiaux", "Energie")
        self.labelCol1 = ("Agriculture", "Chasse", "Peche", "Bois", "Metaux", "Pierre")
        #self.labelCol2 = ("Petrole", "Eau")        
        self.labelCol3 = ("Population", "Sante", "Bonheur", "Recherche", "Education", "Panique", "Criminalite", "Influence", "Pollution", "Tresors", "Production")    
        #self.labelCol4 = ("Tresors", "Production")         

       
    def ShowStatus(self, zone):
        # Show Zone name
        pygame.draw.rect(self.menuSurface, self.bgColor, self.menuCoord, 0)
        pygame.draw.rect(self.menuSurface, self.borderColor, self.menuCoord, 3)        
        # Zone name
        label = self.font.render(zone.name, 1, self.fontColor)
        self.menuSurface.blit(label, (2, 2))
       
        # Display resource first columns
        self.CreateColumsText(zone, self.labelCol1, 5)
        #self.CreateColumsText(zone, self.labelCol2, 150)
        self.CreateColumsText(zone, self.labelCol3, 300)
        #self.CreateColumsText(zone, self.labelCol4, 450)
             
        self.screen.blit(self.menuSurface, (self.menuPos[0], self.menuPos[1]) )     
        
    def CreateColumsText(self, zone, itemList, posX):
        label = self.font.render("Resource", 1, self.fontColor)
        height = label.get_rect().height
        posY = height
        self.menuSurface.blit(label, (posX, posY))  
        
        label = self.font.render("Stock/Avail/Max", 1, self.fontColor)
        self.menuSurface.blit(label, (posX+110, posY))  
                            
        for index, item in enumerate(itemList):
            resString = ("%s:" % (item))
            label = self.font.render(resString, 1, self.fontColor)
            posY = (index * height) + (height *2) 
            self.menuSurface.blit(label, (posX, posY))
            
            stock = 0
            available = 0
            stockMax = 0
            if item in zone.resources:
                stock = zone.resources[item].stock
                available = zone.resources[item].current
                stockMax = zone.resources[item].max
            resString = ("%d / %d / %d" % (stock, available, stockMax ))
            label = self.font.render(resString, 1, self.fontColor)
            self.menuSurface.blit(label, (posX+110, posY))
