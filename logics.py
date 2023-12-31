from random import random
import pygame
class board:
    currentBoard = None
    white = 89
    black = -11
    player = [white, black]
    def __init__(self):
        board.currentBoard = list()
        for i in range(8):
            board.currentBoard.append(list())
            for _ in range(8):
                board.currentBoard[i].append(0)
        board.currentBoard[3][3] = board.white       #-11 is black
        board.currentBoard[3][4] = board.black       #89 is white
        board.currentBoard[4][3] = board.black       #89 is white
        board.currentBoard[4][4] = board.white       #-11 is black

    def allLegalMoves(self, color):
        Board = board.currentBoard
        legalMoves = set()
        for x in range(8):
            for y in range(8):
                if Board[x][y] == 0:
                    color_sum =  sum([Board[(x+1) if x < 7 else x][(y-1) if y > 0 else y], 
                                      Board[(x+1) if x < 7 else x][y], 
                                      Board[(x+1) if x < 7 else x][(y+1) if y < 7 else y], 
                                      Board[x][(y-1) if y > 0 else y], 
                                      Board[x][(y+1) if y < 7 else y], 
                                      Board[(x-1) if x > 0 else x][(y-1) if y > 0 else y], 
                                      Board[(x-1) if x > 0 else x][y], 
                                      Board[(x-1) if x > 0 else x][(y+1) if y < 7 else y]])
                    if (color_sum != 0) and (color_sum%color != 0):
                        if board.isLegalMove(board, (x, y), color):
                            legalMoves.add((x, y))
                continue
        return legalMoves
    
    def opp(color):
        return board.white if color == board.black else (board.black if color == board.white else None)
    
    def colour(color):
        return 0 if color == board.white else (1 if color == board.black else None)


    def isLegalMove(self, coords, color):
        Board = board.currentBoard

        if Board[coords[0]][coords[1]] != 0:
            return False

        if Board[min(coords[0]+1, 7)][coords[1]] == board.opp(color):
            for x in range(coords[0]+2, 8):
                if Board[x][coords[1]] == color:
                    return True
                if Board[x][coords[1]] == 0:
                    break

        if Board[coords[0]][min(coords[1]+1, 7)] == board.opp(color):
            for y in range(coords[1]+2, 8):
                if Board[coords[0]][y] == color:
                    return True
                if Board[coords[0]][y] == 0:
                    break

        if Board[max(coords[0]-1, 0)][coords[1]] == board.opp(color):
            for x in range(coords[0]-2, -1, -1):
                if Board[x][coords[1]] == color:
                    return True
                if Board[x][coords[1]] == 0:
                    break

        if Board[coords[0]][max(coords[1]-1, 0)] == board.opp(color):
            for y in range(coords[1]-2, -1, -1):

                if Board[coords[0]][y] == color:
                    return True
                if Board[coords[0]][y] == 0:
                    break
      
        if Board[min(coords[0]+1, 7)][min(coords[1]+1, 7)] == board.opp(color):
            for i in range(2,8):
                if max(coords[0], coords[1]) + i > 7:
                    break
                if Board[coords[0]+i][coords[1]+i] == color:
                    return True
                if Board[coords[0]+i][coords[1]+i] == 0:
                    break

        if Board[max(coords[0]-1, 0)][min(coords[1]+1, 7)] == board.opp(color):
            for i in range(2,8):
                if coords[0]-i < 0 or coords[1]+i > 7:
                    break
                if Board[coords[0]-i][coords[1]+i] == color:
                    return True
                if Board[coords[0]-i][coords[1]+i] == 0:
                    break

        if Board[min(coords[0]+1, 7)][max(coords[1]-1, 0)] == board.opp(color):
            for i in range(2,8):
                if coords[0]+i > 7 or coords[1]-i < 0:
                    break
                if Board[coords[0]+i][coords[1]-i] == color:
                    return True
                if Board[coords[0]+i][coords[1]-i] == 0:
                    break

        if Board[max(coords[0]-1, 0)][max(coords[1]-1, 0)] == board.opp(color):
            for i in range(2,8):
                if min(coords[0], coords[1]) - i < 0:
                    break
                if Board[coords[0]-i][coords[1]-i] == color:
                    return True
                if Board[coords[0]-i][coords[1]-i] == 0:
                    break

        return False

    def makeMove(self, coords, color):
        Board = board.currentBoard
        discs = list()

        if Board[min(coords[0]+1, 7)][coords[1]] == board.opp(color):
            discs.append((min(coords[0]+1, 7), coords[1]))
            for x in range(coords[0]+2, 8):
                discs.append((x, coords[1]))
                if Board[x][coords[1]] == color:
                    for disc in discs:
                        board.currentBoard[disc[0]][disc[1]] = color
                    discs.clear()
                    break
                if Board[x][coords[1]] == 0:
                    discs.clear()
                    break
        discs.clear()
        if Board[coords[0]][min(coords[1]+1, 7)] == board.opp(color):
            discs.append((coords[0], min(coords[1]+1, 7)))
            for y in range(coords[1]+2, 8):
                discs.append((coords[0], y))
                if Board[coords[0]][y] == color:
                    for disc in discs:
                        board.currentBoard[disc[0]][disc[1]] = color
                    discs.clear()
                    break
                if Board[coords[0]][y] == 0:
                    discs.clear()
                    break
        discs.clear()
        if Board[max(coords[0]-1, 0)][coords[1]] == board.opp(color):
            discs.append((max(coords[0]-1, 0), coords[1]))
            for x in range(coords[0]-2, -1, -1):
                discs.append((x, coords[1]))
                if Board[x][coords[1]] == color:
                    for disc in discs:
                        board.currentBoard[disc[0]][disc[1]] = color
                    discs.clear()
                    break
                if Board[x][coords[1]] == 0:
                    discs.clear()
                    break
        discs.clear()
        if Board[coords[0]][max(coords[1]-1, 0)] == board.opp(color):
            discs.append((coords[0], max(coords[1]-1, 0)))
            for y in range(coords[1]-2, -1, -1):
                discs.append((coords[0], y))
                if Board[coords[0]][y] == color:
                    for disc in discs:
                        board.currentBoard[disc[0]][disc[1]] = color
                    discs.clear()
                    break
                if Board[coords[0]][y] == 0:
                    discs.clear()
                    break
        discs.clear()
        if Board[min(coords[0]+1, 7)][min(coords[1]+1, 7)] == board.opp(color):
            discs.append((min(coords[0]+1, 7), min(coords[1]+1, 7)))
            for i in range(2,8):
                discs.append((coords[0]+i, coords[1]+i))
                if max(coords[0], coords[1]) + i > 7:
                    discs.clear()
                    break
                if Board[coords[0]+i][coords[1]+i] == color:
                    for disc in discs:
                        board.currentBoard[disc[0]][disc[1]] = color
                    discs.clear()
                    break
                if Board[coords[0]+i][coords[1]+i] == 0:
                    discs.clear()
                    break
        discs.clear()
        if Board[max(coords[0]-1, 0)][min(coords[1]+1, 7)] == board.opp(color):
            discs.append((max(coords[0]-1, 0), min(coords[1]+1, 7)))
            for i in range(2,8):
                discs.append((coords[0]-i, coords[1]+i))
                if coords[0]-i < 0 or coords[1]+i > 7:
                    discs.clear()
                    break
                if Board[coords[0]-i][coords[1]+i] == color:
                    for disc in discs:
                        board.currentBoard[disc[0]][disc[1]] = color
                    discs.clear()
                    break
                if Board[coords[0]-i][coords[1]+i] == 0:
                    discs.clear()
                    break
        discs.clear()
        if Board[min(coords[0]+1, 7)][max(coords[1]-1, 0)] == board.opp(color):
            discs.append((min(coords[0]+1, 7), max(coords[1]-1, 0)))
            for i in range(2,8):
                discs.append((coords[0]+i, coords[1]-i))
                if coords[0]+i > 7 or coords[1]-i < 0:
                    discs.clear()
                    break
                if Board[coords[0]+i][coords[1]-i] == color:
                    for disc in discs:
                        board.currentBoard[disc[0]][disc[1]] = color
                    discs.clear()
                    break
                if Board[coords[0]+i][coords[1]-i] == 0:
                    discs.clear()
                    break
        discs.clear()
        if Board[max(coords[0]-1, 0)][max(coords[1]-1, 0)] == board.opp(color):
            discs.append((max(coords[0]-1, 0), max(coords[1]-1, 0)))
            for i in range(2,8):
                discs.append((coords[0]-i, coords[1]-i))
                if min(coords[0], coords[1]) - i < 0:
                    discs.clear()
                    break
                if Board[coords[0]-i][coords[1]-i] == color:
                    for disc in discs:
                        board.currentBoard[disc[0]][disc[1]] = color
                    discs.clear()
                    break
                if Board[coords[0]-i][coords[1]-i] == 0:
                    discs.clear()
                    break

        return False
    
class sphere:
    def __init__(self, position : list, radius : float, velocity, number : int, color : list):
        self.pos = pygame.math.Vector2(position[0], position[1])
        self.radius = radius
        self.vel = pygame.math.Vector2(velocity[0], velocity[1])
        self.n = number
        self.color = color
    
    def update(self, dt, screen_res, cell_side):

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