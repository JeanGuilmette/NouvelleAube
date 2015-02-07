
import pygame
from pygame.locals import *
import sys, os
if sys.platform == 'win32' or sys.platform == 'win64':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

Screen = (800,600)

icon = pygame.Surface((1,1)); icon.set_alpha(0); pygame.display.set_icon(icon)
pygame.display.set_caption("Rounded Rectangle Demo - Ian Mallett - 2008")
surface = pygame.display.set_mode(Screen)

def GetInput():
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT or key[K_ESCAPE]:
            pygame.quit(); sys.exit()

def DrawRoundRect(surface, color, rect, width, xr, yr):
    clip = surface.get_clip()
    
    # left and right
    surface.set_clip(clip.clip(rect.inflate(0, -yr*2)))
    pygame.draw.rect(surface, color, rect.inflate(1-width,0), width)

    # top and bottom
    surface.set_clip(clip.clip(rect.inflate(-xr*2, 0)))
    pygame.draw.rect(surface, color, rect.inflate(0,1-width), width)

    # top left corner
    surface.set_clip(clip.clip(rect.left, rect.top, xr, yr))
    pygame.draw.ellipse(surface, color, pygame.Rect(rect.left, rect.top, 2*xr, 2*yr), width)

    # top right corner
    surface.set_clip(clip.clip(rect.right-xr, rect.top, xr, yr))
    pygame.draw.ellipse(surface, color, pygame.Rect(rect.right-2*xr, rect.top, 2*xr, 2*yr), width)

    # bottom left
    surface.set_clip(clip.clip(rect.left, rect.bottom-yr, xr, yr))
    pygame.draw.ellipse(surface, color, pygame.Rect(rect.left, rect.bottom-2*yr, 2*xr, 2*yr), width)

    # bottom right
    surface.set_clip(clip.clip(rect.right-xr, rect.bottom-yr, xr, yr))
    pygame.draw.ellipse(surface, color, pygame.Rect(rect.right-2*xr, rect.bottom-2*yr, 2*xr, 2*yr), width)

    surface.set_clip(clip)

def main():
    while True:
        GetInput()
        surface.fill((0,0,0))
        DrawRoundRect(surface, (255,0,0), pygame.Rect(100, 100, 200, 200), 0, 32, 32)
        DrawRoundRect(surface, (0,255,0), pygame.Rect(100, 100, 200, 200), 1, 32, 32)

        DrawRoundRect(surface, (0,0,255), pygame.Rect(450,100,250,300), 2, 32, 32)

        DrawRoundRect(surface, (0,0,255), pygame.Rect(150,350,200,200), 0, 32, 32)
        DrawRoundRect(surface, (0,255,0), pygame.Rect(150,350,200,200), 16, 32, 32)

        DrawRoundRect(surface, (0,255,0), pygame.Rect(400,450,350,64), 3, 32, 32)
        pygame.display.flip()

if __name__ == '__main__': main()
