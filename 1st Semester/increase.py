n=int(input())
for i in range(n):
    m=int(input())
    b=input()
    k=list(map(str,b.split()))
    a='Yes'
    for j in range(len(k)):
        for l in range(len(k)):
            if j==l:
                break
            elif k[j]==k[i]:
                a="N0"
    print(a)        
