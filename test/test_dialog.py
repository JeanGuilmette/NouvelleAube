'''
Created on Jan 11, 2015

@author: SJS
'''
import sys

sys.path.append("../src")
sys.path.append("../lib")
sys.path.append("../src/SoundTrack")
sys.path.append("../src/image")
import pygame
pygame.init()
from BuildMenu import BuildMenu, TransferMenu
from pgu import gui
import Zone
import Island
import Events
import CustomWidget
  
##########################################################    
if __name__ in '__main__':

    pygame.display.set_caption('Enjeux-Survie')        
    pygame.display.set_icon(pygame.image.load("../src/image/pygame.bmp"))
    disp = pygame.display.set_mode((1027, 768))
    disp.convert_alpha()

    t = gui.Theme(["NouvelleAube"])
    app = gui.Desktop(theme=t, width=1024, height=800)
        
    ##################################
    # Epidemie
    ##################################
    desc = "Un terrifiant fléau vient de s'abattre sur nos têtes. Une maladie qui a pris de tel proportion dans le secteur qu'elle en est devenu une épidémie et menace désormais de se répandre sur le reste de l'île. Cette maladie est extrêmement dangereuse et fait déjà plusieurs dizaines de victimes. Que faire?"
    choix_A=("Bouclez le secteur, je ne veux personne qui puisse en entrer  ou en sortir.")
    effect_A = ["MultiplyPop=0.5", "panic=12"]
    result_A = "La mise en quarantaine du secteur à certainement empêché la maladie de se répandre sur le reste de l'île, mais malheureusement, le manque d'aide accordé aux malades a fait en sorte que beaucoup on perdu la vie. Les survivants et les habitants des autres secteurs sont bien sûr heureux d'avoir survécu, cependant ils se demandent à quel point ils peuvent s'attendre à recevoir votre aide advenant qu'une catastrophe leur arrive à eux...  "
    choix_B=("Envoyez des équipes collecter les malades et enfermez-les dans n'importe quel édifice dont ils ne pouront pas sortir. À partir de là soignez-les au mieux possible.")
    effect_B = ["MultiplyPop=0.1", "panic=12"]
    result_B ="Tout est bien qui fini bien. Grâce aux soins prodigué par vos équipes, la majorité des malades ont survécu et la maladie ne s'est pas répandu partout sur l'île. Les gens parlent désormais de vous avec plus de considération."
    choix_C=("Par conséquent, envoyez des équipes collecter les malades et emprisonnez-les dans un édifice quelconque et peu important, puis mettez-y feu. Il faut absolument éviter que la maladie se répandent encore plus.")
    effect_C = ["MultiplyPop=0.3", "panic=35"]
    result_C ="Malheureusement, la chasse aux malades s'est très mal déroulée. Dès que la rumeur d'équipes de nettoyages envoyée par vos soins pour brûler vifs les contaminés s'est répandu, une vague de terreur s'est emparée de tous et chacun. Beaucoup ont tenté, et souvent avec succès, de cacher leur proches pour éviter qu'ils soient capturer. Par ailleurs, les équipes ont énormément usé des informations transmissent par des voisins inquiets et autres, sauf qu'au final, nous avons probablement ainsi aussi bien réglé des querelles qu'empêcher la maladie de se répandre, car plusieurs de ces dénonciations, ont le sait maintenant, étaient fausse. Au final,  la confiance des habitants du secteur sera longue à regagner, car notre remède aura été bien pire que le mal. "
    choix_D=("Une maladie à déjà faillit détruire notre monde et je ne laisserai pas cela ce reproduire! Bombarder le secteur infecté jusqu'à ce qu'il ne puisse avoir aucun survivant.")
    effect_D = ["Exterminate=0"]
    result_D = "Une vague de stupeur s'est répandu sur tout Man'ana'toura dès que la première bombe a explosée. Personne ne voulait croire que vous aviez vraiment fait ça. Mais alors qu'un abominable silence s'installait, une fois le massacre terminé, les gens sont sortis de leur maison, une bougie à la mains dans la noirceur de la nuit, pour rendre hommage à vos victimes. Cette nuit, mue par la tristesse et l'horreur, le peuple chanta un air funèbre et tragique. Les conséquences de cet acte seront graves."
    
    options =[]
    options.append(("Option A", choix_A, effect_A, result_A))
    options.append(("Option B", choix_B, effect_B, result_B))
    options.append(("Option C", choix_C, effect_C, result_C))
    options.append(("Option D", choix_D, effect_D, result_D))
    
    evt_epidemie = Events.Event("now", "Epidemie", desc, options)
    #####################################   

    
    app.connect(gui.QUIT,app.quit,None)
    
    c = gui.Table(width=200,height=100)
    
    ##The button CLICK event is connected to the dialog.open method.
    secteurA = Island.Island("new")
  
    dialog = BuildMenu(secteurA, "RegionD")  
    dialog2 = TransferMenu(secteurA) 
    dialog3 = Events.EventsViewer(secteurA, evt_epidemie)
    dialog4 = CustomWidget.MessageBox("Test", "building could not be build. Not enough ressource.")
    
             
    c.tr() 
    e = gui.Button("Build Management")
    e.connect(gui.CLICK,dialog.open,None)
    c.td(e)
      
    c.tr()
    e = gui.Button("Transfert")    
    e.connect(gui.CLICK,dialog2.open, None)      
    c.td(e)   
     
    c.tr()
    e = gui.Button("Events")    
    e.connect(gui.CLICK,dialog3.open, None)      
    c.td(e)  
    
    c.tr()
    e = gui.Button("Message Box")    
    e.connect(gui.CLICK,dialog4.open, None)      
    c.td(e)      
    
    app.run(c, screen=disp)


