'''
Created on Dec 24, 2014

@author: JA
'''
# Pour permettre <aparition des evenements
import pygame
import sys; sys.path.append("../lib")

from pgu import gui
from pygame.transform import smoothscale
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
        self.desc = self.CreateDescription(description, 640, 0)
        self.options = self.CreateOptions(options)
        self.effects = []
        self.regions = []               

             
    def CreateDescription(self, text, width, align=0):
        doc = gui.Document(width=width) 
        doc.block(align=align)
        for word in text.split(" "): 
            doc.add(gui.Label(word))
            doc.space(self.space)
        doc.br(self.space[1])
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
        
                 
class EventsViewer(gui.Dialog):          
    def __init__(self, island, event):
        title = gui.Label("Events")
        self.island = island
        self.gameEvent = event
        self.value = gui.Form()
        self.widgetList = []
        self.bgImage = pygame.image.load("../Src/image/Nouvelle_Aube.jpg")
        self.isClosing = False
        self.isOpenning = False
        self.isFirst = True 
        self.winWidth = 640
        self.winHeight = 400
        self.winMaxWidth = 640
        self.winMaxHeight = 400
        self.delta = -20 

 
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
        for opt, doc, effect, result in self.gameEvent.options:
            t.tr()
            t.td(gui.Radio(g,index))
            t.td(gui.Label(opt))
            index += 1
        c.add(t, 10, y)
        g.value = 0
        g.connect(gui.CHANGE, self.action_SelectOption, g)

         
        b = gui.Button("Confirmez votre choix", width=125, height=40)
        b.connect(gui.CLICK, self.action_ConfirmChoice, g, b)
        c.add(b, 10, 400)
        gui.Dialog.__init__(self, title, c)
 
    def action_SelectOption(self, ctl):
        self.displayOption.widget = self.gameEvent.options[ctl.value][1]
         
    def action_ConfirmChoice(self, ctl, btn):
        if(self.isFirst == True):
            print(ctl.value)
            print(self.gameEvent.options[ctl.value][2])
            self.gameEvent.effects = self.gameEvent.options[ctl.value][2]
            self.displayOption.widget = self.gameEvent.options[ctl.value][3]
            self.isFirst = False
            btn.value = "Fermez"
        else:
            self.isClosing = True

        

    def EvaluateNewDialogSize(self):
        w = self.winWidth + self.delta
        self.winWidth = w if w > 0 else 0
        self.winWidth = w if w < self.winMaxWidth else self.winMaxWidth
        h = self.winHeight + self.delta
        self.winHeight = h if h > 0 else 0
        self.winHeight = h if h < self.winMaxHeight else self.winMaxHeight
        if( self.winWidth <= 0):
            self.isClosing = False
            pygame.event.post(pygame.event.Event(pygame.QUIT))
            self.close()            


    def render(self):
        self.EvaluateNewDialogSize()
        surf = self.get_toplevel().screen        
        r = self.get_abs_rect()
        s1 = surf.subsurface(r)
        s1 = pygame.transform.smoothscale(s1,(self.winWidth, self.winHeight))
        surf.blit(s1, (r.x, r.y))
        self.resize(width=self.winWidth, height=self.winHeight)
        pygame.display.update()
        pygame.display.flip() 
        pygame.time.wait(100)


#     def close(self):
#         self.render()
#         gui.Dialog.close(self)
        
    def paint(self, surf):
        if(self.isClosing == True):
            surf.fill(0xFF0000)
            self.render()
        elif(self.isOpenning == True):
            pass

#         gui.Dialog.paint(self, surf)
        
         
           
#     def paint(self, surf):
#         gui.Dialog.paint(self, surf)
#         s = surf.copy()
#         s.blit(self.bgImage, [0, 20])
#         s.set_alpha(150)
#         surf.blit(s, [0, 0])
      
#         surf = self.get_toplevel().screen
#         for i in range(640, 0, -20):
#             r = self.get_abs_rect()
#             s1 = surf.subsurface(r)
#             s1 = pygame.transform.smoothscale(s1,(i, 400))
#             surf.blit(s1, (r.x, r.y))
#             pygame.display.update()
#             pygame.display.flip() 
#             pygame.time.wait(100)
#         self.isClosing = False        