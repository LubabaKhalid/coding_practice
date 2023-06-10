'''from random import *
s=randint(10,20)
x=[0]*s
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
'''from random import *
x=[0]*12
for i in range(len(x)):
    x[i]=randint(10,100)
    print(x[i],end=' ')
print()
for i in range(len(x)-1):
    if x[i]>x[i+1]:
        x[i],x[i+1]=x[i+1],x[i]
for i in range(len(x)):
    print(x[i],end=' ')'''

'''from random import *
def main():
    l=randint(5,15)
    x=[0]*l
    for i in range(l):
        x[i]=randint(0,100)
        print(x[i],end=' ')
    print()
    print('Pair in order : ')
    for i in range(l-1):
        if x[i]<x[i+1]:
            print(x[i],x[i+1])
main()'''

'''from random import *
def main():
    l=randint(5,15)
    x=[0]*l
    y=[0]*l
    for i in range(l):
        x[i]=randint(0,100)
        print(x[i],end=' ')
    print()
    for i in range(l):
        y[i]=randint(0,100)
        print(y[i],end=' ')
    print()
    for i in range(l):
        if x[i]<y[i]:
            print(y[i],end=' ')
        else:
            print(x[i],end=' ')
main()'''

'''from random import *
def main():
    l=randint(5,15)
    x=[0]*l
    y=[0]*l
    l1=[0]*l
    l2=[0]*l
    print('List 1:',end=' ')
    for i in range(l):
        x[i]=randint(0,100)
        print(x[i],end=' ')
    print()
    print('List 2:',end=' ')
    for i in range(l):
        y[i]=randint(0,100)
        print(y[i],end=' ')
    print()
    for i in range(l):
        if x[i]<y[i]:
            l1[i]=x[i]
        else:
            l1[i]=y[i]
    for i in range(l):
        if x[i]<y[i]:
            l2[i]=y[i]
        else:
            l2[i]=x[i]
    print('List 1: ',end=' ')
    for i in range(l):
        print(l1[i],end=' ')
    print()
    print('List 2: ',end=' ')
    for i in range(l):
        print(l2[i],end=' ')
main()'''
 
 '''from random import *
def main():
    c=0
    l=randint(5,15)
    x=[0]*l
    for i in range(l):
        x[i]=randint(0,100)
        print(x[i],end=' ')
    print()
    for i in range(l-2):
        if x[i]<x[i+1]<x[i+2]:
            c=1
        else:
            c=0
    if c==1:
        print('List is sorted')
    else:
        print('List not sorted')
main()'''




















    
