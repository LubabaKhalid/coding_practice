t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=[0]*(k+1)
    for j in range(k):
        z,b=map(int,input().split())
        arr[z]+=b
    if n==k:
        print(sum(arr))
    else:
        
        arr=sorted(arr,reverse=True)
        print(sum(arr[:n]))
        