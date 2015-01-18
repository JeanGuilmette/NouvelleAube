'''
Created on Dec 24, 2014

@author: JA
'''
# Pour permettre <aparition des evenements
import pygame
import sys; sys.path.append("../lib")
from pgu import gui
from bokeh.server.models.docs import Doc

##########################################################
#
##########################################################                                                        
class Event(gui.Dialog): 
    def __init__(self, title, description, options):
        self.name = title
        self.desc = self.CreateDescription(description)
        self.options = self.CreateOptions(options)
     
    def CreateDescription(self, text):
        doc = gui.Document(width=640) 
#         space = "  "        
        doc.block(align=0)
        for word in """Cuzco's Paint v1.0 by Phil Hassey""".split(" "): 
            doc.add(gui.Label(word))
#             doc.space(space)
#         doc.br(space[1])
        return doc
    
    def CreateOptions(self, options): 
        docs = []
        doc = gui.Document(width=400) 
        doc.block(align=-1)
        for word in """Cuzco's Paint will drive you wild!  Cuzco's Paint was made as a demo of Phil's Pygame Gui.  We hope you enjoy it!Cuzco's Paint will drive you wild!  Cuzco's Paint was made as a demo of Phil's Pygame Gui.  We hope you enjoy it!Cuzco's Paint will drive you wild!  Cuzco's Paint was made as a demo of Phil's Pygame Gui.  We hope you enjoy it!Cuzco's Paint will drive you wild!  Cuzco's Paint was made as a demo of Phil's Pygame Gui.  We hope you enjoy it!Cuzco's Paint will drive you wild!  Cuzco's Paint was made as a demo of Phil's Pygame Gui.  We hope you enjoy it!Cuzco's Paint will drive you wild!  Cuzco's Paint was made as a demo of Phil's Pygame Gui.  We hope you enjoy it!Cuzco's Paint will drive you wild!  Cuzco's Paint was made as a demo of Phil's Pygame Gui.  We hope you enjoy it!Cuzco's Paint will drive you wild!  Cuzco's Paint was made as a demo of Phil's Pygame Gui.  We hope you enjoy it!Cuzco's Paint will drive you wild!  Cuzco's Paint was made as a demo of Phil's Pygame Gui.  We hope you enjoy it!Cuzco's Paint will drive you wild!  Cuzco's Paint was made as a demo of Phil's Pygame Gui.  We hope you enjoy it!Cuzco's Paint will drive you wild!  Cuzco's Paint was made as a demo of Phil's Pygame Gui.  We hope you enjoy it!Cuzco's Paint will drive you wild!  Cuzco's Paint was made as a demo of Phil's Pygame Gui.  We hope you enjoy it!Cuzco's Paint will drive you wild!  Cuzco's Paint was made as a demo of Phil's Pygame Gui.  We hope you enjoy it!Cuzco's Paint will drive you wild!  Cuzco's Paint was made as a demo of Phil's Pygame Gui.  We hope you enjoy it!Cuzco's Paint will drive you wild!  Cuzco's Paint was made as a demo of Phil's Pygame Gui.  We hope you enjoy it!Cuzco's Paint will drive you wild!  Cuzco's Paint was made as a demo of Phil's Pygame Gui.  We hope you enjoy it!""".split(" "): 
            doc.add(gui.Label(word))
        docs.append(("Option A", doc)) 
       
        doc = gui.Document(width=400) 
        doc.block(align=-1)
        for word in """Cuzco's Paint will drive you wild! Cuzco's Paint will drive you wild! Cuzco's Paint will drive you wild! Cuzco's Paint will drive you wild! Cuzco's Paint will drive you wild! Cuzco's Paint will drive you wild! Cuzco's Paint will drive you wild! Cuzco's Paint will drive you wild! Cuzco's Paint will drive you wild!  Cuzco's Paint was made as a demo of Phil's Pygame Gui.  We hope you enjoy it!""".split(" "): 
            doc.add(gui.Label(word))
        docs.append(("Option B", doc))    
        
        doc = gui.Document(width=400) 
        doc.block(align=-1)
        for word in """Cuzco's Paint will drive you wild! Cuzco's Paint will drive you wild! Cuzco's Paint will drive you wild! Cuzco's Paint will drive you wild! Cuzco's Paint will drive you wild! Cuzco's Paint will drive you wild! Cuzco's Paint will drive you wild! Cuzco's Paint will drive you wild! Cuzco's Paint will drive you wild!  Cuzco's Paint was made as a demo of Phil's Pygame Gui.  We hope you enjoy it!""".split(" "): 
            doc.add(gui.Label(word))
        docs.append(("Option C", doc))             
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


        label_heigth = 20 
        width = 640
        height=400
        c = gui.Container(width=width, height=height, background=(220, 220, 220))        
        
        # Title
        c.add(gui.Label("Event: %s" % self.gameEvent.name), 10, 10)
          
        # Description
        c.add(gui.ScrollArea(self.gameEvent.desc, width, 100, hscrollbar=False, vscrollbar=True), 0, 40)
    
        # Option
        y = 150
        c.add(gui.ScrollArea(self.gameEvent.options[0][1], 440, 200, hscrollbar=False,  vscrollbar=True), 200, y)
        
        t = gui.Table()
        g = gui.Group(name='options',value='A')        
        for opt, doc in self.gameEvent.options:
            t.tr()
            t.td(gui.Radio(g,opt))
            t.td(gui.Label(opt))
        c.add(t, 10, y)
        gui.Dialog.__init__(self,title,c)


    def CreateTable(self):
        t = gui.Table(witdh=400, height=400)
#         c = gui.Container(width=640, height=400, background=(220, 220, 220))        

        
        # Title
        t.tr()
        t.td(gui.Label("Event: %s" % self.gameEvent.name))
          
        # Description
        t.tr()
        t.td(gui.ScrollArea(self.gameEvent.desc, 200, 100))
    
        # Option
        g = gui.Group()        
        for opt in self.gameEvent.options:
            t.tr()
            t.td(gui.Radio(g,value="Option A"))
            t.td(gui.ScrollArea(self.gameEvent.options[0], 200, 100))        