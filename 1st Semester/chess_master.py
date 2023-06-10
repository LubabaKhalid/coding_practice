n,q=map(int,input().split())
def valid(x,y):
    return x>0 and y>0 and x<=n and y<=n
board=[[True]*(n+1) for i in range(n+1)]
x,y=map(int,input().split())
for i in range(q):
    _x,_y=map(int,input().split())
    if valid(_x,_y):
        board[_x][_y]=False
dx=[0,1,1,-1]
dy=[1,0,1,1]
ans=0
for i in range(4):
    _x,_y=x+dx[i],y+dy[i]
    while valid(_x,_y) and board[_x][_y]:
        ans+=1
        _x+=dx[i]
        _y+=dy[i]
    _x,_y=x-dx[i],y-dy[i]
    while valid(_x,_y) and board[_x][_y]:
        ans+=1
        _x-=dx[i]
        _y-=dy[i]
print(ans)
            
