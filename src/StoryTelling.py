__author__ = 'Jean-Alexandre'
import Story
import random
import conda
import pygame
import math
from Defines import COLORS
from pygame.locals import *

def FacteurHasard():
    pourcentage = random.randrange (100)
    return pourcentage

# def StoryTelling():
#     def __init__(self,texte, menuitem):
#         Situation = Story (texte , Story.position.center)
#         Reaction = Story.Choix(menuitem)

def Effet():
    def __init__(self,naturedeleffet): #compose of dictionairies, where naturedeleffet = identifier , modifier

        for  StoryEffects in range():
            if naturedeleffet.identifier ==  StoryEffects.Effects.naturedeleffet:
                StoryEffects.Effects.naturedeleffet += naturedeleffet.modifier


def StartMusic(music):
    pygame.mixer.music.load(music)
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()




StoryMode=True
AFFICHERTEXTe = ("Page d'intoduction")
TEXTEPOURLESCHOIX = ((""), (""))
CHANGEMENTDUAUCHOIX = ("")

#while StoryMode == True:
 #   texte = AFFICHERTEXTe
  #  menuitem = TEXTEPOURLESCHOIX
  #  naturedeleffet = CHANGEMENTDUAUCHOIX
  #  StoryTelling (texte, menuitem)
 #   Effet (naturedeleffet)
  #  if
class StoryTelling():
    choicetaken = 0
    path = ""
    Base_Sociale = Story.RapportElements()
    Ressources_depart = Story.StoryEffects()
    def __init__(self, display):
        # self.epidemie(display)
         #self.Famine(display)
         #self.PorteAvions(display)
        # self.Recontagion(display)
         #self.Rencontre(display)



        a = Story.StoryEffects.Effects
        #INTRODUCTION, PAS DE CHOIX
        self.intro(display,1000)
        self.ISaveTheWorld(display)
        self.VerificationClic(display)
        self.depart(display, 1000)
        #VERIFICATION SI LE JOUEUR VA AVOIR UNE FAMINE
        if self.verifyFamine() == True:
            self.Famine(display)
            #GUARDER LE SECRET
            if self.choicetaken == "1":
                self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/10))
                self.add("Sante",0,10)
                self.add("Influence", 0, 20)
                self.add("Bonheur", 0, 15)
                self.add("Criminalite", 10, 0)
                self.Base_Sociale.mensonge +=1
                #Story.RapportElements.value1=
            # DISTRIBUTION NOURRITURE SELON LES BESIONS
            elif self.choicetaken == "2":
                self.add("Sante", 0, 5)
                self.add( "Bonheur", 0, 20 )
                self.Base_Sociale.pragmatisme +=1
            # SERRONS-NOUS LA CEINTURE TOUS ENSEMBLE
            elif self.choicetaken =="3":
                self.add("Sante", 0, 25)
                self.Base_Sociale.solidarite +=1
            #JETER LE SURPLUS PAR DESSUS BORD
            elif self.choicetaken == "4":
                Story.StoryEffects.Effects ["Population"] = Story.StoryEffects.Effects ["Nourriture"] /10
                self.add("Influence", 0, 20)
                self.add("Bonheur", 0, 35)
                self.add("Criminalite", 15, 0)
                self.Base_Sociale.cruaute +=1
#       VERIFIER SI LA UNE EPIDEMIE SE PROPAGE AU D/BUT DU VOYAGE

        if self.verifyepidemie() == True:
            self.epidemie(display)
            # ETABLIR UNE QUARANTAINE
            if self.choicetaken == "1":
                self.add( "Bonheur", 0, 5 )
                self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/15))
                self.Base_Sociale.pragmatisme +=1
            # AIDE AUX MALADES
            elif self.choicetaken == "2":
                self.add("Sante", 0, 10)
                self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/30))
                self.Base_Sociale.solidarite +=1
            #GUARDER LE SECRET
            elif self.choicetaken =="3":
                self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/10))
                self.add("Sante",0,10)
                self.add("Influence", 0, 20)
                self.add("Bonheur", 0, 15)
                self.add("Criminalite", 10, 0)
                self.Base_Sociale.mensonge +=1
                #JETER LES MALADES PAR DESSUS BORD
            elif self.choicetaken == "4":
                self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/100))
                self.add("Influence", 0, 20)
                self.add("Bonheur", 0, 35)
                self.add("Criminalite", 15, 0)
                self.Base_Sociale.cruaute +=1
#       LE PORTE-AVIONS EST EN VUE
        self.PorteAvions(display)
        # CHOIX 1 = NE PAS S'APPROCHER ET PASSE DIRECTEMENT A MAM'ANA'TOURA
        #ALLER A LA RENCONTRE DU PORTE-AVIONS
        if self.choicetaken == "1":
            self.Base_Sociale.surete +=1
        if self.choicetaken == "2":
            self.Rencontre(display)
            #SI LE PORTE-AVIONS EST VIDE
            if self.path == "vide":
            #NE PAS S'APPROCHER D'AVANTAGE, FAIBLE CHANCE DE CONTAGION
                if self.choicetaken == "1" and self.verifyepidemie(7)==True :
                        self.Recontagion(display)
                        #QUARANTAINE
                        if self.choicetaken == "1":
                            self.add( "Bonheur", 0, 5 )
                            self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/15))
                            self.Base_Sociale.pragmatisme +=1
                        # AIDE AUX MALADES
                        elif self.choicetaken == "2":
                            self.add("Sante", 0, 10)
                            self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/30))
                            self.Base_Sociale.solidarite +=1
                        # GUARDER LE SECRET
                        elif self.choicetaken =="3":
                            self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/10))
                            self.add("Sante",0,10)
                            self.add("Influence", 0, 20)
                            self.add("Bonheur", 0, 15)
                            self.add("Criminalite", 10, 0)
                            self.Base_Sociale.mensonge +=1
                        #JETER PAR DESSU BORD
                        elif self.choicetaken == "4":
                            self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/100))
                            self.add("Influence", 0, 20)
                            self.add("Bonheur", 0, 35)
                            self.add("Criminalite", 15, 0)
                            self.Base_Sociale.cruaute +=1

#               #PRENDRE LES RESSOURCES DU BATEAU AVEC VOUS, CHANCES DE CONTAGION
                if self.choicetaken == "2":
                    self.Base_Sociale.pragmatisme +=1
                    self.add("Petrole", 700, 0)
                    self.add("Influence", 0, 5)
                    self.add("Bonheur", 20, 0)
                    self.add("Criminalite", 15, 0)
                    self.add("Minerai", 300, 0)
                    self.add("Nourriture", 600, 0)
                    #VERIFIT SI CONTAGION
                    if self.verifyepidemie(65)==True :
                        self.Recontagion(display)
                        #QUARANTAINE
                        if self.choicetaken == "1":
                            self.add( "Bonheur", 0, 5 )
                            self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/15))
                            self.Base_Sociale.pragmatisme +=1
                        #AIDES AUX MALADES
                        elif self.choicetaken == "2":
                            self.add("Sante", 0, 10)
                            self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/30))
                            self.Base_Sociale.solidarite +=1
                        #NE RIEN DIRE
                        elif self.choicetaken =="3":
                            self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/10))
                            self.add("Sante",0,10)
                            self.add("Influence", 0, 20)
                            self.add("Bonheur", 0, 15)
                            self.add("Criminalite", 10, 0)
                            self.Base_Sociale.mensonge +=1
                        #JETER PAR DESSU BORD
                        elif self.choicetaken == "4":
                            self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/100))
                            self.add("Influence", 0, 20)
                            self.add("Bonheur", 0, 35)
                            self.add("Criminalite", 15, 0)
                            self.Base_Sociale.cruaute +=1

#           SI LE BATEAU EST ENCORE HABITE
            else:
                # FINALEMENT DECIDER DE NE PAS LUI PARLER
                if self.choicetaken=="1" and  self.verifyepidemie(5)==True:
                    self.Recontagion(display)
                    #CHANCES FAIBLE DE CONTAGION

                    if self.choicetaken == "1":
                        self.add( "Bonheur", 0, 5 )
                        self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/15))
                        self.Base_Sociale.pragmatisme +=1
                    #AIDES AUX MALADES
                    elif self.choicetaken == "2":
                        self.add("Sante", 0, 10)
                        self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/30))
                        self.Base_Sociale.solidarite +=1
                    #NE RIEN DIRE
                    elif self.choicetaken =="3":
                        self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/10))
                        self.add("Sante",0,10)
                        self.add("Influence", 0, 20)
                        self.add("Bonheur", 0, 15)
                        self.add("Criminalite", 10, 0)
                        self.Base_Sociale.mensonge +=1
                    #JETER PAR DESSU BORD
                    elif self.choicetaken == "4":
                        self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/100))
                        self.add("Influence", 0, 20)
                        self.add("Bonheur", 0, 35)
                        self.add("Criminalite", 15, 0)
                        self.Base_Sociale.cruaute +=1

#               LEUR PROPOSER DE VENIR AVEC VOUS
                if self.choicetaken=="2":
                    self.Base_Sociale.solidarite +=1
                    self.add("Petrole", 700, 0)
                    self.add("Influence", 0, 5)
                    self.add("Bonheur", 20, 0)
                    self.add("Criminalite", 15, 0)
                    self.add("Minerai", 300, 0)
                    self.add("Nourriture", 600, 0)
                    self.add("Population", 80, 0)
                    if self.verifyepidemie(30)==True :
                        # POSSIBILITE DE CONTAGION
                        self.Recontagion(display)
                        if self.choicetaken == "1":
                            self.add( "Bonheur", 0, 5 )
                            self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/15))
                            self.Base_Sociale.pragmatisme +=1
                        #AIDES AUX MALADES
                        elif self.choicetaken == "2":
                            self.add("Sante", 0, 10)
                            self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/30))
                            self.Base_Sociale.solidarite +=1
                        #NE RIEN DIRE
                        elif self.choicetaken =="3":
                            self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/10))
                            self.add("Sante",0,10)
                            self.add("Influence", 0, 20)
                            self.add("Bonheur", 0, 15)
                            self.add("Criminalite", 10, 0)
                            self.Base_Sociale.mensonge +=1
                        #JETER PAR DESSU BORD
                        elif self.choicetaken == "4":
                            self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/100))
                            self.add("Influence", 0, 20)
                            self.add("Bonheur", 0, 35)
                            self.add("Criminalite", 15, 0)
                            self.Base_Sociale.cruaute +=1

#               DECIDER DE LES PREVENIR QUE LE CANADA N'EST PLUS UNE BONNE DESTINATION MAIS S'EN QU'ILS VIENNENT AVEC LE JOUEUR
                if self.choicetaken=="3" and  self.verifyepidemie(15)==True:
                    self.Base_Sociale.surete +=1
                    self.Recontagion(display)
                    if self.choicetaken == "1":
                        self.add( "Bonheur", 0, 5 )
                        self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/15))
                        self.Base_Sociale.pragmatisme +=1
                    #AIDES AUX MALADES
                    elif self.choicetaken == "2":
                        self.add("Sante", 0, 10)
                        self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/30))
                        self.Base_Sociale.solidarite +=1
                    #NE RIEN DIRE
                    elif self.choicetaken =="3":
                        self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/10))
                        self.add("Sante",0,10)
                        self.add("Influence", 0, 20)
                        self.add("Bonheur", 0, 15)
                        self.add("Criminalite", 10, 0)
                        self.Base_Sociale.mensonge +=1
                    #JETER PAR DESSU BORD
                    elif self.choicetaken == "4":
                        self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/100))
                        self.add("Influence", 0, 20)
                        self.add("Bonheur", 0, 35)
                        self.add("Criminalite", 15, 0)
                        self.Base_Sociale.cruaute +=1

#               LES LAISSER ALLER AU CANADA... CONTAGION, EN VENGEANCE/KARMA
                if self.choicetaken=="4":
                    self.Base_Sociale.cruaute +=4
                    self.Base_Sociale.mensonge +=2
                    self.Recontagion(display)
                    if self.choicetaken == "1":
                        self.add( "Bonheur", 0, 5 )
                        self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/15))
                        self.Base_Sociale.pragmatisme +=1
                    #AIDES AUX MALADES
                    elif self.choicetaken == "2":
                        self.add("Sante", 0, 10)
                        self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/30))
                        self.Base_Sociale.solidarite +=1
                    #NE RIEN DIRE
                    elif self.choicetaken =="3":
                        self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/10))
                        self.add("Sante",0,10)
                        self.add("Influence", 0, 20)
                        self.add("Bonheur", 0, 15)
                        self.add("Criminalite", 10, 0)
                        self.Base_Sociale.mensonge +=1
                    #JETER PAR DESSU BORD
                    elif self.choicetaken == "4":
                        self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/100))
                        self.add("Influence", 0, 20)
                        self.add("Bonheur", 0, 35)
                        self.add("Criminalite", 15, 0)
                        self.Base_Sociale.cruaute +=3



#       CHOIX N'EXISTANT PAS EN PRINCIPE, ET NE DEVANT AVOIR AUCUN EFFET
#         elif self.choicetaken =="3":
#               self.PorteAvions(display)
#         elif self.choicetaken == "4":
#               self.PorteAvions(display)

#       L'ARRIVEE A MAN'ANA'TOURA

        self.Arrivee(display, 2000)


    def add(self, variableamodifier, modificateurPOSITIF, modificateurNEGATIF):
        self.Ressources_depart.Effects [variableamodifier] = Story.StoryEffects.Effects [variableamodifier] + modificateurPOSITIF - modificateurNEGATIF

    def Backround(self, displ):
        backround = pygame.image.load("image/Nouvelle_Aube.jpg").convert()
        displ.blit(backround,[0,0])

    def intro(self, displ, temps):
        #StartMusic('Choral december.ogg')
        #Posi=Story.position(displ)
        displ.fill(COLORS.BLACK)
        self.Backround(displ)
        Story.Story(Story.Texte.texte1 , 0 , 0, 850, displ)
      #  pygame.display.flip()
        whatAction(displ,[400,600],'clic')




        displ.fill(COLORS.BLACK)
        self.Backround(displ)
        Story.Story(Story.Texte.texte6 , 0 , 0, 850,   displ)
        pygame.display.flip()
        whatAction(displ,([400,600]),'clic')



    def ISaveTheWorld(self, displ):
        displ.fill(COLORS.BLACK)
        self.Backround(displ)
        ISaveTheWorld_interface = pygame.image.load("image/ISaveTheWorld/interfaceGeneral.png").convert_alpha()


        running = True
        x=25
        y=50


        while running == True:
            if x < 939:
                x=x+100
                self.Backround(displ)
                t =pygame.transform.smoothscale(ISaveTheWorld_interface,(x,y))
                displ.blit(t,[41,34])
                pygame.display.flip()
                pygame.time.wait(2)
            else :
                running = False
                run = True

        while run == True:
            if y < 691:
                y=y+100
                self.Backround(displ)
                r=pygame.transform.smoothscale(ISaveTheWorld_interface,(x,y))
                displ.blit(r,[41,34])
                pygame.display.flip()
                pygame.time.wait(4)
            else:
                run = False
#Intro
        self.Backround(displ)
        displ.blit(ISaveTheWorld_interface,[41,34])
        pygame.display.flip()
        Story.Story(Story.Texte.iTexte1,475,50, 809,displ,467, 24 )
        whatAction(displ,[621,463])





    def depart(self,displ, temps):
        ISaveTheWorld_illu_DepartGrenn =pygame.image.load("image/ISaveTheWorld/illiminegreenDepart.png").convert_alpha()
        Simple_interface =pygame.image.load("image/Simple_interface.png").convert_alpha()
        Journal_interface_general =pygame.image.load("image/journal_interface_variation/Journal_interface_general.png").convert_alpha()
        self.Backround(displ)
        running = True
        x=931
        y=691


        while running == True:
            if x > 2:
                x=int(x-(930/30))
                self.Backround(displ)
                t =pygame.transform.smoothscale(ISaveTheWorld_illu_DepartGrenn,(x,y))
                displ.blit(t,[41,34])
                pygame.display.flip()
                pygame.time.wait(2)
            else :
                running = False

        # self.Backround(displ)
        # displ.blit(Simple_interface,[41,34])
        # Story.Story(Story.Texte.texte7 , 47 , 40, 900,  displ)
    #    pygame.display.flip()
    #    pygame.time.wait(temps)


        self.Backround(displ)
        #displ.blit(Simple_interface,[41,34])
        Story.Story(Story.Texte.texte8 , 220 , 315, 880,  displ, 0,45)
     #   pygame.display.flip()
      #  pygame.time.wait(temps)
        whatAction(displ, [400,600],'clic')

        self.Backround(displ)
        #displ.blit(Simple_interface,[41,34])
        Story.Story(Story.Texte.texte9 , 10 , 10, 800,  displ)
     #   pygame.display.flip()
      #  pygame.time.wait(temps)
        whatAction(displ, [400,600],'clic')

        self.Backround(displ)
        #displ.blit(Simple_interface,[41,34])
        Story.Story(Story.Texte.texte9a , 10 , 10, 750,  displ)
     #   pygame.display.flip()
      #  pygame.time.wait(temps)
        whatAction(displ, [400,600],'clic')

        x=0
        y=691
        run = True
        while run == True:
            if x < 939:
                x=int(x+(930/30))
                self.Backround(displ)
                h =pygame.transform.smoothscale(Simple_interface,(x,y))
                displ.blit(h,[41,34])
                pygame.display.flip()
                pygame.time.wait(2)
                print(x)
            else :
                run = False




                #------------------





        self.Backround(displ)
        displ.blit(Simple_interface,[41,34])
        Story.Story("Initialisation du module Voyage_vers_Man'ana'toura... " , 57 , 50, 800,  displ)
     #   pygame.display.flip()
        pygame.time.wait(2000)

        self.Backround(displ)
        displ.blit(Simple_interface,[41,34])
        Story.Story("Recalcul en cours... " , 57 , 50, 800,  displ)
     #   pygame.display.flip()
        pygame.time.wait(800)

        self.Backround(displ)
        displ.blit(Simple_interface,[41,34])
        Story.Story("Recalcul en cours... " , 57 , 50, 800,  displ)
     #   pygame.display.flip()
        pygame.time.wait(800)

        self.Backround(displ)
        displ.blit(Simple_interface,[41,34])
        Story.Story("Recalcul en cours... " , 57 , 50, 800,  displ)
     #   pygame.display.flip()
        pygame.time.wait(800)

        self.Backround(displ)
        displ.blit(Simple_interface,[41,34])
        Story.Story("Bonjour, vous venez bien d'activer l'application ISaveTheWorld: Voyage vers votre avenir(TM). Si vous appréciez votre expérience avec cette application, nous vous invitons à exprimer votre contentement sur le site officiel de distribution d'applications de notre compagnie. Puisqu'il semble que c'est la première fois que vous utilisez le logiciel, voici comment s'en servir:" , 57 , 50, 700,  displ)
     #   pygame.display.flip()
      #  pygame.time.wait(temps)
        whatAction(displ, [400,600],'clic')

        running = True
        x=931
        y=691
        while running == True:
            if x > 2:
                x=int(x-(930/30))
                self.Backround(displ)
                t =pygame.transform.smoothscale(Simple_interface,(x,y))
                displ.blit(t,[41,34])
                pygame.display.flip()
                pygame.time.wait(2)
            else :
                running = False
        x=0
        y=691
        runner =True
        while runner == True:
            if x <939:
                x=int(x+(930/30))
                self.Backround(displ)
                t =pygame.transform.smoothscale(Journal_interface_general,(x,y))
                displ.blit(t,[41,34])
                pygame.display.flip()
                pygame.time.wait(2)
            else :
                runner = False
        self.Backround(displ)
        displ.blit(Journal_interface_general ,[41,34])
        Story.Story("Ici, une description fera état de la situation à laquelle vous êtes confrontée. Cet interface apparaîtra à chaque fois qu'une situation de crise s'annoncera.",506,63,810,displ,366,24,COLORS.BLACK,False)
        Story.Story("Ici, vous pourez voir une description sommaire du choix que vous viendrez de sélectionner en cliquant dessu. Lorsque vous serez prêt à poursuivre votre voyage, appuyez sur n'importe quelle touche.",506,379,810,displ,654,24,COLORS.BLACK,False)
        whatAction(displ,[680,670], 'clic')

    def epidemie(self,displ):
        if self.Base_Sociale.value1 == 'La Santé':

            Simple_interface =pygame.image.load("image/Simple_interface.png").convert_alpha()
            Journal_interface_general =pygame.image.load("image/journal_interface_variation/Journal_interface_general.png").convert_alpha()
            running = True
            x=931
            y=691
            while running == True:
                if x > 2:
                    x=int(x-(930/30))
                    self.Backround(displ)
                    t =pygame.transform.smoothscale(Journal_interface_general,(x,y))
                    displ.blit(t,[41,34])
                    pygame.display.flip()
                    pygame.time.wait(2)
                else :
                    running = False
            x=0
            y=691
            runner =True
            while runner == True:
                if x <939:
                    x=int(x+(930/30))
                    self.Backround(displ)
                    t =pygame.transform.smoothscale(Simple_interface,(x,y))
                    displ.blit(t,[41,34])
                    pygame.display.flip()
                    pygame.time.wait(2)
                else :
                    runner = False

            self.Backround(displ)
            displ.blit(Simple_interface,[41,34])
            Story.Story("Jour 2" , 57 , 50, 750,  displ)
            Story.Story("Commandant... j'ai une très mauvaise nouvelle à vous annoncer... LA MORT ROUGE VA TUER TOUT LE MONDE SUR LE NAVIRE!!! Du moins, selons les rumeurs, rumeurs grondantes de plus en plus fort au seins des passagers et menaçant d'en faire céder plus d'un à la panique! Car même s'il ne s'agit pas de la Mort Rouge, comme le confirme mes analyses, il est incontestable qu'une épidémie de quelque chose s'annonce, vue le nombre de patient à l'infirmerie. Que souhaitez vous faire par rapport à cela?  " , 57 , 80, 750,  displ)
         #   pygame.display.flip()
          #  pygame.time.wait(temps)
            whatAction(displ, [400,600],'clic')
            running = True
            x=931
            y=691
            while running == True:
                if x > 2:
                    x=int(x-(930/30))
                    self.Backround(displ)
                    t =pygame.transform.smoothscale(Simple_interface,(x,y))
                    displ.blit(t,[41,34])
                    pygame.display.flip()
                    pygame.time.wait(2)
                else :
                    running = False
            x=0
            y=691
            runner =True
            while runner == True:
                if x <939:
                    x=int(x+(930/30))
                    self.Backround(displ)
                    t =pygame.transform.smoothscale(Journal_interface_general,(x,y))
                    displ.blit(t,[41,34])
                    pygame.display.flip()
                    pygame.time.wait(2)
                else :
                    runner = False
            Story.Verificationtouche(displ,Story.Texte.texte10,Story.Texte.choix10a,Story.Texte.choix10b,Story.Texte.choix10c,Story.Texte.choix10d, True )



    def Famine(self, displ):
        Simple_interface =pygame.image.load("image/Simple_interface.png").convert_alpha()
        Journal_interface_general =pygame.image.load("image/journal_interface_variation/Journal_interface_general.png").convert_alpha()
        running = True
        x=931
        y=691
        while running == True:
            if x > 2:
                x=int(x-(930/30))
                self.Backround(displ)
                t =pygame.transform.smoothscale(Journal_interface_general,(x,y))
                displ.blit(t,[41,34])
                pygame.display.flip()
                pygame.time.wait(2)
            else :
                running = False
        x=0
        y=691
        runner =True
        while runner == True:
            if x <939:
                x=int(x+(930/30))
                self.Backround(displ)
                t =pygame.transform.smoothscale(Simple_interface,(x,y))
                displ.blit(t,[41,34])
                pygame.display.flip()
                pygame.time.wait(2)
            else :
                runner = False

        self.Backround(displ)
        displ.blit(Simple_interface,[41,34])
        Story.Story("Jour 1" , 57 , 50, 750,  displ)
        Story.Story("Commandant... j'ai une très mauvaise nouvelle à vous annoncer... Il se trouve qu'il se pourrait peut-être qu'éventuellement on puisse devoir envisager... une famine à bord du navire. Si j'avais des émotions, je serais probablement extrêmement gêné, car ceci est ma faute; un bug s'est produit durant le transfert de vos ordre par rapport au chargement de ressource et plus précisément, de nourriture. Nous en avons, mais selons mes calculs, il va en manquer pour accomplir la totalité du voyage. Il est trop tard pour s'en retourner au Québec et le seul lieu connu de réapprovisionnement est notre destination, l'île de Man'ana'toura. Qu'ordonnez-vous pour résoudre la situation?" , 57 , 80, 750,  displ)
     #   pygame.display.flip()
      #  pygame.time.wait(temps)
        whatAction(displ, [400,600],'clic')
        running = True
        x=931
        y=691
        while running == True:
            if x > 2:
                x=int(x-(930/30))
                self.Backround(displ)
                t =pygame.transform.smoothscale(Simple_interface,(x,y))
                displ.blit(t,[41,34])
                pygame.display.flip()
                pygame.time.wait(2)
            else :
                running = False
        x=0
        y=691
        runner =True
        while runner == True:
            if x <939:
                x=int(x+(930/30))
                self.Backround(displ)
                t =pygame.transform.smoothscale(Journal_interface_general,(x,y))
                displ.blit(t,[41,34])
                pygame.display.flip()
                pygame.time.wait(2)
            else :
                runner = False
        Story.Verificationtouche(displ,Story.Texte.texte11,Story.Texte.choix11a,Story.Texte.choix11b,Story.Texte.choix11c,Story.Texte.choix11d, True )



    def PorteAvions(self, displ):
        Simple_interface =pygame.image.load("image/Simple_interface.png").convert_alpha()
        Journal_interface_general =pygame.image.load("image/journal_interface_variation/Journal_interface_general.png").convert_alpha()
        running = True
        x=931
        y=691
        while running == True:
            if x > 2:
                x=int(x-(930/30))
                self.Backround(displ)
                t =pygame.transform.smoothscale(Journal_interface_general,(x,y))
                displ.blit(t,[41,34])
                pygame.display.flip()
                pygame.time.wait(2)
            else :
                running = False
        x=0
        y=691
        runner =True
        while runner == True:
            if x <939:
                x=int(x+(930/30))
                self.Backround(displ)
                t =pygame.transform.smoothscale(Simple_interface,(x,y))
                displ.blit(t,[41,34])
                pygame.display.flip()
                pygame.time.wait(2)
            else :
                runner = False

        self.Backround(displ)
        displ.blit(Simple_interface,[41,34])
        Story.Story("Jour 3" , 57 , 50, 750,  displ)
        Story.Story("Commandant... j'ai une très bonne nouvelle à vous annoncer... Je crois... Nous venons d'avoir un visuel avec ce qui semble être un porte-avions Européen. Cependant, il semble voguer depuis longtemps déjà et il est dans un état lamentable mais encore assez bon pour pouvoir être utilisable. Qu'envisagez-vous de faire par rapport à la situation?" , 57 , 80, 750,  displ)
        print("Le Père Noël frappe encore: Deux innocents pingouins furent kidnappés, sauvagement paralisés puis distribué à des enfants!!! En passant, le programme réussi à lire cette partie de code :D")
     # pygame.display.flip()
      #  pygame.time.wait(temps)
        whatAction(displ, [400,600],'clic')
        running = True
        x=931
        y=691
        while running == True:
            if x > 2:
                x=int(x-(930/30))
                self.Backround(displ)
                t =pygame.transform.smoothscale(Simple_interface,(x,y))
                displ.blit(t,[41,34])
                pygame.display.flip()
                pygame.time.wait(2)
            else :
                running = False
        x=0
        y=691
        runner =True
        while runner == True:
            if x <939:
                x=int(x+(930/30))
                self.Backround(displ)
                t =pygame.transform.smoothscale(Journal_interface_general,(x,y))
                displ.blit(t,[41,34])
                pygame.display.flip()
                pygame.time.wait(2)
            else :
                runner = False
        Story.Verificationtouche(displ,Story.Texte.texte12,Story.Texte.choix12a,Story.Texte.choix12b, "Il n'y a pas d'autres options...","Il n'y a pas d'autres options...", True)



    def Rencontre(self, displ):
        a =FacteurHasard()

        if  a<30:
            #self.path = "vide"
            Story.Verificationtouche(displ,Story.Texte.texte13,Story.Texte.choix13a,Story.Texte.choix13b,"Il n'y a pas d'autres options...","Il n'y a pas d'autres options...")

        #
        else:
            #self.path = "plein"
            Story.Verificationtouche(displ,Story.Texte.texte14,Story.Texte.choix14a,Story.Texte.choix14b,Story.Texte.choix14c,Story.Texte.choix14d )




    def Recontagion(self, displ):
        Story.Verificationtouche(displ,Story.Texte.texte15,Story.Texte.choix10a,Story.Texte.choix10b,Story.Texte.choix10c,Story.Texte.choix10d )




    def Arrivee(self, displ, temps):
        Simple_interface =pygame.image.load("image/Simple_interface.png").convert_alpha()
        Journal_interface_general =pygame.image.load("image/journal_interface_variation/Journal_interface_general.png").convert_alpha()
        Rapport_Preliminaire=pygame.image.load("image/Rapport_Preliminaire.png").convert_alpha()
        running = True
        x=931
        y=691
        while running == True:
            if x > 2:
                x=int(x-(930/30))
                self.Backround(displ)
                t =pygame.transform.smoothscale(Journal_interface_general,(x,y))
                displ.blit(t,[41,34])
                pygame.display.flip()
                pygame.time.wait(2)
            else :
                running = False
        x=0
        y=691
        runner =True
        while runner == True:
            if x <939:
                x=int(x+(930/30))
                self.Backround(displ)
                t =pygame.transform.smoothscale(Simple_interface,(x,y))
                displ.blit(t,[41,34])
                pygame.display.flip()
                pygame.time.wait(2)
            else :
                runner = False

        self.Backround(displ)
        displ.blit(Simple_interface,[41,34])
        Story.Story("Jour 4" , 57 , 50, 750,  displ)
        Story.Story(Story.Texte.texte16 , 57 , 80, 750,  displ)
        pygame.time.wait(800)
        self.Backround(displ)
        displ.blit(Simple_interface,[41,34])
        Story.Story("Jour 5" , 57 , 50, 750,  displ)
        Story.Story(Story.Texte.texte16 , 57 , 80, 750,  displ)
        pygame.time.wait(800)
        self.Backround(displ)
        displ.blit(Simple_interface,[41,34])
        Story.Story("Jour 6" , 57 , 50, 750,  displ)
        Story.Story(Story.Texte.texte16 , 57 , 80, 750,  displ)
        pygame.time.wait(800)
        self.Backround(displ)
        displ.blit(Simple_interface,[41,34])
        Story.Story("Jour 7" , 57 , 50, 750,  displ)
        Story.Story(Story.Texte.texte16 , 57 ,80, 750,  displ)
        pygame.time.wait(800)
        self.Backround(displ)
        displ.blit(Simple_interface,[41,34])
        Story.Story("Jour 8" , 57 , 50, 750,  displ)
        Story.Story(Story.Texte.texte17 , 57 , 80, 750,  displ)

        whatAction(displ, [400,600],'clic')
        running = True
        x=931
        y=691
        while running == True:
            if x > 2:
                x=int(x-(930/30))
                self.Backround(displ)
                t =pygame.transform.smoothscale(Simple_interface,(x,y))
                displ.blit(t,[41,34])
                pygame.display.flip()
                pygame.time.wait(2)
            else :
                running = False
        x=0
        y=691
        runner =True
        while runner == True:
            if x <939:
                x=int(x+(930/30))
                self.Backround(displ)
                t =pygame.transform.smoothscale(Rapport_Preliminaire,(x,y))
                displ.blit(t,[41,34])
                pygame.display.flip()
                pygame.time.wait(2)
            else :
                runner = False





        self.Backround(displ)
        displ.blit(Rapport_Preliminaire,[41,34])

        self.Base_Sociale.findValue()

        Story.Story("Valeurs à la base de votre nouvelle société:" , 107 , 150, 750,  displ)
        Story.Story( self.Base_Sociale.value1+ " et " +self.Base_Sociale.value2, 107 , 185, 750,  displ)

        Story.Story( "Données démographiques:", 107 , 250, 750,  displ)
        Story.Story( "Bonheur:", 107 , 290, 750,  displ)
        Story.Story( "Influence:", 107 , 315, 750,  displ)
        Story.Story( "Santé:", 107 , 340, 750,  displ)
        Story.Story( "Éducation:" , 107 , 365, 750,  displ)
        Story.Story( "Criminalité:" , 107 , 390, 750,  displ)
        Story.Story( "Population:" , 107 , 415, 750,  displ)

        Story.Story( str(self.Ressources_depart.Effects['Bonheur']), 307 , 290, 750,  displ)
        Story.Story( str(self.Ressources_depart.Effects['Influence']), 307 , 315, 750,  displ)
        Story.Story( str(self.Ressources_depart.Effects['Sante']), 307 , 340, 750,  displ)
        Story.Story( str(self.Ressources_depart.Effects['Education']), 307 , 365, 750,  displ)
        Story.Story( str(self.Ressources_depart.Effects['Criminalite']), 307 , 390, 750,  displ)
        self.Ressources_depart.Effects['Population']=math.floor(self.Ressources_depart.Effects['Population'])
        Story.Story( str(self.Ressources_depart.Effects['Population']), 307 , 415, 750,  displ)


        Story.Story( "Stock de ressources:",547 , 250, 750,  displ)
        Story.Story( "Bois:" , 547 , 290, 750,  displ)
        Story.Story( "Minerai:", 547 , 315, 750,  displ)
        Story.Story( "Nourriture:" , 547 , 340, 750,  displ)
        Story.Story( "Pétrole:" , 547 , 365, 750,  displ)

        Story.Story( str(self.Ressources_depart.Effects['Bois']), 717 , 290, 750,  displ)
        Story.Story( str(self.Ressources_depart.Effects['Minerai']), 717 , 315, 750,  displ)
        Story.Story( str(self.Ressources_depart.Effects['Nourriture']), 717 , 340, 750,  displ)
        Story.Story( str(self.Ressources_depart.Effects['Petrole']), 717 , 365, 750,  displ)

        whatAction(displ,[400,600],'clic')


    def verifyFamine(self):
        return True

    def verifyepidemie(self, chances=100):
        a = FacteurHasard()
        if a < chances :
            if self.Base_Sociale.value1 != "La Santé":
                return True
            else:
                return False
        else:
            return False


    def VerificationClic(self, displ):
        run = True
        clock = pygame.time.Clock()
        etat =''
        checkedproposition = 'none'

        ISaveTheWorld_selec_Audace =pygame.image.load("image/ISaveTheWorld/selectionneAudace.png").convert_alpha()
        ISaveTheWorld_selec_Sante =pygame.image.load("image/ISaveTheWorld/selectionneSante.png").convert_alpha()
        ISaveTheWorld_selec_Ordre =pygame.image.load("image/ISaveTheWorld/selectionneOrdre.png").convert_alpha()
        ISaveTheWorld_selec_Industrie =pygame.image.load("image/ISaveTheWorld/selectionneIndustrie.png").convert_alpha()
        ISaveTheWorld_selec_Galanterie =pygame.image.load("image/ISaveTheWorld/selectionneGalanterie.png").convert_alpha()
        ISaveTheWorld_selec_Equite =pygame.image.load("image/ISaveTheWorld/selectionneEquite.png").convert_alpha()
        ISaveTheWorld_selec_Bonheur =pygame.image.load("image/ISaveTheWorld/selectionneBonheur.png").convert_alpha()
        ISaveTheWorld_selec_Argent =pygame.image.load("image/ISaveTheWorld/selectionneArgent.png").convert_alpha()
        ISaveTheWorld_selec_Altruisme =pygame.image.load("image/ISaveTheWorld/selectionneAltruisme.png").convert_alpha()



        ISaveTheWorld_illu_Audace =pygame.image.load("image/ISaveTheWorld/illumineAudace.png").convert_alpha()
        ISaveTheWorld_illu_Sante =pygame.image.load("image/ISaveTheWorld/illimineSante.png").convert_alpha()
        ISaveTheWorld_illu_DepartRed =pygame.image.load("image/ISaveTheWorld/illimineredDepart.png").convert_alpha()
        ISaveTheWorld_illu_Ordre =pygame.image.load("image/ISaveTheWorld/illimineOrdre.png").convert_alpha()
        ISaveTheWorld_illu_Industrie =pygame.image.load("image/ISaveTheWorld/illimineIndustrie.png").convert_alpha()
        ISaveTheWorld_illu_DepartGrenn =pygame.image.load("image/ISaveTheWorld/illiminegreenDepart.png").convert_alpha()
        ISaveTheWorld_illu_Galanterie =pygame.image.load("image/ISaveTheWorld/illimineGalanterie.png").convert_alpha()
        ISaveTheWorld_illu_Equite =pygame.image.load("image/ISaveTheWorld/illimineEquite.png").convert_alpha()
        ISaveTheWorld_illu_Bonheur =pygame.image.load("image/ISaveTheWorld/illimineBonheur.png").convert_alpha()
        ISaveTheWorld_illu_Argent =pygame.image.load("image/ISaveTheWorld/illimineArgent.png").convert_alpha()
        ISaveTheWorld_illu_Altruisme =pygame.image.load("image/ISaveTheWorld/illumineAltruisme.png").convert_alpha()

        Ressources_Prevues =pygame.image.load("image/ISaveTheWorld/Communstartingressources .png").convert_alpha()
        ISaveTheWorld_interface = pygame.image.load("image/ISaveTheWorld/interfaceGeneral.png").convert_alpha()
        while run==True:
            clock.tick(30)
            if etat == 'choix de concept':
                for event in pygame.event.get():

                    if event.type == pygame.MOUSEBUTTONDOWN:

                        #if pygame.mouse.get_pressed() == (True, (False or True) ,(False or True)):
                        pos =pygame.mouse.get_pos()
                        posX = pos[0]
                        posY = pos[1]
                            # checking part
                        if posX <118 and posX >84:
                            if posY >76  and posY <109 :
                                self.ALTRUISME()
                                CheckingCheck.checked = True
                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_selec_Altruisme,[41,34])
                                CheckingCheck.checkedproposition = 'Altruisme'
                                CheckingCheck(displ)
                                displ.blit(Ressources_Prevues,[515,506])

                                pygame.display.flip()
                                Story.Story(Story.Texte.iTexteALTRUISME,475,50, 809,displ,467, 22 )


                            if posY > 142 and posY < 172:
                                self.AUDACE()
                                CheckingCheck.checked = True
                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_selec_Audace,[41,34])
                                CheckingCheck.checkedproposition = 'Audace'
                                CheckingCheck(displ)



                                pygame.display.flip()
                                Story.Story(Story.Texte.iTexteAUDACE,475,50, 809,displ,450, 22 )
                                whatAction(displ,[621,463],'clic')
                                self.Backround(displ)

                                displ.blit(ISaveTheWorld_selec_Audace,[41,34])
                                CheckingCheck(displ)
                                Story.Story(Story.Texte.iTexteAUDACE2,475,50, 809,displ,450, 22 )

                            if posY >208  and posY <241 :
                                self.ARGENT()
                                CheckingCheck.checked = True
                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_selec_Argent,[41,34])
                                CheckingCheck.checkedproposition = 'Argent'
                                CheckingCheck(displ)


                                pygame.display.flip()
                                Story.Story(Story.Texte.iTexteARGENT,475,50, 809,displ,467, 22 )


                            if posY >275  and posY <307 :
                                self.BONHEUR()
                                CheckingCheck.checked = True
                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_selec_Bonheur,[41,34])
                                CheckingCheck.checkedproposition = 'Bonheur'
                                CheckingCheck(displ)
                                displ.blit(Ressources_Prevues,[515,506])

                                pygame.display.flip()
                                Story.Story(Story.Texte.iTexteBONHEUR,475,50, 809,displ,450, 22 )
                                whatAction(displ,[621,463],'clic')
                                self.Backround(displ)

                                displ.blit(ISaveTheWorld_selec_Bonheur,[41,34])
                                CheckingCheck(displ)
                                displ.blit(Ressources_Prevues,[515,506])
                                Story.Story(Story.Texte.iTexteBONHEUR2,475,50, 809,displ,450, 22 )


                            if posY >341  and posY <374 :
                                self.EQUITE()
                                CheckingCheck.checked = True
                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_selec_Equite,[41,34])
                                CheckingCheck.checkedproposition = 'Equite'
                                CheckingCheck(displ)
                                displ.blit(Ressources_Prevues,[515,506])

                                pygame.display.flip()
                                Story.Story(Story.Texte.iTexteEQUITE,475,50, 809,displ,467, 22 )


                            if posY >408  and posY < 443:
                                self.GALANTERIE()
                                CheckingCheck.checked = True
                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_selec_Galanterie,[41,34])
                                CheckingCheck.checkedproposition = 'Galanterie'
                                CheckingCheck(displ)
                                displ.blit(Ressources_Prevues,[515,506])

                                pygame.display.flip()
                                Story.Story(Story.Texte.iTexteGALANTERIE,475,50, 809,displ,450, 22 )
                                whatAction(displ,[621,463],'clic')
                                self.Backround(displ)

                                displ.blit(ISaveTheWorld_selec_Galanterie,[41,34])
                                CheckingCheck(displ)
                                displ.blit(Ressources_Prevues,[515,506])
                                Story.Story(Story.Texte.iTexteGALANTERIE2,475,50, 809,displ,450, 22 )



                            if posY > 471 and posY <505 :
                                self.INDUSTRIE()
                                CheckingCheck.checked = True
                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_selec_Industrie,[41,34])
                                CheckingCheck.checkedproposition = 'Industrie'
                                CheckingCheck(displ)


                                pygame.display.flip()
                                Story.Story(Story.Texte.iTexteINDUSTRIE,475,50, 809,displ,467, 22 )


                            if posY > 538 and posY < 570 :
                                self.ORDRE()
                                CheckingCheck.checked = True
                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_selec_Ordre,[41,34])
                                CheckingCheck.checkedproposition = 'Ordre'
                                CheckingCheck(displ)
                                displ.blit(Ressources_Prevues,[515,506])

                                pygame.display.flip()
                                Story.Story(Story.Texte.iTexteORDRE,475,50, 809,displ,467, 22 )


                            if posY >597  and posY <629:
                                self.SANTE()
                                CheckingCheck.checked = True
                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_selec_Sante,[41,34])
                                CheckingCheck.checkedproposition = 'Sante'
                                CheckingCheck(displ)
                                displ.blit(Ressources_Prevues,[515,506])

                                pygame.display.flip()
                                Story.Story(Story.Texte.iTexteSANTE,475,50, 809,displ,467, 22 )

                        elif (posX <84 and posX >75) or (posX <474 and posX >118) :
                            if posY > 65 and posY < 124:

                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_selec_Altruisme,[41,34])
                                CheckingCheck(displ )
                                displ.blit(Ressources_Prevues,[515,506])
                                pygame.display.flip()
                                Story.Story(Story.Texte.iTexteALTRUISME,475,50, 809,displ,467, 22 )




                            if posY > 124 and posY < 190:

                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_selec_Audace,[41,34])
                                CheckingCheck(displ )


                                pygame.display.flip()
                                Story.Story(Story.Texte.iTexteAUDACE,475,50, 809,displ,450, 22 )
                                whatAction(displ,[621,463],'clic')
                                self.Backround(displ)


                                displ.blit(ISaveTheWorld_selec_Audace,[41,34])
                                CheckingCheck(displ )
                                Story.Story(Story.Texte.iTexteAUDACE2,475,50, 809,displ,450, 22 )


                            if posY > 190 and posY < 256:

                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_selec_Argent,[41,34])
                                CheckingCheck(displ)

                                pygame.display.flip()
                                Story.Story(Story.Texte.iTexteARGENT,475,50, 809,displ,467, 22 )



                            if posY > 256 and posY < 322:

                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_selec_Bonheur,[41,34])
                                CheckingCheck(displ )
                                displ.blit(Ressources_Prevues,[515,506])
                                pygame.display.flip()
                                Story.Story(Story.Texte.iTexteBONHEUR,475,50, 809,displ,450, 22 )
                                whatAction(displ,[621,463],'clic')
                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_selec_Bonheur,[41,34])
                                CheckingCheck(displ )
                                displ.blit(Ressources_Prevues,[515,506])


                                Story.Story(Story.Texte.iTexteBONHEUR2,475,50, 809,displ,450, 22 )



                            if posY > 322 and posY < 385:

                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_selec_Equite,[41,34])
                                CheckingCheck(displ )
                                displ.blit(Ressources_Prevues,[515,506])
                                pygame.display.flip()
                                Story.Story(Story.Texte.iTexteEQUITE,475,50, 809,displ,467, 22 )


                            if posY > 385 and posY < 454:

                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_selec_Galanterie,[41,34])
                                CheckingCheck(displ )
                                displ.blit(Ressources_Prevues,[515,506])
                                pygame.display.flip()
                                Story.Story(Story.Texte.iTexteGALANTERIE,475,50, 809,displ,450, 22 )
                                whatAction(displ,[621,463],'clic')
                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_selec_Galanterie,[41,34])
                                CheckingCheck(displ )
                                displ.blit(Ressources_Prevues,[515,506])


                                Story.Story(Story.Texte.iTexteGALANTERIE2,475,50, 809,displ,450, 22 )


                            if posY > 454 and posY < 518:

                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_selec_Industrie,[41,34])
                                CheckingCheck(displ )
                                pygame.display.flip()
                                Story.Story(Story.Texte.iTexteINDUSTRIE,475,50, 809,displ,467, 22 )


                            if posY > 518 and posY < 582:

                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_selec_Ordre,[41,34])
                                CheckingCheck(displ )
                                displ.blit(Ressources_Prevues,[515,506])
                                pygame.display.flip()
                                Story.Story(Story.Texte.iTexteORDRE,475,50, 809,displ,467, 22 )


                            if posY > 582 and posY < 646:

                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_selec_Sante,[41,34])
                                CheckingCheck(displ)
                                displ.blit(Ressources_Prevues,[515,506])
                                pygame.display.flip()
                                Story.Story(Story.Texte.iTexteSANTE,475,50, 809,displ,467, 22 )


                            if posY > 646 and posY < 697:
                                if CheckingCheck.checked == True:
                                    run = False


                    else:
                        pos =pygame.mouse.get_pos()
                        posX = pos[0]
                        posY = pos[1]
                        if posX <474 and posX >75:
                            if posY > 65 and posY < 124:

                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_illu_Altruisme,[40,34])
                                CheckingCheck(displ )
                                pygame.display.flip()



                            if posY > 124 and posY < 190:

                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_illu_Audace,[41,34])
                                CheckingCheck(displ )
                                pygame.display.flip()



                            if posY > 190 and posY < 256:

                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_illu_Argent,[41,34])
                                CheckingCheck(displ )
                                pygame.display.flip()



                            if posY > 256 and posY < 322:

                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_illu_Bonheur,[41,34])
                                CheckingCheck(displ )
                                pygame.display.flip()



                            if posY > 322 and posY < 385:

                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_illu_Equite,[41,34])
                                CheckingCheck(displ )
                                pygame.display.flip()



                            if posY > 385 and posY < 454:

                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_illu_Galanterie,[41,34])
                                CheckingCheck(displ )
                                pygame.display.flip()

                            if posY > 454 and posY < 518:

                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_illu_Industrie,[41,34])
                                CheckingCheck(displ )
                                pygame.display.flip()

                            if posY > 518 and posY < 582:

                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_illu_Ordre,[41,34])
                                CheckingCheck(displ )
                                pygame.display.flip()

                            if posY > 582 and posY < 646:

                                self.Backround(displ)
                                displ.blit(ISaveTheWorld_illu_Sante,[41,34])
                                CheckingCheck(displ )
                                pygame.display.flip()

                            if posY > 646 and posY < 697:

                                self.Backround(displ)
                                if CheckingCheck.checked == False:
                                    displ.blit(ISaveTheWorld_illu_DepartRed,[41,34])
                                if CheckingCheck.checked == True:
                                    displ.blit(ISaveTheWorld_illu_DepartGrenn,[41,34])
                                CheckingCheck(displ)
                                pygame.display.flip()

            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYUP:
                        if etat == 'suite':

                            self.Backround(displ)
                            displ.blit(ISaveTheWorld_interface,[41,34])
                            pygame.display.flip()
                            Story.Story(Story.Texte.iTexte1part3,475,50,809,displ,467,24)
                            etat = 'choix de concept'

                        else:
                            etat = 'suite'

                            self.Backround(displ)
                            displ.blit(ISaveTheWorld_interface,[41,34])
                            pygame.display.flip()
                            Story.Story(Story.Texte.iTexte1part2,475,50,809,displ,467,24)
                            whatAction(displ,[621,463])

    def set(self, setcible, valor ):
        self.Ressources_depart.Effects [setcible] = valor

    def ALTRUISME(self):
         self.set('Bois', 1200)
         self.set('Minerai', 200)
         self.set('Nourriture',1800)


         self.set('Criminalite', 38)
         self.set('Influence', 75)
         self.set('Education', 75)
         self.set('Sante', 75)
         self.set('Bonheur', 75)
         self.Base_Sociale.value1 ="L'Altruisme"
         self.Base_Sociale.solidarite +=1

    def AUDACE(self):
        if FacteurHasard() < 50:
            self.set('Bois', 2400)
            self.set('Minerai', 400)
            self.set('Nourriture', 3600)
            self.set('Petrole',400)

            self.set('Influence', 63)
            self.set('Bonheur', 63)
        else:
            self.set('Bois', 1200)
            self.set('Minerai', 200)
            self.set('Nourriture',1800)

            self.set('Sante', 12)
            self.set('Influence', 12)
            self.set('Bonheur', 12)
        self.Base_Sociale.value1 ="L'Audace"
        self.Base_Sociale.surete -=3


    def ARGENT(self):
        self.set('Bois', 1800)
        self.set('Minerai', 300)
        self.set('Nourriture',2700)
        self.set('Petrole',250)

        self.set('Education', 63)
        self.set('Influence', 25)
        self.set('Bonheur', 63)
        self.Base_Sociale.value1 ="L'Argent"
        self.Base_Sociale.solidarite -=1


    def BONHEUR(self):
        self.set('Bois', 1200)
        self.set('Minerai', 200)
        self.set('Nourriture',1800)

        #centre multim/dia bonus batiment de depart

        self.set('Criminalite', 38)
        self.set('Influence', 63)
        self.set('Bonheur', 100)
        self.Base_Sociale.value1 ="Le Bonheur"


    def EQUITE(self):
        self.set('Bois', 1200)
        self.set('Minerai', 200)
        self.set('Nourriture',1800)

        self.set('Criminalite', 38)
        self.set('Influence', 75)
        self.set('Bonheur', 63)
        self.Base_Sociale.value1 ="L'Équité"

    def GALANTERIE(self):
        self.set('Bois', 1200)
        self.set('Minerai', 200)
        self.set('Nourriture',1800)

        self.set('Population', 3500)

        self.set('Criminalite', 25)
        self.set('Influence', 75)
        self.set('Bonheur', 63)
        self.set('Education', 83)
        self.Base_Sociale.value1 ="La Galanterie"
        self.Base_Sociale.pragmatisme -=1

    def INDUSTRIE(self):
        self.set('Bois', 900)
        self.set('Minerai', 150)
        self.set('Nourriture',1350)
        self.set('Petrole',75)
        # + un batiment special de production, efficace mais polluant

        self.set('Population', 2500)

        self.set('Education', 75)
        self.set('Bonheur', 38)
        self.Base_Sociale.value1 ="L'Industrie"
        self.Base_Sociale.pragmatisme +=1

    def ORDRE(self):
        self.set('Bois', 1200)
        self.set('Minerai', 200)
        self.set('Nourriture',1800)

        self.set('Criminalite', 0)
        self.set('Influence', 100)
        self.set('Education', 25)
        self.set('Sante', 63)
        self.Base_Sociale.value1 ="L'Ordre"
        self.Base_Sociale.pragmatisme +=1

    def SANTE(self):
        self.set('Bois', 1200)
        self.set('Minerai', 200)
        self.set('Nourriture',1800)

        self.set('Education', 63)
        self.set('Sante', 100)
        self.Base_Sociale.value1 ="La Santé"
        self.Base_Sociale.surete +=1

class CheckingCheck():
        checked = False
        pcheckmark_image = pygame.image.load("image/ISaveTheWorld/green_checkmark.png")

        pcheckmark_image.set_colorkey((255,255,255))

        checkmark_image = pcheckmark_image
        checkedproposition = ''
        checkedOne =  checkedproposition

        coordinate = [0,0]
        firstCheck= False
        def __init__(self, displ):
            self.checkedOne =  self.checkedproposition


            if self.checkedOne == 'Altruisme':
                self.coordinate = [84,76]
                self.firstCheck= True

            if self.checkedOne == 'Audace':
                self.coordinate = [84,142]
                self.firstCheck= True

            if self.checkedOne == 'Argent':
                self.coordinate = [84,208]
                self.firstCheck= True

            if self.checkedOne == 'Bonheur':
                self.coordinate = [84,275,]
                self.firstCheck= True

            if self.checkedOne == 'Equite':
                self.coordinate = [84,341]
                self.firstCheck= True

            if self.checkedOne == 'Galanterie':
                self.coordinate = [84,408]
                self.firstCheck= True

            if self.checkedOne == 'Industrie':
                self.coordinate = [84,471]
                self.firstCheck= True

            if self.checkedOne == 'Ordre':
                self.coordinate = [84,538]
                self.firstCheck= True

            if self.checkedOne == 'Sante':
                self.coordinate = [84,597]
                self.firstCheck= True


            if self.firstCheck == True:
                displ.blit(self.checkmark_image,self.coordinate)
                Story.RapportElements.value1= self.checkedOne





class whatAction():

    def __init__(self,  display, Position, TrueAction = 'pingouin'):
       font = pygame.font.SysFont ('None' , 25, True, False)
       text = font.render ('Cliquez pour la suite', True , COLORS.WHITE)


       run = True
       #alphaValor= 0

       while run == True:

           # text.set_colorkey(alphaValor)
           display.blit(text, Position)
           pygame.display.flip()
           # if alphaValor < 255:
           #     alphaValor += 1
           # if alphaValor == 255:
           #     alphaValor = 0
           if TrueAction == 'clic':
               event =pygame.event.peek((pygame.QUIT,pygame.MOUSEBUTTONDOWN,pygame.KEYUP))
               pygame.event.clear()
               if event==True:
                   run = False
           else:
               run = False