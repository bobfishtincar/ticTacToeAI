import functions
import ai
import random
import time

board = functions.createNewBoard()
print()

turn = True

while functions.isGameOver(board) == -1:
    if turn:
        functions.printBoard(board)
        print()
        row = int(input('Input Row: '))
        assert row < functions.numRows
        assert row >= 0
        col = int(input('Input Col: '))
        print()
        assert col < functions.numRows
        assert col >= 0
        assert functions.isEmpty(row, col, board)
        board[row][col] = True
    else:
        functions.printBoard(board)
        time.sleep(random.randint(0, 2))
        print()
        board = ai.play(board)
    turn = not turn

functions.printBoard(board)
print()

if functions.isGameOver(board) == False:
    print('You lose!')
elif functions.isGameOver(board) == True:
    print('You win!')
else:
    print('It\'s a tie!')

print()
