from random import *
from time import *
#if element exists, return position of element, otherwise return -1
#This is binary search assuming list is sorted
def find_index(list, element):
    start = 0
    last = len(list)-1
    while start <= last:
        middle = (start + last) // 2
        if element == list[middle]:     return middle;
        elif element < list[middle]:    last = middle - 1;
        else:                           start = middle + 1;
    return -1

def main():
    length = 30
    x = [0]*length
    for i in range(length):
        x[i] = randint(0, 50)
    for j in range(length-1):
        for i in range(length-1):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
    print (x)
    for i in range(10):
        value = randint(0, 50)
        index = find_index(x, value)
        if index == -1: print(f'{value} does not exist in the list');
        else:           print(f'{value} exists at {index} position')

main()
