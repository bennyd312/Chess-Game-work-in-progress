"""
Main will process input and game state
"""

import pygame as p
import ChessEngine

p.init()
p.display.set_caption("Chess")
info = p.display.Info()

user_monitor = [info.current_w, info.current_h]

user_size = min(user_monitor)
user_optimal_size = 0
for i in range(100):
    if i*8*8<user_size-100:
        user_optimal_size = i*8*8
    else:
        break

WIDTH = HEIGHT = user_optimal_size  #rozměr
DIMENSION = 8 #dimenze člověče

SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # pro pripadne animace
IMAGES = {}

def main():
    p.init()
    screen = p.display.set_mode((WIDTH ,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    gameOver = False

    white = ChessEngine.Players("white","w")
    black = ChessEngine.Players("black","b")
    white.opponent = black
    black.opponent = white

    player = white

    sqSelected = () #selected square using mouseclicks, remembers the last clicked square.
    playerClicks = [] #storing two consecutive clicks (two tuples) ex.: klik od (1,1) do (2,2) je [(1,1),(2,2)] for performing moves
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                if gameOver == False:

                    location = p.mouse.get_pos()#(x,y) souřadnice myši
                    col = location[0] // SQ_SIZE
                    row = location[1] // SQ_SIZE
                    
                    if len(playerClicks)==0:
                        if gs.board[row][col][0] == player.tag:
                            sqSelected = (row,col)
                            playerClicks.append(sqSelected)
                            sqSelected = ()
                    elif len(playerClicks)==1:
                        sqSelected = (row,col)
                        playerClicks.append(sqSelected)
                        gs.MakeMove(playerClicks[0],playerClicks[1],player.tag)
                        playerClicks = []
                        sqSelected=()
                        player = player.opponent
                        

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

"""loads all graphics"""
def drawGameState(screen, gs,):
    drawBoard(screen) #nakreslit pole
    drawPieces(screen , gs.board) #nakreslit figurky

def drawBoard(screen):
    colors = [p.Color("white"), p.Color("brown")]
    outline = "black"
    color = colors[0]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            if (r+c)%2==1:
                color=colors[1]
            else:
                color = colors[0]
            p.draw.rect(screen, outline, p.Rect(c*SQ_SIZE+SQ_SIZE/32, r*SQ_SIZE+SQ_SIZE/32, SQ_SIZE-SQ_SIZE/16, SQ_SIZE-SQ_SIZE/16))
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE+SQ_SIZE/16, r*SQ_SIZE+SQ_SIZE/16, SQ_SIZE-SQ_SIZE/8, SQ_SIZE-SQ_SIZE/8))


def drawPieces(screen,board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE+SQ_SIZE*1/10, r*SQ_SIZE+SQ_SIZE*1/10, SQ_SIZE, SQ_SIZE))

def loadImages():
    #obrázky načteme do slovníku a můžeme k nim tedy v budoucnu přistupovat bez toho, abychom je načítali ze souboru znova
    pieces = ["wp","wr","wn","wb","wk","wq","bp","br","bn","bb","bk","bq"]
    i=1

    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("C:\\Users\\bdesi\\Desktop\\chessgame\\chess\\images\\" + piece + ".png"), (SQ_SIZE*4/5,SQ_SIZE*4/5))

main()
