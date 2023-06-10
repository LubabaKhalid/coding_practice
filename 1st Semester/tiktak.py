def is_valid_input(board,i,j):
    if i<len(board) and i>=0 and j<len(board) and j>=0 and board[i][j]=='_':
        return True
    return take_input(board)

def take_input(board):
    i=int(input())
    j=int(input())
    if is_valid_input(board,i,j):
        board[i][j]=input()

        
def check_win(board):
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2] and board[i][1]!='_':
            return True
    for i in range(3):
        if board[0][i]==board[1][i]==board[2][i] and board[1][i]!='_':
            return True
    if board[1][1]==board[2][2]==board[0][0] and board[1][1]!='_':
        return True
    if board[0][2]==board[1][1]==board[2][0] and board[2][0]!='_':
        return True
    return False

def draw_board(board):
    for row in board:
        for element in row:
            print(element,end=' ')
        print()
        

def main():
    board=[['_','_','_'],['_','_','_'],['_','_','_']]
    draw_board(board)
    take_input(board)
main()    
