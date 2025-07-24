from time import sleep
import pygame
for cont in range(10, 0, -1):
    print(cont)
    sleep(0.5)
print('ACABOU!')
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('FOGOS.mp3')
pygame.mixer_music.play()
pygame.event.wait()
