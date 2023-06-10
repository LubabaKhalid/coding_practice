from random import *
a=[0]*10
b=[0]*10
c=[0]*10
x=[0]*10
c=0
n=[0]*10
for i in range(len(a)):
    a[i]=randint(0,9)
    b[i]=randint(0,9)
    print(a[i],end=' ')
print()
for i in range(len(b)):
    print(b[i],end=' ')
print()
for i in range(len(a)):
    print(f'{a[i]} + {b[i]} = ',end='')
    x[i]=int(input())
for i in range(len(x)):
    if x[i]==a[i]+b[i]:
        c=c+1
print(f'Score : {c}/{len(x)}')
print('Incorrect ')
for i in range(len(x)):
    if x[i]!=a[i]+b[i]:
        print(f'{a[i]} + {b[i]} = {x[i]}',end='       ')
        print(f'{a[i]} + {b[i]} = {a[i]+b[i]}')
        
        
          
          
          
    

    
    
