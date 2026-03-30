import pprint
/** class Board:
    def __init__(self,board=[]):
        self.board = board
**/
    column =  "ABCDEFGHIJ"
    for col in column:
        x = list(col)
    for r in range(1,10+1):
        y = []
        y.append(r)

    board = [ x,y ]
    def show(self,board):
        print(board)

