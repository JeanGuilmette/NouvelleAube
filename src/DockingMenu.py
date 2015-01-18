__author__ = 'SJS'

# This module allow to create custom menu. 
# Initializing with list of menu item and display properties.
# Use draw() method to display the menu
# Use validSelectedMenu() on mouse click event to determine which button has been clicked.

import pygame
from Defines import COLORS
import sys; sys.path.append("../lib")
from pgu import gui

class DockingMenu(gui.Widget):
    def __init__(self, display, items, pos=(0,0,10,10), bg_color= COLORS.BLACK, font=None, font_size=30, font_color= COLORS.WHITE):
        gui.Widget.__init__(self, width=pos[2], height=pos[3])
        self.menuSurface =  display
        self.menuPos = pos

        self.bgColor = bg_color

        self.items = items
        self.font = pygame.font.SysFont(font, font_size)
        self.fontColor = font_color
        self.quitFlag = 0

        self.items = []
        for index, item in enumerate(items):
            label = self.font.render(item, 1, font_color)

            width = label.get_rect().width
            height = label.get_rect().height

            posx = (self.menuPos[0]) + (self.menuPos[2]/2) - (width / 2)
            posy = (self.menuPos[1]) + (index * height) + 10

            self.items.append([item, label, (width, height), (posx, posy)])


    def draw(self):

        for name, label, (width, height), (posx, posy) in self.items:
            self.menuSurface.blit(label, (posx, posy))
            name, width, height

    def paint(self, surf):
        self.draw()

    def validSelectedMenu(self, event):
        # Read location and which buttons are down...
        posX = event.dict["pos"][0]
        posY = event.dict["pos"][1]

        # First: Check Menus. Menus trump all.
        for name, label, (width, height), (posx, posy) in self.items:
            if( (posY > posy) and (posY < (posy+height)) and (posX > posx) and (posX < (posx + width)) ): 
                label
                return name
        return "none"