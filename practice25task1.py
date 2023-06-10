from random import *
x=[1]*10
print('Length: ',len(x))
s=0
p=0
n=0
for i in range(10):
    x[i]=randint(30,100)
    print(x[i],end=" ")
    s=s+x[i]
print()
av=s/10
print(f'Average: {av:.2f}')
for i in range(10):
    x[i]=av-x[i]
    print(f'{x[i]:.2f}',end=' ')
    if x[i]>0:
        p=p+1
    else:
        n=n+1
print()
print("Count of positive values: ",p)
print("Count of negative values: ",n)

        
    
    
