def solve():
    x,y=map(int,input().split())
    board = []
    for i in range(x):
        str1 = ""
        for i in range(y):
            str1+="+-"
        str1+="+"
        board.append(list(str1))
        str1 = ""
        
        for i in range(y):
            str1+="|."
        str1+="|"
        board.append(list(str1))
    str1 = ""
    for i in range(y):
        str1+="+-"
    str1+="+"
    board.append(list(str1))
    board[0][0]='.'
    board[1][0]='.'
    board[1][1]='.'
    board[0][1]='.'
    for i in board:
        print(*i,sep="")
t = int(input())
for i in range(t):
    print(f"Case #{i+1}:")
    solve()