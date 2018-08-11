import random
import pickle

fileName = 'mark2Memory'
fileObject = open(fileName,'rb')
loseBoards = pickle.load(fileObject)
fileObject.close()

def unload():
    fileName = 'mark2Memory'
    fileObject = open(fileName,'wb')
    pickle.dump(loseBoards, fileObject)
    fileObject.close()

def play(board2):
    board = [n[:] for n in board2]
    numSpaces = getNumSpaces(board)
    randNum = random.randint(0, len(numSpaces) - 1)
    if willLose(board, numSpaces, randNum):
        if len(numSpaces) == 1:
            loseBoards.append(board)
            board[numSpaces[randNum][0]][numSpaces[randNum][1]] = False
        else:
            numSpaces.pop(randNum)
            board = play2(board, numSpaces)
    else:
        board[numSpaces[randNum][0]][numSpaces[randNum][1]] = False
    return board

def play2(board2, numSpaces):
    board = [n[:] for n in board2]
    randNum = random.randint(0, len(numSpaces) - 1)
    if willLose(board, numSpaces, randNum):
        if len(numSpaces) == 1:
            loseBoards.append(board)
            board[numSpaces[randNum][0]][numSpaces[randNum][1]] = False
        else:
            numSpaces.pop(randNum)
            board = play2(board, numSpaces)
    else:
        board[numSpaces[randNum][0]][numSpaces[randNum][1]] = False
    return board

def getNumSpaces(board):
    ret = []
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] is None:
                ret.append([i, j])
    return ret

def willLose(board, numSpaces, randNum):
    newBoard = [n[:] for n in board]
    newBoard[numSpaces[randNum][0]][numSpaces[randNum][1]] = False
    for i in range(0, len(loseBoards)):
        if newBoard == loseBoards[i]:
            return True
    return False
