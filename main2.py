import functions
import mark2
import mark1
import random
import time

numGames = 0
games1 = 0
games2 = 0

while True:

    board = functions.createNewBoard()
    prevBoard = [n[:] for n in board]
    # print()

    turn = True if random.randint(0, 1) == 0 else False

    while functions.isGameOver(board) == -1:

        prevBoard = [n[:] for n in board]

        if turn:
            # functions.printBoard(board)
            # print()
            # row = int(input('Input Row: '))
            # assert row < functions.numRows
            # assert row >= 0
            # col = int(input('Input Col: '))
            # print()
            # assert col < functions.numRows
            # assert col >= 0
            # assert functions.isEmpty(row, col, board)
            # board[row][col] = True
            # functions.printBoard(board)
            # time.sleep(random.randint(0, 2))
            # print()
            board = functions.reverse(board)
            board = mark1.play(board)
            board = functions.reverse(board)
        else:
            # functions.printBoard(board)
            # time.sleep(random.randint(0, 2))
            # print()
            board = mark2.play(board)
        turn = not turn

    if functions.isGameOver(board) == False:
        print('Mark 2 Wins!')
        mark2.loseBoards.append(functions.reverse(prevBoard))
        games2 += 1
    elif functions.isGameOver(board) == True:
        print('Mark 1 Wins!')
        mark2.loseBoards.append(prevBoard)
        games1 += 1
    else:
        print('It\'s a tie!')

    numGames += 1
    print(numGames)
    print(float(games2) / float(games1 + games2))
    print(float(numGames - games1 - games2) / float(numGames))
