class board:
    currentBoard = None
    def __init__(self):
        board.currentBoard = list()
        for i in range(8):
            board.currentBoard.append(list())
            for _ in range(8):
                board.currentBoard[i].append(0)

    def isLegalMove(self, coords, color):
        Board = board.currentBoard
        if Board[min(coords[0]+1, 7)][coords[1]] == -color:
            for x in range(coords[0]+2, 8):
                if Board[x][coords[1]] == color:
                    return True

        if Board[coords[0]][min(coords[1]+1, 7)] == -color:
            for y in range(coords[1]+2, 8):
                if Board[coords[0]][y] == color:
                    return True
        
        if Board[max(coords[0]-1, 0)][coords[1]] == -color:
            for x in range(coords[0]-2, -1, -1):
                if Board[x][coords[1]] == color:
                    return True
        
        if Board[coords[0]][max(coords[1]-1, 0)] == -color:
            for y in range(coords[1]-2, -1, -1):
                if Board[coords[0]][y] == color:
                    return True