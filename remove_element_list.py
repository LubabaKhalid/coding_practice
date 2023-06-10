s=int(input('Size '))
max=0
for i in range(s):
    y=input()
    x=list(map(str,y.split()))
    for j in range(len(x)-1):
        for k in range(len(x)-1):
            if x[k]>x[k+1]:
                x[k],x[k+1]=x[k+1],x[k]
    for j in range(len(x)-1):
        print(x[j],end=' ')
    print()
    for j in range(len(x)-1):
        if j==len(x)-2:
            print(x[j])

    
    
    
