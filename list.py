'''from random import *
x=[0]*12
for i in range(len(x)):
    x[i]=randint(10,100)
    print(x[i],end=' ')
for i in range(len(x)-1):
    max=x[i+1]
    if x[i]>x[i+1]:
        max=x[i]
    min'''


'''from random import *
x=[0]*12
for i in range(len(x)):
    x[i]=randint(10,100)
    print(x[i],end=' ')
for i in range(len(x)-1):
    if x[i]>x[i+1]:
        print('First value is greater ',x[i])
    else:
        print('second value is greater ',x[i+1])'''

'''from random import *
x=[0]*12
for i in range(len(x)):
    x[i]=randint(10,100)
    print(x[i],end=' ')
for i in range(1,len(x)-1):
    if x[i-1]>x[i]>x[i+1]:
        print('In order ')
    else:
        print('Not in order ')'''
from random import *
x=[0]*12
for i in range(len(x)):
    x[i]=randint(10,100)
    print(x[i],end=' ')
print()
for i in range(len(x)-1):
    if x[i]>x[i+1]:
        x[i],x[i+1]=x[i+1],x[i]
for i in range(len(x)):
    print(x[i],end=' ')
        




























        
        
    
