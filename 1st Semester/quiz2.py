from random import *
x=[0]*30
for i in range(len(x)):
    x[i]=randint(1,20)
print(x)
for i in range(len(x)):
    for j in range(len(x)-1):
        if x[j]>x[j+1]:
            x[j],x[j+1]=x[j+1],x[j]
print(x)
for i in range(len(x)):
    z=x[i]
    c=1
    if z!=x[i+1]:
         for j in range(1,len(x)):
            if x[i]==x[j]:
                c=c+1
            else:
                break
    print(f'{x[i]} is {c} times')
        
        
