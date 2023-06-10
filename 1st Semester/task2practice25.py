from random import *
x=[0]*30
s=0
p=0
f=0
sp=0
for i in range(len(x)):
    m=randint(1,100)
    print(m,end="")
    s=s+m
print()
for i in range(len(x)):
    if x[i]>=50:
        print(x[i],end=' ')
        sp=sp+x[i]
        p=p+1
        
print()
for i in range(len(x)):
    if x[i]<50:
        print(x[i],end=' ')
        f=f+1
print()
av=s/len(x)

        
