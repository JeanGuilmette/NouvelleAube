'''
Created on Dec 24, 2014

@author: JA
'''
# Pour permettre <aparition des evenements
import pygame
import sys; sys.path.append("../lib")

from pgu import gui
from pygame.transform import smoothscale
from pygame.tests import surflock_test
# from pygame.tests import surflock_test


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

             
    def CreateDescription(self, text, width, align=0):
        doc = gui.Document(width=width) 
        doc.block(align=align)
        for word in text.split(" "): 
            doc.add(gui.Label(word))
            doc.space(self.space)
#         doc.br(self.space[1])
        return doc
    
    def CreateOptions(self, options): 
        docs = []
        for id, desc, effects, result in options:
            docDesc = self.CreateDescription(desc, 400, -1)
            docResult = self.CreateDescription(result, 400, -1)
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
        title = gui.Label("Event: %s" % self.gameEvent.name)        
        
 
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
            pygame.event.post(pygame.event.Event(pygame.QUIT))
            self.close()  

    def close(self):
        if(self.isFirst == False):
            gui.Dialog.close(self)
            
    def paint(self, surf):
        gui.Dialog.paint(self, surf)
        self.DrawBorder(self.descCoord, surf)
        self.DrawBorder(self.OptCoord, surf)
        self.DrawBorder(self.OptIdCoord, surf)        
        pygame.display.update()
        pygame.display.flip() 
        
    def DrawBorder(self, r, s):
        colorList = [0x000000, 0x778899, 0xd3d3d3, 0xd3d3d3, 0x778899, 0x000000 ]
        for color in colorList:
            pygame.draw.rect(s, color, r, 1) 
            r = pygame.Rect(r.x-1, r.top-1, r.width+2, r.height+2)        
                             
        