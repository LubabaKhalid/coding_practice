t=int(input())
for i in range(t):
    x,m=map(int,input().split())
    n=len(x)-2
    count=0
    for j in range(1,2**(n-1)):
        y=x^j
        if y==0:
            continue
        elif (x%j==0 or y%j==0) and y<=m:
             count+=1
    print(count)
            