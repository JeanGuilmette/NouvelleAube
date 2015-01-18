'''
Created on Dec 24, 2014

@author: JA
'''
# Pour permettre <aparition des evenements
import pygame
import sys; sys.path.append("../lib")

from pgu import gui
# from bokeh.server.models.docs import Doc

##########################################################
#
##########################################################                                                        
class Event(gui.Dialog): 
    def __init__(self, title, description, options):
        self.name = title
        self.font = pygame.font.SysFont(None, 30)        
        self.space = self.font.size(" ")         
        self.desc = self.CreateDescription(description)
        self.options = self.CreateOptions(options)

             
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
        c = gui.Container(width=width, height=height, background=(220, 220, 220))        
        
        # Title
        c.add(gui.Label("Event: %s" % self.gameEvent.name), 10, 10)
          
        # Description
        c.add(gui.ScrollArea(self.gameEvent.desc, width, 100, hscrollbar=False, vscrollbar=False), 0, 40)
    
        # Option
        y = 150
        self.displayOption = gui.ScrollArea(self.gameEvent.options[0][1], 440, 300, hscrollbar=False,  vscrollbar=False)
        c.add(self.displayOption, 200, y)
        
        t = gui.Table()
        g = gui.Group(name='options',value='0')   
        index = 0     
        for opt, doc, effect in self.gameEvent.options:
            t.tr()
            t.td(gui.Radio(g,index))
            t.td(gui.Label(opt))
            index += 1
        c.add(t, 10, y)
        g.value = "0"
        g.connect(gui.CHANGE, self.action_SelectOption, g)
        
        b = gui.Button("Confirmez votre choix", width=150, height=50)
        b.connect(gui.CLICK, self.action_ConfirmChoice, g)
        c.add(b, 5, 400)
        gui.Dialog.__init__(self,title,c)

    def action_SelectOption(self, ctl):
        self.displayOption.widget = self.gameEvent.options[ctl.value][1]
        
    def action_ConfirmChoice(self, ctl):
        print(ctl.value)
        print(self.gameEvent.options[ctl.value][2])
        self.close()
        
        
 
