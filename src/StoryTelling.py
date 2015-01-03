__author__ = 'Jean-Alexandre'
import Story
import random
import conda
import pygame
from defines import COLORS

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
        self.intro(display,2000)
        self.depart(display, 2000)
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


    def intro(self, displ, temps):
        #StartMusic('Choral december.ogg')
        Posi=Story.position(displ)
        displ.fill(COLORS.BLACK)
        Story.Story(Story.Texte.texte1 , Posi.topleft, displ)
        pygame.display.flip()
        pygame.time.wait(temps)


        displ.fill(COLORS.BLACK)
        Story.Story(Story.Texte.texte2 , Posi.topleft,  displ)
        pygame.display.flip()
        pygame.time.wait(temps)


        displ.fill(COLORS.BLACK)
        Story.Story(Story.Texte.texte3 , Posi.topleft,   displ)
        pygame.display.flip()
        pygame.time.wait(temps)


        displ.fill(COLORS.BLACK)
        Story.Story(Story.Texte.texte4 , Posi.topleft,   displ)
        pygame.display.flip()
        pygame.time.wait(temps)


        displ.fill(COLORS.BLACK)
        Story.Story(Story.Texte.texte5 , Posi.topleft,   displ)
        pygame.display.flip()
        pygame.time.wait(temps)

        displ.fill(COLORS.BLACK)
        Story.Story(Story.Texte.texte6 , Posi.topleft,   displ)
        pygame.display.flip()
        pygame.time.wait(temps)

    def depart(self,displ, temps):
        Posi=Story.position(displ)

        displ.fill(COLORS.BLACK)
        Story.Story(Story.Texte.texte7 , Posi.topleft,  displ)
        pygame.display.flip()
        pygame.time.wait(temps)

        displ.fill(COLORS.BLACK)
        Story.Story(Story.Texte.texte8 , Posi.center,  displ)
        pygame.display.flip()
        pygame.time.wait(temps)

        displ.fill(COLORS.BLACK)
        Story.Story(Story.Texte.texte9 , Posi.topleft,  displ)
        pygame.display.flip()
        pygame.time.wait(temps)

    def epidemie(self,displ):
        Posi=Story.position(displ)

        displ.fill(COLORS.BLACK)
        Story.Story(Story.Texte.texte10 , Posi.topleft,  displ)


        Story.Story(Story.Texte.choix10a , Posi.choixa,  displ)

        Story.Story(Story.Texte.choix10b , Posi.choixb,  displ)

        Story.Story(Story.Texte.choix10c , Posi.choixc,  displ)

        Story.Story(Story.Texte.choix10d , Posi.choixd,  displ)
        pygame.display.flip()



        Story.Verificationtouche()



    def Famine(self, displ):
        Posi=Story.position(displ)

        displ.fill(COLORS.BLACK)
        Story.Story(Story.Texte.texte11 , Posi.topleft,  displ)


        Story.Story(Story.Texte.choix11a , Posi.choixa,  displ)

        Story.Story(Story.Texte.choix11b , Posi.choixb,  displ)

        Story.Story(Story.Texte.choix11c , Posi.choixc,  displ)

        Story.Story(Story.Texte.choix11d , Posi.choixd,  displ)
        pygame.display.flip()




        Story.Verificationtouche()


    def PorteAvions(self, displ):
        Posi=Story.position(displ)

        displ.fill(COLORS.BLACK)
        Story.Story(Story.Texte.texte12 , Posi.topleft,  displ)


        Story.Story(Story.Texte.choix12a , Posi.choixa,  displ)

        Story.Story(Story.Texte.choix12b , Posi.choixb,  displ)
        pygame.display.flip()


        Story.Verificationtouche()


    def Rencontre(self, displ):
        a =FacteurHasard(40)

        if  a== True:
            self.path = "vide"
            Posi=Story.position(displ)

            displ.fill(COLORS.BLACK)
            Story.Story(Story.Texte.texte13 , Posi.topleft,  displ)


            Story.Story(Story.Texte.choix13a , Posi.choixa,  displ)


            Story.Story(Story.Texte.choix13b , Posi.choixb,  displ)
            pygame.display.flip()




            Story.Verificationtouche()

        elif a == False:
             self.path = "plein"
             Posi=Story.position(displ)

             displ.fill(COLORS.BLACK)
             Story.Story(Story.Texte.texte14 , Posi.topleft,  displ)


             Story.Story(Story.Texte.choix14a , Posi.choixa,  displ)

             Story.Story(Story.Texte.choix14b , Posi.choixb,  displ)

             Story.Story(Story.Texte.choix14c , Posi.choixc,  displ)

             Story.Story(Story.Texte.choix14d , Posi.choixd,  displ)
             pygame.display.flip()

             Story.Verificationtouche()



    def Recontagion(self, displ):
        Posi=Story.position(displ)

        displ.fill(COLORS.BLACK)
        Story.Story(Story.Texte.texte15 , Posi.topleft,  displ)


        Story.Story(Story.Texte.choix10a , Posi.choixa,  displ)

        Story.Story(Story.Texte.choix10b , Posi.choixb,  displ)

        Story.Story(Story.Texte.choix10c , Posi.choixc,  displ)

        Story.Story(Story.Texte.choix10d , Posi.choixd,  displ)
        pygame.display.flip()

        Story.Verificationtouche()



    def Arrivee(selfself, displ, temps):
        Posi=Story.position(displ)
        displ.fill(COLORS.BLACK)
        Story.Story(Story.Texte.texte16 , Posi.topleft,  displ)
        pygame.display.flip()
        pygame.time.wait(temps)


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




