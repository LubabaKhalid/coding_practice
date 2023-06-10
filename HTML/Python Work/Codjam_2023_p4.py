from math import ceil
def solve():
    n = int(input())
    ch = 26
    i = 1
    while n>ch:
        n-=ch
        ch*=i+1
        i+=1
    n = ceil(n/i)
    print(chr(n-1+ord("A")))
t = int(input())
for i in range(t):
    print(f"Case #{i+1}: ",end="")
    solve()
