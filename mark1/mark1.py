import functions

board = functions.createNewBoard()

board[0][0] = True
board[0][1] = True
board[0][2] = True





functions.printBoard(board)
print(functions.isGameOver(board))
