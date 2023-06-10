'''from random import *
s=9
def init(x):
    for i in range(s):
        for j in range(s):
            x[i][j]=randint(0,9)
            
def print_list(x):
    for i in range(s):
        for j in range(s):
            print(x[i][j],end=' ')
        print()

def average_out(x):
    for i in range(1,s-1):
        for j in range(1,s-1):
            x[i][j]=(x[i-1][j-1]+x[i-1][j]+x[i-1][j+1]+x[i][j-1]+x[i][j+1]+x[i+1][j-1]+x[i+1][j]+x[i+1][j+1])//8
        



def main():
    x=[[randint(0,9) for i in range(s)] for j in range(s)]
    init(x)
    print_list(x)
    average_out(x)
    print('------------')
    print_list(x)
main()'''

def is_valid(b,i,j):
    if i<0 or i>=3 or j<0 or j>=3 or b[i][j]!='-':
        return False
    return True


def draw_board(b):
    for i in range(3):
        for j in range(3):
            print(b[i][j],end=' ')
        print()
        
def take_and_place(b,mark):
    while True:
        i,j=map(int,input('Enter row and column ').split())
        if is_valid(b,i,j):
            b[i][j]=mark
        return True
def check_board(b):
    if b[0][0]!='-' and b[0][0]==b[0][1]==b[0][2]:
        return True
    if b[1][0]!='-' and b[1][0]==b[1][1]==b[1][2]:
        return True
    if b[2][0]!='-' and b[2][0]==b[2][1]==b[2][2]:
        return True
    if b[0][0]!='-' and b[0][0]==b[1][0]==b[2][0]:
        return True
    if b[0][1]!='-' and b[0][1]==b[1][1]==b[2][1]:
        return True
    if b[0][2]!='-' and b[0][2]==b[1][2]==b[2][2]:
        return True
    if b[0][0]!='-' and b[0][0]==b[1][1]==b[2][2]:
        return True
    if b[0][2]!='-' and b[0][2]==b[1][1]==b[2][0]:
        return True
    return False
        
    


def main():
    board=[['-' for _ in range(3)] for j in range(3)]
    turn='A'
    turn_total=0
    while turn_total<9:
        draw_board(board)
        take_and_place(board,turn)
        if check_board(board):
            break
        
        if turn=='A':
            turn='B'
        else:
            turn='A'
        turn_total+=1
        if turn_total==9:
            print('draw')
        elif turn=='A':
            print('A wins ')
        else:
            print('B wins ')
main()
        
    











