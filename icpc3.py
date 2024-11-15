def isPrime(x):
    if x<2:
        return False
    if x==2:
        return True
    for i in range(2,x//2+1):
        if x%i==0:
            return False
    return True
        
    
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    ans_x=isPrime(x)
    ans_y=isPrime(y)
    if ans_x and ans_y:
        print(f"Case #{i}:",x+y)
    elif ans_x or ans_y:
        print(f"Case #{i}: ",x*y)
    else:
        print(f"Case #{i}: not possible")
        
    