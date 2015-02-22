__author__ = 'Jean-Alexandre'
import pygame
import EventAdvancement





pygame.mixer.init()
def StartMusic(music, volume= 0.3):# Stop  before call again some music
    pygame.mixer.music.stop()

    pygame.mixer.music.load(music)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(1000)


def StopMusic():
    pygame.mixer.music.stop()
def PauseMusic():
    pygame.mixer.music.pause()
def unpauseMusic():
    pygame.mixer.music.unpause()
def fadeoutMusic ():
    pygame.mixer.music.fadeout()

# class Sound():
#     #Placer TOUT les sons et les lier comme objets
    #
def PlaySound(sound, volume=0.4):
    sound.set_volume(volume)
    sound.play()


def StopSound():#Affect ALL sound
    pygame.mixer.stop()

def fadeoutSound (): #Affect ALL sound
    pygame.mixer.fadeout()