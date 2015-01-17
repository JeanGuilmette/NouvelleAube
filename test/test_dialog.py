'''
Created on Jan 11, 2015

@author: SJS
'''
import sys
sys.path.append("../src")
sys.path.append("../lib")
from BuildMenu import BuildMenu, TransferMenu
from pgu import gui
import zone
import Island


if __name__ in '__main__':
#     t = gui.Theme(["clean", "tools"])
    t = gui.Theme(["default", "tools"])
#     t = gui.Theme(["gray", "tools"])
#     t = gui.Theme("gray")
#     t = gui.Theme("default")   
#     t = gui.Theme("clean")
#    top = gui.Desktop(theme=gui.Theme(['default','tools']))
  
    app = gui.Desktop(theme=t)
    app.connect(gui.QUIT,app.quit,None)
    
    c = gui.Table(width=1024,height=800)
    
    ##The button CLICK event is connected to the dialog.open method.
    secteurA = Island.Island("new")
 
    dialog = BuildMenu(secteurA)  
    dialog2 = TransferMenu(secteurA)
            
    c.tr() 
    e = gui.Button("Build Management")
    e.connect(gui.CLICK,dialog.open,None)
    c.td(e)
    
    c.tr()
    e = gui.Button("Transfert")    
    e.connect(gui.CLICK,dialog2.open,None)      
    c.td(e)    
    
    app.run(c)
