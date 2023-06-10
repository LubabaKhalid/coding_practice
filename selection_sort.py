from random import *
def main():
    x=[0]*10
    for i in range(10):
        print(x[i],end=' ')
    print(find_min_index(x))
main()
def find_min_index(x):
    for i in range(len(x)):
        if i==0:
            index=i
        elif x[index]>x[i]:
            index=i
        return index
