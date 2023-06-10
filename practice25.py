from random import *
x=[0]*10
y=[0]*10
s=0
for i in range(10):
    x[i]=randint(1,10)
for i in range(10):
    print(x[i],end=' ')
    s=s+x[i]
av=s/10
print()
print(av{0:.2f})
for i in range(10):
    y[i]=av-x[i]
for j in range(10):
    print(y[j],end=' ')
    

