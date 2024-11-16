a=list(map(str,input().split()))
b=list(map(str,input().split()))
t=int(input())
for i in range(t):
    x,y=(map(str,input().split()))
    if x==y:
        print('Yes')
    for j in range(len(x)):
        if x[j]!=y[j]:
            if y[j]==b[a.index(x[j])] or x[j]==b[a.index([y[j]])] or x[j]==a[b.index(x[j])] or y[j]==a[b.index(y[j])]:
                print('Yes')
            else:
                print('No')
                break
    