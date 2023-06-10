'''def fun(c,n):
    for j in range(1,n+1):
        i=j-1
        if i>=0:
            value,c[i]=c[i],value
        else:
            break'''
                



n=int(input())
for i in range(n):
    x=list(map(int,input().split()))
    y=set(x)
    print(y)
    z=sorted(y)
    print(z)
    if len(z)>1:
        for i in range(len(z)):
            if i==len(z)-2:
                print(z[i])
    else:
        print('NO')
    '''print(fun(x,y))'''
