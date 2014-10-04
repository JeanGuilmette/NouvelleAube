
from unittest import TestCase
from ZoneStatusDisplay import *
from zone import Secteur
pygame.init()

class TestZoneStatusDislay(TestCase):

    def testCreation(self):
        display = pygame.display.set_mode((600, 800), 0, 32)        
        resList = ("Agriculture", "Chasse") 
        zone = Secteur("Zone 1", resList)
        secteur = ["Zone 1", zone]
        resourceMenu = ZoneStatusDisplay(display, secteur, [0, 450, 650, 150])
        resourceMenu.draw()    
        pygame.display.flip();
        resourceMenu.draw()            
        