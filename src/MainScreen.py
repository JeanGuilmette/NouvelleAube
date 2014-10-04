import pygame
from defines import COLORS, CELLSIZE


# 
# def LoadWallGraphics(graphicsData):
#     #graphicsData.LoadTexture("walls","art\\brick32.png")
#     graphicsData.LoadTexture("walls","art\\walls.png")
#     graphicsData.spriteRects["walls"].append(pygame.rect.Rect(0,0,32,32))
#     graphicsData.spriteRects["walls"].append(pygame.rect.Rect(32,0,32,32))
#     graphicsData.spriteRects["walls"].append(pygame.rect.Rect(0,32,32,32))
#     graphicsData.spriteRects["walls"].append(pygame.rect.Rect(32,32,32,32))
# 
# 
# def LoadTitleGraphics(graphicsData):
#     graphicsData.LoadTexture("hacktitle","art\\hacktitle.png")
# 
# 
# 
# def LoadItemsGraphics(graphicsData):
#     graphicsData.LoadTexture("items1","art\\items1.png")
#     for y in range(0,8):
#         for x in range(0,8):
#             graphicsData.spriteRects["items1"].append(pygame.rect.Rect(x*32,y*32,32,32))
# 
# def LoadFloorGraphics(graphicsData):
#     graphicsData.LoadTexture("floors","art\\floors.png")
#     for y in range(0,4):
#         for x in range(0,4):
#             graphicsData.spriteRects["floors"].append(pygame.rect.Rect(x*32,y*32,32,32))
# 
# def LoadMonsterGraphics(graphicsData):
#     graphicsData.LoadTexture("monsters1","art\\monsters1.png")
#     for y in range(0,4):
#         for x in range(0,4):
#             graphicsData.spriteRects["monsters1"].append(pygame.rect.Rect(x*32,y*32,32,32))
# 
# 
# 
# def LoadFeaturesGraphics(graphicsData):
#     graphicsData.LoadTexture("features","art\\features.png")
#     for y in range(0,8):
#         for x in range(0,8):
#             graphicsData.spriteRects["features"].append(pygame.rect.Rect(x*32,y*32,32,32))
# 
# 
#     features1 = pygame.transform.rotate(graphicsData.textures["features"][0],90)
#     features2 = pygame.transform.rotate(graphicsData.textures["features"][0],180)
#     features3 = pygame.transform.rotate(graphicsData.textures["features"][0],270)
# 
#     graphicsData.AssignTexture("features1",features1)
#     graphicsData.AssignTexture("features2",features2)
#     graphicsData.AssignTexture("features3",features3)
# 
# 
#     # Now set up the appropriate rects for all 3 rotations
#     for origY in range(0,8):
#         for origX in range(0,8):
#             # 90 degree turn: X0-7 maps to Y7-0, Y0-7 maps to X0-7
#             x = origY
#             y = 7 - origX
#             graphicsData.spriteRects["features1"].append(pygame.rect.Rect(x*32,y*32,32,32))
# 
#             # 180 degree turn: X0-7 maps to X7-0, Y0-7 maps to Y0-7
#             x = 7 - origX
#             y = 7 - origY
#             graphicsData.spriteRects["features2"].append(pygame.rect.Rect(x*32,y*32,32,32))
# 
#             # 270 degree turn: X0-7 maps to Y0-7, Y0-7 maps to X7-0
#             x = 7 - origY
#             y = origX
#             graphicsData.spriteRects["features3"].append(pygame.rect.Rect(x*32,y*32,32,32))




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
        
            