'''
Created on Jan 11, 2015

@author: SJS
'''
import sys
sys.path.append("../src")
sys.path.append("../lib")
from BuildMenu import BuildMenu, TransferMenu
from pgu import gui
import Zone
import Island
import Events
import pygame


if __name__ in '__main__':
#     t = gui.Theme(["clean", "tools"])
    t = gui.Theme(["default", "tools"])
#     t = gui.Theme(["gray", "tools"])
#     t = gui.Theme("gray")
#     t = gui.Theme("default")   
#     t = gui.Theme("clean")
#    top = gui.Desktop(theme=gui.Theme(['default','tools']))
    backg = gui.Background((255, 255, 255), t)

    ##################################
    # Epidemie
    ##################################
    desc = "L'infirmerie du navire se remplit de plus en plus. Manifestement, une maladie se répand au travers les passagers. Nous ignorons se qu'elle pourrait causer, néanmoins il est impératif de réagir! Des rumeurs de contaminations par la Mort Rouge commence déjà à ébranler l'équipage."
    choix_A=("Je pense de ce fait qu'une mise en quarantaine des malades est tout à fait justifiée; ainsi la maladie ne devrait plus se répandre.")
    effect_A = "panic=-10 poisson=-20 bonheur=20"
    choix_B=("J'ai donc décidé que tout les passagers pouvant offrir de leurs temps pour le soins des malades se devront de le faire. La maladie sera ainsi enrayée grâce aux petits soins que prodigueront les autres passagers.")
    effect_B = "panic=10 poisson=-200 bonheur=20"
    choix_C=("Par conséquent, pour éviter de créer des perturbations au seins de l'équipage et nuire à son efficacité, ainsi qu'au moral de la population, à cause de rumeurs sur ce qui ne semble qu'être que des rhumes des plus banals, il faudra étouffer les rumeurs et rassuré tout le monde.")
    effect_C = "panic=100 bonheur=-50"
    choix_D=("Ce qui réduirait à néant toutes chances de re-bâtir notre monde! C'est inadmissible. Pour le bien du plus grand nombre et pour éviter tout risques, nous lancerons par dessus bord tout individu suspecté de maladie, discrètement, bien sûr.")
    effect_D = "poisson=-20 bonheur=20"
    options =[]
    options.append(("Option A", choix_A, effect_A))
    options.append(("Option B", choix_B, effect_B))
    options.append(("Option C", choix_C, effect_C))
    options.append(("Option D", choix_D, effect_D)) 
    
    evt_epidemie = Events.Event("now", "Epidemie", desc, options)          
    #####################################  


    app = gui.Desktop(theme=t, width=1024, height=800, background=backg)
    app.connect(gui.QUIT,app.quit,None)
    
    c = gui.Table(width=200,height=100)
    
    ##The button CLICK event is connected to the dialog.open method.
    secteurA = Island.Island("new")
 
    dialog = BuildMenu(secteurA)  
    dialog2 = TransferMenu(secteurA)

    dialog3 = Events.EventsMenu(secteurA, evt_epidemie)
            
    c.tr() 
    e = gui.Button("Build Management")
    e.connect(gui.CLICK,dialog.open,None)
    c.td(e)
    
    c.tr()
    e = gui.Button("Transfert")    
    e.connect(gui.CLICK,dialog2.open,None)      
    c.td(e)   
    
    c.tr()
    e = gui.Button("Events")    
    e.connect(gui.CLICK,dialog3.open,None)      
    c.td(e)  
    
    app.run(c)


