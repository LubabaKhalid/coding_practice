from random import *
x=[0]*20
for i in range(len(x)-2):
    while True:
        x[i]=randint(1,100)
        x[i+1]=randint(1,100)
        x[i+2]=randint(1,100)
        u=False
        if x[i+1]>x[i] and x[i+1]<x[i+2]:
            u=True
        if u:
            break
print(x)
