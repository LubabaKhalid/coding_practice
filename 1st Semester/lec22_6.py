from random import *
#Function to add elements in order
def add_in_order(list, element, size):#may be empty positions atf the list
    i = 0
    while list[i] < element and i < size:
        i += 1
    for j in range(size, i - 1, -1):
        list[j] = list[j - 1]
    list[i] = element

def main():
    length = 6
    x = [0]*length
    for i in range(length):
        value = randint(0, 100)
        print("Valiue ",value)
        add_in_order(x, value, i)
    print(x)

main()
