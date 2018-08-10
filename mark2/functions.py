numRows = 5;
numWin = 3;

def createNewBoard():
    ret = [];
    for i in range(0, numRows):
        subRet = [];
        for j in range(0, numRows):
            subRet.append(None)
        ret.append(subRet)
    return ret

def isWinner(i, j, board):
    if board[i][j] is None:
        return False

    try:
        vertical = True
        for x in range(numWin):
            if board[i][j] != board[i+x][j]:
                vertical = False
    except IndexError:
        vertical = False

    try:
        horizontal = True
        for x in range(numWin):
            if board[i][j] != board[i][j+x]:
                horizontal = False
    except IndexError:
        horizontal = False

    try:
        diagonal = True
        for x in range(numWin):
            if board[i][j] != board[i+x][j+x]:
                diagonal = False
    except IndexError:
        diagonal = False

    return vertical or horizontal or diagonal

def isGameOver(board):
    isNone = False
    for i in range(0, numRows):
        for j in range(0, numRows):
            if isWinner(i, j, board):
                return board[i][j]
            if board[i][j] is None:
                isNone = True
    if not isNone:
        return 0
    return -1

def printBoard(board):
    for i in range(0, numRows):
        for j in range(0, numRows):
            print(board[i][j], end = ' ')
        print()

def isEmpty(row, col, board):
    return board[row][col] is None
