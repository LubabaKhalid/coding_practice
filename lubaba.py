from random import *
n=int(input())
for i in range(n):
    c=0
    x=int(input())
    a=[0]*x
    for j in range(len(a)):
        a[j]=randint(0,1)
        print(a[j],end=' ')
    print()
    b=[0]*x
    for j in range(len(b)):
        b[j]=randint(0,1)
        print(b[j],end=' ')
    print()
    for j in range(len(b)):
        if a[j]==b[j]:
            c=c+0
        else:
            c=c+1
    print(c)
