t=int(input())
lis=[5000,1000,500,200,100,50,20,10]
for i in range(t):
    n=int(input())
    print(f"Case #{i+1}:",end=' ')
    flag=False
    x=n//5000
    if x>0 or flag:
        flag=True
        n=n%5000
        print(f"{x}x5000",end=', ')
    x=n//1000
    if x>0 or flag:
        flag=True
        n=n%1000
        print(f"{x}x1000",end=', ')
    x=n//500
    if x>0 or flag:
        flag=True
        n=n%500
        print(f"{x}x500",end=', ')
    x=n//200
    if x>0 or flag:
        flag=True
        n=n%200
        print(f"{x}x200",end=', ')
    x=n//100
    if x>0 or flag:
        flag=True
        n=n%100
        print(f"{x}x100",end=', ')
    x=n//50
    if x>0 or flag:
        flag=True
        n=n%50
        print(f"{x}x50",end=', ')
    x=n//20
    if x>0 or flag:
        flag=True
        n=n%20
        print(f"{x}x20",end=', ')
    x=n//10
    if x>0 or flag:
        flag=True
        n=n%10
        print(f"{x}x10")
    