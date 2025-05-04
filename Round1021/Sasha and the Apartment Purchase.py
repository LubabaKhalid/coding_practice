t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    if k>=n:
        print(10**5)
        continue
    x=(n-k-1)//2
    y=k+(n-k)//2
    print(a[y]-a[x]+1)