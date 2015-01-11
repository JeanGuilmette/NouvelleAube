'''
Created on Jan 11, 2015

@author: SJS
'''
import sys
sys.path.append("../src")
sys.path.append("../lib")
from BuildMenu import BuildMenu
from pgu import gui
import zone


if __name__ in '__main__':
    
#     t = gui.Theme("gray")
    

    app = gui.Desktop()
    app.connect(gui.QUIT,app.quit,None)
    
    c = gui.Table(width=640,height=480)
    
    ##The button CLICK event is connected to the dialog.open method.
    ##::
    sectorA = zone.Secteur("Saguenay",  "Foret",  ("Agriculture", "Chasse", "Peche", "Bois", "Minerais", "Petrole"), "../src/image/region2.jpg")
    sectorA.Initialize()    
    dialog = BuildMenu(None, sectorA, [50, 50, 550, 300])  
            
    e = gui.Button("Build Management")
    e.connect(gui.CLICK,dialog.open,None)
    ##
    c.tr()
    c.td(e)
    
    app.run(c)
