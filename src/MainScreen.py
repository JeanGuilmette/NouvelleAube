import pygame
import sys; sys.path.append("../lib")
from pgu import gui
import ZoneStatusDisplay
import MapDisplay
import DockingMenu
from defines import COLORS
from Island import OVERVIEW_ZONE_NAME
import Island
import BuildMenu
        
        
                    
class MainScreen(gui.Desktop):
    
    def __init__(self, island, disp):
        gui.Desktop.__init__(self)  
        self.connect(gui.QUIT,self.quit,None)
        self.island = island
        disp.fill( COLORS.BLACK)
        c = gui.Container(width=disp.get_width(), height=disp.get_height())

        self.buildMenu = BuildMenu.BuildMenu(disp, self.island.GetActiveZone(), [50, 50, 550, 300])        
        
        sizeX = disp.get_width()
        sizeY = disp.get_height()
        spacer = 8
        btn_witdh = 157
        btn_heigth = 30 
        
        ##Initializing the Menus, we connect to a number of Dialog.open methods for each of the dialogs.
        menus = gui.Menus([
            ('File/New',self.action_new,None),
            ('File/Open',self.action_open,None),
            ('File/Save',self.action_save,None),
            ('File/Save As',self.action_saveas,None),
            ('File/Exit',self.action_quit,None),
            ('Help/Help',self.action_help,None),
            ('Help/About',self.action_about,None),
            ])
        ##
        c.add(menus,0,0)
        menus.rect.w,menus.rect.h = menus.resize()
        #print 'menus',menus.rect
             
                  
        self.region = gui.Select(value= OVERVIEW_ZONE_NAME, width=btn_witdh, height=btn_heigth)
        self.region.add('Island Overview',OVERVIEW_ZONE_NAME)        
        for item in Island.secteurDef:
            if(item != OVERVIEW_ZONE_NAME):
                self.region.add(item, item)
        self.region.connect(gui.CHANGE, self.ChangeZone)
        c.add(self.region, 0, menus.rect.bottom)

        offsetX = btn_witdh +10
        tbl = MapDisplay.MapDisplay(island, sizeX-offsetX, sizeY-menus.rect.bottom-(4*btn_heigth))
        c.add(tbl, 250, menus.rect.bottom)

        offsetY = sizeY - (4*btn_heigth) - 2
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
        
        

        c.add(self.CreateStatus(), 0, 500)
        
            
        self.init(c, disp)

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
#         self.buildMenu.Run(self.island.GetActiveZone())
        self.buildMenu.open()
    def action_transfer(self, value):
        pass 
      
    def action_option(self, value):
        pass

    def CreateStatus(self):
        tbl = gui.Table()
        tbl.tr()
        tbl.td(gui.Label("Ressource:"))
        tbl.td(gui.Label("Current\Available\Max"))
        
        tbl.tr()
        tbl.td(gui.Label("Agriculture"))
        tbl.td(ZoneStatusDisplay.RessourceLabel(self.island, "Agriculture"))

        tbl.tr()
        tbl.td(gui.Label("Chasse"))
        tbl.td(ZoneStatusDisplay.RessourceLabel(self.island, "Chasse")) 
               
        tbl.tr()
        tbl.td(gui.Label("Peche"))
        tbl.td(ZoneStatusDisplay.RessourceLabel(self.island, "Peche")) 
        
        tbl.tr()
        tbl.td(gui.Label("Bois"))
        tbl.td(ZoneStatusDisplay.RessourceLabel(self.island, "Bois")) 
        
        tbl.tr()
        tbl.td(gui.Label("Minerais"))
        tbl.td(ZoneStatusDisplay.RessourceLabel(self.island, "Minerais")) 
        
        tbl.tr()
        tbl.td(gui.Label("Petrole"))
        tbl.td(ZoneStatusDisplay.RessourceLabel(self.island, "Petrole")) 
        return tbl         