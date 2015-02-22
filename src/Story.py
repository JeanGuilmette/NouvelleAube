__author__ = 'Jean-Alexandre'
from Defines import COLORS
import MainScreen
import DockingMenu
import conda
import pygame
import StoryTelling
import Musique
import EventAdvancement
from pygame.locals import *
# import StoryTelling
# class position(): #entre les lignes le rapport de 30 pour la taille des caracteres et de 35 d<espapce entre les lignes sembles bon.
#     def __init__(self, Ecran):
#         self.topleft = [25 ,  25]
#         self.toprigth = [int(Ecran.get_width()) - 25 , 25]
#         self.center = [int(Ecran.get_width())/2 , int(Ecran.get_height())/2]
#         self.choixa =[25, 260]
#         self.choixb =[25,295]
#         self.choixc =[25, 340]
#         self.choixd =[25, 375]
#         self.choixe =[25, 460]


class Story (): # envoyer cette classe dans choix, pour n<avoir a appeler qu<une seule classe lors de Storytelling

    def __init__(self, texte,commX,commY ,limiteX , display, limiteY = 0, taille = 30, color = COLORS.BLACK, instantScript=False):
        font = pygame.font.SysFont ('None' , taille, True, False)
        DeplacementX = 0
        DeplacementY = 0
        Pos = [commX , commY]
        m=0
        delay = 40


        for i in texte:

            event =pygame.event.peek((pygame.QUIT,pygame.MOUSEBUTTONDOWN,pygame.KEYUP))
            pygame.event.clear()
            if event==True or instantScript == True:
                delay = 0

            DeplacementX = DeplacementX + (taille/2) #15

            if (DeplacementX + commX + 25) > limiteX and i == " ":
                DeplacementY = DeplacementY + 23 #30
                DeplacementX = 0

            if m == 'l' or m == 'i' or m == 't' or m== 'r' or m == 'f' :
                DeplacementX = DeplacementX -5 #-5

            if m == 'm':
                DeplacementX = DeplacementX + 7 #7
            if limiteY != 0:
                if (DeplacementY +25+Pos[1]) > limiteY:
                    print("lack of space")
                    return


            text = font.render (i, True , color)
            Positionnement = [Pos[0] + DeplacementX + 25, Pos[1] + DeplacementY + 25]
            display.blit(text, Positionnement)
            Musique.PlaySound(EventAdvancement.sound_Typing, 0.1)
            pygame.display.flip()
            pygame.time.delay(delay)
            m = i



class RapportElements():
    value1 = ''
    value2 = ''
    value3=''
    value4=''
    value5=''
    surete = 0
    pragmatisme=0
    solidarite=0
    mensonge=0
    cruaute=0
    curiosite=0
    def findValue(self):
        t= [self.surete,self.pragmatisme,self.solidarite,self.mensonge,self.cruaute,self.curiosite]
        max = 0

        for i in t:
            if i>max:
                max = i

        if self.surete == max:
            self.value2='la Prudence'
        elif self.pragmatisme == max:
            self.value2='le Pragmatisme'
        elif self.solidarite == max:
            self.value2='la Solidarité'
        elif self.mensonge == max:
            self.value2='la Désinformation'
        elif self.cruaute == max:
            self.value2='La Brutalité'
        else:
            self.value2 = "quelque chose d'encore indéfinie"
        print(t)


class StoryEffects():
    Effects = dict( \
    Bonheur  = (20),
    Influence = (40),
    Sante  = (60),
    Education  = (30),
    Criminalite = (30),

    Panique = (0),

    Bois  = (1200),
    Minerai  = (200),

    Nourriture  = (1800),
    Petrole = (100),
    Population = (3000)
    )


class Texte():
    #INSTRUCTIONS



    iTexte1=("Salutation, je suis votre dispositif personnel de conseil et gestion ISaveTheWorld (TM), celui qui vous aidera à remplir vos nouvelles fonctions.")
    iTexte1part2=(" Vous voilà en effet responsable de l'ARCHE, un projet de sauvegarde de l'humanité orchestré par la plus grande (et seule) puissance mondiale du moment, le Canada! Alors que la Mort Rouge vient d'en franchir la frontière sud, votre port-avions, nommé de manière originale l'ARCHE, n'attend que d'être chargé en ressouces et gens pour partir sur l'île de Man'ana'toura qui par son climat... disons hors du commun, est impropre à l'implantation de la bactérie appocalyptique qui a détruit l'humanité.")
    iTexte1part3=("En ce qui concerne le chargement du porte-avions, il vous suffit de choisir l'une des propositions sur le côté, qui est la plus avantageuse possible selon le principe auquel il est rattaché par son nom et qui deviendra la valeur de la base de la société que vous allez construire à  Man'ana'toura. Pour plus de détail sur cette proposition, cliquez dessu. Une fois prêt à donner l'ordre du départ, appuyez sur Départ. ")

    iTexteALTRUISME=("L'Altruisme, voilà une bien belle valeur, grâce à cette proposition, je choisirai les gens qui viennent avec nous pour l'aptitude qu'ils ont montré par le passé à prendre naturellement soins de son prochain. Ainsi, même si ces gens ne possèdent pas d'avoir allant faire une grande différence dans la reconstruction de notre monde, peut-être en auront nous un meilleurs, basé sur l'entraide, la paix et la compassion! Par ailleurs, nous avons toujours ce que nos entrepôts contiennent pour la colonisation de Man'ana'toura.")
    iTexteAUDACE=("L'Audace? Eh bien, C'est un choix très risqué mais également potentiellement très profitable. Il se trouve que nous avons d'énormes chargements de différentes ressources qui vont arriver d'ici 3 heures. Ce qui est très bien! Cependant, il se trouve également qu'ils proviennent de zones dont le statut par rapport à la Mort Rouge est indéfini, faute de nouvelles. Ces chargements pourraient amener la maladie jusqu'ici et il ne nous resterait plus qu'à partir le plus vite possible, en espérant ne pas amener le virus avec nous... Il est cependant clair que tout ceux qui vont avoir")
    iTexteAUDACE2=("vécu l'aventure, d'une manière ou d'une autre, en seront fort inspiré et en deviendrons plus brave! Ou vous en voudrons pour le risque inutile que vous avez prit, on verra...")
    iTexteARGENT=("L'Argent, le moteur de l'humanité depuis si longtemps! Cela ne m'étonne presque pas que vous considériez le principe comme prometteur... Il se trouve que plusieurs particuliers souhaiterait obtenir des places de choix dans l'ARCHE ainsi que quelques petits... avantages... pour eux et leurs proches. Bref, ils sont prêt a faire généreusement... don... au programme de beaucoup de ressources qui autrement, n'appartient pas au gouvernement et donc, pas à notre future colonie. En sommes, ils nous ouvre l'accès à plus de ressources que nous pourrions en disposer autrement.")
    iTexteBONHEUR=("Le Bonheur est un élément essentiel du pouvoir: Panem et circenses; du pain et des jeux, la Rome antique l'avais comprise. Effectivement, alors que tous et chacun a le gris au cœur, vu l’apocalypse actuel, votre population sur le bateau pourra profiter d'une foule de divertissements virtuels et gastronomiques ayant pour but d'y ramener un peu de couleurs et de leurs faire oublier leur problèmes. Par ailleurs, des agents spécialement formés par l'ARCHE parcourront les foules et remonteront suptilement le moral des gens grâce à des techniques psychologiques expérimentales de")
    iTexteBONHEUR2=("la GRC (Gendarmerie Royale du Canada). Ainsi, ils vous seront de par beaucoup plus réceptif et l’ambiance sera bien meilleurs car plutôt que de gaspiller leur énergies à ruminer la mort de tout le monde, ils la concentreront plutôt à la reconstruction  de notre société.")
    iTexteEQUITE=("L'Équité, une de mes proposition avec laquelle tout le monde, peut importe ses caractéristiques, aura les même chances de monter à bord de l'ARCHE puisque je choisirai les futurs passagers au hasard.  Un système socio-économique sera spécialement développé et  instauré a bord pour que tout racisme, sexisme et autres soient annihilé dans l'esprit des gens. ")
    iTexteGALANTERIE=("La Galanterie? Selon mes données, c'est une vielle valeur de jadis... cependant elle correspond bien, selon la définition d'un dictionnaire de 1960 à la situation: ce choix implique de sauver d'abord les femmes et les enfants et d'embarquer en moins grand nombre des hommes. Le principal (seul?) avantage est qu'en moyenne, mes données indique que les femmes et les enfants consomment moins de nourriture que les hommes. Ainsi, nous pourront embarquer moins de nourritures pour disposer d'espace pour plus de monde. En tout cas, il ne faut pas trop compter sur ça...")
    iTexteGALANTERIE2=("Également, pour une raison inconnue, les simulations que j'ai effectué grâce à l'une de mes applications indique que le moral serait de façon général un peu meilleur... disons, peut-être plus solennel?")
    iTexteINDUSTRIE=("L'Industrie est une proposition visant a obtenir dès le début sur Man'ana'toura des moyens techniques de production visant à obtenir une solide base industrielle dès le début sur l'île. Si vous la choisissez, je ferai embarquer plus d'équipement spécialisé et de personnel qualifié à son utilisation et autres mains-d'oeuvres, au détriment de la quantité des ressources.")
    iTexteORDRE=("L'Ordre et la Loi, choses sans quoi une société ne pourrait fonctionner. Si vous sélectionner cette proposition, les gens qui monterons à bord de L'ARCHE seront des gens droits et rigoureux, principalement des militaires et des membres des forces de l'ordre et autres représentants de la loi. Il est clair qu'une société ainsi composé sera dépourvu de toute criminalité et très habitué à obéir aux ordres sans poser de question, mais cependant probablement moins encline à développer leur curiosité intellectuelle.")
    iTexteSANTE=("La Santé est la clé de la survie d'une population, car la maladie, sont antithèse, peut provoquer sa mort comme on le voit présentement avec la Mort Rouge. Pour éviter qu'une maladie mette fin à la dernière chance de l'humanité, c’est-à-dire notre future colonie à Man'ana'toura, l'ARCHE sera équipé d'un surplus de matériel médical et de spécialistes de la santé. Par ailleurs, je sélectionnerai les passagers selon leur état de santé, seul les plus sains seront admis sur le bateau.")
    #introduction
    texte1=("Il était une fois, une maladie ravageuse. Elle était si dangereuse, que seulement quelques heures après l'avoir  contractée, ses victimes se prennaient d'une folie meurtrière sanglante, les poussant à tuer, tuer et re-tuer même les gens qui leurs étaient les plus cher. Après selement 24 heures d'incubation, le malade avait afin la chance de mourrir. Atrocement, certe, d'une agonie abominable causée par la sublimation de sa chair, mais ayant au moins le mérite de le libérer d'autres douleurs encore plus atroces. Car il semblerait, comble de l'horreur, que les victimes restent conscientes de leurs douleurs et actions, comme dans un cauchemard. Cette maladie, appelée la Mort Rouge, mit un terme à l'existance de notre chère humanité.")

    texte6=("Enfin, presque...")
    #départ
    texte7=("Voici l'histoire des derniers survivants de Man'ana'toura et l'archipel du Nouvelle Aube!")
    texte8=("Journal du commandant")
    texte9=("Une fois prêt au départ, nous sommes partis, sans un regard n'y regret pour le pays bientôt dévasté que nous laissons dernière nous. Nous sommes dorénavant le dernière espoir de l'humanité et cela ne peut que nous emplir de fierté...et faire peser sur nos épaules le poids de tout un futur.")
    texte9a = ("Heureusement, pour aider, il se trouve que mon ISaveTheWorld a une application pour facilité la gestion des crises pouvant survenir durant le voyage! Ce programme est même pourvu d'un système GPS révolutionnaire! Il ne me reste plus qu'à trouver son icone... Et voilà!")
   #Épidémie
    texte10=("L'infirmerie du navire se remplit de plus en plus. Manifestement, une maladie se répand au travers les passagers. Nous ignorons se qu'elle pourrait causer, néanmoins il est impératif de réagir! Des rumeurs de contaminations par la Mort Rouge commence déjà à ébranler l'équipage.")
    choix10a=("Je pense de ce fait qu'une mise en quarantaine des malades est tout à fait justifiée; ainsi la maladie ne devrait plus se répandre.")
    choix10b=("J'ai donc décidé que tout les passagers pouvant offrir de leurs temps pour le soins des malades se devront de le faire. La maladie sera ainsi enrayée grâce aux petits soins que prodigueront les autres passagers.")
    choix10c=("Par conséquent, pour éviter de créer des perturbations au seins de l'équipage et nuire à son efficacité, ainsi qu'au moral de la population, à cause de rumeurs sur ce qui ne semble qu'être que des rhumes des plus banals, il faudra étouffer les rumeurs et rassuré tout le monde.")
    choix10d=("Ce qui réduirait à néant toutes chances de re-bâtir notre monde! C'est inadmissible. Pour le bien du plus grand nombre et pour éviter tout risques, nous lancerons par dessus bord tout individu suspecté de maladie, discrètement, bien sûr.")
    #Famine
    texte11=("Il va très probablement nous manquer de nourritures avant que l'on arrive à Man'ana'toura, seul lieu où nous pourrons nous réaprovisionner une fois notre colonis établit. La famine nous menace si nous n'agissons pas.")
    choix11a=("Cependant, il ne s'agit que de rapports... il se peut tout aussi bien, je pense, que nous ayons assez de nourriture pour finir le voyage. Donc, nul besoins d'inquiété tout le monde avec ça.")
    choix11b=("Il va donc falloir que l'on rationne la nourriture. Nous la distriburons tout d'abord à l'équipage, qui doit travailler et qui a donc plus besoins de se sustenter que la populace qui elle ne fait rien de ses journées et qui attend simplement d'être arrivé à destination.")
    choix11c=("Tout le monde devra donc se serrer la ceinture, car à partir de maintenant, la nourriture sera strictement rationnée! Tout le monde n'aura que sa part et elle seule, pas plus grosse pas plus petite qu'une autre!")
    choix11d=("Manisfestement, nous avons ambitionné sur la quantité de gens que nous pouvions ammené avec nous. Il y a, la situation en est la preuve, beaucoup trop de monde à bord! Je vais donc sélectionner les gens les moins utiles à notre future société et les jetter par dessu bord...")
    #Porte-Avions
    texte12=("Nous venons d'appercevoir à l'horizon un porte-avions aborant le pavillon français. Nous ignorons encore s'il y a du monde à bord.")
    choix12a=("Étrange, au dernières nouvelles, nous étions, le Canada, le dernier pays n'étant pas détruit par la maladie. Le bateau est soit contaminé, soit un vestige du passé inutile. Il vaut mieux passer notre chemin.")
    choix12b=("Peut-être ne sommes nous pas les derniers sur cette Terre qui nous est devenu si hostile! Allons voir si nous ne pouvons pas faire équipe pour notre survie commune.")
    #il est vide
    texte13=("Très manisfestement, le porte- avions est vide de toutes vies...")
    choix13a=("... c'est pourquoi il vaut mieux ne pas s'approcher. Ce qui les a tué peut aussi nous tuer, c'est clair.")
    choix13b=("... c'est pourquoi je suis sûr que personne ne s'opposera si nous allons en récupérer tout le matériel qui pourrait nous être utile.")
    #il est encore habité
    texte14=("Nous nous sommes encore un peu approché, puis le porte-avions français se mit à nous envoyer des signaux lumineux. Manifestement, il y a encore des gens sur le bâteau mais ils ne se servent pas de la radio pour entrer en communication avec nous... ")
    choix14a=("...se qui est très suspect. Vaut mieux passer notre chemin en tentant des les évités.")
    choix14b=("... se qui est génial! D'autres êtres vivants, merveilleux! Une fois proche, nous leurs proposerons de faire route avec nous vers Man'ana'toura. Mettre en commun nos resources ne peut qu'être bénéfique.")
    choix14c=("... et en plus, ils semblaient se diriger vers l'Amérique! Comme s'ils se rendaient vers le Québec, qui était le dernier lieu non-infecté... Apprenons-leur que le Canada est également tombé, puis continuons notre chemin. Nous ne les connaisons pas et n'avons aucune raisons de les cotoyer.")
    choix14d=("...laissons-les poursuivre leur chemin. Seul. Il ne faudrait pas qu'ils nous suivent sur Man'ana'toura, qui n'est après tout qu'une île, dont ils voleraient les ressources qui NOUS reviennent!")
    #s'il y a une épidémie
    texte15=("Le bateau habritait un agent pathogène encore non-identifié qui semble avoir réussi par un moyen ou un autre à pénétrer l'ARCHE et maintenant cette maladie se répand! L'équipage a encore en tête les images de la Mort Rouge et la panique les gagnent rapidement.")
    #Arriver
    texte16=("Erreur GPS... recalcul en cours...")
    texte17=("Vous êtes finalement arrivé à destination.")

class Verificationtouche():
    run = True
    endrun = True
    clock = pygame.time.Clock()
    choix =''



    def __init__(self, displ, texteSituation, texteChoixA,texteChoixB,texteChoixC,texteChoixD, passdescriptionSituation = False):
        backround = pygame.image.load("image/Nouvelle_Aube.jpg").convert()
        Journal_interface_choix1 =pygame.image.load("image/journal_interface_variation/Journal_interface_choix1.png").convert_alpha()
        Journal_interface_choix2 =pygame.image.load("image/journal_interface_variation/Journal_interface_choix2.png").convert_alpha()
        Journal_interface_choix3 =pygame.image.load("image/journal_interface_variation/Journal_interface_choix3.png").convert_alpha()
        Journal_interface_choix4 =pygame.image.load("image/journal_interface_variation/Journal_interface_choix4.png").convert_alpha()

        Journal_interface_choix1_green =pygame.image.load("image/journal_interface_variation/Journal_interface_choix1_green.png").convert_alpha()
        Journal_interface_choix2_green =pygame.image.load("image/journal_interface_variation/Journal_interface_choix2_green.png").convert_alpha()
        Journal_interface_choix3_green =pygame.image.load("image/journal_interface_variation/Journal_interface_choix3_green.png").convert_alpha()
        Journal_interface_choix4_green =pygame.image.load("image/journal_interface_variation/Journal_interface_choix4_green.png").convert_alpha()

        Journal_interface_choix1_validgreen =pygame.image.load("image/journal_interface_variation/Journal_interface_choix1_validgreen.png").convert_alpha()
        Journal_interface_choix2_validgreen =pygame.image.load("image/journal_interface_variation/Journal_interface_choix2_validgreen.png").convert_alpha()
        Journal_interface_choix3_validgreen =pygame.image.load("image/journal_interface_variation/Journal_interface_choix3_validgreen.png").convert_alpha()
        Journal_interface_choix4_validgreen =pygame.image.load("image/journal_interface_variation/Journal_interface_choix4_validgreen.png").convert_alpha()

        Journal_interface_choix1_green_white2 =pygame.image.load("image/journal_interface_variation/Journal_interface_choix1_green_white2.png").convert_alpha()
        Journal_interface_choix1_green_white3 =pygame.image.load("image/journal_interface_variation/Journal_interface_choix1_green_white3.png").convert_alpha()
        Journal_interface_choix1_green_white4 =pygame.image.load("image/journal_interface_variation/Journal_interface_choix1_green_white4.png").convert_alpha()

        Journal_interface_choix2_green_white1 =pygame.image.load("image/journal_interface_variation/Journal_interface_choix2_green_white1.png").convert_alpha()
        Journal_interface_choix2_green_white3 =pygame.image.load("image/journal_interface_variation/Journal_interface_choix2_green_white3.png").convert_alpha()
        Journal_interface_choix2_green_white4 =pygame.image.load("image/journal_interface_variation/Journal_interface_choix2_green_white4.png").convert_alpha()

        Journal_interface_choix3_green_white1 =pygame.image.load("image/journal_interface_variation/Journal_interface_choix3_green_white1.png").convert_alpha()
        Journal_interface_choix3_green_white2 =pygame.image.load("image/journal_interface_variation/Journal_interface_choix3_green_white2.png").convert_alpha()
        Journal_interface_choix3_green_white4 =pygame.image.load("image/journal_interface_variation/Journal_interface_choix3_green_white4.png").convert_alpha()

        Journal_interface_choix4_green_white1 =pygame.image.load("image/journal_interface_variation/Journal_interface_choix4_green_white1.png").convert_alpha()
        Journal_interface_choix4_green_white2 =pygame.image.load("image/journal_interface_variation/Journal_interface_choix4_green_white2.png").convert_alpha()
        Journal_interface_choix4_green_white3 =pygame.image.load("image/journal_interface_variation/Journal_interface_choix4_green_white3.png").convert_alpha()



        Journal_interface_general =pygame.image.load("image/journal_interface_variation/Journal_interface_general.png").convert_alpha()
        Journal_interface_redvalid =pygame.image.load("image/journal_interface_variation/Journal_interface_redvalid.png").convert_alpha()


        displ.blit(backround,[0,0])
        displ.blit(Journal_interface_general ,[41,34])
        Story(texteSituation,506,63,810,displ,366,24,COLORS.BLACK,passdescriptionSituation)
       # StoryTelling.whatAction(displ,[680,670], 'clic' )
        while self.run==True:
            self.clock.tick(30)
            StoryTelling.StoryTelling.choicetaken = "0"

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos =pygame.mouse.get_pos()
                    posX = pos[0]
                    posY = pos[1]


                    if posX <489 and posX >82:
                        if posY >70  and posY <183 :
                           Musique.PlaySound(EventAdvancement.sound_validation)
                           self.choix ='1'
                           displ.blit(backround,[0,0])
                           displ.blit(Journal_interface_choix1_green,[41,34])
                           Story(texteSituation,506,63,810,displ,366,24,COLORS.BLACK,True)
                           Story(texteChoixA,506,379,810,displ,654,24,COLORS.BLACK,False)
                           pygame.display.flip()
                        if posY >183  and posY <315 :
                           Musique.PlaySound(EventAdvancement.sound_validation)
                           self.choix ='2'
                           displ.blit(backround,[0,0])
                           displ.blit(Journal_interface_choix2_green,[41,34])
                           Story(texteSituation,506,63,810,displ,366,24,COLORS.BLACK,True)
                           Story(texteChoixB,506,379,810,displ,654,24,COLORS.BLACK,False)
                           pygame.display.flip()
                        if posY >315  and posY <448 :
                           Musique.PlaySound(EventAdvancement.sound_validation)
                           self.choix ='3'
                           displ.blit(backround,[0,0])
                           displ.blit(Journal_interface_choix3_green,[41,34])
                           Story(texteSituation,506,63,810,displ,366,24,COLORS.BLACK,True)
                           Story(texteChoixC,506,379,810,displ,654,24,COLORS.BLACK,False)
                           pygame.display.flip()
                        if posY >448  and posY <581 :
                           Musique.PlaySound(EventAdvancement.sound_validation)
                           self.choix ='4'
                           displ.blit(backround,[0,0])
                           displ.blit(Journal_interface_choix4_green,[41,34])
                           Story(texteSituation,506,63,810,displ,366,24,COLORS.BLACK,True)
                           Story(texteChoixD,506,379,810,displ,654,24,COLORS.BLACK,False)
                           pygame.display.flip()
                        if self.choix != '' and posY >581 and posY < 693:

                            if self.choix =='1':
                                self.Return1()
                                Musique.PlaySound(EventAdvancement.sound_ValidChoiceOK)
                                self.endrun = False
                            if self.choix =='2':
                                self.Return2()
                                Musique.PlaySound(EventAdvancement.sound_ValidChoiceOK)
                                self.endrun = False
                            if self.choix =='3':
                                self.Return3()
                                Musique.PlaySound(EventAdvancement.sound_ValidChoiceOK)
                                self.endrun = False
                            if self.choix =='4':
                                self.Return4()
                                Musique.PlaySound(EventAdvancement.sound_ValidChoiceOK)
                                self.endrun = False

                            else:
                                Musique.PlaySound(EventAdvancement.sound_buttonpassOver)
                                displ.blit(backround,[0,0])
                                displ.blit(Journal_interface_redvalid,[41,34])
                                pygame.display.flip()

                else:
                    pos =pygame.mouse.get_pos()
                    posX = pos[0]
                    posY = pos[1]
                    if posX <489 and posX >82:
                        if posY >70  and posY <183 :
                            if self.choix != '':


                                if self.choix =='2':
                                    Musique.PlaySound(EventAdvancement.sound_buttonpassOver)
                                    displ.blit(backround,[0,0])
                                    displ.blit(Journal_interface_choix2_green_white1,[41,34])
                                    pygame.display.flip()
                                if self.choix =='3':
                                    Musique.PlaySound(EventAdvancement.sound_buttonpassOver)
                                    displ.blit(backround,[0,0])
                                    displ.blit(Journal_interface_choix3_green_white1,[41,34])
                                    pygame.display.flip()
                                if self.choix =='4':
                                    Musique.PlaySound(EventAdvancement.sound_buttonpassOver)
                                    displ.blit(backround,[0,0])
                                    displ.blit(Journal_interface_choix4_green_white1,[41,34])
                                    pygame.display.flip()
                            else:
                                displ.blit(backround,[0,0])
                                displ.blit(Journal_interface_choix1,[41,34])
                                pygame.display.flip()


                        if posY >183  and posY <315 :
                            if self.choix != '':

                                if self.choix =='1':
                                    Musique.PlaySound(EventAdvancement.sound_buttonpassOver)
                                    displ.blit(backround,[0,0])
                                    displ.blit(Journal_interface_choix1_green_white2,[41,34])
                                    pygame.display.flip()

                                if self.choix =='3':
                                    Musique.PlaySound(EventAdvancement.sound_buttonpassOver)
                                    displ.blit(backround,[0,0])
                                    displ.blit(Journal_interface_choix3_green_white2,[41,34])
                                    pygame.display.flip()
                                if self.choix =='4':
                                    Musique.PlaySound(EventAdvancement.sound_buttonpassOver)
                                    displ.blit(backround,[0,0])
                                    displ.blit(Journal_interface_choix4_green_white2,[41,34])
                                    pygame.display.flip()
                            else:
                                displ.blit(backround,[0,0])
                                displ.blit(Journal_interface_choix2,[41,34])
                                pygame.display.flip()

                        if posY >315  and posY <448 :
                            if self.choix != '':

                                if self.choix =='1':
                                    Musique.PlaySound(EventAdvancement.sound_buttonpassOver)
                                    displ.blit(backround,[0,0])
                                    displ.blit(Journal_interface_choix1_green_white3,[41,34])
                                    pygame.display.flip()
                                if self.choix =='2':
                                    Musique.PlaySound(EventAdvancement.sound_buttonpassOver)
                                    displ.blit(backround,[0,0])
                                    displ.blit(Journal_interface_choix2_green_white3,[41,34])
                                    pygame.display.flip()

                                if self.choix =='4':
                                    Musique.PlaySound(EventAdvancement.sound_buttonpassOver)
                                    displ.blit(backround,[0,0])
                                    displ.blit(Journal_interface_choix4_green_white3,[41,34])
                                    pygame.display.flip()
                            else:
                                displ.blit(backround,[0,0])
                                displ.blit(Journal_interface_choix3,[41,34])
                                pygame.display.flip()



                        if posY >448  and posY <581 :
                            if self.choix != '':

                                if self.choix =='1':
                                    Musique.PlaySound(EventAdvancement.sound_buttonpassOver)
                                    displ.blit(backround,[0,0])
                                    displ.blit(Journal_interface_choix1_green_white4,[41,34])
                                    pygame.display.flip()
                                if self.choix =='2':
                                    Musique.PlaySound(EventAdvancement.sound_buttonpassOver)
                                    displ.blit(backround,[0,0])
                                    displ.blit(Journal_interface_choix2_green_white4,[41,34])
                                    pygame.display.flip()
                                if self.choix =='3':
                                    Musique.PlaySound(EventAdvancement.sound_buttonpassOver)
                                    displ.blit(backround,[0,0])
                                    displ.blit(Journal_interface_choix3_green_white4,[41,34])
                                    pygame.display.flip()
                                #
                            else:
                                displ.blit(backround,[0,0])
                                displ.blit(Journal_interface_choix4,[41,34])
                                pygame.display.flip()




                        if  posY >581 and posY < 693:
                            if self.choix != '':

                                if self.choix =='1':
                                    Musique.PlaySound(EventAdvancement.sound_buttonpassOver)
                                    displ.blit(backround,[0,0])
                                    displ.blit(Journal_interface_choix1_validgreen,[41,34])
                                    pygame.display.flip()
                                if self.choix =='2':
                                    Musique.PlaySound(EventAdvancement.sound_buttonpassOver)
                                    displ.blit(backround,[0,0])
                                    displ.blit(Journal_interface_choix2_validgreen,[41,34])
                                    pygame.display.flip()
                                if self.choix =='3':
                                    Musique.PlaySound(EventAdvancement.sound_buttonpassOver)
                                    displ.blit(backround,[0,0])
                                    displ.blit(Journal_interface_choix3_validgreen,[41,34])
                                    pygame.display.flip()
                                if self.choix =='4':
                                    displ.blit(backround,[0,0])
                                    displ.blit(Journal_interface_choix4_validgreen,[41,34])
                                    pygame.display.flip()

                            else:
                                displ.blit(backround,[0,0])
                                displ.blit(Journal_interface_redvalid,[41,34])
                                pygame.display.flip()

            self.run = self.endrun
    def Return1(self):
        StoryTelling.StoryTelling.choicetaken = "1"



    def Return2(self):
        StoryTelling.StoryTelling.choicetaken = "2"


    def Return3(self):
        StoryTelling.StoryTelling.choicetaken = "3"


    def Return4(self):
        StoryTelling.StoryTelling.choicetaken = "4"

