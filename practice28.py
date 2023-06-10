#task1
'''from random import *
s=int(input())
x=[0]*s
for i in range(s):
    x[i]=randint(10,99)
    print(x[i],end=' ')
print()
for i in range(s-1,-1,-1):
    print(x[i],end=' ')'''

#task2
'''from random import *
s=int(input())
x=[0]*s
c=0
for i in range(s):
    x[i]=randint(10,99)
    print(x[i],end=' ')
    c=c+x[i]
print()
print('sum of all elements is ',c)'''

#task3
'''from random import *
x=[10,23,34,54,32,76,68]
y=x.copy()
for i in range(len(y)):
    print(y[i],end=' ')'''

#task4

#task4BubbleSorting
'''x=[3,5,8,9,10]
y=[6,7,8,9,13]
n=[0]*10
for i in range(5):
    n[i]=x[i]
j=5
for i in range(5):
    n[j]=y[i]
    j=j+1
print(n)
for i in range(10):
    for j in range(10-1):
        if n[j]>n[j+1]:
            n[j],n[j+1]=n[j+1],n[j]
print(n)'''


#task5
from random import *
x=[0]*10
e=[]
o=[]
even=ev=0
odd=od=0
for i in range(10):
    x[i]=randint(1,50)
print(x)
for i in range(10):
    if x[i]%2==0:
        e[ev]=x[i]
        even=even+1
        ev=ev+1
    else:
        o[od]=x[i]
        od=od=1
print('even ', ev)
print('odd ',od)
if ev>od:
    for i in range(10):
        if x[i]%2!=0:
            x[i]=x[i]+1
else:
    for i in range(10):
        if x[i]%2==0:
            x[i]=x[i]-1
print(x)
    
    
        
    

