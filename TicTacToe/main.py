import sys
if __name__ == '__main__':
    board_dim = 3
    for pos, val in enumerate(sys.argv):
        print( f'{pos}: {val}')
    if len(sys.argv) >=2: #user provided a board dimension
        #board_dim = int(sys.argv[1])
        pass
    # game = TicTacToeGame(board_dim)
    # game.play()