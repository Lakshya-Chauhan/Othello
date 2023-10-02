import pygame
from os import system
import time
from assets import *
from logics import *
from random import random
FoNt = 0
FoNtprint = 0

# MAX_SIZE = (1920, 1080)#px 1009
MIN_SIZE = (120, 80)#px
prevScreen_res = (1200, 800)
screen_res = [1200, 800]
cell_side = (min(screen_res))*(3/32)
WINDOW = "homeScreen"
mcolor = [128, 128, 128]
mrad = (sum(screen_res))/30
bBack = pygame.transform.scale(boardBack, ((min(screen_res))*(7/16)*(2**0.5), (min(screen_res))*(7/16)*(2**0.5)))
lOthello = pygame.transform.scale(icon, (cell_side, cell_side))

gameOver = False
discsOnBoard = [(3,3), (3,4), (4,3), (4,4)]
rGame = pygame.transform.scale(restartGame, (cell_side*(2**0.5)*0.8/2, cell_side*(2**0.5)*0.8/2))
hScreen = pygame.transform.scale(homeScreen, (cell_side*(2**0.5)/2, cell_side*(2**0.5)/2))
Color = [(255, 255, 255), (0, 0, 0)]
TURN = 1
discCount = [2, 2]
def nearest(num, a, b):
    return a if abs(a - num) < abs(b - num) else b
board.__init__(board)
def cls():
    system("cls")
def font(face:str, size=18, Bold = False, Italic = False):
    global FoNt
    FoNt = pygame.font.SysFont(face,size,Bold,Italic)
def printpy(text:str,coords=(100,400),color=(128,128,128), center = False):
    global FoNt,FoNtprint
    FoNtprint = FoNt.render(text, True, color)
    if center == True:
        screen.blit(FoNtprint, [coords[0]-FoNtprint.get_width()/2, coords[1]-FoNtprint.get_height()/2])
    else:
        screen.blit(FoNtprint, coords)


def drawBoard():
    global cell_side, screen_res, discsOnBoard, prevScreen_res, Color, boardBack,bBack, OBJS, TURN, discCount, gameOver, hScreen, rGame
    pr = (min(screen_res))*(7/16)*(2**0.5) #pattern radius
    if prevScreen_res != screen_res:
        prevScreen_res = list(screen_res)
        cell_side = (min(screen_res))*(3/32)
        pr = (min(screen_res))*(7/16)*(2**0.5) #pattern radius
        bBack = pygame.transform.scale(boardBack, (pr*2.5*1.826087, pr*2.5))
        rGame = pygame.transform.scale(restartGame, (cell_side*(2**0.5)*0.8/2, cell_side*(2**0.5)*0.8/2))
        hScreen = pygame.transform.scale(homeScreen, (cell_side*(2**0.5)/2, cell_side*(2**0.5)/2))
        
        OBJS = list()
        for _ in range(int((sum(screen_res))/60)):
            OBJS.append( sphere([random()*screen_res[0], random()*screen_res[1]], random()*(sum(screen_res))/7.5, [(0.5-random())*8, (0.5-random())*8], _, [random()*256, random()*256, random()*256]) )

    screen.blit(bBack, ((screen_res[0]/2-(bBack.get_height())/2),(screen_res[1]/2-(bBack.get_height())/2)), ((bBack.get_width())/2-(bBack.get_height())/2, 0, bBack.get_height(), bBack.get_height()))
    for x in range(8):
        for y in range(8):
            pygame.draw.rect(screen, (46, 174, 82), pygame.Rect(screen_res[0]/2-cell_side*(4-x), screen_res[1]/2-cell_side*(4-y), cell_side, cell_side))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(screen_res[0]/2-cell_side*(4-x), screen_res[1]/2-cell_side*(4-y), cell_side, cell_side), 1)
    for disc in discsOnBoard:
    # screen.blit(Disc[board.colour(board.currentBoard[disc[0]][disc[1]])], (screen_res[0]/2 + (disc[0]-4)*cell_side + cell_side/20, screen_res[1]/2 + (disc[1]-4)*cell_side + cell_side/20))
        pygame.draw.circle(screen, Color[board.colour(board.currentBoard[disc[0]][disc[1]])], (screen_res[0]/2 + (disc[0]-4)*cell_side + cell_side/2, screen_res[1]/2 + (disc[1]-4)*cell_side + cell_side/2), cell_side*9/20)
    
    for c in board.allLegalMoves(board, board.player[TURN]):
        pygame.draw.circle(screen, [200, 200, 200] if TURN == 0 else [55, 55, 55], (screen_res[0]/2 + (c[0]-4)*cell_side + cell_side/2, screen_res[1]/2 + (c[1]-4)*cell_side + cell_side/2), cell_side*3/20)
        pygame.draw.circle(screen, [230, 230, 230] if TURN == 0 else [25, 25, 25], (screen_res[0]/2 + (c[0]-4)*cell_side + cell_side/2, screen_res[1]/2 + (c[1]-4)*cell_side + cell_side/2), cell_side/10)
    
    pygame.draw.circle(screen, [225, 225, 225], (screen_res[0]/2 -cell_side, screen_res[1]/2 - 4.6*cell_side), cell_side/2)
    pygame.draw.circle(screen, [195, 195, 195], (screen_res[0]/2 -cell_side, screen_res[1]/2 - 4.6*cell_side), cell_side/2, int(cell_side/12))
    pygame.draw.circle(screen, [30, 30, 30], (screen_res[0]/2 +cell_side, screen_res[1]/2 - 4.6*cell_side), cell_side/2)
    pygame.draw.circle(screen, [60, 60, 60], (screen_res[0]/2 +cell_side, screen_res[1]/2 - 4.6*cell_side), cell_side/2, int(cell_side/12))
    
    pygame.draw.circle(screen, [255, 220, 220], (screen_res[0]/2 +4.6*cell_side + cell_side*2/15, screen_res[1]/2 + cell_side + cell_side), cell_side/2)
    pygame.draw.circle(screen, [255, 180, 180], (screen_res[0]/2 +4.6*cell_side + cell_side*2/15, screen_res[1]/2 + cell_side + cell_side), cell_side/2, int(cell_side/12))
    screen.blit(hScreen, ((screen_res[0]/2 +4.6*cell_side + cell_side*2/15 - (hScreen.get_width())/2, screen_res[1]/2 + cell_side + cell_side - (hScreen.get_height())/2)))

    if gameOver == True:
        pygame.draw.circle(screen, [220, 220, 255], (screen_res[0]/2 +4.6*cell_side + cell_side*2/15, screen_res[1]/2 ), cell_side/2)
        pygame.draw.circle(screen, [180, 180, 255], (screen_res[0]/2 +4.6*cell_side + cell_side*2/15, screen_res[1]/2 ), cell_side/2, int(cell_side/12))
        screen.blit(rGame, ((screen_res[0]/2 +4.6*cell_side + cell_side*2/15 - (rGame.get_width())/2, screen_res[1]/2 - (rGame.get_height())/2)))

    font("calibri", int(cell_side*0.4), True)
    if discCount[0] > discCount[1]:
        printpy(str(discCount[0]), (screen_res[0]/2 -cell_side, screen_res[1]/2 - 4.6*cell_side), (64, 128, 64), True)
        printpy(str(discCount[1]), (screen_res[0]/2 +cell_side, screen_res[1]/2 - 4.6*cell_side), (128, 64, 64), True)
        if gameOver == True:
            font("Agency FB", int(cell_side*0.5), False)
            printpy("White Wins!", (screen_res[0]/2, screen_res[1]/2 + 4.9*cell_side), (128, 128, 128), True)

    elif discCount[0] < discCount[1]:
        printpy(str(discCount[0]), (screen_res[0]/2 -cell_side, screen_res[1]/2 - 4.6*cell_side), (128, 64, 64), True)
        printpy(str(discCount[1]), (screen_res[0]/2 +cell_side, screen_res[1]/2 - 4.6*cell_side), (64, 128, 64), True)
        if gameOver == True:
            font("Agency FB", int(cell_side*0.5), False)
            printpy("Black Wins!", (screen_res[0]/2, screen_res[1]/2 + 4.9*cell_side), (128, 128, 128), True)
    else:
        printpy(str(discCount[0]), (screen_res[0]/2 -cell_side, screen_res[1]/2 - 4.6*cell_side), (64, 64, 128), True)
        printpy(str(discCount[1]), (screen_res[0]/2 +cell_side, screen_res[1]/2 - 4.6*cell_side), (64, 64, 128), True)
        if gameOver == True:
            font("Agency FB", int(cell_side*0.5), False)
            printpy("Draw!!", (screen_res[0]/2, screen_res[1]/2 + 4.9*cell_side), (128, 128, 128), True)
    # font("agency fb", int(cell_side*0.4), True)
    # printpy(str(discCount[0]), (screen_res[0]/2 -cell_side, screen_res[1]/2 - 4.6*cell_side), (64, 128, 64), True)
    # printpy(str(discCount[1]), (screen_res[0]/2 +cell_side, screen_res[1]/2 - 4.6*cell_side), (64, 128, 64), True)
    if gameOver == True:
        font("Agency FB", int(cell_side*0.75), True)
        printpy("GAME OVER", (screen_res[0]/2, screen_res[1]/2 + 4.35*cell_side), (128, 128, 128), True)
        
def drawHomeScreen():
    global cell_side, screen_res, prevScreen_res, boardBack, bBack, OBJS, lOthello, mainOthelloText, WINDOW
    if prevScreen_res != screen_res:
        prevScreen_res = list(screen_res)
        cell_side = (min(screen_res))*(3/32)
        pr = (min(screen_res))*(7/16)*(2**0.5) #pattern radius
        bBack = pygame.transform.scale(boardBack, (pr*2.5*1.826087, pr*2.5))
        font("Bauhaus 93", int(cell_side*2))
        mainOthelloText = FoNt.render("Othello", True, (190, 255, 225))
        lOthello = pygame.transform.scale(icon, (cell_side*1.5, cell_side*1.5))
        OBJS = list()
        for _ in range(int((sum(screen_res))/60)):
            OBJS.append( sphere([random()*screen_res[0], random()*screen_res[1]], random()*(sum(screen_res))/7.5, [(0.5-random())*8, (0.5-random())*8], _, [random()*256, random()*256, random()*256]) )

    screen.blit(bBack, ((screen_res[0]/2-(bBack.get_height())/2),(screen_res[1]/2-(bBack.get_height())/2)), ((bBack.get_width())/2-(bBack.get_height())/2, 0, bBack.get_height(), bBack.get_height()))
    screen.blit(lOthello, (screen_res[0]/2-(cell_side*1.5)/2-(mainOthelloText.get_width())/2- cell_side/4, screen_res[1]/2 - 3*cell_side))
    screen.blit(mainOthelloText, (screen_res[0]/2+(cell_side*1.5)/2-(mainOthelloText.get_width())/2, screen_res[1]/2 -cell_side*0.4 - 3*cell_side))

    font("Arial Black", int(cell_side/2))
    if WINDOW == "homeScreen":
        mousePos = pygame.mouse.get_pos()
        cursorOn = None
        if (screen_res[0]/2-0.58*cell_side<mousePos[0]<screen_res[0]/2+0.58*cell_side) and (screen_res[1]/2 - 0.3533*cell_side < mousePos[1] < screen_res[1]/2 + 0.3533*cell_side):
            cursorOn = 0
        if (screen_res[0]/2-1.0467*cell_side<mousePos[0]<screen_res[0]/2+1.0467*cell_side) and (screen_res[1]/2 + 0.6467*cell_side < mousePos[1] < screen_res[1]/2 + 1.3533*cell_side):
            cursorOn = 1
        if (screen_res[0]/2-0.8*cell_side<mousePos[0]<screen_res[0]/2+0.8*cell_side) and (screen_res[1]/2 + 1.6467*cell_side < mousePos[1] < screen_res[1]/2 + 2.3533*cell_side):
            cursorOn = 2
        if (screen_res[0]/2-0.64*cell_side<mousePos[0]<screen_res[0]/2+0.64*cell_side) and (screen_res[1]/2 + 2.6467*cell_side < mousePos[1] < screen_res[1]/2 + 3.3533*cell_side):
            cursorOn = 3
        printpy("Play", (screen_res[0]/2, screen_res[1]/2), (150, 150, 255) if cursorOn == 0 else (150, 235, 255), True)
        printpy("Options", (screen_res[0]/2, screen_res[1]/2 + cell_side), (150, 150, 255) if cursorOn == 1 else (150, 235, 255), True)
        printpy("About", (screen_res[0]/2, screen_res[1]/2 + cell_side*2), (150, 150, 255) if cursorOn == 2 else (150, 235, 255), True)
        printpy("Quit", (screen_res[0]/2, screen_res[1]/2 + 3*cell_side), (150, 150, 255) if cursorOn == 3 else (150, 235, 255), True)
    if WINDOW == "PlayType":
        pass
    if WINDOW == "Options":
        pass
    if WINDOW == "About":
        pass




def background():
    global mrad, mcolor, OBJS
    screen.fill((0, 0, 0))
    screen.blit(rectangle, (0, 0))
    surface1 = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    mpos = pygame.mouse.get_pos()
    mrad += (1 - random())
    mrad = ((sum(screen_res))/20) if mrad > ((sum(screen_res))/20) else ( ((sum(screen_res))/60) if mrad < ((sum(screen_res))/60) else mrad)
    mcolor = (mcolor[0]+(0.5-random()), mcolor[1]+(0.5-random()), mcolor[2]+(0.5-random()))
    mcolor = (255 if mcolor[0] > 255 else (0 if mcolor[0] < 0 else mcolor[0]), 255 if mcolor[1] > 255 else (0 if mcolor[1] < 0 else mcolor[1]), 255 if mcolor[2] > 255 else (0 if mcolor[2] < 0 else mcolor[2]))

    for circle in OBJS:
        if sphere.distance(circle.pos, mpos) < circle.radius + mrad:
            pygame.draw.line(surface1, [(circle.color[0]+mcolor[0])/2, (circle.color[1]+mcolor[1])/2, (circle.color[2]+mcolor[2])/2, (1-((sphere.distance(circle.pos, mpos))/(mrad + circle.radius)))*255], circle.pos[:2], mpos[:2])
            pygame.draw.circle(surface1, list(circle.color)+[(1-((sphere.distance(circle.pos, mpos))/(mrad + circle.radius)))*255], circle.pos[:2], 1)
            pygame.draw.circle(surface1, list(mcolor)+[(1-((sphere.distance(circle.pos, mpos))/(mrad + circle.radius)))*255], mpos[:2], 1)

        for circle2 in OBJS:
            if circle.n != circle2.n:
                if sphere.is_colliding(circle, circle2):
                    pygame.draw.line(surface1, [(circle.color[0]+circle2.color[0])/2, (circle.color[1]+circle2.color[1])/2, (circle.color[2]+circle2.color[2])/2, (1-((sphere.distance(circle.pos, circle2.pos))/(circle2.radius + circle.radius)))*255], circle.pos[:2], circle2.pos[:2])
                    pygame.draw.circle(surface1, list(circle.color)+[(1-((sphere.distance(circle.pos, circle2.pos))/(circle2.radius + circle.radius)))*255], circle.pos[:2], 1)
                    pygame.draw.circle(surface1, list(circle2.color)+[(1-((sphere.distance(circle.pos, circle2.pos))/(circle2.radius + circle.radius)))*255], circle2.pos[:2], 1)

        circle.vel[0] += (0.5-random())*120*dt*2
        circle.vel[1] += (0.5-random())*120*dt*2
    
        circle.update(dt, screen_res, cell_side)
    screen.blit(surface1, (0, 0))
        

if __name__ == '__main__':
    frameRate = 1000
    dt = 1/1000
    pygame.init()
    screen = pygame.display.set_mode(screen_res, pygame.RESIZABLE)
    pygame.display.set_caption("Othello / Reversi")
    pygame.display.set_icon(icon)
    cls()
    font("Bauhaus 93", int(cell_side*2))
    mainOthelloText = FoNt.render("Othello", True, (190, 255, 225))
    lOthello = pygame.transform.scale(icon, (cell_side*1.5, cell_side*1.5))
    OBJS = list()
    for _ in range(int((sum(screen_res))/60)):
        OBJS.append( sphere([random()*screen_res[0], random()*screen_res[1]], random()*(sum(screen_res))/7.5, [(0.5-random())*8, (0.5-random())*8], _, [random()*256, random()*256, random()*256]) )
    running = True
    clock = pygame.time.Clock()
    rectangle = pygame.Surface(screen_res)
    rectangle.set_alpha(50)
    rectangle.fill((0, 0, 0))
    while running == True:
        initTime = time.time()
        clock.tick(frameRate)
        screen_res = list(screen.get_size())
        tempScreen_res = list(screen_res)
        screen_res[0] = MIN_SIZE[0] if screen_res[0] < MIN_SIZE[0] else screen_res[0]
        screen_res[1] = MIN_SIZE[1] if screen_res[1] < MIN_SIZE[1] else screen_res[1]
        if tempScreen_res != screen_res:
            screen = pygame.display.set_mode(screen_res, pygame.RESIZABLE)
            OBJS = list()
            for _ in range(int((sum(screen_res))/60)):
                OBJS.append( sphere([random()*screen_res[0], random()*screen_res[1]], random()*(sum(screen_res))/7.5, [(0.5-random())*8, (0.5-random())*8], _, [random()*256, random()*256, random()*256]) )
    
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
                            discCount[0] = sum(i.count(board.white) for i in board.currentBoard)
                            discCount[1] = len(discsOnBoard) - discCount[0]
                            TURN = (TURN+1)%2
                            if len(board.allLegalMoves(board, board.player[TURN])) == 0:
                                TURN = (TURN+1)%2
                                if len(board.allLegalMoves(board, board.player[TURN])) == 0:
                                    gameOver = True
                    else:
                        if sphere.distance((screen_res[0]/2 +4.6*cell_side + cell_side*2/15, screen_res[1]/2 + cell_side + cell_side), mspos) < cell_side/2:
                            WINDOW = "homeScreen"
                        if gameOver == True:
                            if sphere.distance((screen_res[0]/2 +4.6*cell_side + cell_side*2/15, screen_res[1]/2), mspos) < cell_side/2:
                                gameOver = False
                                cell_side = (min(screen_res))*(3/32)
                                discsOnBoard = [(3,3), (3,4), (4,3), (4,4)]
                                bBack = pygame.transform.scale(boardBack, ((min(screen_res))*(7/16)*(2**0.5), (min(screen_res))*(7/16)*(2**0.5)))
                                rGame = pygame.transform.scale(restartGame, (cell_side*(2**0.5)*0.8/2, cell_side*(2**0.5)*0.8/2))
                                hScreen = pygame.transform.scale(homeScreen, (cell_side*(2**0.5)/2, cell_side*(2**0.5)/2))
                                Color = [(255, 255, 255), (0, 0, 0)]
                                TURN = 1
                                discCount = [2, 2]
                                board.__init__(board)
                elif WINDOW == "homeScreen":
                    if (screen_res[0]/2-0.58*cell_side<mspos[0]<screen_res[0]/2+0.58*cell_side) and (screen_res[1]/2 - 0.3533*cell_side < mspos[1] < screen_res[1]/2 + 0.3533*cell_side):
                        WINDOW = "PvP"
                        gameOver = False
                        cell_side = (min(screen_res))*(3/32)
                        discsOnBoard = [(3,3), (3,4), (4,3), (4,4)]
                        bBack = pygame.transform.scale(boardBack, ((min(screen_res))*(7/16)*(2**0.5), (min(screen_res))*(7/16)*(2**0.5)))
                        rGame = pygame.transform.scale(restartGame, (cell_side*(2**0.5)*0.8/2, cell_side*(2**0.5)*0.8/2))
                        hScreen = pygame.transform.scale(homeScreen, (cell_side*(2**0.5)/2, cell_side*(2**0.5)/2))
                        Color = [(255, 255, 255), (0, 0, 0)]
                        TURN = 1
                        discCount = [2, 2]
                        board.__init__(board)

                    if (screen_res[0]/2-1.0467*cell_side<mspos[0]<screen_res[0]/2+1.0467*cell_side) and (screen_res[1]/2 + 0.6467*cell_side < mspos[1] < screen_res[1]/2 + 1.3533*cell_side):
                        pass
                    if (screen_res[0]/2-0.8*cell_side<mspos[0]<screen_res[0]/2+0.8*cell_side) and (screen_res[1]/2 + 1.6467*cell_side < mspos[1] < screen_res[1]/2 + 2.3533*cell_side):
                        pass
                    if (screen_res[0]/2-0.64*cell_side<mspos[0]<screen_res[0]/2+0.64*cell_side) and (screen_res[1]/2 + 2.6467*cell_side < mspos[1] < screen_res[1]/2 + 3.3533*cell_side):
                        running = False
                                    
                        
        #Code Here
        if WINDOW == "PvP":
            # =====================START OF CODE FOR BACKGROUND=====================
            background()
            # ======================END OF CODE FOR BACKGROUND======================
            drawBoard()
        elif WINDOW == "homeScreen":
            background()
            drawHomeScreen()
            pass


        pygame.display.update()
        endTime = time.time()
        dt = endTime-initTime
        if dt != 0:
            frameRate = 1/dt
        else:
            frameRate = 1000
