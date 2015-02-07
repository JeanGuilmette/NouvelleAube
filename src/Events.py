'''
Created on Dec 24, 2014

@author: JA
'''
# Pour permettre <aparition des evenements
import pygame
import sys; 
import CustomWidget
sys.path.append("../lib")
sys.path.append("../src")

from pgu import gui
from pygame.transform import smoothscale
from pygame.tests import surflock_test


##########################################################
#
##########################################################                                                        
class Event(object): 
    def __init__(self, date, title, description, options):
        self.date = date
        self.name = title
        self.font = pygame.font.SysFont(None, 30)        
        self.space = self.font.size(" ")         
        self.desc = self.CreateDescription(description, 600, 0)
        self.options = self.CreateOptions(options)
        self.effects = []
        self.regions = []   
        self.surf = "" 
        self.surfRect = ""         

             
    def CreateDescription(self, text, width, align=0):
        doc = gui.Document(width=width) 
        doc.block(align=align)
        for word in text.split(" "): 
            doc.add(gui.Label(word))
            doc.space(self.space)
        return doc
    
    def CreateOptions(self, options): 
        docs = []
        for id, desc, effects, result in options:
            docDesc = self.CreateDescription(desc, 418, -1)
            docResult = self.CreateDescription(result, 418, -1)
            docs.append((id, docDesc, effects, docResult)) 
        return docs
    
    
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
class EventsViewer(gui.Dialog):
    winWidth = 640
    winHeigth = 400
    descCoord = pygame.Rect(10, 30, 635, 158)  
    OptCoord = pygame.Rect(220, 200, 425, 250) 
    OptIdCoord = pygame.Rect(10, 200, 198, 210)  
    btnCoord = pygame.Rect(5, 392, 122, 35)   
     
    def __init__(self, island, event):
        self.island = island
        self.gameEvent = event
        self.value = gui.Form()
        self.isFirst = True 
        self.ipOpen = False
        title = gui.Label("Event: %s les régions touché sont: %s" % (self.gameEvent.name, self.gameEvent.regions) )        
        
 
        label_heigth = 20 
        c = gui.Container(width=self.winWidth, height=self.winHeigth)            
        # Title
#         c.add(gui.Label("Event: %s" % self.gameEvent.name), 10, 10)
           
        # Description
        c.add(self.gameEvent.desc, self.descCoord.x, self.descCoord.y - label_heigth)   
           
        # Option
        self.displayOption = gui.ScrollArea(self.gameEvent.options[0][1], self.OptCoord.width, self.OptCoord.height, hscrollbar=False,  vscrollbar=True)
        c.add(self.displayOption, self.OptCoord.x-7, self.OptCoord.y -label_heigth-5)
          
        t = gui.Table()
        g = gui.Group(name='options',value=0)   
        index = 0  
        y = self.OptIdCoord.y - label_heigth
        for opt, doc, effect, result in self.gameEvent.options:
            t.tr()
            t.td(gui.Radio(g,index))
            t.td(gui.Label(opt))
            index += 1
        c.add(t, self.OptIdCoord.x, y)
        g.value = 0
        g.connect(gui.CHANGE, self.action_SelectOption, g)

         
        b = gui.Button("Confirmez votre choix", width=self.btnCoord.width, height=self.btnCoord.height)
        b.connect(gui.CLICK, self.action_ConfirmChoice, g, b)
        c.add(b, self.btnCoord.x, self.btnCoord.y)
        gui.Dialog.__init__(self, title, c)
 
    def action_SelectOption(self, ctl):
        if(self.isFirst == True):
            self.displayOption.widget = self.gameEvent.options[ctl.value][1]
         
    def action_ConfirmChoice(self, ctl, btn):
        if(self.isFirst == True):
            print(ctl.value)
            print(self.gameEvent.options[ctl.value][2])
            self.gameEvent.effects = self.gameEvent.options[ctl.value][2]
            self.displayOption.widget = self.gameEvent.options[ctl.value][3]
            self.isFirst = False
            btn.value = "Fermez"
            btn.resize(width=self.btnCoord.width, height=self.btnCoord.height)
        else:
            surf = self.get_toplevel().screen        
            self.gameEvent.surfRect = self.get_abs_rect()
            s = surf.subsurface(self.gameEvent.surfRect)  
            self.gameEvent.surf = s.copy()
#             disp = pygame.display.get_surface()
            pygame.event.post(pygame.event.Event(pygame.QUIT))
            self.close()  
            closeScreen(self.get_toplevel(), surf, self.gameEvent.surf, self.gameEvent.surfRect)            

    def close(self):
        if(self.isFirst == False):
            gui.Dialog.close(self)
            
    def open(self, w=None, x=None, y=None):
        gui.Dialog.open(self)
        surf = self.get_toplevel().screen 
        self.gameEvent.surfRect = self.get_abs_rect()
        s = surf.subsurface(self.gameEvent.surfRect)  
        self.gameEvent.surf = s.copy()                
        openScreen(self.get_toplevel(), surf, self.gameEvent.surf, self.gameEvent.surfRect)
        self.isOpen = True

    def paint(self, surf):
        gui.Dialog.paint(self, surf)
        self.DrawBorder(self.descCoord, surf)
        self.DrawBorder(self.OptCoord, surf)
        self.DrawBorder(self.OptIdCoord, surf)     
        if(self.isOpen == True):  
            pygame.display.update()

        
    def DrawBorder(self, r, s):
#         colorList = [0x000000, 0x778899, 0xd3d3d3, 0xd3d3d3, 0x778899, 0x000000 ] #Black/Grey
        colorList = [0x87ceeb, 0xadd8e6, 0xafeeee, 0xafeeee, 0xafeeee, 0xadd8e6, 0xadd8e6, 0x87ceeb ] #Blue
        for color in colorList:
            CustomWidget.DrawRoundRect(s, color, r, 1, 32, 32)
            r = pygame.Rect(r.x-1, r.top-1, r.width+2, r.height+2)        
   
 
 
# //////////////////////////////////////////////////////////////////////////////////////
# def flipScreen(ctl, display, surf, r):
#     for i in range(640, 0, -20):
#         ctl.paint()         
#         surf = pygame.transform.smoothscale(surf,(i, 400))
#         display.blit(surf, (r.x, r.y))
#         pygame.display.update(r)
#         pygame.time.wait(10) 
  

def closeScreen(ctl, display, surf, r):
    # Erase dialog and get a snapshot as background.
    ctl.paint()    
    backg = display.copy() 
    # Draw background and resized dialog
    for i in range(r.width, 0, -10):
        display.blit(backg, (0,0))
        surf = pygame.transform.smoothscale(surf,(i, r.height))
        display.blit(surf, (r.x, r.y))
        pygame.display.update(r)
        pygame.time.wait(5) 
    
def openScreen(ctl, display, surf, r):
    # Erase dialog and get a snapshot as background.
    backg = display.copy()
    bgImage = pygame.image.load("../lib/data/themes/NouvelleAube/glassPanel.png")    
    # Draw background and resized dialog
    for i in range(0, r.width, 10):
        display.blit(backg, (0,0))
        surf = pygame.transform.smoothscale(bgImage, (i, r.height))
        display.blit(surf, (r.x, r.y))
        pygame.display.update(r)
        pygame.time.wait(5) 
     
     
##########################################################
#
##########################################################                 
class EventsViewer2(gui.Container):  
    winWidth = 640
    winHeigth = 377
    descCoord = pygame.Rect(20, 60, 635, 158)  
    OptCoord = pygame.Rect(220, 200, 380, 200) 
    OptIdCoord = pygame.Rect(20, 200, 198, 180)  
    btnCoord = pygame.Rect(30, 325, 100, 40) 
    borderSize = 10
    cadreCoord = pygame.Rect(borderSize, borderSize, winWidth-(2*borderSize), winHeigth-(2*borderSize)) 
     
    def __init__(self, island, event, **params):
        # Initialize internal object
        params.setdefault('cls', 'dialog')
        gui.Container.__init__(self, **params)
        self.value = gui.Form()
        self.island = island
        self.gameEvent = event
        self.isFirst = True 
        self.ipOpen = False   
    
        # Title
        title = gui.Label("Event: %s les régions touché sont: %s" % (self.gameEvent.name, self.gameEvent.regions) )        
        self.add(title, 10, 10)
 
        label_heigth = 20 
          
        # Description
        self.add(self.gameEvent.desc, self.descCoord.x, self.descCoord.y - label_heigth)   
            
        # Option
        self.displayOption = gui.ScrollArea(self.gameEvent.options[0][1], self.OptCoord.width, self.OptCoord.height, hscrollbar=False,  vscrollbar=True)
        self.add(self.displayOption, self.OptCoord.x-7, self.OptCoord.y -label_heigth-5)
           
        t = gui.Table()
        g = gui.Group(name='options',value=0)   
        index = 0  
        y = self.OptIdCoord.y - label_heigth
        for opt, doc, effect, result in self.gameEvent.options:
            t.tr()
            t.td(gui.Radio(g,index))
            t.td(gui.Label(opt))
            index += 1
        self.add(t, self.OptIdCoord.x, y)
        g.value = 0
        g.connect(gui.CHANGE, self.action_SelectOption, g)
 
          
        b = gui.Button("Confirmez votre choix", width=self.btnCoord.width, height=self.btnCoord.height)
        b.connect(gui.CLICK, self.action_ConfirmChoice, g, b)
        self.add(b, self.btnCoord.x, self.btnCoord.y)
       
 
    def action_SelectOption(self, ctl):
        if(self.isFirst == True):
            self.displayOption.widget = self.gameEvent.options[ctl.value][1]
         
    def action_ConfirmChoice(self, ctl, btn):
        if(self.isFirst == True):
            print(ctl.value)
            print(self.gameEvent.options[ctl.value][2])
            self.gameEvent.effects = self.gameEvent.options[ctl.value][2]
            self.displayOption.widget = self.gameEvent.options[ctl.value][3]
            self.isFirst = False
            btn.value = "Fermez"
            btn.resize(width=self.btnCoord.width, height=self.btnCoord.height)
        else:
            surf = self.get_toplevel().screen        
            self.gameEvent.surfRect = self.get_abs_rect()
            s = surf.subsurface(self.gameEvent.surfRect)  
            self.gameEvent.surf = s.copy()
#             disp = pygame.display.get_surface()
            pygame.event.post(pygame.event.Event(pygame.QUIT))
            self.close()  
            closeScreen(self.get_toplevel(), surf, self.gameEvent.surf, self.gameEvent.surfRect)            

    def close(self):
        if(self.isFirst == False):
            gui.Dialog.close(self)
             
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
#         self.DrawBorder(self.descCoord, surf)
#         self.DrawBorder(self.OptCoord, surf)
#         self.DrawBorder(self.OptIdCoord, surf)  
        self.DrawBorder(self.cadreCoord, surf)  
#         r =surf.get_rect() 
#         self.DrawBorder(r, surf)  
        if(self.isOpen == True):  
            pygame.display.update()
  
         
    def DrawBorder(self, r, s):
#         colorList = [0x000000, 0x778899, 0xd3d3d3, 0xd3d3d3, 0x778899, 0x000000 ] #Black/Grey
        colorList = [0x87ceeb, 0xadd8e6, 0xafeeee, 0xafeeee, 0xafeeee, 0xadd8e6, 0xadd8e6, 0x87ceeb ] #Blue
        for color in colorList:
            CustomWidget.DrawRoundRect(s, color, r, 1, 32, 32)            
            #pygame.draw.rect(s, color, r, 1) 
            r = pygame.Rect(r.x-1, r.top-1, r.width+2, r.height+2)     
               
   
##########################################################
#
##########################################################                 
class EventsViewer3(gui.Table):  
    winWidth = 640
    winHeigth = 400
    btnCoord = pygame.Rect(10, 325, 300, 40) 
    borderSize = 10
    label_height = 20     
    cadreCoord = pygame.Rect(borderSize, borderSize+label_height, winWidth-(2*borderSize), winHeigth-(2*borderSize)-20) 
    descCoord = pygame.Rect( 5, 5, 615, 128)  
    descBoxCoord = pygame.Rect( borderSize, borderSize+label_height, winWidth-(2*borderSize), 130)    
    OptIdCoord = pygame.Rect(20, 180, 198, 320)  
    OptIdBoxCoord = pygame.Rect(borderSize, 164, 198, 320)  
    OptCoord = pygame.Rect(204, 140, 418, 320) 
    OptBoxCoord = pygame.Rect(212, 164, 418, 320) 
 
    
       
    def __init__(self, island, event, **params):
        # Initialize internal object     
        params.setdefault('cls','dialog')
        gui.Table.__init__(self,**params)
        
        self.value = gui.Form()
        self.island = island
        self.gameEvent = event
        self.isFirst = True 
        self.ipOpen = False   
                
        self.tr()
        title =  gui.Label("Event: %s les régions touché sont: %s" % (self.gameEvent.name, self.gameEvent.regions) ) 
        self.td(title,align=-1,cls=self.cls+'.bar')
        
        # Create container
        c = gui.Container(width=640, heigth=400)
          
        # Description
        d = gui.ScrollArea(self.gameEvent.desc, self.descCoord.width, self.descCoord.height, hscrollbar=False,  vscrollbar=True)
        c.add(d, self.descCoord.x, self.descCoord.y)   
            
        # Option
        self.displayOption = gui.ScrollArea(self.gameEvent.options[0][1], self.OptCoord.width, self.OptCoord.height, hscrollbar=False,  vscrollbar=True)
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
        self.td(c,colspan=2,cls=self.cls+".main")   
          
        # Add confirmation button
        self.tr()
        b = gui.Button("Confirmez votre choix", width=self.btnCoord.width, height=self.btnCoord.height)
        b.connect(gui.CLICK, self.action_ConfirmChoice, g, b)
        self.td(b, align=0, valign=0)       
      
 
    def action_SelectOption(self, ctl):
        if(self.isFirst == True):
            self.displayOption.widget = self.gameEvent.options[ctl.value][1]
         
    def action_ConfirmChoice(self, ctl, btn):
        if(self.isFirst == True):
            print(ctl.value)
            print(self.gameEvent.options[ctl.value][2])
            self.gameEvent.effects = self.gameEvent.options[ctl.value][2]
            self.displayOption.widget = self.gameEvent.options[ctl.value][3]
            self.isFirst = False
            btn.value = "Fermez"
            btn.resize(width=self.btnCoord.width, height=self.btnCoord.height)
        else:
            surf = self.get_toplevel().screen        
            self.gameEvent.surfRect = self.get_abs_rect()
            s = surf.subsurface(self.gameEvent.surfRect)  
            self.gameEvent.surf = s.copy()
#             disp = pygame.display.get_surface()
            pygame.event.post(pygame.event.Event(pygame.QUIT))
            self.close()  
            closeScreen(self.get_toplevel(), surf, self.gameEvent.surf, self.gameEvent.surfRect)            

    def close(self):
        if(self.isFirst == False):
            gui.Dialog.close(self)
             
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
        self.DrawBorder(self.descBoxCoord, surf)
        self.DrawBorder(self.OptBoxCoord, surf)
        self.DrawBorder(self.OptIdBoxCoord, surf)  
        self.DrawBorder(self.cadreCoord, surf)  
#         r =surf.get_rect() 
#         self.DrawBorder(r, surf)  
        if(self.isOpen == True):  
            pygame.display.update()
  
         
    def DrawBorder(self, r, s):
#         colorList = [0x000000, 0x778899, 0xd3d3d3, 0xd3d3d3, 0x778899, 0x000000 ] #Black/Grey
        colorList = [0x87ceeb, 0xadd8e6, 0xafeeee, 0xafeeee, 0xafeeee, 0xadd8e6, 0xadd8e6, 0x87ceeb ] #Blue

        for color in colorList:
            CustomWidget.DrawRoundRect(s, color, r, 1, 8, 8)            
            #pygame.draw.rect(s, color, r, 1) 
            r = pygame.Rect(r.x-1, r.top-1, r.width+2, r.height+2)     
               
   
      
   