def checkEvenOdd(arr):
    e=o=0
    for i in range(len(arr)):
        if i%2==0:
            e=e+arr[i]
        else:
            o=o+arr[i]
    if e==o:
        return "equal"
    elif e>o:
        return "even"
    else:
        return "odd"


arr=[1,2,3,4,5,6]
print(checkEvenOdd(arr))