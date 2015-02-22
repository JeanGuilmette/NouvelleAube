import pygame
import sys; sys.path.append("../lib")
from pgu import gui
import CustomWidget
from Defines import COLORS, FPS, FPS_MIN, FPS_MAX, FPS_DAY
from Island import OVERVIEW_ZONE_NAME
import Island
import BuildMenu
import Events
import EventAdvancement
import Musique
        
                    
class MainScreen(gui.Desktop):
    leftBorder = 39
    
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
        offsetY = sizeY - (5*btn_heigth) + 10
        offsetX = sizeX - btn_witdh - 55       
        c.add(self.gameTime, offsetX+40, offsetY) 

        e = gui.HSlider(value=FPS_DAY,min=FPS_MIN,max=FPS_MAX,size=32,width=128,height=15) 
        e.connect(gui.CHANGE,self.adjustTime,e)
        c.add(e, offsetX+26, offsetY + 20)  
                           
        ###############################
        # Acitve Zone selection      
        self.region = gui.Select(value= OVERVIEW_ZONE_NAME, width=btn_witdh, height=btn_heigth)
        for item in sorted(Island.secteurDef):
            self.region.add(Island.secteurDef[item]["name"], item)
        self.region.connect(gui.CHANGE, self.ChangeZone)
#         c.add(self.region, 0, 0)
        
        ###############################
        # Map Display
        tbl = CustomWidget.MapDisplay(island, sizeX-(2*self.leftBorder), sizeY-(6*btn_heigth)-7)
        c.add(tbl, self.leftBorder, btn_heigth+8)
        c.add(self.region, self.leftBorder, btn_heigth+8)
        
        ###############################
        # Action Button menu
        offsetY = sizeY - (4*btn_heigth) + 20
        offsetX = sizeX - btn_witdh - 55
        btn = gui.Button("Building", width=btn_witdh, height=btn_heigth)
        btn.connect(gui.CLICK, self.action_building, None)
        c.add(btn, offsetX, offsetY)
        
        btn = gui.Button("Transfer", width=btn_witdh, height=btn_heigth)
        btn.connect(gui.CLICK, self.action_transfer, None)
        c.add(btn, offsetX, offsetY + btn_heigth) 
      
        btn = gui.Button("Quit", width=btn_witdh, height=btn_heigth )
        btn.connect(gui.CLICK, self.action_quit, None)
        c.add(btn, offsetX, offsetY + (2*btn_heigth) )     
        

        ###############################
        # Active Zone resource status    
        offsetY = (sizeY - (5*btn_heigth)) + 10
        c.add(self.CreateResourceStatus(), self.leftBorder-10, offsetY)
           
        ###############################
        # Active Zone population status      
        c.add(self.CreatePopulationStatus(), 375, offsetY)
        c.add(self.CreatePopulationStatus2(), 600, offsetY)        
        
        self.init(c, disp)

    def adjustTime(self, ctl):
        self.gameTime.day = ctl.value

    def ChangeZone(self):
        Musique.PlaySound(EventAdvancement.sound_validation)
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
        Musique.PlaySound(EventAdvancement.sound_QuitOrReturn)
        self.quit()
        pygame.event.post(pygame.event.Event(pygame.QUIT))       

    def action_building(self, value):
        Musique.PlaySound(EventAdvancement.sound_validation)
        d = BuildMenu.BuildMenu(self.island, self.region.value)            
        d.open()
#         self.WaitEndOfDialog()
        

    def WaitEndOfDialog(self):
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
                    self.event(ev) # Pass the event off to pgu
        

    def action_transfer(self, value):
        Musique.PlaySound(EventAdvancement.sound_validation)
        d = BuildMenu.TransferMenu(self.island)            
        d.open() 
#         self.WaitEndOfDialog()
      
    def action_option(self, value):
        pass
    
    def action_event(self, evt):
        dialog = Events.EventsViewer(self.island, evt)
        dialog.open()
        self.WaitEndOfDialog()
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
        demographieList = ["Population", "Worker", "Bonheur", "Education", "Sante"]
       
        tbl = gui.Table()
        tbl.tr()
        tbl.td(gui.Label("Demographie:"))
        
        for item in demographieList:
            tbl.tr()
            tbl.td(gui.Label(item))
            tbl.td(CustomWidget.DemographieLabel(self.island, self.region, item))

        return tbl      
    
    def CreatePopulationStatus2(self):
        demographieList = ["Criminalite", "Influence", "Panique", "Pollution"]

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