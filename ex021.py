# Desafio: Faça um programa que abra e reproduza um áudio em mp3.
import pygame
pygame.init() #mesmo com o comando import é necessário chamar o pygame aqui também
pygame.mixer.music.load('steven-abertura.mp3')
pygame.mixer.music.play()
input() #ação para iniciar a musica do código até aqui
pygame.event.wait()