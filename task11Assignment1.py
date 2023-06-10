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
'''x=[3,5,8,9,10]
y=[6,7,8,9,13]
n=[0]*10
for i in range(5):
    n[i]=x[i]
j=5
for i in range(5):
    n[j]=x[i]
    j=j+1
print(n)
    
n.sort()
for i in range(len(n)):
    print(n[i],end=' ')'''
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
'''from random import *
x=[0]*10

even=0
odd=0
for i in range(10):
    x[i]=randint(1,50)
    print(x[i],end=' ')
print()
for i in range(10):
    if x[i]%2==0:
        print(x[i],end=' ')
        even=even+1
    else:
        odd=odd=1
print()
for i in range(10):
    if x[i]%2!=0:
        print(x[i],end=' ')
print()
if even>odd:
    for i in range(10):
        if x[i]%2!=0:
            x[i]=x[i]+1
else:
    for i in range(10):
        if x[i]%2==0:
            x[i]=x[i]-1
for i in range(10):
    print(x[i],end=' ')'''
#task6
'''from random import *
x=[0]*10
for i in range(10):
    x[i]=randint(1,15)
    print(x[i],end=' ')
print()
for i in range(10):
    for j in range(i+1,10):
        if x[i]==x[j]:
            x[j]=-1
for i in range(10):
    if x[i]>0:
        print(x[i],end=' ')'''
#task7
'''from random import *
x=[0]*10
for i in range(10):
    x[i]=randint(1,5)
    print(x[i],end=' ')
print()
for i in range(10):
    print(f'{x[i]} at {i}',end=' ')
    for j in range(i+1,10):
        if x[i]==x[j]:
            print(j,end=' ')
    print()'''
#task8
'''from import random *
arr = [0] * 20
arr[0] = randint(1, 10)
print(arr[0],end=' ')
for i in range(1, 20):
  arr[i] = arr[i-1] + randint(1, 3)
  print(arr[i],end=' ')
print()
for i in range(1, arr[19]):
  if i not in arr:
    print(i, end=" ")'''
#task9
'''from random import *
x=[0]*20
for i in range(20):
    x[i]=randint(0,9)
    print(x[i],end=' ')
print()
for i in range(2,18):
    s=0
    s=x[i-2]+x[i-1]+x[i+1]+x[i+2]
    av=s//4
    x[i]=av
for i in range(20):
    print(x[i],end=' ')'''
#comment here 
'''for i in range(2, 18):
    arr[i] = sum(arr[i-2:i+3]) // 4'''

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










#task11
'''from random import *
l=randint(3,7)
x=[0]*l
for i in range(l):
    x[i]=randint(0,9)
    print(x[i],end=' ')
print()
for i in range(1,l+1):
    for j in range(i):
        print(x[j],end=' ')
    print()'''
#task12
'''from random import *
l=randint(3,7)
x=[0]*l
for i in range(l):
    x[i]=randint(0,9)
    print(x[i],end=' ')
print()
for i in range(1,l+1):
    s=0
    for j in range(i):
        print(x[j],end=' ')
        s=s+x[j]
    print(' = ',s)'''
#task13
'''from random import *
x=[0]*10
for i in range(10):
    x[i]=randint(0,9)
    print(x[i],end=' ')
print()
for i in range(10-2):
    n=0
    for j in range(i,10+1):
        if n!=3:
            print(x[j],end=' ')
            n=n+1
    print()'''
#task14 A
'''from random import *
x=[[randint(0,9) for i in range(10)]for j in range(10)]                                                                                                                                                                 
for i in range(10):
    for j in range(10):
        print(x[i][j],end=' ')
    print()
print()
for i in range(10):
    for j in range(10):
        if i==j:
            print(x[i][j])
            break
        else:
            print(' ',end=' ')'''

#task14 B
'''from random import *
x=[[randint(0,9) for i in range(10)]for j in range(10)]                                                                                                                                                                 
for i in range(10):
    for j in range(10):
        print(x[i][j],end=' ')
    print()
print()
for i in range(10):
    for j in range(10):
        if x[i][j]==0:
            x[i][j]=1
for i in range(10):
    for j in range(10):
        print(x[i][j],end=' ')
    print()'''
#task15

'''from random import *
x=[[randint(0,9) for i in range(10)]for j in range(10)]                                                                                                                                                                 
for i in range(10):
    for j in range(10):
        print(x[i][j],end=' ')
    print()
print()
for i in range(10):
    for j in range(10):
        if x[i][j]==0:
            print(i,j)'''


























