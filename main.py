import pygame
from os import system
import time
from assets import *
from logics import *
FoNt = 0
FoNtprint = 0
MIN_SIZE = (120, 80)#px
# MAX_SIZE = (1920, 1080)#px 1009
prevScreen_res = (1200, 800)
screen_res = [1200, 800]
cell_side = (min(screen_res))*(3/32)
discsOnBoard = [(3,3), (3,4), (4,3), (4,4)]
Disc = [pygame.transform.scale(DISC[0], (cell_side*9/10, cell_side*9/10)),
        pygame.transform.scale(DISC[1], (cell_side*9/10, cell_side*9/10))]
Color = [(255, 255, 255), (0, 0, 0)]
TURN = 1
WINDOW = "PvP"
board.__init__(board)
def cls():
    system("cls")
def font(a:str,b=18):
    global FoNt
    FoNt = pygame.font.SysFont(a,b)
def printpy(x:str,a=(100,400),y=(128,128,128)):
    global FoNt,FoNtprint
    FoNtprint = FoNt.render(x,True,y)
    screen.blit(FoNtprint,a)

def drawBoard():
    global cell_side, screen_res, discsOnBoard, Disc, prevScreen_res, Color
    if prevScreen_res != screen_res:
        prevScreen_res = list(screen_res)
        cell_side = (min(screen_res))*(3/32)
        # Disc = [pygame.transform.scale(DISC[0], (cell_side*9/10, cell_side*9/10)),
        #         pygame.transform.scale(DISC[1], (cell_side*9/10, cell_side*9/10))]

    pr = (min(screen_res))*(7/16)*(2**0.5) #pattern radius
    for l in range(int(pr/28), int(pr), int(pr/28)):
        b = (pr*pr - l*l)**0.5
        b = ((b//(pr/14))+1)*(pr/14)
        rectAngle = pygame.Surface((l*2,b*2))
        rectAngle1 = pygame.Surface((b*2,l*2))
        rectAngle.fill((0, 0, 0))
        rectAngle1.fill((0, 0, 0))
        rectAngle.set_alpha(50)
        rectAngle1.set_alpha(50)
        screen.blit(rectAngle, (screen_res[0]/2-l, screen_res[1]/2-b))
        screen.blit(rectAngle1, (screen_res[0]/2-b, screen_res[1]/2-l))
        for x in range(8):
            for y in range(8):
                pygame.draw.rect(screen, (46, 174, 82), pygame.Rect(screen_res[0]/2-cell_side*(4-x), screen_res[1]/2-cell_side*(4-y), cell_side, cell_side))
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(screen_res[0]/2-cell_side*(4-x), screen_res[1]/2-cell_side*(4-y), cell_side, cell_side), 1)
    for disc in discsOnBoard:
        # screen.blit(Disc[board.colour(board.currentBoard[disc[0]][disc[1]])], (screen_res[0]/2 + (disc[0]-4)*cell_side + cell_side/20, screen_res[1]/2 + (disc[1]-4)*cell_side + cell_side/20))
        pygame.draw.circle(screen, Color[board.colour(board.currentBoard[disc[0]][disc[1]])], (screen_res[0]/2 + (disc[0]-4)*cell_side + cell_side/2, screen_res[1]/2 + (disc[1]-4)*cell_side + cell_side/2), cell_side*9/20)
if __name__ == '__main__':
    frameRate = 1000
    dt = 1/1000
    pygame.init()
    screen = pygame.display.set_mode((1200, 800), pygame.RESIZABLE)
    icon = pygame.image.load('assets/images/icon.jpg')
    pygame.display.set_caption("Othello / Reversi")
    pygame.display.set_icon(icon)
    cls()
    running = True
    clock = pygame.time.Clock()
    while running == True:
        initTime = time.time()
        clock.tick(frameRate)
        screen_res = list(screen.get_size())
        tempScreen_res = list(screen_res)
        screen_res[0] = MIN_SIZE[0] if screen_res[0] < MIN_SIZE[0] else screen_res[0]
        screen_res[1] = MIN_SIZE[1] if screen_res[1] < MIN_SIZE[1] else screen_res[1]
        if tempScreen_res != screen_res:
            screen = pygame.display.set_mode(screen_res, pygame.RESIZABLE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mspos = pygame.mouse.get_pos()
                if WINDOW == "PvP":
                    if (screen_res[0]/2 - cell_side*4 < mspos[0] < screen_res[0]/2 + cell_side*4) and (screen_res[1]/2 - cell_side*4 < mspos[1] < screen_res[1]/2 + cell_side*4):
                        boardMpos = [mspos[0] - screen_res[0]/2 + cell_side*4, mspos[1] - screen_res[1]/2 + cell_side*4]
                        cellClicked = [int(boardMpos[0]//cell_side), int(boardMpos[1]//cell_side)]
                        if board.isLegalMove(board, cellClicked, board.player[TURN]):
                            board.currentBoard[cellClicked[0]][cellClicked[1]] = board.player[TURN]
                            board.makeMove(board, cellClicked, board.player[TURN])
                            discsOnBoard.append(cellClicked)
                            TURN = (TURN+1)%2
                            # print(board.allLegalMoves(board, board.player[TURN]), board.allLegalMoves(board, board.player[(TURN+1)%2]))
                            # if len(board.allLegalMoves(board, board.player[TURN])) == 0:
                            #     TURN = (TURN+1)%2
                        
        #Code Here
        # (46, 174, 82) RGB of green board
        screen.fill((255, 255, 255))
        drawBoard()
        pygame.display.update()

        endTime = time.time()
        dt = endTime-initTime
        if dt != 0:
            frameRate = 1/dt
        else:
            frameRate = 1000
