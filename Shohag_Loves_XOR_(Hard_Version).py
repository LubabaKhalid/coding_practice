t=int(input())
for i in range(t):
    x,m=map(int,input().split())
    m+=1
    s=0
    for j in range(1,min(x,m)):
        if (x^j)%j==0:
            s+=1
    while m:
        z=m&-m
        m=m^z
        t=m^x
        t=t^t&(z-1)
        s=s+(t+z+x-1)//x-(t+x-1)//x
    print(s-1)
        
        