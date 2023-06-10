#26
#task1
'''from random import *
s=randint(5,10)
x=[0]*s
for i in range(s):
    x[i]=randint(10,30)
    print(x[i],end=' ')
print()
print('Pairs in order:')
for i in range(s-1):
    if x[i]<x[i+1]:
        print(x[i],x[i+1])'''

'''from random import *
def corresponding_ele(x,y,s):
    print('larger: ',end=' ')
    for i in range(s):
        if x[i]>y[i]:
            print(x[i],end=' ')
        else:
            print(y[i],end=' ')
    print()
    print('Smaller: ',end=' ')
    for i in range(s):
        if x[i]>y[i]:
            print(y[i],end=' ')
        else:
            print(x[i],end=' ')
    
def main():
    s=randint(5,10)
    x=[0]*s
    y=[0]*s
    print('list 1: ',end=' ')
    for i in range(s):
        x[i]=randint(10,30)
        y[i]=randint(10,30)
        print(x[i],end=' ')
    print()
    print('list 2: ',end=' ')
    for i in range(s):
        print(y[i],end=' ')
    print()
    corresponding_ele(x,y,s)
main()'''


'''x = [23, 45, 18, 23, 17, 45, 36, 23, 45, 18, 36, 45, 18, 17, 36, 23, 17]
y=[]
for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i]==x[j]:
            x[j]=-1
        
c=0           
for i in range(len(x)):
    if x[i]>-1:
        c=c+1
        print(x[i],end=' ')
print()
y=[]*(c-1)
n=0
for i in range(len(x)):
    if x[i]>-1:
        y[n]=x[i]
        n=n+1
print()
print(y)'''

#task1
'''x = [23, 45, 18, 23, 17, 45, 36, 23, 45, 18, 36, 45, 18, 17, 36, 23, 17]
y=x.copy()
for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i]==x[j]:
            x[j]=-1
for i in range(len(x)):
    print(y[i],end=' ')
print()
for i in range(len(x)):
    if x[i]>0:
        print(x[i],end=' ')'''

#task2
'''x = [23, 45, 18, 23, 17, 45, 36, 23, 45, 18, 36, 45, 18, 17, 36, 23, 17]
X=x.copy()
for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i]==x[j]:
            x[j]=-1
print('X: ',end=' ')
for i in range(len(x)):
    print(X[i],end=' ')
print()
c=0
for i in range(len(x)):
    if x[i]>0:
        c=c+1
Y=[0]*c
j=0
print('Y: ',end=' ')
for i in range(len(x)):
    if x[i]>0:
        Y[j]=x[i]
        j=j+1    
for i in range(len(Y)):
    print(Y[i],end=' ')'''
#task3
'''x = [23, 45, 18, 23, 17, 45, 36, 23, 45, 18, 36, 45, 18, 17, 36, 23, 17]
X=x.copy()
for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i]==x[j]:
            x[j]=-1
print('X: ',end=' ')
for i in range(len(x)):
    print(X[i],end=' ')
print()
c=0
for i in range(len(x)):
    if x[i]>0:
        c=c+1
Y=[0]*c
j=0
print('Y: ',end=' ')
for i in range(len(x)):
    if x[i]>0:
        Y[j]=x[i]
        j=j+1    
for i in range(len(Y)):
    print(Y[i],end=' ')
print()
C=[0]*c

for i in range(len(Y)):
    count=0
    for j in range(len(X)):
        if Y[i]==X[j]:
            count=count+1
    C[i]=count
print('C: ',end=' ')
for i in range(c):
    print(C[i],end=' ')'''


#task4
'''from random import *
r=int(input())
c=int(input())
n=[0]*r*c
for i in range(r*c):
    n[i]=randint(10,100)
for i in range(r*c):
    print(n[i],end=' ')
print()
m=0
for i in range(r):
    for j in range(c):
        print(n[m],end=' ')
        m=m+1
    print()'''


#task5
'''from random import *
x=[0]*16
for i in range(16):
    x[i]=randint(10,99)
    print(x[i],end=' ')
print()
m=0
for i in range(4):
    for j in range(4):
        print(x[m],end=' ')
        m=m+1
    print()
print('Principle Diagonal : ',end=' ')
for i in range(0,16,5):
    for j in range(16):
        if i==j:
            print(x[i],end=' ')
print()
print('Secondary diagonal: ',end=' ')
for i in range(3,16,3):
    for j in range(15):
        if i==j:
            print(x[i],end=' ')'''
#task6
'''from random import *
x=[0]*12
for i in range(12):
    x[i]=randint(10,99)
    print(x[i],end=' ')
print()
m=0
for i in range(4):
    c=0
    for j in range(3):
        print(x[m],end=' ')
        c=c+x[m]
        m=m+1
    print('= ',c)'''
'''from random import *
x=[0]*12
for i in range(12):
    x[i]=randint(5,10)
    print(x[i],end=' ')
print()
y=0
for i in range(4):
    for j in range(3):
        print(x[y],end=' ')
        y=y+1
    print()'''
  
from random import *
x=[[randint(0,9) for i in range(4)] for j in range(4)]
for i in range(4):
    for j in range(4):
        print(x[i][j],end=' ')
    print()
print('Principle diagonal ',end=' ')
for i in range(4):
    print(x[i][i],end=' ')
print()
i=0
print('secondary diagonal ',end=' ')
for j in range(3,-1,-1):
        print(x[i][j],end=' ')
        i=i+1
    














