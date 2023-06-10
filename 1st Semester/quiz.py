def fun(list,p):
    s=list[p-1]+list[p+1]
    av=s/2
    return av
from random import *
def main():
    len=10
    x=[0]*len
    for i  in range(len):
        x[i]=randint(1,10)
    print(x)
    for p in range(1,len-1):
        x[p]=fun(x,p)
    for p in range(len):
        print(f'{x[p]:.2f}',end=' ')
main()
