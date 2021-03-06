'''
Created on Dec 24, 2014

@author: JA
'''
# Pour permettre <aparition des evenements
import pygame
import sys; 
import CustomWidget
import Musique
import EventAdvancement
sys.path.append("../lib")
sys.path.append("../src")
import Musique
from pgu import gui
from pygame.transform import smoothscale
import Island



##########################################################
#
##########################################################                                                        
class Event(object): 
    def __init__(self, date, title, description, options):
        self.date = date
        self.name = title
        self.desc = description
        self.options = options
        self.effects = []
        self.regions = []   
        self.surf = "" 
        self.surfRect = ""         
    
    
##########################################################
#
##########################################################      
class EventsMgr(object):
    def __init__(self):
        self.eventList = dict()
    
    def add(self, evt ):
        if(evt.date in self.eventList):
            self.eventList[evt.date].append(evt) 
        else:
            self.eventList[evt.date] = [evt]
    
    def pop(self, date):
        # Return event always trigged
        if("now" in self.eventList):
            if(len(self.eventList["now"]) > 0):
                return self.eventList["now"].pop(0)
            else:
                del self.eventList["now"]
        
        # Return event trigged for a specific date
        if(date in self.eventList):
            if(len(self.eventList[date]) > 0):
                return self.eventList[date].pop(0)
            else:
                del self.eventList[date]
        
        return False

   
##########################################################
#
##########################################################                 
class EventsViewer(gui.Table):  
    winWidth = 640
    winHeigth = 400
    btnCoord = pygame.Rect(10, 325, 300, 30) 
    borderSize = 10
    label_height = 20     
    cadreCoord = pygame.Rect(10, 15, 630, 545) 
    descCoord = pygame.Rect( 5, 5, 625, 128)  
    descBoxCoord = pygame.Rect( 10, 50,630, 130)    
    OptIdCoord = pygame.Rect(20, 165, 198, 320)  
    OptIdBoxCoord = pygame.Rect(10, 184, 198, 320)  
    OptCoord = pygame.Rect(204, 140, 428, 320) 
    OptBoxCoord = pygame.Rect(212, 184, 428, 320) 
 
    def __init__(self, island, event, **params):
        # Initialize internal object  
        self.isOpen = False 
        params.setdefault('cls','dialog')
        gui.Table.__init__(self,**params)
        
        self.value = gui.Form()
        self.island = island
        self.gameEvent = event
  
        #Add space at dialog top
        self.tr() 
        self.td(gui.Label("   " ))  
                        
        self.tr()
        
        regionString = self.BuildRegionString(self.gameEvent)
        title =  gui.Label("Event: %s les régions touché sont: %s" % (self.gameEvent.name, regionString) ) 
        self.td(title,align=0,cls=self.cls+'.bar')
        
        # Create container
        c = gui.Container(width=640, heigth=400)
          
        # Description
        doc = CreateDescription( self.gameEvent.desc, 600)
        self.displayDesc = gui.ScrollArea(doc, self.descCoord.width, self.descCoord.height, hscrollbar=False,  vscrollbar=True)
        c.add(self.displayDesc, self.descCoord.x, self.descCoord.y)   
            
        # Option
        doc = CreateDescription(self.gameEvent.options[0][1], 400, align=-1)       
        self.displayOption = gui.ScrollArea(doc, self.OptCoord.width, self.OptCoord.height, hscrollbar=False,  vscrollbar=True)
        c.add(self.displayOption, self.OptCoord.x, self.OptCoord.y)
           
        t = gui.Table()
        g = gui.Group(name='options',value=0)   
        index = 0  
        y = self.OptIdCoord.y - self.label_height
        for opt, doc, effect, result in self.gameEvent.options:
            t.tr()
            t.td(gui.Radio(g,index))
            t.td(gui.Label(opt))
            index += 1
        c.add(t, self.OptIdCoord.x, y)
        g.value = 0
        g.connect(gui.CHANGE, self.action_SelectOption, g)
 
        self.tr()
        self.td(c,cls=self.cls+".main")   
          
        # Add confirmation button
        self.tr()
        b = gui.Button("Confirmez votre choix", width=self.btnCoord.width, height=self.btnCoord.height)
        b.connect(gui.CLICK, self.action_ConfirmChoice, g, b)
        self.td(b, align=0, valign=0)       
      
        #Add space at dialog bottom
        self.tr() 
        self.td(gui.Label("   " ))  
  
    def BuildRegionString(self, evt):
        regionString = ""
        for region in evt.regions:
            if(region in Island.secteurDef):
                regionString += Island.secteurDef[region]["name"] + ", "
            else:
                regionString += region + ", "
        return regionString
        
    def action_SelectOption(self, ctl):
        Musique.PlaySound(EventAdvancement.sound_validation)
        self.displayOption.widget = CreateDescription(self.gameEvent.options[ctl.value][1], 400, align=-1)        
#         text = "" 
#         for word in self.gameEvent.options[ctl.value][1].split(" "):
#             text = text + word + " "
#             self.displayOption.widget = CreateDescription(text, 400, align=-1)
#             self.get_toplevel().paint()
#             pygame.display.flip()            
#             pygame.display.update()
#             pygame.time.wait(20)             
         
    def action_ConfirmChoice(self, ctl, btn):
        Musique.PlaySound(EventAdvancement.sound_ValidChoiceOK)
        self.gameEvent.effects = self.gameEvent.options[ctl.value][2]
        self.displayOption.widget = CreateDescription(self.gameEvent.options[ctl.value][3], 400)
        surf = self.get_toplevel().screen        
        self.gameEvent.surfRect = self.get_abs_rect()
        s = surf.subsurface(self.gameEvent.surfRect)  
        self.gameEvent.surf = s.copy()
        Musique.PlaySound(EventAdvancement.sound_Woosh)
        gui.Dialog.close(self) 
        closeScreen(self.get_toplevel(), surf, self.gameEvent.surf, self.gameEvent.surfRect)  
        result = EventsReport(self.gameEvent, ctl.value)
        result.open()

    def open(self, w=None, x=None, y=None):
        Musique.PlaySound(EventAdvancement.sound_Woosh)
        gui.Table.open(self)
        surf = self.get_toplevel().screen 
        self.gameEvent.surfRect = self.get_abs_rect()
        s = surf.subsurface(self.gameEvent.surfRect)  
        self.gameEvent.surf = s.copy()                
        openScreen(self.get_toplevel(), surf, self.gameEvent.surf, self.gameEvent.surfRect)
        self.isOpen = True
        pygame.time.wait(50)

#         self.WriteDescription()        



    def paint(self, surf):
        gui.Table.paint(self, surf)
        self.DrawBorder(self.descBoxCoord, surf)
        self.DrawBorder(self.OptBoxCoord, surf)
        self.DrawBorder(self.OptIdBoxCoord, surf)  
        self.DrawBorder(self.cadreCoord, surf)  
        if(self.isOpen == True):  
            pygame.display.update()
  
         
    def DrawBorder(self, r, s):
#         colorList = [0x000000, 0x778899, 0xd3d3d3, 0xd3d3d3, 0x778899, 0x000000 ] #Black/Grey
        colorList = [0x87ceeb, 0xadd8e6, 0xafeeee, 0xafeeee, 0xafeeee, 0xadd8e6, 0xadd8e6, 0x87ceeb ] #Blue

        for color in colorList:
            CustomWidget.DrawRoundRect(s, color, r, 1, 8, 8)            
            #pygame.draw.rect(s, color, r, 1) 
            r = pygame.Rect(r.x-1, r.top-1, r.width+2, r.height+2)     
    
    def WriteDescription(self): 
        text = "" 
        for word in self.gameEvent.desc.split(" "):
            text = text + word + " "
            print(text)
            self.displayDesc.widget = CreateDescription(text, 500, align=-1)
            self.get_toplevel().paint()            
#             pygame.display.update()
            pygame.time.wait(10) 
  
   
   
class EventsReport(gui.Table):  
    winWidth = 640
    winHeigth = 400
    btnCoord = pygame.Rect(10, 325, 300, 40) 
    borderSize = 10
    label_height = 20     
    effectCoord = pygame.Rect(5, 5, 625, 200) 
    effectBoxCoord = pygame.Rect(borderSize, borderSize+label_height,  630, 200)     
       
    def __init__(self, event, choice, **params):
        # Initialize internal object     
        params.setdefault('cls','dialog')
        gui.Table.__init__(self,**params)
        self.value = gui.Form()
        self.gameEvent = event
        self.choice = choice
        self.isOpen = False   
                
        self.tr() 
        regionString = ""
        for region in self.gameEvent.regions:
            regionString += region +", "
        title =  gui.Label("Event: %s les régions touché sont: %s" % (self.gameEvent.name, regionString) ) 
        self.td(title,align=-1,cls=self.cls+'.bar')                
        
        # Create container
        c = gui.Container(width=640, heigth=400)
 
        # Effect
        doc = CreateDescription(self.gameEvent.options[self.choice][3], 600, align=-1)        
        d = gui.ScrollArea(doc, self.effectCoord.width, self.effectCoord.height, hscrollbar=False,  vscrollbar=True)
        c.add(d, self.effectCoord.x, self.effectCoord.y)
            
        self.tr()
        self.td(c,cls=self.cls+".main")   
        
        # Add confirmation button
        self.tr()
        b = gui.Button("Fermez", width=self.btnCoord.width, height=self.btnCoord.height)
        b.connect(gui.CLICK, self.action_Close)
        self.td(b, align=0, valign=0)      
        
 
         
    def action_Close(self):
        Musique.PlaySound(EventAdvancement.sound_QuitOrReturn)
        surf = self.get_toplevel().screen        
        self.gameEvent.surfRect = self.get_abs_rect()
        s = surf.subsurface(self.gameEvent.surfRect)  
        self.gameEvent.surf = s.copy()
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        gui.Dialog.close(self) 
        closeScreen(self.get_toplevel(), surf, self.gameEvent.surf, self.gameEvent.surfRect)            

             
    def open(self, w=None, x=None, y=None):
        gui.Dialog.open(self)
        surf = self.get_toplevel().screen 
        self.gameEvent.surfRect = self.get_abs_rect()
        s = surf.subsurface(self.gameEvent.surfRect)  
        self.gameEvent.surf = s.copy()                
        openScreen(self.get_toplevel(), surf, self.gameEvent.surf, self.gameEvent.surfRect)
        self.isOpen = True

    def paint(self, surf):
        gui.Container.paint(self, surf)
        self.DrawBorder(self.effectBoxCoord, surf)  
        if(self.isOpen == True):  
            pygame.display.update()
  
         
    def DrawBorder(self, r, s):
        colorList = [0x000000, 0x778899, 0xd3d3d3, 0xd3d3d3, 0x778899, 0x000000 ] #Black/Grey
        colorList = [0x87ceeb, 0xadd8e6, 0xafeeee, 0xafeeee, 0xafeeee, 0xadd8e6, 0xadd8e6, 0x87ceeb ] #Blue
#         colorList = [(0,0,0,128), (119,136,153,0), (211,211,211,0), (211,211,211,0), (119,136,153,128), (0,0,0,0) ] #Black/Grey
        for color in colorList:
            CustomWidget.DrawRoundRect(s, color, r, 1, 8, 8)            
            #pygame.draw.rect(s, color, r, 1) 
            r = pygame.Rect(r.x-1, r.top-1, r.width+2, r.height+2)     
                         
#///////////////////////////////////////////////////////////////////////////////////////////
#///
#///
def closeScreen(ctl, display, surf, r):
    # Erase dialog and get a snapshot as background.
    Musique.PlaySound(EventAdvancement.sound_Woosh)
    ctl.paint()    
    backg = display.copy() 
    # Draw background and resized dialog
    for i in range(r.width, 0, -10):
        display.blit(backg, (0,0))
        surf = pygame.transform.smoothscale(surf,(i, r.height))
        display.blit(surf, (r.x, r.y))
        pygame.display.update(r)
        pygame.time.wait(10)
        
    display.blit(backg, (0,0))
    surf = pygame.transform.smoothscale(surf,(0, r.height))
    display.blit(surf, (r.x, r.y))
    pygame.display.update(r)
    pygame.time.wait(10)
   
    
def openScreen(ctl, display, surf, r):
    # Erase dialog and get a snapshot as background.
    Musique.PlaySound(EventAdvancement.sound_Woosh)
    backg = display.copy()
    bgImage = pygame.image.load("image/Building_Interface.png").convert_alpha()    
    # Draw background and resized dialog
    for i in range(0, r.width, 10):
        display.blit(backg, (0,0))
        surf = pygame.transform.smoothscale(bgImage, (i, r.height))
        surf.fill((173, 216, 230, 200))
        display.blit(surf, (r.x, r.y))
        pygame.display.update(r)
        pygame.time.wait(10)
     
def CreateDescription(text, width, align=-1, fontName=None, fontSize=30):
    font = pygame.font.SysFont(fontName, fontSize)        
    space = font.size(" ")      
    doc = gui.Document(width=width) 
    doc.block(align=align)
    for word in text.split(" "): 
        doc.add(gui.Label(word))
        doc.space(space)
    return doc
