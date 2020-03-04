import pygame

pygame.init()

pygame.mixer.music.load("/home/fernando/Música/voracity.mp3")
pygame.mixer.music.play()
pygame.event.wait()