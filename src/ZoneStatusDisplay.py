__author__ = 'SJS'

import pygame
from defines import COLORS
import resources
import Island


class ZoneStatusDisplay(object):
    
    def __init__(self, display, zone, pos):
        self.island = zone
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
        self.labelColResources = ("Agriculture", "Chasse", "Peche", "Bois", "Metaux", "Pierre")
        self.labelCol3 = ("Population", "Sante", "Bonheur", "Recherche", "Education", "Panique", "Criminalite", "Influence", "Pollution", "Tresors", "Production")  
     
    def ShowStatus(self):
        # Show Zone name
        zone = self.island.GetActiveZone()
        pygame.draw.rect(self.menuSurface, self.bgColor, self.menuCoord, 0)
        pygame.draw.rect(self.menuSurface, self.borderColor, self.menuCoord, 3)        
        # Zone name
        label = self.font.render(zone.name, 1, self.fontColor)
        self.menuSurface.blit(label, (2, 2))
       
        # Display resource first columns
        self.CreateRessourcesColumsText(self.labelColResources, 5)
        self.CreatePopulationColumsText(300)
             
        self.screen.blit(self.menuSurface, (self.menuPos[0], self.menuPos[1]) )     
        
    def CreateRessourcesColumsText(self, itemList, posX):
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
            stock, available, stockMax = self.island.GetRessourceInfo(item)
            resString = ("{:0>6d} / {:0>6d} / {:0>6d}".format(stock, available, stockMax ))
            label = self.font.render(resString, 1, self.fontColor)
            self.menuSurface.blit(label, (posX+110, posY))

    def CreatePopulationColumsText(self, posX):
        label = self.font.render("Demographie", 1, self.fontColor)
        height = label.get_rect().height
        posY = height
        self.menuSurface.blit(label, (posX, posY))  
        
        label = self.font.render("Value", 1, self.fontColor)
        self.menuSurface.blit(label, (posX+110, posY))  
 
        posY = posY + height
        self.CreateTextLine("Population", ("%d/%d" % (self.island.GetCurrentPopulation(), self.island.GetPopulationMax()) ), posX, posY)
#         posY = posY + height
#         self.CreateTextLine("Sante", ("%d" % self.island.GetSante()), posX, posY)   
#         posY = posY + height
#         self.CreateTextLine("Bonheur", ("%d" % self.island.GetBonheur()), posX, posY)
#         posY = posY + height
#         self.CreateTextLine("Recherche", ("%d" % self.island.GetRecherche()), posX, posY)        
#         posY = posY + height
#         self.CreateTextLine("Education", ("%d" % self.island.GetEducation()), posX, posY)        
#         posY = posY + height
#         self.CreateTextLine("Panique", ("%d" % self.island.GetPanique()), posX, posY)    
#         posY = posY + height
#         self.CreateTextLine("Criminalite", ("%d" % self.island.GetCriminalite()), posX, posY)            
#         posY = posY + height
#         self.CreateTextLine("Influence", ("%d" % self.island.GetInfluence()), posX, posY)   
#         posY = posY + height
#         self.CreateTextLine("Pollution", ("%d" % self.island.GetPollution()), posX, posY)  
#         posY = posY + height
#         self.CreateTextLine("Production", ("%d" %self.island.GetProduction()), posX, posY)  
#         posY = posY + height
#         self.CreateTextLine("Tresors", ("%d" % self.island.GetTresors()), posX, posY)          
              
                
    def CreateTextLine(self, name, val, posX, posY):
        label = self.font.render(name, 1, self.fontColor)
        self.menuSurface.blit(label, (posX, posY))
        label = self.font.render(val, 1, self.fontColor)
        self.menuSurface.blit(label, (posX + 110, posY))        