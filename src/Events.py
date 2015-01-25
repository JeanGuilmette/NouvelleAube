'''
Created on Dec 24, 2014

@author: JA
'''
# Pour permettre <aparition des evenements
import pygame
import sys; sys.path.append("../lib")

from pgu import gui
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
        self.desc = self.CreateDescription(description)
        self.options = self.CreateOptions(options)
        self.effects = []
        self.regions = []        

             
    def CreateDescription(self, text):
        doc = gui.Document(width=640) 
     
        doc.block(align=0)
        for word in text.split(" "): 
            doc.add(gui.Label(word))
            doc.space(self.space)
        doc.br(self.space[1])
        return doc
    
    def CreateOptions(self, options): 
        docs = []
        for id, desc, effects in options:
            doc = gui.Document(width=400) 
            doc.block(align=-1)
            for word in desc.split(" "): 
                doc.add(gui.Label(word))
                doc.space(self.space)
            doc.br(self.space[1])                
            docs.append((id, doc, effects)) 
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
# class EventsViewerMenu(gui.Container):  
#     def __init__(self, island, event):
#         self.island = island
#         self.gameEvent = event
#         self.value = gui.Form()
#         self.widgetList = []
#         self.bgImage = pygame.image.load("../Src/image/Nouvelle_Aube.jpg")
#         
#         
#         self.params.setdefault('cls','dialog')
#         title = gui.Label("Events")
#         label_heigth = 20 
#         width = 640
#         height=400
#         gui.Container.__init__(self, width=width, height=height, background=(220, 220, 220))        
#         
#         # Title
#         self.add(gui.Label("Event: %s" % self.gameEvent.name), 10, 10)
#           
#         # Description
#         self.add(gui.ScrollArea(self.gameEvent.desc, width, 100, hscrollbar=False, vscrollbar=False), 0, 40)
#     
#         # Option
#         y = 150
#         self.displayOption = gui.ScrollArea(self.gameEvent.options[0][1], 440, 300, hscrollbar=False,  vscrollbar=False)
#         self.add(self.displayOption, 200, y)
#         
#         t = gui.Table()
#         g = gui.Group(name='options',value='0')   
#         index = 0     
#         for opt, doc, effect in self.gameEvent.options:
#             t.tr()
#             t.td(gui.Radio(g,index))
#             t.td(gui.Label(opt))
#             index += 1
#         self.add(t, 10, y)
#         g.value = "0"
#         g.connect(gui.CHANGE, self.action_SelectOption, g)
#         
#         b = gui.Button("Confirmez votre choix", width=150, height=50)
#         b.connect(gui.CLICK, self.action_ConfirmChoice, g)
#         self.add(b, 5, 400)
# 
# 
#     def action_SelectOption(self, ctl):
#         self.displayOption.widget = self.gameEvent.options[ctl.value][1]
#         
#     def action_ConfirmChoice(self, ctl):
#         print(ctl.value)
#         print(self.gameEvent.options[ctl.value][2])
# 
#         self.close()
#         
# #     def paint(self, surf):
# #         gui.Container.paint(self, surf)
# #         s = surf.copy()
# #         surf.blit(self.bgImage, [0, 20])
# #         s.set_alpha(100)
# #         surf.blit(s, [0, 0])
#         
#         
         
class EventsMenu(gui.Dialog):          
    def __init__(self, island, event):
        title = gui.Label("Events")
        self.island = island
        self.gameEvent = event
        self.value = gui.Form()
        self.widgetList = []
        self.bgImage = pygame.image.load("../Src/image/Nouvelle_Aube.jpg")

 
        label_heigth = 20 
        width = 640
        height=400
        c = gui.Container(width=width, height=height)            
        # Title
        c.add(gui.Label("Event: %s" % self.gameEvent.name), 10, 10)
           
        # Description
#         c.add(gui.ScrollArea(self.gameEvent.desc, width, 100, hscrollbar=False, vscrollbar=False), 0, 40)        
        c.add(self.gameEvent.desc, 0, 40)   
           
        # Option
        y = 150
        self.displayOption = gui.ScrollArea(self.gameEvent.options[0][1], 440, 250, hscrollbar=False,  vscrollbar=False)
#         self.displayOption = self.gameEvent.options[0][1]
        c.add(self.displayOption, 200, y)
          
        t = gui.Table()
        g = gui.Group(name='options',value=0)   
        index = 0     
        for opt, doc, effect in self.gameEvent.options:
            t.tr()
            t.td(gui.Radio(g,index))
            t.td(gui.Label(opt))
            index += 1
        c.add(t, 10, y)
        g.value = 0
        g.connect(gui.CHANGE, self.action_SelectOption, g)

         
        b = gui.Button("Confirmez votre choix", width=125, height=40)
        b.connect(gui.CLICK, self.action_ConfirmChoice, g)
        c.add(b, 10, 400)
        gui.Dialog.__init__(self, title, c)
 
    def action_SelectOption(self, ctl):
        self.displayOption.widget = self.gameEvent.options[ctl.value][1]
         
    def action_ConfirmChoice(self, ctl):
        print(ctl.value)
        print(self.gameEvent.options[ctl.value][2])
        self.gameEvent.effects = self.gameEvent.options[ctl.value][2]
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        self.close()
         
        
        