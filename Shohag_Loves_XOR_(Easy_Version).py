t=int(input())
for i in range(t):
    x,m=map(int,input().split())
    count=0
    for j in range(1,min(m + 1, 10**6 + 1)):
        if x==j:
            continue
        n=x^j
        if (x%n==0 or j%n==0):
             count+=1
    print(count)
            