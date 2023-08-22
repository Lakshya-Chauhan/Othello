import pygame
from os import system
FoNt = 0
FoNtprint = 0
def cls():
    system("cls")
def font(a:str,b=18):
    global FoNt
    FoNt = pygame.font.SysFont(a,b)
def printpy(x:str,a=(100,400),y=(128,128,128)):
    global FoNt,FoNtprint
    FoNtprint = FoNt.render(x,True,y)
    screen.blit(FoNtprint,a)
pygame.init()
screen = pygame.display.set_mode((800,800))
icon = pygame.image.load('assets/images/icon.jpg')
pygame.display.set_caption("Othello / Reversi")
pygame.display.set_icon(icon)
cls()
running = True
clock = pygame.time.Clock()
while running == True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Code Here
    # (46, 174, 82) RGB of green board
    pygame.display.update()