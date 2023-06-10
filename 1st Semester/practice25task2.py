from random import *
x=[0]*30
s=0
p=0
f=0
sp=0
g=0
l=0
for i in range(len(x)):
    x[i]=randint(1,100)
    print(x[i],end="  ")
    if x[i]>50:
        p=p+1
    s=s+x[i]
print()
print('pass students ',p)
av=s/len(x)
print(f'Average {av:.2f}')
for i in range(len(x)):
    if x[i]<50:
        print(x[i],end=' ')
print()
for i in range(len(x)):
    if x[i]>=av:
        g=g+1
    else:
        l=l+1
g=[0]*g
l=[0]*l
a=0
b=0
for i in range(len(x)):
    if x[i]>av:
        g[a]=x[i]
        print(g[a],end=' ')
        a=a+1
print()
for i in range(len(x)):
    if x[i]<av:
        l[b]=x[i]
        print(l[b],end=' ')
        b=b+1


