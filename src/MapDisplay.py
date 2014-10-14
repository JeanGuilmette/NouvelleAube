__author__ = 'SJS'

import pygame
import zone
from defines import COLORS


class MapDisplay(object):
    def __init__(self, display, zone, pos):
        # Windows characteristic
        self.bgColor = COLORS.BLACK

        self.menuSurface = pygame.Surface((pos[2], pos[3]))
        self.screen = display
        self.menuPos = pos
        self.menuCoord = [0, 0, pos[2], pos[3]]

        # Object game data
        # self.bgImage = pygame.image.load("image/islandMap.jpg")

        self.draw(zone)

    def draw(self, zone):
        # img = zone.draw()
        # self.menuSurface.blit(img, [0, 0])
        scale1 = pygame.transform.scale(zone.draw(), (self.menuPos[2], self.menuPos[3]))
        self.screen.blit(scale1, (self.menuPos[0], self.menuPos[1]))