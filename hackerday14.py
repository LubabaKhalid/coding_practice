#maxdifference
'''s=int(input())
x=list(map(int,input().split()))
min=x[0]
max=x[0]
for i in range(len(x)-1):
    if min>x[i+1]:
        min=x[i+1]
    if x[i+1]>max:
        max=x[i+1]
print(max-min)'''

'''class difference:
    def __init__(self,a):
        self.__elements=a
    def computdiff(self):
        x=[]
        l=a[0]
        for i in a:
            if l<i:
                l=i
        for j in a:
            a1=abs(j-l)
            x.append(a1)
            self.maxdifference=max(x)
        


n=int(input())
a=list(map(int,input().split()))
d=difference(a)
d.computdiff()
print(d.maxdifference)'''
'''from random import *
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
    print(c)'''
from random import *
n=int(input())
c=0
for i in range(n):
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

