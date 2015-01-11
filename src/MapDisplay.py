__author__ = 'SJS'

import pygame
import zone
import Island
import sys; sys.path.append("../lib")
from pgu import gui

class MapDisplay(gui.Widget):
    def __init__(self, zone, width, height):
        gui.Widget.__init__(self, width=width, height=height)
        self.island = zone        
   
    def paint(self, surf):
        zone = self.island.GetActiveZone()
        scale1 = pygame.transform.smoothscale(zone.draw(), (surf.get_width(), surf.get_height()))
        surf.blit(scale1, (0, 0))
        pygame.display.update()