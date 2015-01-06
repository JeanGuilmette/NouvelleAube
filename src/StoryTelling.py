__author__ = 'Jean-Alexandre'
import Story
import random
import conda
import pygame
from defines import COLORS
from pygame.locals import *

def FacteurHasard( Seuil_arrive):
    pourcentage = random.randrange (100)
    if Seuil_arrive < pourcentage:
            return True
    else:
        return False

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

    def __init__(self, display):
        a = Story.StoryEffects.Effects
        #INTRODUCTION, PAS DE CHOIX
        #self.intro(display,1000)
        self.ISaveTheWorld(display)
        self.VerificationClic(display)
        #self.depart(display, 1000)
        #VERIFICATION SI LE JOUEUR VA AVOIR UNE FAMINE
        if self.verifyFamine() == True:
            self.Famine(display)
            #GUARDER LE SECRET
            if self.choicetaken == "1":
                self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/7))
                self.add("Sante",0,10)
                self.add("Influence", 0, 20)
                self.add("Bonheur", 0, 15)
                self.add("Criminalite", 10, 0)
            # DISTRIBUTION NOURRITURE SELON LES BESIONS
            elif self.choicetaken == "2":
                self.add("Sante", 0, 5)
                self.add( "Bonheur", 0, 20 )
            # SERRONS-NOUS LA CEINTURE TOUS ENSEMBLE
            elif self.choicetaken =="3":
                self.add("Sante", 0, 25)
            #JETER LE SURPLUS PAR DESSUS BORD
            elif self.choicetaken == "4":
                Story.StoryEffects.Effects ["Population"] = Story.StoryEffects.Effects ["Nourriture"] / 7
                self.add("Influence", 0, 20)
                self.add("Bonheur", 0, 35)
                self.add("Criminalite", 15, 0)
#       VERIFIER SI LA UNE EPIDEMIE SE PROPAGE AU D/BUT DU VOYAGE
        if self.verifyepidemie(50) == True:
            self.epidemie(display)
            # ETABLIR UNE QUARANTAINE
            if self.choicetaken == "1":
                self.add( "Bonheur", 0, 5 )
                self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/15))
            # AIDE AUX MALADES
            elif self.choicetaken == "2":
                self.add("Sante", 0, 10)
                self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/30))
            #GUARDER LE SECRET
            elif self.choicetaken =="3":
                self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/7))
                self.add("Sante",0,10)
                self.add("Influence", 0, 20)
                self.add("Bonheur", 0, 15)
                self.add("Criminalite", 10, 0)
                #JETER LES MALADES PAR DESSUS BORD
            elif self.choicetaken == "4":
                self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/100))
                self.add("Influence", 0, 20)
                self.add("Bonheur", 0, 35)
                self.add("Criminalite", 15, 0)
#       LE PORTE-AVIONS EST EN VUE
        self.PorteAvions(display)
        # CHOIX 1 = NE PAS S'APPROCHER ET PASSE DIRECTEMENT A MAM'ANA'TOURA
        #ALLER A LA RENCONTRE DU PORTE-AVIONS
        if self.choicetaken == "2":
            self.Rencontre(display)
            #SI LE PORTE-AVIONS EST VIDE
            if self.path == "vide":
            #NE PAS S'APPROCHER D'AVANTAGE, FAIBLE CHANCE DE CONTAGION
                if self.choicetaken == "1" and self.verifyepidemie(98)==True :
                        self.Recontagion(display)
                        #QUARANTAINE
                        if self.choicetaken == "1":
                            self.add( "Bonheur", 0, 5 )
                            self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/15))
                        # AIDE AUX MALADES
                        elif self.choicetaken == "2":
                            self.add("Sante", 0, 10)
                            self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/30))
                        # GUARDER LE SECRET
                        elif self.choicetaken =="3":
                            self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/7))
                            self.add("Sante",0,10)
                            self.add("Influence", 0, 20)
                            self.add("Bonheur", 0, 15)
                            self.add("Criminalite", 10, 0)
                        #JETER PAR DESSU BORD
                        elif self.choicetaken == "4":
                            self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/100))
                            self.add("Influence", 0, 20)
                            self.add("Bonheur", 0, 35)
                            self.add("Criminalite", 15, 0)

#               #PRENDRE LES RESSOURCES DU BATEAU AVEC VOUS, CHANCES DE CONTAGION
                if self.choicetaken == "2":
                    self.add("Petrole", 700, 0)
                    self.add("Influence", 0, 5)
                    self.add("Bonheur", 20, 0)
                    self.add("Criminalite", 15, 0)
                    self.add("Metaux", 300, 0)
                    self.add("Pierre", 400, 0)
                    self.add("Nourriture", 600, 0)
                    #VERIFIT SI CONTAGION
                    if self.verifyepidemie(20)==True :
                        self.Recontagion(display)
                        #QUARANTAINE
                        if self.choicetaken == "1":
                            self.add( "Bonheur", 0, 5 )
                            self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/15))
                        #AIDES AUX MALADES
                        elif self.choicetaken == "2":
                            self.add("Sante", 0, 10)
                            self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/30))
                        #NE RIEN DIRE
                        elif self.choicetaken =="3":
                            self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/7))
                            self.add("Sante",0,10)
                            self.add("Influence", 0, 20)
                            self.add("Bonheur", 0, 15)
                            self.add("Criminalite", 10, 0)
                        #JETER PAR DESSU BORD
                        elif self.choicetaken == "4":
                            self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/100))
                            self.add("Influence", 0, 20)
                            self.add("Bonheur", 0, 35)
                            self.add("Criminalite", 15, 0)

#           SI LE BATEAU EST ENCORE HABITE
            else:
                # FINALEMENT DECIDER DE NE PAS LUI PARLER
                if self.choicetaken=="1" and  self.verifyepidemie(94)==True:
                    self.Recontagion(display)
                    #CHANCES FAIBLE DE CONTAGION

                    if self.choicetaken == "1":
                        self.add( "Bonheur", 0, 5 )
                        self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/15))
                    elif self.choicetaken == "2":
                        self.add("Sante", 0, 10)
                        self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/30))
                    elif self.choicetaken =="3":
                        self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/7))
                        self.add("Sante",0,10)
                        self.add("Influence", 0, 20)
                        self.add("Bonheur", 0, 15)
                        self.add("Criminalite", 10, 0)
                    elif self.choicetaken == "4":
                        self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/100))
                        self.add("Influence", 0, 20)
                        self.add("Bonheur", 0, 35)
                        self.add("Criminalite", 15, 0)

#               LEUR PROPOSER DE VENIR AVEC VOUS
                if self.choicetaken=="2":
                    self.add("Petrole", 700, 0)
                    self.add("Influence", 0, 5)
                    self.add("Bonheur", 20, 0)
                    self.add("Criminalite", 15, 0)
                    self.add("Metaux", 300, 0)
                    self.add("Pierre", 400, 0)
                    self.add("Nourriture", 600, 0)
                    self.add("Population", 80, 0)
                    if self.verifyepidemie(20)==True :
                        # POSSIBILITE DE CONTAGION
                        self.Recontagion(display)
                        if self.choicetaken == "1":
                            self.add( "Bonheur", 0, 5 )
                            self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/15))
                        elif self.choicetaken == "2":
                            self.add("Sante", 0, 10)
                            self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/30))
                        elif self.choicetaken =="3":
                            self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/7))
                            self.add("Sante",0,10)
                            self.add("Influence", 0, 20)
                            self.add("Bonheur", 0, 15)
                            self.add("Criminalite", 10, 0)
                        elif self.choicetaken == "4":
                            self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/100))
                            self.add("Influence", 0, 20)
                            self.add("Bonheur", 0, 35)
                            self.add("Criminalite", 15, 0)

#               DECIDER DE LES PREVENIR QUE LE CANADA N'EST PLUS UNE BONNE DESTINATION MAIS S'EN QU'ILS VIENNENT AVEC LE JOUEUR
                if self.choicetaken=="3" and  self.verifyepidemie(45)==True:
                    self.Recontagion(display)
                    if self.choicetaken == "1":
                        self.add( "Bonheur", 0, 5 )
                        self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/15))
                    elif self.choicetaken == "2":
                        self.add("Sante", 0, 10)
                        self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/30))
                    elif self.choicetaken =="3":
                        self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/7))
                        self.add("Sante",0,10)
                        self.add("Influence", 0, 20)
                        self.add("Bonheur", 0, 15)
                        self.add("Criminalite", 10, 0)
                    elif self.choicetaken == "4":
                        self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/100))
                        self.add("Influence", 0, 20)
                        self.add("Bonheur", 0, 35)
                        self.add("Criminalite", 15, 0)

#               LES LAISSER ALLER AU CANADA... CONTAGION, EN VENGEANCE/KARMA
                if self.choicetaken=="4":
                    self.Recontagion(display)
                    if self.choicetaken == "1":
                        self.add( "Bonheur", 0, 5 )
                        self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/15))
                    elif self.choicetaken == "2":
                        self.add("Sante", 0, 10)
                        self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/30))
                    elif self.choicetaken =="3":
                        self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/7))
                        self.add("Sante",0,10)
                        self.add("Influence", 0, 20)
                        self.add("Bonheur", 0, 15)
                        self.add("Criminalite", 10, 0)
                    elif self.choicetaken == "4":
                        self.add("Population", 0, (Story.StoryEffects.Effects ["Population"]/100))
                        self.add("Influence", 0, 20)
                        self.add("Bonheur", 0, 35)
                        self.add("Criminalite", 15, 0)



#       CHOIX N'EXISTANT PAS EN PRINCIPE, ET NE DEVANT AVOIR AUCUN EFFET
#         elif self.choicetaken =="3":
#               self.PorteAvions(display)
#         elif self.choicetaken == "4":
#               self.PorteAvions(display)

#       L'ARRIVEE A MAN'ANA'TOURA

        self.Arrivee(display, 2000)

    def add(self, variableamodifier, modificateurPOSITIF, modificateurNEGATIF):
        Story.StoryEffects.Effects [variableamodifier] = Story.StoryEffects.Effects [variableamodifier] + modificateurPOSITIF - modificateurNEGATIF

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
        pygame.time.wait(temps)




        displ.fill(COLORS.BLACK)
        self.Backround(displ)
        Story.Story(Story.Texte.texte6 , 0 , 0, 850,   displ)
     #   pygame.display.flip()
        pygame.time.wait(temps)


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

#Intropart2



#Intropart3
        #
        #     self.Backround(displ)
        #     displ.blit(ISaveTheWorld_interface,[41,34])
        #     pygame.display.flip()
        #     Story.Story(Story.Texte.iTexte1part3,475,50, 809,displ,467, 24 )





        # self.Backround(displ)
        # displ.blit(ISaveTheWorld_interface,[41,34])
        # pygame.display.flip()
        # Story.Story(Story.Texte.iTexteALTRUISME,475,50, 809,displ,467, 22 )
        # pygame.time.wait(1000)
        #
        # self.Backround(displ)
        # displ.blit(ISaveTheWorld_interface,[41,34])
        # pygame.display.flip()
        # Story.Story(Story.Texte.iTexteAUDACE,475,50, 809,displ,467, 22 )
        # pygame.time.wait(1000)
        #
        # self.Backround(displ)
        # displ.blit(ISaveTheWorld_interface,[41,34])
        # pygame.display.flip()
        # Story.Story(Story.Texte.iTexteARGENT,475,50, 809,displ,467, 22 )
        # pygame.time.wait(1000)
        #
        # self.Backround(displ)
        # displ.blit(ISaveTheWorld_interface,[41,34])
        # pygame.display.flip()
        # Story.Story(Story.Texte.iTexteBONHEUR,475,50, 809,displ,467, 22 )
        # pygame.time.wait(1000)
        #
        # self.Backround(displ)
        # displ.blit(ISaveTheWorld_interface,[41,34])
        # pygame.display.flip()
        # Story.Story(Story.Texte.iTexteEQUITE,475,50, 809,displ,467, 22 )
        # pygame.time.wait(1000)
        #
        # self.Backround(displ)
        # displ.blit(ISaveTheWorld_interface,[41,34])
        # pygame.display.flip()
        # Story.Story(Story.Texte.iTexteGALANTERIE,475,50, 809,displ,467, 22 )
        # pygame.time.wait(1000)
        #
        # self.Backround(displ)
        # displ.blit(ISaveTheWorld_interface,[41,34])
        # pygame.display.flip()
        # Story.Story(Story.Texte.iTexteINDUSTRIE,475,50, 809,displ,467, 22 )
        # pygame.time.wait(1000)
        #
        # self.Backround(displ)
        # displ.blit(ISaveTheWorld_interface,[41,34])
        # pygame.display.flip()
        # Story.Story(Story.Texte.iTexteORDRE,475,50, 809,displ,467, 22 )
        # pygame.time.wait(1000)
        #
        # self.Backround(displ)
        # displ.blit(ISaveTheWorld_interface,[41,34])
        # pygame.display.flip()
        # Story.Story(Story.Texte.iTexteSANTE,475,50, 809,displ,467, 22 )
        # pygame.time.wait(1000)


    def depart(self,displ, temps):
        #Posi=Story.position(displ)

        displ.fill(COLORS.BLACK)
        self.Backround(displ)
        Story.Story(Story.Texte.texte7 , 0 , 0, 900,  displ)
    #    pygame.display.flip()
    #    pygame.time.wait(temps)

        displ.fill(COLORS.BLACK)
        self.Backround(displ)
        Story.Story(Story.Texte.texte8 , 0 , 0, 900,  displ)
     #   pygame.display.flip()
      #  pygame.time.wait(temps)

        displ.fill(COLORS.BLACK)
        self.Backround(displ)
        Story.Story(Story.Texte.texte9 , 0 , 0, 900,  displ)
     #   pygame.display.flip()
      #  pygame.time.wait(temps)

    def epidemie(self,displ):
       # Posi=Story.position(displ)

        displ.fill(COLORS.BLACK)
        self.Backround(displ)
        Story.Story(Story.Texte.texte10 , 0 , 0, 900,  displ)


        Story.Story(Story.Texte.choix10a , 0 , 0, 900,  displ)

        Story.Story(Story.Texte.choix10b , 0 , 0, 900,  displ)

        Story.Story(Story.Texte.choix10c , 0 , 0, 900,  displ)

        Story.Story(Story.Texte.choix10d , 0 , 0, 900,  displ)
      #  pygame.display.flip()



        Story.Verificationtouche()



    def Famine(self, displ):
      #  Posi=Story.position(displ)

        displ.fill(COLORS.BLACK)
        self.Backround(displ)
        Story.Story(Story.Texte.texte11 , 0 , 0, 900,  displ)


        Story.Story(Story.Texte.choix11a , 0 , 0, 900,  displ)

        Story.Story(Story.Texte.choix11b , 0 , 0, 900,  displ)

        Story.Story(Story.Texte.choix11c , 0 , 0, 900,  displ)

        Story.Story(Story.Texte.choix11d , 0 , 0, 900,  displ)
      #  pygame.display.flip()




        Story.Verificationtouche()


    def PorteAvions(self, displ):
       # Posi=Story.position(displ)

        displ.fill(COLORS.BLACK)
        self.Backround(displ)
        Story.Story(Story.Texte.texte12 , 0 , 0, 900,  displ)


        Story.Story(Story.Texte.choix12a , 0 , 0, 900,  displ)

        Story.Story(Story.Texte.choix12b , 0 , 0, 900,  displ)
      #  pygame.display.flip()


        Story.Verificationtouche()


    def Rencontre(self, displ):
        a =FacteurHasard(40)

        if  a== True:
            self.path = "vide"
           # Posi=Story.position(displ)

            displ.fill(COLORS.BLACK)
            self.Backround(displ)
            Story.Story(Story.Texte.texte13 , 0 , 0, 900,  displ)


            Story.Story(Story.Texte.choix13a ,0 , 0, 900,  displ)


            Story.Story(Story.Texte.choix13b , 0 , 0, 900,  displ)
         #   pygame.display.flip()




            Story.Verificationtouche()

        elif a == False:
             self.path = "plein"
           #  Posi=Story.position(displ)

             displ.fill(COLORS.BLACK)
             self.Backround(displ)
             Story.Story(Story.Texte.texte14 , 0 , 0, 900,  displ)


             Story.Story(Story.Texte.choix14a , 0 , 0, 900,  displ)

             Story.Story(Story.Texte.choix14b , 0 , 0, 900,  displ)

             Story.Story(Story.Texte.choix14c , 0 , 0, 900,  displ)

             Story.Story(Story.Texte.choix14d , 0 , 0, 900,  displ)
           #  pygame.display.flip()

             Story.Verificationtouche()



    def Recontagion(self, displ):
      #  Posi=Story.position(displ)

        displ.fill(COLORS.BLACK)
        self.Backround(displ)
        Story.Story(Story.Texte.texte15 ,0 , 0, 900,   displ)


        Story.Story(Story.Texte.choix10a , 0 , 0, 900,  displ)

        Story.Story(Story.Texte.choix10b , 0 , 0, 900,  displ)

        Story.Story(Story.Texte.choix10c , 0 , 0, 900,  displ)

        Story.Story(Story.Texte.choix10d ,0 , 0, 940,  displ)
     #   pygame.display.flip()

        Story.Verificationtouche()



    def Arrivee(self, displ, temps):
     #  Posi=Story.position(displ)
        displ.fill(COLORS.BLACK)
        self.Backround(displ)
        Story.Story(Story.Texte.texte16 ,0 , 0, 900,  displ)
     #   pygame.display.flip()
     #   pygame.time.wait(temps)


    def verifyFamine(self):
        a =  Story.StoryEffects.Effects ["UNVP"] * 7
        if a > Story.StoryEffects.Effects ["Nourriture"]:
            return True
        else:
            return False

    def verifyepidemie(self, mods):
        a = Story.StoryEffects.Effects ["Sante"] + mods
        b = random.randrange (100)
        if a <  b:
            return True
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
                                Story.Story(Story.Texte.iTexteAUDACE,475,50, 809,displ,467, 22 )


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
                                Story.Story(Story.Texte.iTexteBONHEUR,475,50, 809,displ,467, 22 )


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
                                Story.Story(Story.Texte.iTexteGALANTERIE,475,50, 809,displ,467, 22 )


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
                                Story.Story(Story.Texte.iTexteAUDACE,475,50, 809,displ,467, 22 )



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
                                Story.Story(Story.Texte.iTexteBONHEUR,475,50, 809,displ,467, 22 )



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
                                Story.Story(Story.Texte.iTexteGALANTERIE,475,50, 809,displ,467, 22 )


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


    def set(self, setcible, valor ):
        Story.StoryEffects.Effects [setcible] = valor

    def ALTRUISME(self):
         self.set('Bois', 1200)
         self.set('Minerai', 200)
         self.set('Nourriture',1800)


         self.set('Criminalite', 38)
         self.set('Influence', 75)
         self.set('Education', 75)
         self.set('Sante', 75)
         self.set('Bonheur', 75)
         for i in Story.StoryEffects.Effects:
             J = Story.StoryEffects.Effects [i]
             print(J)


    def AUDACE(self):
        if FacteurHasard(50) == True:
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
        for i in Story.StoryEffects.Effects:
             J = Story.StoryEffects.Effects [i]
             print(J)

    def ARGENT(self):
        self.set('Bois', 1800)
        self.set('Minerai', 300)
        self.set('Nourriture',2700)
        self.set('Petrole',250)

        self.set('Education', 63)
        self.set('Influence', 25)
        self.set('Bonheur', 63)
        for i in Story.StoryEffects.Effects:
             J = Story.StoryEffects.Effects [i]
             print(J)
    def BONHEUR(self):
        self.set('Bois', 1200)
        self.set('Minerai', 200)
        self.set('Nourriture',1800)

        #centre multim/dia bonus batiment de depart

        self.set('Criminalite', 38)
        self.set('Influence', 63)
        self.set('Bonheur', 100)
        for i in Story.StoryEffects.Effects:
             J = Story.StoryEffects.Effects [i]
             print(J)

    def EQUITE(self):
        self.set('Bois', 1200)
        self.set('Minerai', 200)
        self.set('Nourriture',1800)

        self.set('Criminalite', 38)
        self.set('Influence', 75)
        self.set('Bonheur', 63)
        for i in Story.StoryEffects.Effects:
             J = Story.StoryEffects.Effects [i]
             print(J)
    def GALANTERIE(self):
        self.set('Bois', 1200)
        self.set('Minerai', 200)
        self.set('Nourriture',1800)

        self.set('Population', 3500)

        self.set('Criminalite', 25)
        self.set('Influence', 75)
        self.set('Bonheur', 63)
        self.set('Education', 83)
        for i in Story.StoryEffects.Effects:
             J = Story.StoryEffects.Effects [i]
             print(J)

    def INDUSTRIE(self):
        self.set('Bois', 900)
        self.set('Minerai', 150)
        self.set('Nourriture',1350)
        self.set('Petrole',75)
        # + un batiment special de production, efficace mais polluant

        self.set('Population', 2500)

        self.set('Education', 75)
        self.set('Bonheur', 38)
        for i in Story.StoryEffects.Effects:
             J = Story.StoryEffects.Effects [i]
             print(J)

    def ORDRE(self):
        self.set('Bois', 1200)
        self.set('Minerai', 200)
        self.set('Nourriture',1800)

        self.set('Criminalite', 0)
        self.set('Influence', 100)
        self.set('Education', 25)
        self.set('Sante', 63)
        for i in Story.StoryEffects.Effects:
             J = Story.StoryEffects.Effects [i]
             print(J)

    def SANTE(self):
        self.set('Bois', 1200)
        self.set('Minerai', 200)
        self.set('Nourriture',1800)

        self.set('Education', 63)
        self.set('Sante', 100)
        for i in Story.StoryEffects.Effects:
             J = Story.StoryEffects.Effects [i]
             print(J)

class CheckingCheck():
        checked = False
        pcheckmark_image = pygame.image.load("image/ISaveTheWorld/green_checkmark.png")

        pcheckmark_image.set_colorkey((255,255,255))

        checkmark_image = pcheckmark_image
        checkedproposition = ''
        checkedOne =  checkedproposition
        LastCheck =''

        coordinate = [0,0]
        def __init__(self, displ):
            self.checkedOne =  self.checkedproposition


            if self.checkedOne == 'Altruisme':
                self.coordinate = [84,76]

            if self.checkedOne == 'Audace':
                self.coordinate = [84,142]

            if self.checkedOne == 'Argent':
                self.coordinate = [84,208]

            if self.checkedOne == 'Bonheur':
                self.coordinate = [84,275,]

            if self.checkedOne == 'Equite':
                self.coordinate = [84,341]

            if self.checkedOne == 'Galanterie':
                self.coordinate = [84,408]

            if self.checkedOne == 'Industrie':
                self.coordinate = [84,471]

            if self.checkedOne == 'Ordre':
                self.coordinate = [84,538]

            if self.checkedOne == 'Sante':
                self.coordinate = [84,597]


            if self.checkedOne != self.LastCheck:
                displ.blit(self.checkmark_image,self.coordinate)


            self.checkedOne = self.LastCheck






