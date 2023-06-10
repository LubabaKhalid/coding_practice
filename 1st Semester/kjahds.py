from random import *
x=[0]*10
for i in range(10):
    x[i]=randint(3,7)
    print(x[i],end=' ')
print()
for i in range(10):
    for j in range(x[i]):
        print('*',end='')
    print()
