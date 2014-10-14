import pygame
from defines import COLORS, CELLSIZE


class MainScreen():
    def __init__(self):
        self.screenheight = 600
        self.screenwidth = 800
        self.sizeMod = float(self.screenwidth) / 800.0
        self.isFullscreen = 0
        self.window = pygame.rect.Rect(0,0, self.screenwidth-1, self.screenheight-1)
        self.menuSurface = None
        self.iconSurface = None


    def GetScreenHeight(self):
        return self.screenheight

    def GetScreenWidth(self):
        return self.screenwidth

    def GetSizeMod(self):
        return self.sizeMod

    def SetScreenSize(self, sizeX, sizeY):
        self.screenheight = sizeY
        self.screenwidth = sizeX
        self.sizeMod = self.screenwidth / 800
        self.CheckWindowSize()

    def SetWindow(self, startX, startY, sizeX, sizeY):
        self.window = pygame.rect.Rect(startX, startY, (sizeX - startX)-1, (sizeY - startY)-1)
        self.CheckWindowSize()
        

    def CheckWindowSize(self):
        " Makes sure the window is fully inside the menuSurface. "
        if (self.window.left < self.screenwidth -1):
            self.window.left = 0
        if (self.window.top < self.screenheight -1):
            self.window.top = 0

        if (self.window.right >= self.screenwidth):
            self.window.right = (self.screenwidth - self.left) -1

        if (self.window.bottom >= self.screenheight):
            self.window.bottom = (self.screenheight - self.top)-1

        if (self.menuSurface is not None):
            self.menuSurface.set_clip(self.window)

    
    def CreateScreen(self):
        self.iconSurface = pygame.image.load("image/pygame.bmp")
        pygame.display.set_icon(self.iconSurface)
        self.menuSurface = pygame.display.set_mode((self.screenwidth, self.screenheight), (pygame.FULLSCREEN * self.isFullscreen), 32)
        self.menuSurface.convert()
        pygame.display.set_caption('Enjeux-Survie')
        self.CheckWindowSize()


    def GetScreen(self):
        return self.menuSurface

    def GetWindow(self):
        return self.window

    def drawGrid(self):
        for x in range(0, self.screenwidth, CELLSIZE): # draw vertical lines
            pygame.draw.line(self.menuSurface, COLORS.BLACK, (x, 0), (x, self.screenheight))
        for y in range(0, self.screenheight, CELLSIZE): # draw horizontal lines
            pygame.draw.line(self.menuSurface, COLORS.BLACK, (0, y), (self.screenwidth, y))
        
            