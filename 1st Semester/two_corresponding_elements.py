from random import *
def main():
    size=int(input())
    x=[0]*size
    y=[0]*size
    for i in range(len(x)):
        x[i]=randint(1,20)
        y[i]=randint(1,20)
    print(x)
    print(y)
    for i in range(len(x)):
        z[i]=fun(x,y)
        print(z)
main()

    
def fun(x,y):
    for i in range(len(x)):
        if x[i]==y[i]:
            return 2
        elif x[i]>y[i]:
            return 1
        elif x[i]<y[i]:
            return -1
        return 0
    
