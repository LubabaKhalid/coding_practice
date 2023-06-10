'''n=int(input())
x=list(set(map(int,input().split())))
z=sorted(x)
if len(z)>1:
    for i in range(len(z)):
        if i==len(z)-2:
            print(z[i])
else:
    print('NO')'''

n,p=map(int,input().split())
for i in range(n):
    x,y=map(int,input().split())
    if x>y:
        x,y=y,x
    if n==1:
        max=y
        min=x
    if n!=1:
        if i==0:
            max=x
            min=y
        if x>max:
            max=x
        if y<min:
            min=y
if n==1:           
    print(1)        
if n!=1:
    if p<=min and p>=max:
        print(1)
    if p<max:
        c=max-p
        print(c)
    if p>min:
        c1=p-min
    if p<min:
        c2=min-p
        if c1<c2:
            print(c1)
        elif c2<c1:
            print(c2)
    if p>min and p<max:
        print(-1)

    
    
