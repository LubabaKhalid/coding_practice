t=int(input())
for i in range(t):
    n=int(input())
    count=0
    arr=[]
    k=1
    flag=True
    j=2
    while j<100 and flag:
        if count==n:
            flag=False
        x=j%k
        y=(j+1)%(k)
        if x<y :
            arr.append(j)
            count+=1
            k=k+1
        j=j+1
    print(arr)
        