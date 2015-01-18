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


if __name__ in '__main__':
#     t = gui.Theme(["clean", "tools"])
    t = gui.Theme(["default", "tools"])
#     t = gui.Theme(["gray", "tools"])
#     t = gui.Theme("gray")
#     t = gui.Theme("default")   
#     t = gui.Theme("clean")
#    top = gui.Desktop(theme=gui.Theme(['default','tools']))
#     backg = gui.Background((255,255,255), "default")
##################################
#
    desc = "L'infirmerie du navire se remplit de plus en plus. Manifestement, une maladie se répand au travers les passagers. Nous ignorons se qu'elle pourrait causer, néanmoins il est impératif de réagir! Des rumeurs de contaminations par la Mort Rouge commence déjà à ébranler l'équipage."
    choix10a=("Je pense de ce fait qu'une mise en quarantaine des malades est tout à fait justifiée; ainsi la maladie ne devrait plus se répandre.")
    effect10a = "panic=-10 poisson=-20 bonheur=20"
    choix10b=("J'ai donc décidé que tout les passagers pouvant offrir de leurs temps pour le soins des malades se devront de le faire. La maladie sera ainsi enrayée grâce aux petits soins que prodigueront les autres passagers.")
    effect10b = "panic=10 poisson=-200 bonheur=20"
    choix10c=("Par conséquent, pour éviter de créer des perturbations au seins de l'équipage et nuire à son efficacité, ainsi qu'au moral de la population, à cause de rumeurs sur ce qui ne semble qu'être que des rhumes des plus banals, il faudra étouffer les rumeurs et rassuré tout le monde.")
    effect10c = "panic=100 bonheur=-50"
    choix10d=("Ce qui réduirait à néant toutes chances de re-bâtir notre monde! C'est inadmissible. Pour le bien du plus grand nombre et pour éviter tout risques, nous lancerons par dessus bord tout individu suspecté de maladie, discrètement, bien sûr.")
    effect10d = "poisson=-20 bonheur=20"
    options =[]
    options.append(("Option A", choix10a, effect10a))
    options.append(("Option B", choix10b, effect10b))
    options.append(("Option C", choix10c, effect10c))
    options.append(("Option D", choix10d, effect10d)) 
    evA = Events.Event("Epidemie", desc, options)          
#####################################  

    app = gui.Desktop(theme=t, width=1024, height=800, background=(255,255,255))
    app.connect(gui.QUIT,app.quit,None)
    
    c = gui.Table(width=200,height=100)
    
    ##The button CLICK event is connected to the dialog.open method.
    secteurA = Island.Island("new")
 
    dialog = BuildMenu(secteurA)  
    dialog2 = TransferMenu(secteurA)

    dialog3 = Events.EventsMenu(secteurA, evA)
            
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


