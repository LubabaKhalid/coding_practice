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
    if p>max:
        print(p-max)
    elif p<min:
        print(min-p)
    else:
        print('0')
if n!=1:
        if p>=max and p<=min:
            print(0)
        elif max<=min:
            print(max-p)
        else:
            print('-1')
        
