__author__ = 'Jean-Alexandre'
from defines import COLORS
import MainScreen
import DockingMenu
import conda
import pygame
from pygame.locals import *
import StoryTelling
class position(): #entre les lignes le rapport de 30 pour la taille des caracteres et de 35 d<espapce entre les lignes sembles bon.
    def __init__(self, Ecran):
        self.topleft = [25 ,  25]
        self.toprigth = [int(Ecran.get_width()) - 25 , 25]
        self.center = [int(Ecran.get_width())/2 , int(Ecran.get_height())/2]
        self.choixa =[25, 260]
        self.choixb =[25,295]
        self.choixc =[25, 340]
        self.choixd =[25, 375]
        self.choixe =[25, 460]


class Story (): # envoyer cette classe dans choix, pour n<avoir a appeler qu<une seule classe lors de Storytelling
    font = pygame.font.SysFont ('None' , 30, True, False)
    def __init__(self, texte, Pos, display):
        text = self.font.render (texte, True , COLORS.WHITE)

        display.blit(text, Pos)
        # pygame.display.flip()
class Choix():
    def __init__(self, _menu_items , display):
        self.clock = pygame.time.Clock()
        self.bgImage = pygame.image.load("image/Nouvelle_Aube.jpg")
        self.menuSurface = display
        self.menuSurface.blit(self.bgImage, [0,0])

        sizeX = MainScreen.MainScreen.screenwidth
        sizeY = 100
        X = display.get_rect().width / 2 - (sizeX / 2)
        Y = display.get_rect().height /2 - (sizeY / 2)
        self.mainMenu = DockingMenu.DockingMenu(display, _menu_items, [X, Y, sizeX, sizeY], COLORS.WHITE, None, 16, COLORS.RED )
        #self.showStartScreen()

    def CheckMenu(self):
        while True:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                else:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        menuName = self.mainMenu.validSelectedMenu(event)
                        if(menuName != "none"):
                            print(menuName)
                            return menuName#C'est ici qu'il faut mettre le code pour ajouter les effets des decision et ou elle menent

            self.menuSurface.blit(self.bgImage, [0,0])
            self.mainMenu.draw()


    def showMenuScreen(self):
        self.mainMenu.draw()
        pygame.display.flip()
        return self.CheckMenu()

class StoryEffects():
    Effects = dict( \
    Bonheur  = (50),
    Influence = (50),
    Sante  = (50),
    Recherche  = (50),
    Criminalite = (50),

    Bois  = (566),
    Metaux  = (220),
    Pierre  = (110),
    Nourriture  = (840),
    Petrole = (440),
    Population = (270),

    UNVP  = (7), # unite de nourriture pour le voyage par personne
    UPC = (390) # unite de petrole consomme par le voyage
    )


class Texte():
    #INSTRUCTIONS

    #introduction
    texte1=("il était une fois, une maladie ravageuse...")
    texte2=("...elle était si dangereuse, que seulement quelques heures après l'avoir  contractée, ses victimes se prennaient d'une folie meurtrière sanglante")
    texte3=("Seulement après 24 heures d'incubation, le malade avait afin la chance de mourrir. Atrocement, certe, d'une agonie abominable causée par la sublimation de sa chair, mais ayant au moins le mérite de les libéré d'autres douleurs encore plus atroces")
    texte4=("Car il semblerait, comble de l'horreur, que les victimes restent conscientes de leurs douleurs et actions, comme dans un cauchemard.")
    texte5=("Cette maladie, appelée la Mort Rouge, mit un terme à l'existance de notre chère humanité.")
    texte6=("Enfin, presque...")
    #départ
    texte7=("Voici l'histoire des derniers survivants de Man'ana'toura et l'archipel du Nouvelle Aube!")
    texte8=("Journal du commandant")
    texte9=("Une fois prêt au départ, nous sommes partis, sans un regard n'y regret pour le pays dévasté que nous laissions dernière nous. Nous sommes dorénavant le dernière espoir de l'humanité et sela ne peut que nous emplir de fierté...et faire peser sur nos épaules le poids de millions d'âmes.")
   #Épidémie
    texte10=("L'infirmerie du navire se remplit de plus en plus. Manifestement, une maladie se répand au travers les passagers. Nous ignorons se qu'elle pourrait causer, néanmoins il est impératif de réagir! Des rumeurs de contaminations par la Mort Rouge commence déjà à ébranler l'équipage.")
    choix10a=("Je pense de ce fait qu'une mise en quarantaine des malades est tout à fait justifier; ainsi la maladie ne devrait plus se répandre.")
    choix10b=("J'ai donc décidé que tout les passagers pouvant offrir de leurs temps pour le soins des malades se devront de le faire. La maladie sera ainsi enrayée grâce aux petits sions que prodigueront les autres passagers.")
    choix10c=("Par conséquent, pour éviter de créer des perturbations au seins de l'équipage et nuire à son efficacité, ainsi qu'au moral de la population, à cause de rumeurs sur ce qui ne semble qu'être que des rhumes des plus banals, je devrai étouffé les rumeurs et rassuré tout le monde.")
    choix10d=("Ce qui réduirait à néant toutes chances de re-bâtir notre monde! C'est inadmissible. Pour le bien du plus grand nombre et pour éviter tout risques, nous lancerons par dessus bord tout individu suspecté de maladie, discrètement, bien sûr.")
    #Famine
    texte11=("Les rapports sont clairs. Il va très probablement nous manquer de nourritures avant que l'on arrive à Man'ana'toura, seul lieu où nous pourrons nous réaprovisionner une fois notre colonis établt. La famine nous menace si nous n'agissons pas.")
    choix11a=("Cependant, il ne s'agit que de rapports... il se peut tout aussi bien, je pense, que nous ayons assez de nourriture pour finir le voyage. Donc, nul besoins d'inquiété tout le monde avec ça.")
    choix11b=("Il va donc falloir que l'on rationne la nourriture. Nous la distriburons tout d'abord à l'équipage, qui doit travailler et qui a donc plus besoins de se sustenter que la populace qui elle ne fait rien de ses journées et qui attend simplement d'être arrivé à destination.")
    choix11c=("Tout le monde devra donc se serrer la ceinture, que à partir de maintenant, la nourriture sera strictement rationnée! Tout le monde n'aura que sa part et elle seule, pas plus grosse pas plus petite qu'une autre!")
    choix11d=("Manisfestement, nous avons ambitionné sur la quantité de gens que nous pouvions ammené avec nous. Il y a, la situation en est la preuve, beaucoup trop de monde à bord! Je vais donc sélectionner les gens les moins utiles à notre future société et les jetter par dessu bord.")
    #Porte-Avions
    texte12=("Nous venons d'appercevoir à l'horizon un port-avions aborant le pavillon français. Nous igorons encore s'il y a du monde à bord.")
    choix12a=("Étrange, au dernières nouvelles, nous étions, le Canada, le dernier pays qui n'était pas détruit par la maladie. Le bateau est soit contaminé, soit un vestige du passé inutile. Il vaut mieux passer notre chemin.")
    choix12b=("Peut-être ne sommes nous pas les derniers sur cette Terre qui nous est devenu si hostile! Allons voir si nous ne pouvons pas faire équipe pour notre survie commune.")
    #il est vide
    texte13=("Très manisfestement, le porte-avions est vide de toutes vies...")
    choix13a=("... c'est pourquoi il vaut mieux ne pas s'approcher. Ce qui les a tué peut aussi nous tuer, c'est clair.")
    choix13b=("... c'est pourquoi je suis sûr que personne ne s'opposera si nous allons en récupérer tout le matériel qui pourrait nous être utile.")
    #il est encore habité
    texte14=("Nous nous sommes encore un peu approché, puis le porte-avions français se mit à nous envoyer des signaux lumineux. Manifestement, il y a encore des gens sur le bâteau mais ils ne se servent pas de la radio pour se signaler... ")
    choix14a=("...se qui est très suspect. Vaut mieux passer notre chemin en tentant des les évités.")
    choix14b=("... se qui est génial! D'autres êtres vivants, merveilleux! Une fois proche, nous leurs proposerons de faire route avec nous vers Man'ana'toura. Mettre en commun nos resources ne peut qu'être bénéfique.")
    choix14c=("... et en plus, ils semblent se diriger vers l'Amérique! Comme s'ils se rendait vers le Québec, qui était le dernier lieu non-infecté... Apprenons-leur que le Canada est également tombé, puis continuons notre chemin. Nous ne les connaisons pas et n'avons aucune raisons de les cotoyer plus qu'ils ne le faut.")
    choix14d=("...laissons-les poursuivre leur chemin. Seul. Il ne faudrait pas qu'ils nous suivent sur Man'ana'toura, qui n'est après tout qu'une île, dont ils grugeraient les ressources qui NOUS reviennent!")
    #s'il y a une épidémie
    texte15=("Le bateau habritait un agent pathogène encore non-identifié qui semble acoir réussi par un moyen ou un autre à pénétrer l'ARCHE et maintenant cette maladie se répand! L'équipage a encore en tête les images de la Mort Rouge et la panique les gagnent rapidement.")
    #Arriver
    texte16=("Nous sommes ARRIVÉ!!!!")

class Verificationtouche():
    run = True
    endrun = True
    clock = pygame.time.Clock()
    def __init__(self):
        while self.run==True:
            self.clock.tick(30)
            StoryTelling.StoryTelling.choicetaken = "0"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:

                     if event.key == pygame.K_1:
                         self.Return1()
                         self.endrun = False
                     if event.key == pygame.K_2:
                         self.Return2()
                         self.endrun = False
                     if event.key == pygame.K_3:
                         self.Return3()
                         self.endrun = False
                     if event.key == pygame.K_4:
                         self.Return4()
                         self.endrun = False

            self.run = self.endrun
    def Return1(self):
        StoryTelling.StoryTelling.choicetaken = "1"



    def Return2(self):
        StoryTelling.StoryTelling.choicetaken = "2"


    def Return3(self):
        StoryTelling.StoryTelling.choicetaken = "3"


    def Return4(self):
        StoryTelling.StoryTelling.choicetaken = "4"




