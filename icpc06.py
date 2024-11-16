import itertools
t=int(input())
for i in range(t):
    n=int(input())
    dep=[]
    for j in range(n):
        x=int(input())
        y=list(map(int,input().split()))
        dep.append(y)
    com=0
    for combination in itertools.product(*dep):
        if len(set(combination)) == n:
            com += 1
    
    print(com)
    
    

