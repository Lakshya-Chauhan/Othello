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
WINDOW = "PvP"
mcolor = [128, 128, 128]
mrad = (sum(screen_res))/30


cell_side = (min(screen_res))*(3/32)
discsOnBoard = [(3,3), (3,4), (4,3), (4,4)]
bBack = pygame.transform.scale(boardBack, ((min(screen_res))*(7/16)*(2**0.5), (min(screen_res))*(7/16)*(2**0.5)))
Color = [(255, 255, 255), (0, 0, 0)]
TURN = 1
discCount = [2, 2]
def nearest(num, a, b):
    return a if abs(a - num) < abs(b - num) else b
board.__init__(board)
class sphere:
    def __init__(self, position : list, radius : float, velocity, number : int, color : list):
        self.pos = pygame.math.Vector2(position[0], position[1])
        self.radius = radius
        self.vel = pygame.math.Vector2(velocity[0], velocity[1])
        self.n = number
        self.color = color
    
    def update(self, dt):

        if self.vel.magnitude() > 50:
            self.vel = pygame.math.Vector2(50).rotate(pygame.math.Vector2(50).angle_to(self.vel))

        if (self.pos[0] > screen_res[0]-10):
            self.pos[0] = (screen_res[0]-11)
            self.vel[0] = -self.vel[0]
        elif self.pos[0] < 10:
            self.pos[0] = 11
            self.vel[0] = -self.vel[0]
        
        if (self.pos[1] > screen_res[1]-10):
            self.pos[1] = (screen_res[1]-11)
            self.vel[1] = -self.vel[1]
        elif self.pos[1] < 10:
            self.pos[1] = 11
            self.vel[1] = -self.vel[1]

        if (screen_res[0]/2 - cell_side*4 < self.pos[0] < screen_res[0]/2 + cell_side*4) and (screen_res[1]/2 - cell_side*4 < self.pos[1] < screen_res[1]/2 + cell_side*4):
            self.pos[0] = (screen_res[0]/2 - cell_side*4) if random() > 0.5 else (screen_res[0]/2 + cell_side*4)
            self.pos[1] = (screen_res[1]/2 - cell_side*4) if random() > 0.5 else (screen_res[1]/2 + cell_side*4)

        self.pos += self.vel*dt

    def is_colliding(obj1, obj2):
        return True if (sphere.distance(obj1.pos, obj2.pos) < obj1.radius + obj2.radius) else False

    def distance(point1 : list, point2 : list):
        if min([len(point1), len(point2)]) == 2:
            return ((((point1[0]-point2[0])**2) + ((point1[1] - point2[1])**2))**0.5)
        
        else:
            return ((((point1[0]-point2[0])**2) + ((point1[1] - point2[1])**2) + ((point1[2] - point2[2])**2))**0.5)
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
    global cell_side, screen_res, discsOnBoard, prevScreen_res, Color, boardBack,bBack, OBJS, TURN, discCount
    pr = (min(screen_res))*(7/16)*(2**0.5) #pattern radius
    if prevScreen_res != screen_res:
        prevScreen_res = list(screen_res)
        cell_side = (min(screen_res))*(3/32)
        pr = (min(screen_res))*(7/16)*(2**0.5) #pattern radius
        bBack = pygame.transform.scale(boardBack, (pr*2.5*1.826087, pr*2.5))
        
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
    pygame.draw.circle(screen, [50, 50, 50], (screen_res[0]/2 -cell_side, screen_res[1]/2 - 4.6*cell_side), cell_side/2, int(cell_side/12))
    pygame.draw.circle(screen, [30, 30, 30], (screen_res[0]/2 +cell_side, screen_res[1]/2 - 4.6*cell_side), cell_side/2)
    pygame.draw.circle(screen, [205, 205, 205], (screen_res[0]/2 +cell_side, screen_res[1]/2 - 4.6*cell_side), cell_side/2, int(cell_side/12))
    
    font("calibri", int(cell_side*0.4), True)
    # printpy(str(discCount[0]), (screen_res[0]/2 -cell_side, screen_res[1]/2 - 4.6*cell_side), (128, 128, 128), True)
    # printpy(str(discCount[1]), (screen_res[0]/2 +cell_side, screen_res[1]/2 - 4.6*cell_side), (128, 128, 128), True)
    if discCount[0] > discCount[1]:
        printpy(str(discCount[0]), (screen_res[0]/2 -cell_side, screen_res[1]/2 - 4.6*cell_side), (64, 128, 64), True)
        printpy(str(discCount[1]), (screen_res[0]/2 +cell_side, screen_res[1]/2 - 4.6*cell_side), (128, 64, 64), True)
    elif discCount[0] < discCount[1]:
        printpy(str(discCount[0]), (screen_res[0]/2 -cell_side, screen_res[1]/2 - 4.6*cell_side), (128, 64, 64), True)
        printpy(str(discCount[1]), (screen_res[0]/2 +cell_side, screen_res[1]/2 - 4.6*cell_side), (64, 128, 64), True)
    else:
        printpy(str(discCount[0]), (screen_res[0]/2 -cell_side, screen_res[1]/2 - 4.6*cell_side), (64, 64, 128), True)
        printpy(str(discCount[1]), (screen_res[0]/2 +cell_side, screen_res[1]/2 - 4.6*cell_side), (64, 64, 128), True)

if __name__ == '__main__':
    frameRate = 1000
    dt = 1/1000
    pygame.init()
    screen = pygame.display.set_mode(screen_res, pygame.RESIZABLE)
    icon = pygame.image.load('assets/images/icon.jpg')
    pygame.display.set_caption("Othello / Reversi")
    pygame.display.set_icon(icon)
    cls()
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
                        
        #Code Here
        if WINDOW == "PvP":
            # =====================START OF CODE FOR BACKGROUND=====================

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

                circle.update(dt)
            screen.blit(surface1, (0, 0))

            # ======================END OF CODE FOR BACKGROUND======================
            drawBoard()
            pygame.display.update()


        endTime = time.time()
        dt = endTime-initTime
        if dt != 0:
            frameRate = 1/dt
        else:
            frameRate = 1000
