from time import sleep
__author__ = 'SJS'

import pygame
from defines import COLORS, FPS
import Building


class BuildMenu(object):
    
    def __init__(self, display, zone, pos):
        self.fpsClock = pygame.time.Clock()         # Timer to calculate time elapsed by turn
        # Windows characteristic
        self.bgColor = COLORS.BLACK  
        self.font = pygame.font.SysFont(None, 20)
        self.fontColor = COLORS.WHITE
        self.borderColor = COLORS.DARKGRAY        
              
        self.menuSurface = pygame.Surface( (pos[2], pos[3]) )
        self.screen = display
        self.menuPos = pos
        self.menuCoord = [0, 0, pos[2], pos[3]]

        self.quitFlag = False
        
        # Build menu display
        self.items = []
        height = 15
        posX = 0
        for index, item in enumerate(Building.buildingDef):
            posY = (index * height) + (height *2) 
            self.items.append([item, height, (posX, posY)])          

      
        
    def Draw(self, zone):
        # Now re-open the window to display everything
        #self.screen = pygame.rect.Rect(self.menuPos[0], self.menuPos[1], self.menuPos[2], self.menuPos[3])   
             
        # Show Zone name
        pygame.draw.rect(self.menuSurface, self.bgColor, self.menuCoord, 0)
        pygame.draw.rect(self.menuSurface, self.borderColor, self.menuCoord, 3)        
        # Zone name
        label = self.font.render(zone.name, 1, self.fontColor)
        self.menuSurface.blit(label, (2, 2))
        
        # Display resource first columns
        self.CreateColumsText(zone, 5)
              
        self.screen.blit(self.menuSurface, (self.menuPos[0], self.menuPos[1]) )     
        pygame.display.flip()
         
    def CreateColumsText(self, zone, posX):
        label = self.font.render("Building", 1, self.fontColor)
        height = label.get_rect().height
        posY = height
        self.menuSurface.blit(label, (posX, posY))  
         
        label = self.font.render("#", 1, self.fontColor)
        self.menuSurface.blit(label, (posX+110, posY))  
                  
        for index, nameBuilding in enumerate(Building.buildingDef):
            resString = ("%s:" % (nameBuilding))
            label = self.font.render(resString, 1, self.fontColor)
            posY = (index * height) + (height *2) 
            self.menuSurface.blit(label, (posX, posY))
             
            stock = zone.batiments[nameBuilding].numberBuilding
            worker = zone.batiments[nameBuilding].worker
                
            resString = ("%d" % (stock))
            label = self.font.render(resString, 1, self.fontColor)
            self.menuSurface.blit(label, (posX+110, posY))
            
            resString = "Add  -  Destroy"
            label = self.font.render(resString, 1, self.fontColor)
            self.menuSurface.blit(label, (posX+150, posY))
            
            resString = ("Worker: %d" % (worker))
            label = self.font.render(resString, 1, self.fontColor)
            self.menuSurface.blit(label, (posX+300, posY))
                        
            resString = "Add  -  Remove"
            label = self.font.render(resString, 1, self.fontColor)
            self.menuSurface.blit(label, (posX+375, posY))            
           
        resString = ("QUIT")
        label = self.font.render(resString, 1, COLORS.GREEN)
        self.menuSurface.blit(label, (self.menuSurface.get_width()-50, self.menuSurface.get_height()-height ))

            
    def validSelectedMenu(self, event):
        # Read location and which buttons are down...
        buttonPressed = event.dict["button"]
        posX = event.dict["pos"][0] - self.menuPos[0]
        posY = event.dict["pos"][1] - self.menuPos[1]
        if( (posX > self.menuSurface.get_width()-50) and (posY > self.menuSurface.get_height()-75) ):
            return "quit", "quit" 
          
        # First: Check Menus. Menus trump all.
        for name, height, (posx, posy) in self.items:
            if( (posY > posy) and (posY < (posy+height))):
                if( (posX > 150) and (posX < 200) ):    
                    return name, "add"
                if( (posX > 200) and (posX < 300) ):                    
                    return name,"remove"
                if( (posX > 375) and (posX < 425) ):    
                    return name, "worker add"
                if( (posX > 475) and (posX < 525) ):                    
                    return name,"worker remove"         
        return "none", "none"
            
            
    def ValidPlayerInput(self, zone):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quitFlag = True
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # First check the button of the build menu
                    (building, action) = self.validSelectedMenu(event)
                    if(building.lower() != "none"):
                        print("Building windows action: %s" % (building))
                        if(building.lower() == "quit"):
                            self.quitFlag = True
                        elif(action.lower() == "add"):
                            print("construct building")
                            zone.AddBuilding(building, (10,340))
                        elif(action.lower() == "remove"):
                            print("remove building")
                            zone.RemoveBuilding(building)
                        elif(action.lower() == "worker add"):
                            print("add worker")
                            zone.AddWorker(building)
                        elif(action.lower() == "worker remove"):
                            print("remove building")    
                            zone.RemoveWorker(building)

                
    def Run(self, zone):
        self.quitFlag = False
        while(self.quitFlag is False):
            self.fpsClock.tick(FPS)
            self.Draw(zone)
            self.ValidPlayerInput(zone)
          
