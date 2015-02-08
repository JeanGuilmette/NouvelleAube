import pygame
import sys; sys.path.append("../lib")
from pgu import gui
import CustomWidget
from Defines import COLORS, FPS, FPS_MIN, FPS_MAX, FPS_DAY
from Island import OVERVIEW_ZONE_NAME
import Island
import BuildMenu
import Events
        
        
                    
class MainScreen(gui.Desktop):
    
    def __init__(self, island, disp):
        t = gui.Theme(["NouvelleAube"])
        gui.Desktop.__init__(self, theme=t)  
        self.connect(gui.QUIT,self.quit,None)
        self.island = island
        self.gameTime = CustomWidget.GameClock()       
         
        sizeX = disp.get_width()
        sizeY = disp.get_height() 
        btn_witdh = 160
        btn_heigth = 30 
        
        c = gui.Container(width=sizeX, height=sizeY)

        ###############################
        # Game time control          
        c.add(self.gameTime, sizeX-225, 0) 

        e = gui.HSlider(value=FPS_DAY,min=FPS_MIN,max=FPS_MAX,size=32,width=128,height=15) 
        e.connect(gui.CHANGE,self.adjustTime,e)
        c.add(e, sizeX-128, 2)       
             
                  
        ###############################
        # Acitve Zone selection      
        self.region = gui.Select(value= OVERVIEW_ZONE_NAME, width=btn_witdh, height=btn_heigth)
        #self.region.add('Island Overview',OVERVIEW_ZONE_NAME)        
        for item in sorted(Island.secteurDef):
            #if(item != OVERVIEW_ZONE_NAME):
            self.region.add(item, item)
        self.region.connect(gui.CHANGE, self.ChangeZone)
        c.add(self.region, 0, 0)

        ###############################
        # Map Display
        tbl = CustomWidget.MapDisplay(island, sizeX, sizeY-(6*btn_heigth))
        c.add(tbl, 0, btn_heigth)

        ###############################
        # Action Button menu
        offsetY = sizeY - (5*btn_heigth)
        offsetX = sizeX - btn_witdh
        btn = gui.Button("Building", width=btn_witdh, height=btn_heigth)
        btn.connect(gui.CLICK, self.action_building, None)
        c.add(btn, offsetX, offsetY)
        
        btn = gui.Button("Transfer", width=btn_witdh, height=btn_heigth)
        btn.connect(gui.CLICK, self.action_transfer, None)
        c.add(btn, offsetX, offsetY + btn_heigth) 
        
        btn = gui.Button("Options", width=btn_witdh, height=btn_heigth)
        btn.connect(gui.CLICK, self.action_option, None)
        c.add(btn, offsetX, offsetY + (2*btn_heigth) ) 
        
        btn = gui.Button("Quit", width=btn_witdh, height=btn_heigth )
        btn.connect(gui.CLICK, self.action_quit, None)
        c.add(btn, offsetX, offsetY + (3*btn_heigth) )     
        
                
        
        ###############################
        # Clock and time control
                
        ###############################
        # Active Zone resource status      
        c.add(self.CreateResourceStatus(), 0, offsetY)
           
        ###############################
        # Active Zone population status      
        c.add(self.CreatePopulationStatus(), 300, offsetY)
        c.add(self.CreatePopulationStatus2(), 600, offsetY)        
        
        self.init(c, disp)

    def adjustTime(self, ctl):
        self.gameTime.day = ctl.value

    def ChangeZone(self):
        print(self.region.value)
        self.island.SetActiveZone(self.region.value)  
               
    def action_new(self,value):
        pass
        
    def action_save(self,value):
        pass
        
    def action_saveas(self,value):
        pass
        
    def action_open(self,value):
        pass
    
    def action_help(self, value):
        pass
    
    def action_about(self, value):
        pass

    def action_quit(self, value):
        self.quit()

    def action_building(self, value):
        d = BuildMenu.BuildMenu(self.island)            
        d.open()
        
    def action_transfer(self, value):
        d = BuildMenu.TransferMenu(self.island)            
        d.open() 
      
    def action_option(self, value):
        pass
    
    def action_event(self, evt):
#         display = self.get_toplevel().screen        
        dialog = Events.EventsViewer(self.island, evt)
        dialog.open()
        self.update()
        done = False
        while not done:
            pygame.time.wait(5)              
            self.update()
            self.paint()
            pygame.display.update()
            pygame.display.flip()              
       
            # Process events
            for ev in pygame.event.get():
                if (ev.type == pygame.QUIT or 
                    ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE):
                    done = True
                else:
                    # Pass the event off to pgu
                    self.event(ev)
                    
        # Remove dialog
#         Events.flipScreen(self, display, evt.surf, evt.surfRect)

        return evt       

    def CreateResourceStatus(self):
        resList = ["Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"]
        
        tbl = gui.Table()
        tbl.tr()
        tbl.td(gui.Label("Ressource:"))
        tbl.td(gui.Label("Current\Available\Max"))
        
        for res in sorted(resList):
            tbl.tr()
            tbl.td(gui.Label(res))
            tbl.td(CustomWidget.RessourceLabel(self.island, self.region,  res))

        return tbl   
    
    def CreatePopulationStatus(self):
        demographieList = ["Population", "Worker", "Bonheur", "Recherche", "Education", "Panique"]
       
        tbl = gui.Table()
        tbl.tr()
        tbl.td(gui.Label("Demographie:"))
        
        for item in demographieList:
            tbl.tr()
            tbl.td(gui.Label(item))
            tbl.td(CustomWidget.DemographieLabel(self.island, self.region, item))

        return tbl      
    
    def CreatePopulationStatus2(self):
        demographieList = ["Criminalite", "Influence", "Pollution", "Production", "Tresors"]
        
        tbl = gui.Table()
        tbl.tr()
        tbl.td(gui.Label("Demographie:"))
        
        for item in demographieList:
            tbl.tr()
            tbl.td(gui.Label(item))
            tbl.td(CustomWidget.DemographieLabel(self.island, self.region, item))

        return tbl  
    def DrawGameClock(self):
        # Windows characteristic
        self.bgColor = COLORS.BLACK  
        self.font = pygame.font.SysFont(None, 25)
        self.fontColor = COLORS.WHITE
        self.borderColor = COLORS.DARKGRAY   
               
        resString = ("%s - %s dps" % (self.gameTime.isoformat(), self.day))
        label = self.font.render(resString, 1, self.fontColor, self.bgColor)
        surface = self.display
        posX =  surface.get_width() - 75 - (label.get_rect().width/2)
        posY =  surface.get_height() - label.get_rect().height 
        self.display.blit(label, (posX, posY))    