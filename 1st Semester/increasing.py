n=int(input())
for i in range(n):
    x=int(input())
    c=0
    m=[0]*x
    for j in range(x):
        m[j]=map(int,input().split())
        if j<x-1:
            if m[j]==m[j+1]:
                c=c+1
    if c>=1:
        print('NO')
    else:
        print('YES')
        
        
        
    
