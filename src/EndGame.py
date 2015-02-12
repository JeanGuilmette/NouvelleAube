__author__ = 'SJS'
import Island
import pygame
from Defines import COLORS

import math
import EventAdvancement

class Writer (): # envoyer cette classe dans choix, pour n<avoir a appeler qu<une seule classe lors de Storytelling

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
            pygame.display.flip()
            pygame.time.delay(delay)
            m = i
class ClicWait():

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
class EndGame():

    def __init__(self, display, island):
        self.island = island
        self.Rapport_final=pygame.image.load("image/RapportFinal.png").convert_alpha()
        self.bgImage = pygame.image.load("image/Nouvelle_Aube.jpg")
        self.blackImage = pygame.image.load("image/BlackBack.png")
        self.FuturHumanite=pygame.image.load("image/FuturHumanite.png").convert_alpha()


        displ = display

        self.fonduNoir(displ)
        if EventAdvancement.TrueEnding == True:
            self.Backround(displ)
            self.LinkMessage(displ)
            ClicWait(displ,[400,600],'clic')



            runner=True
            x=0
            y=691
            while runner == True:
                if x <939:
                    x=int(x+(930/30))
                    self.Backround(displ)
                    t =pygame.transform.smoothscale(self.Rapport_final,(x,y))
                    displ.blit(t,[41,34])
                    pygame.display.flip()
                    pygame.time.wait(2)
                else :
                    runner = False

            self.Backround(displ)
            displ.blit(self.Rapport_final,[41,34])



            Writer("Valeurs à la base de votre société:" , 107 , 150, 750,  displ)
            Writer( EventAdvancement.PremiereValeur+ " et " +EventAdvancement.DeuxiemeValeur, 107 , 185, 750,  displ)

            Writer( "Données démographiques:", 107 , 250, 750,  displ)
            Writer( "Bonheur:", 107 , 290, 750,  displ)
            Writer( "Influence:", 107 , 315, 750,  displ)
            Writer( "Santé:", 107 , 340, 750,  displ)
            Writer( "Éducation:" , 107 , 365, 750,  displ)
            Writer( "Criminalité:" , 107 , 390, 750,  displ)
            Writer( "Population:" , 107 , 415, 750,  displ)
            Writer( "Pollution:" , 107 , 440, 750,  displ)
            Writer( "Panique:" , 107 , 465, 750,  displ)

            Writer( EventAdvancement.Ending_Bonheur, 307 , 290, 750,  displ)
            Writer( EventAdvancement.Ending_Influence, 307 , 315, 750,  displ)
            Writer( EventAdvancement.Ending_Sante, 307 , 340, 750,  displ)
            Writer( EventAdvancement.Ending_Education, 307 , 365, 750,  displ)
            Writer( EventAdvancement.Ending_Criminalite, 307 , 390, 750,  displ)
           # self.Ressources_depart.Effects['Population']=math.floor(self.Ressources_depart.Effects['Population'])
            Writer( EventAdvancement.Ending_Population, 307 , 415, 750,  displ)
            Writer( EventAdvancement.Ending_Pollution, 307 , 440, 750,  displ)
            Writer( EventAdvancement.Ending_Panique, 307 , 465, 750,  displ)


            ClicWait(displ,[400,600],'clic')
            self.Backround(displ)
            running = True
            x=931
            y=691
            while running == True:
                if x > 2:
                    x=int(x-(930/30))
                    self.Backround(displ)
                    t =pygame.transform.smoothscale(self.Rapport_final,(x,y))
                    displ.blit(t,[41,34])
                    pygame.display.flip()
                    pygame.time.wait(2)
                else :
                    running = False
            self.Backround(displ)


            if EventAdvancement.HappyEnd == True:

                runner=True
                x=0
                y=691
                while runner == True:
                    if x <939:
                        x=int(x+(930/30))
                        self.Backround(displ)
                        t =pygame.transform.smoothscale(self.FuturHumanite,(x,y))
                        displ.blit(t,[41,34])
                        pygame.display.flip()
                        pygame.time.wait(2)
                    else :
                        runner = False

                self.Backround(displ)
                displ.blit(self.FuturHumanite,[41,34])
                Writer(EventAdvancement.The_EndingText , 75 , 100, 750,  displ)
                ClicWait(displ,[400,600],'clic')

                self.Backround(displ)

                running = True
                x=931
                y=691
                while running == True:
                    if x > 2:
                        x=int(x-(930/30))
                        self.Backround(displ)
                        t =pygame.transform.smoothscale(self.FuturHumanite,(x,y))
                        displ.blit(t,[41,34])
                        pygame.display.flip()
                        pygame.time.wait(2)
                    else :
                        running = False
                self.Backround(displ)

        else:
            Writer( "Vous abandonnez déjà!?! Dommage...", 240 , 300, 750,  displ)
            pygame.time.wait(1000)

    def Backround(self, displ):
        backround = pygame.image.load("image/Nouvelle_Aube.jpg").convert()
        displ.blit(backround,[0,0])
    def fonduNoir(self, display):
        disply = display

        for x in range(0,105):
            self.blackImage.set_alpha(x)

            disply.blit(self.blackImage,[0,0])
            pygame.display.flip()
            pygame.time.wait(1)
        for x in range(0,55):
            self.bgImage.set_alpha(x)
            disply.blit(self.bgImage,[0,0])
            pygame.display.flip()
            pygame.time.wait(1)


    def LinkMessage(self,displ):
        Writer(EventAdvancement.Linkmessage , 10 , 10, 750,  displ)






    # def __init__(self, display, score):
    #     self.menuSurface =  display
    #     self.scr_width = self.menuSurface.get_rect().width
    #     self.scr_height = self.menuSurface.get_rect().height
    #
    #     self.bgColor = COLORS.BLACK
    #     self.clock = pygame.time.Clock()
    #
    #     self.bgImage = pygame.image.load("image/Nouvelle_Aube.jpg")
    #
    #     self.font = pygame.font.SysFont(None, 30)
    #
    #     self.score = score
    #     self.showScreen()
    #
    #
    # def drawPressKeyMsg(self):
    #     pressKeySurf =  self.font.render('Press a key to exit.', True, COLORS.YELLOW)
    #     pressKeyRect = pressKeySurf.get_rect()
    #     pressKeyRect.topleft = ( self.scr_width - 200,  self.scr_height - 30)
    #     self.menuSurface.blit(pressKeySurf, pressKeyRect)
    #
    #
    # def checkForKeyPress(self):
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYUP:
    #             return "quit"
    #     return "none"
    #
    #
    # def showScreen(self):
    #     titleFont = pygame.font.Font('freesansbold.ttf', 100)
    #     titleSurf1 = titleFont.render('Game Over!', True, COLORS.DARKGRAY)
    #     resString = ("Your Score: %d" % (self.score))
    #     scoreSurf = titleFont.render(resString, True, COLORS.BLACK)
    #
    #     centerX = (self.menuSurface.get_rect().width/2) - (scoreSurf.get_rect().width/2)
    #     centerY = (self.menuSurface.get_rect().height/2) - (scoreSurf.get_rect().height/2)
    #     posX = 50
    #     posY = 50
    #     dirY = -1
    #     dirX = 1
    #     while True:
    #         self.menuSurface.blit(self.bgImage, [0,0])
    #         self.menuSurface.blit(titleSurf1, ( posX, posY) )
    #         self.menuSurface.blit(scoreSurf, (centerX, centerY))
    #
    #         self.drawPressKeyMsg()
    #
    #         if self.checkForKeyPress().lower() == "quit":
    #             pygame.event.get() # clear event queue
    #             self.menuSurface.fill(self.bgColor) # Redraw the background
    #             return
    #
    #         pygame.display.update()
    #         self.clock.tick(60)
    #
    #         expX = posX + dirX + titleSurf1.get_rect().width
    #         expY = posY + dirY + titleSurf1.get_rect().height
    #         dirX =  dirX if( ( expX < self.scr_width) and (posX + dirX > 0)) else -dirX
    #         posX += dirX
    #         dirY =  dirY if( ( expY < self.scr_height) and (posY + dirY > 0)) else -dirY
    #         posY += dirY
    #
    #
    #