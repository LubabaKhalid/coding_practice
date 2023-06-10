#Binary maxOnes
'''def maxConsecutiveOnes(x):
    count = 0
    while (x!=0):
        x = (x & (x << 1))
  
        count=count+1
    return count
n=int(input())
print(maxConsecutiveOnes(n))'''

n=input()
m=input()
x=''
x=n^m
print(x)
