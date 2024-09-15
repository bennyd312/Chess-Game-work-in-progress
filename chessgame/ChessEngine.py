class GameState():
    def __init__(self):
        #herní plochu reprezentujeme seznamem o rozměrech 11x11
        #první písmeno reprezentuje barvu
        #číslo reprezentuje pořadí
        #"--" reprezentuje postranní pole
        #"--" reprezentuje prázdné herní pole
        self.board = [
            ["br","bn","bb","bq","bk","bb","bn","br"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wr","wn","wb","wq","wk","wb","wn","wr"]]
    
    def LegalMove(self, startsq, finishsq, playercolor):
        startsqfigure = "--"
        finishsqfigure = self.board[startsq[0]][startsq[1]]
        kingposition = [None,None]
        check = None

        while kingposition == [None,None]: #find king position

            for row in range(8):
                for col in range(8):
                    if self.board[row][col]==playercolor+"k":
                        kingposition = [row,col]

        if playercolor == "w": #WARNING: check == true means that the move is ILLEGAL
            check = self.CheckWhite(kingposition,playercolor)
        #else: 
            #check = self.CheckBlack(kingposition,playercolor)

        return check
    



    def MakeMove(self,startsq,finishsq,playercolor):
        figure = self.board[startsq[0]][startsq[1]]
        if figure[1]=="b":
            print(self.BishopMoves(startsq,playercolor))
        
        elif figure[1]=="r":
            print(self.RookMoves(startsq,playercolor))

        elif figure[1]=="q":
            print(self.QueenMoves(startsq,playercolor))
        
        elif figure[1]=="n":
            print(self.KnightMoves(startsq,playercolor))
        
        elif figure[1]=="k":
            print(self.KingMoves(startsq,playercolor))
        
        elif figure == "wp":
            print(self.wpawnmoves(startsq,playercolor))
        
        elif figure == "bp":
            print(self.bpawnmoves(startsq,playercolor))
        
  
        #if move legal for figure type:
        self.board[startsq[0]][startsq[1]] = "--"
        self.board[finishsq[0]][finishsq[1]] = figure
        #else: print('Illegal move')



    """In the following part we will define movement types for all figures"""
    #Returns a list of possible moves for a bishop, ignoring checks
    def BishopMoves(self,position,color):
        row = position[0]
        col = position[1]

        moves = []
        #starting bishop coordinates are (x,y), bishop moves diagonally
        #moves down the diagonal:
        i=1
        while True:
            if row+i<8 and col+i<8:
                if self.board[row+i][col+i]!="--" and self.board[row+i][col+i][0]!=color:
                    print(self.board[row+i][col+i][0])
                    moves.append([row+i,col+i])
                    i=1
                    break
                elif self.board[row+i][col+i]=="--":
                    moves.append([row+i,col+i])
                    i+=1
                else:
                    i=1
                    break
            else:
                i=1
                break
        #up the diagonal
        while True:
            if row-i>-1 and col-i>-1:

                if self.board[row-i][col-i]!="--" and self.board[row-i][col-i][0]!=color:
                    print(self.board[row-i][col-i][0])
                    moves.append([row-i,col-i])
                    i=1
                    break

                elif self.board[row-i][col-i]=="--":
                    moves.append([row-i,col-i])
                    i+=1

                else:
                    i=1
                    break
            else:
                i=1
                break
        #moves up the antidiagonal
        
        while True:
            if row+i<8 and col-i>-1:
                if self.board[row+i][col-i]!="--" and self.board[row+i][col-i][0]!=color:
                    moves.append([row+i,col-i])
                    i=1
                    break
                elif self.board[row+i][col-i]=="--":
                    moves.append([row+i,col-i])
                    i+=1
                else:
                    i=1
                    break
            else:
                i=1
                break
        #moves down the antidiagonal
        while True:
            if row-i>-1 and col+i<8:
                if self.board[row-i][col+i]!="--" and self.board[row-i][col+i][0]!=color:
                    moves.append([row-i,col+i])
                    i=1
                    break
                
                elif self.board[row-i][col+i]=="--":
                    moves.append([row-i,col+i])
                    i+=1
                
                else:
                    i=1
                    break
            else:
                i=1
                break
        return moves
    
    #Returns a list of possible moves for a rook, ignoring checks
    def RookMoves(self,position,color):
        row = position[0]
        col = position[1]
        moves = []
        
        i=1

        while True: #rook moves up
            if row+i<8:
                if self.board[row+i][col]!="--" and self.board[row+i][col][0]!=color:
                    moves.append([row+i,col])
                    i=1
                    break
                elif self.board[row+i][col]=="--":
                    moves.append([row+i,col])
                    i+=1
                else:
                    i=1
                    break
            else:
                i=1
                break

        
        while True: #rook moves down
            if row-i>-1:
                if self.board[row-i][col]!="--" and self.board[row-i][col][0]!=color:
                    moves.append([row-i,col])
                    i=1
                    break
                elif self.board[row-i][col]=="--":
                    moves.append([row-i,col])
                    i+=1
                else:
                    i=1
                    break
            else:
                i=1
                break

        while True: #rook moves right
            if col+i<8:
                if self.board[row][col+i]!="--" and self.board[row][col+i][0]!=color:
                    moves.append([row,col+i])
                    i=1
                    break
                elif self.board[row][col+i]=="--":
                    moves.append([row,col+i])
                    i+=1
                else:
                    i=1
                    break
            else:
                i=1
                break
        
        while True: #rook moves left
            if col-i>-1:
                if self.board[row-i][col]!="--" and self.board[row][col-i][0]!=color:
                    moves.append([row,col-i])
                    i=1
                    break
                elif self.board[row][col-i]=="--":
                    moves.append([row,col-i])
                    i+=1
                else:
                    i=1
                    break
            else:
                i=1
                break
        
        return moves
    

    #Returns a list of possible moves for a queen, ignoring checks
    def QueenMoves(self,position,color):
        movesA = self.BishopMoves(self,position,color)
        movesB = self.RookMoves(self,position,color)
        moves = [i for i in movesA]
        for i in movesB:
            moves.append(i)
        
        return moves
    
    #Returns a list of possible knight moves, ignoring checks
    def KnightMoves(self,position,color):
        moves = []
        row = position[0]
        col = position[1]

        possibleMoves = [[row+2,col+1],[row+2,col-1],[row-2,col+1],[row-2,col-1],[row+1,col+2],[row-1,col+2],[row+1,col-2],[row-1,col-2]]

        for move in possibleMoves:
            if move[0]>-1 and move[0]<8:
                if move[1]>-1 and move[1]<8:
                    target = self.board[move[0]][move[1]]
                    if target!="--" and target[0]!=color:
                        moves.append(move)
                    elif target=="--":
                        moves.append(move)
        
        return moves

    #returns all possible king moves, ignoring checks 
    def KingMoves(self,position,color):
        moves = []
        row = position[0]
        col = position[1]

        possibleMoves = [[row+1,col-1],[row+1,col],[row+1,col+1],[row,col+1],[row,col-1],[row-1,col-1],[row-1,col],[row-1,col+1]]

        for move in possibleMoves:
            if move[0]>-1 and move[0]<8:
                if move[1]>-1 and move[1]<8:
                    target = self.board[move[0]][move[1]]
                    if target!="--" and target[0]!=color:
                        moves.append(move)
                    elif target=="--":
                        moves.append(move)

        return moves
    #returns all white pawn moves, ignoring checks
    def wpawnmoves(self,position,color):
        row = position[0]
        col = position[1]
        moves = []


        possibleMoves= [[row-1,col-1],[row-1,col],[row-1,col+1]]
        
        if row==6 and self.board[4][col]=="--" and self.board[5][col]=="--":
            moves.append([4,col])
        for move in possibleMoves:
            target = self.board[move[0]][move[1]]
            if move[1]==col:
                if target=="--":
                    moves.append(move)
            else:
                if target[0]!=color and target!="--":
                    moves.append(move)
        return moves
    #returns all black pawn moves, ignoring checks
    def bpawnmoves(self,position,color):
        row = position[0]
        col = position[1]
        moves = []


        possibleMoves= [[row+1,col-1],[row+1,col],[row+1,col+1]]
        
        if row==1 and self.board[3][col]=="--" and self.board[2][col]=="--":
            moves.append([3,col])
        for move in possibleMoves:
            target = self.board[move[0]][move[1]]
            if move[1]==col:
                if target=="--":
                    moves.append(move)
            else:
                if target[0]!=color and target!="--":
                    moves.append(move)
        return moves

    #This function will tell us whether the white king is in check or not
    def CheckWhite(self,kingposition,kingcolor):
        row = kingposition[0]
        col = kingposition[1]

        checked = False

        KnightMoves = [[row+2,col+1],[row+2,col-1],[row-2,col+1],[row-2,col-1],[row+1,col+2],[row-1,col+2],[row+1,col-2],[row-1,col-2]]
        RookMoves = self.RookMoves(kingposition,kingcolor)
        BishopMoves = self.BishopMoves(kingposition,kingcolor)
        PawnMoves = [[row-1,col-1],[row-1,col+1]]

        while True:

            for move in KnightMoves:

                if self.board[move[0]][move[1]]=="bn":
                    checked = True
                    break

            for move in RookMoves:

                if self.board[move[0]][move[1]]=="br":
                    checked=True
                    break

                elif self.board[move[0]][move[1]]=="bq":
                    checked=True

                    break

            for move in BishopMoves:

                if self.board[move[0]][move[1]]=="bb":
                    checked = True
                    break
                
                elif self.board[move[0]][move[1]]=="bq":
                    checked = True
                    break

            for move in PawnMoves:

                if self.board[move[0]][move[1]]=="bp":
                    checked=True
                    break
            
            break

class Players():

    def __init__(self,color,tag,opponent=None):
        self.color = color
        self.tag = tag
        self.opponent = None
