from random import *
s=randint(2,10)
x=[0]*s
print('nums = ',end='')
print('[',end=' ')
for i in range(len(x)):
    x[i]=randint(0,20)
    print(f'{x[i]}',end=' ')
    if i<len(x)-1:
        print(',',end=' ')
print(']')
y=int(input('target = '))
for i in range(len(x)):
    if x[i]==y:
        print(f'[{i}]')
        break
    for j in range(i+1,len(x)):
        if x[i]+x[j]==y:
            print(f'[{i},{j}]',end='')
            break
    
    
