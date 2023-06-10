from random import *
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
main()
