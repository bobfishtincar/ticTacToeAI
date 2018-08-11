import random

def play(board):
    numSpaces = getNumSpaces(board)
    randNum = random.randint(0, len(numSpaces) - 1)
    board[numSpaces[randNum][0]][numSpaces[randNum][1]] = False
    return board

def getNumSpaces(board):
    ret = []
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] is None:
                ret.append([i, j])
    return ret
