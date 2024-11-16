import itertools
t=int(input())
for i in range(t):
    m,g=map(int,input().split())
    arr=[]
    for j in range(g):
        n=int(input())
        l=list(map(int,input().split()))
        arr.append(l)
    maximum=-1
    for combination in itertools.product(*arr):
        total=sum(combination)
        if total<=m:
            
            maximum=max(total,maximum)    
    print(maximum)