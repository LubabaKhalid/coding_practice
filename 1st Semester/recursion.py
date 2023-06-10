
'''def printFun(test): 
    if (test < 1):
        return
    else: 
        print(test, end=" ")
        printFun(test-1)  
        print(test, end=" ")
        return
    
test = 10
printFun(test)'''
#factorial
'''def factorial(x):
    if x<=1:
        return 1
    else:
        return x*factorial(x-1)
n=int(input())
print(factorial(n))'''
# Function for fibonacci
'''def fib(n):
    if (n == 0):
        return 0
    if (n == 1 or n == 2):
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))

n = 10
print("Fibonacci series of 5 numbers is :",end=" ")
for i in range(0,n):
    print(fib(i),end=" ")'''
#x(x+1)x(x+1)/2 + y. For example, if x is 5 and y is 2, then fun should return 15 + 2 = 17.
'''def fun1(x, y) :
  
    if (x == 0) :
        return y
    else :
        return fun1(x - 1, x + y)
x=int(input())
y=int(input())
print(fun1(x,y))'''

'''Example 1:

Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements 
from 2nd position to 4th position 
is 12.'''
















    
