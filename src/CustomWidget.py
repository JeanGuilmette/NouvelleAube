__author__ = 'SJS'
import time
import datetime
import pygame
from Defines import COLORS, FPS, FPS_MIN, FPS_MAX, FPS_DAY
import Resources
import Island
import Zone
import sys; sys.path.append("../lib")
from pgu import gui, text

class RessourceLabel(gui.Label):
    def __init__(self, island, activeZone, resName):
        self.resource = resName
        self.island = island
        self.zoneCtl = activeZone
        stock, available, stockMax = self.island.GetRessourceInfo(self.resource, self.zoneCtl.value)
        resString = ("{:0>6d} | {:0>6d} | {:0>6d}".format(stock, available, stockMax ))
        gui.Label.__init__(self, value=resString)
        
    def paint(self, surf):
        stock, available, stockMax = self.island.GetRessourceInfo(self.resource, self.zoneCtl.value)
        self.value = ("{:0>6d} | {:0>6d} | {:0>6d}".format(stock, available, stockMax ))
        if(available < (0.3 * stockMax)):
            self.style.color = (255, 0, 0)
        else:
            self.style.color = (0, 0, 0)            
        gui.Label.paint(self, surf)
       
class StockLabel(gui.Label):
    def __init__(self, island, activeZone, resName):
        self.resource = resName
        self.island = island
        self.zoneCtl = activeZone
        stock, available, stockMax = self.island.GetRessourceInfo(self.resource, self.zoneCtl.value)
        resString = ("{:0>6d}".format(stock))
        gui.Label.__init__(self, value=resString)
        
    def paint(self, surf):
        stock, available, stockMax = self.island.GetRessourceInfo(self.resource, self.zoneCtl.value)
        self.value = ("{:0>6d}".format(stock))
        gui.Label.paint(self, surf)
        
              
class DemographieLabel(gui.Label):
    def __init__(self, island, activeZone, popName):
        self.popName = popName
        self.island = island
        self.zoneCtl = activeZone
        resString = self.BuildString()
        gui.Label.__init__(self, value=resString)
        
    def paint(self, surf):
        self.value = self.BuildString()
        gui.Label.paint(self, surf)     
        self.resize() 
      
    def BuildString(self):  
        if(self.popName == "PopulationActive"):
            return ("%6d   " % (self.island.GetCurrentPopulation(self.zoneCtl.value)))
        if(self.popName == "Population"):
            return ("%d/%d" % (self.island.GetCurrentPopulation(self.zoneCtl.value), self.island.GetPopulationMax(self.zoneCtl.value)) )
        elif(self.popName == "Worker"):
            return ("%d/%d/%d" % (self.island.GetCurrentWorker(self.zoneCtl.value), self.island.GetAvailableWorker(self.zoneCtl.value), self.island.GetMaxWorker(self.zoneCtl.value)) )
        elif(self.popName == "Sante"):
            return ("%2.2f" % self.island.GetSante(self.zoneCtl.value))
        elif(self.popName == "Bonheur"):
            return ("%2.2f" % self.island.GetBonheur(self.zoneCtl.value))
        elif(self.popName == "Recherche"):
            return ("%2.2f" % self.island.GetRecherche(self.zoneCtl.value))
        elif(self.popName == "Education"):
            return ("%2.2f" % self.island.GetEducation(self.zoneCtl.value))
        elif(self.popName == "Panique"):
            return ("%2.2f" % self.island.GetPanique(self.zoneCtl.value))
        elif(self.popName == "Criminalite"):
            return ("%2.2f" % self.island.GetCriminalite(self.zoneCtl.value))
        elif(self.popName == "Influence"):
            return ("%2.2f" % self.island.GetInfluence(self.zoneCtl.value))
        elif(self.popName == "Pollution"):
            return ("%2.2f" % self.island.GetPollution(self.zoneCtl.value))
        elif(self.popName == "Production"):
            return ("%d" % self.island.GetProduction(self.zoneCtl.value))
        elif(self.popName == "Tresors"):
            return ("%d" % self.island.GetTresors(self.zoneCtl.value))        
        else:
            return "Not Applicable"  
                       
class MapDisplay(gui.Widget):
    def __init__(self, zone, width, height):
        gui.Widget.__init__(self, width=width, height=height)
        self.island = zone        
   
    def paint(self, surf):
        zone = self.island.GetActiveZone()
        scale1 = pygame.transform.smoothscale(zone.draw(), (surf.get_width(), surf.get_height()))
        surf.blit(scale1, (0, 0))

class MessageBox(gui.Dialog):
    def __init__(self, Title, msg, icon=None): 
        
        title = gui.Label(Title)
        t = gui.Table()
        t.tr()
        doc = CreateMessage(msg, 400, icon)
        t.td(gui.ScrollArea(doc, 400, 300, hscrollbar=False,  vscrollbar=True))
        
        t.tr()
        b = gui.Button("Close")
        b.connect(gui.CLICK, self.action_quit)  
        t.td(b)  
            
        gui.Dialog.__init__(self, title, t, background=( 128, 128, 128, 10) )
#         gui.Dialog.__init__(self, title, t )       
          
    def action_quit(self):
        pygame.event.post(pygame.event.Event(pygame.QUIT))  
                                  
    def open(self, w=None, x=None, y=None):
        gui.Dialog.open(self)
        done = False
        while not done:
            pygame.time.wait(5)             
            self.get_toplevel().update()
            pygame.display.update()
            # Process events
            for ev in pygame.event.get():
                if (ev.type == pygame.QUIT or 
                    ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE):
                    done = True
                else:
                    # Pass the event off to pgu
                    self.get_toplevel().event(ev)
        self.close()
                    
                            
class GameClock(gui.Label):
    def __init__(self):
        self.counter = 0
        self.day = FPS_DAY
        self.gameTime = datetime.date(2014, 12, 29) # Fisrt day of the game
        gui.Label.__init__(self, value=self.gameTime.isoformat())       
   
    def paint(self, surf):
        self.value =   self.gameTime.isoformat()
        gui.Label.paint(self, surf)  

        
    def Tick(self):
        self.counter += 1
        if(self.counter >= self.day):        
            self.gameTime += datetime.timedelta(days=1)
            self.counter = 0
            return True
        return False
    
    def GetDateString(self):
        return self.value
           


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
    
#///////////////////////////////////////////////////////////////////////////////////////////
#///
#/// 
def CreateMessage(text, width, icon=None, align=-1, fontName=None, fontSize=30):
    font = pygame.font.SysFont(fontName, fontSize)        
    space = font.size(" ")      
    doc = gui.Document(width=width) 
    doc.block(align=align)
    if(icon != None):
        doc.add(gui.Image(icon),align=1)    
    for word in text.split(" "): 
        doc.add(gui.Label(word))
        doc.space(space)
    return doc