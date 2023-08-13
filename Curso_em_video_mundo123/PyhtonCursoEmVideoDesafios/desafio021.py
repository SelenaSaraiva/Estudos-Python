# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.init()
pygame.mixer.music.load('Nome do meu arquivo')
pygame.mixer.music.play()
pygame.evnt.wait()
