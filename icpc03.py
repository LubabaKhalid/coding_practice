t=int(input())
threshold=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    arr=[]
    for j in range(len(l)-1):
        dif=abs(l[j]-l[j+1])
        arr.append(dif)
    arr2=[]
    for j in range(len(arr)-1):
        dif=abs(arr[j]-arr[j+1])
        arr2.append(dif)
    for j in range(len(arr2)):
        if arr2[j]<threshold:
            print(0,end=' ')
        else:
            print(1,end=' ')
    print()
        
        