t=int(input())
for _ in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    for i in range(n-1):
        if p[i]-p[i+1]==1:
            p[i],p[i+1]=p[i+1],p[i]
    if all(p[i]<p[i+1] for i in range(n-1)):
        print("YES")
       
    else:
        print("NO")