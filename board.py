class Board:
    WHITE = 1 
    BLACK = -1
    EMPTY = 0

    DIRECTIONS = (  ( 1, 0),    # right
                    (-1, 0),    # left
                    ( 0, 1),    # down
                    (-1, 1),    # downwards left
                    ( 1, 1),    # downwards right
                    ( 0,-1),    # up
                    (-1,-1),    # upwards left
                    ( 1,-1),    # upwards right
                )

    def __init__(self):
        
        # create an empty board
        self.board = [ 8 * [Board.EMPTY] for _ in range(8)]

        # initialising centre squares
        self.board[3][3] = self.board[4][4] = Board.WHITE      
        self.board[3][4] = self.board[4][3] = Board.BLACK
    

    def getAllLegalMoves(self, PLAYER) -> set:
        '''Return all the legal moves for the given player.'''
        
        all_legal_moves = set()
        for row in range(8):
            for col in range(8):
                if self.board[row][col] == PLAYER:
                    all_legal_moves.update(self.getLegalMoves(PLAYER, (row, col)))
        return all_legal_moves

    @staticmethod
    def checkCoordRange(x: int, y: int) -> bool:
        '''Returns true if the given parameters represent an actual cell in a 8x8 matrix'''

        return (x >= 0 and y >= 0) and (x < 8 and y < 8)
    
    def getLegalMoves(self, PLAYER: int, coords: tuple[int, int]):
        '''Return legal moves for a given player's disc, at a given cell in the board.'''
    
        OPPONENT = PLAYER * -1

        legal_moves = []
        for dir in Board.DIRECTIONS:
            row, col  = coords
            rowDir, colDir = dir

            row += rowDir
            col += colDir
                
            if Board.checkCoordRange(row, col) is False or self.board[row][col] != OPPONENT:
                continue
            
            row += rowDir
            col += colDir
            while (Board.checkCoordRange(row, col) is True and self.board[row][col] == OPPONENT):
                row += rowDir
                col += colDir
            if (Board.checkCoordRange(row, col) is True and self.board[row][col] == Board.EMPTY):   # possible move
                legal_moves.append((row, col))

    def flipDiscs(self, PLAYER: int, initCoords: tuple[int, int], endCoords: tuple[int, int], direction: tuple[int, int]):
        '''Flip the discs between the given two cells to the given PLAYER color.'''

        OPPONENT = PLAYER * -1
        rowDir, colDir = direction
        row, col = initCoords
        r, c = endCoords

        while (self.board[row][col] == OPPONENT) and (row != r and col != c):
            self.board[row, col] = PLAYER
            row += rowDir
            col += colDir

    def makeMove(self, coords, PLAYER):
        '''Place the PLAYER's coin on the given cell, and outflank the opponent discs accordingly.'''

        OPPONENT = PLAYER * - 1
        row, col = coords
        self.board[row][col] = PLAYER
        
        for dir in Board.DIRECTIONS:
            rowDir, colDir = dir
            r, c = coords

            r += rowDir
            c += colDir
            
            if Board.checkCoordRange(r, c) is False or self.board[r][c] != OPPONENT:
                continue
            
            r += rowDir
            c += colDir
            while (Board.checkCoordRange(r, c) is True and self.board[r][c] == OPPONENT):
                r += rowDir
                c += colDir
            if (Board.checkCoordRange(r, c) is True and self.board[r][c] == PLAYER):
                self.flipDiscs(PLAYER, (row, col), (r, c), dir) 