t=int(input())
for i in range(t):
    s=list(input())
    q=int(input())
    for j in range(q):
        l,r=map(int,input().split())
        s[l-1]=str(r)
        start=max(0,i-3)
        end=min(len(s)-1,i+3)
        flag=False
        for k in range(start,end-2):
            if ''.join(s[j:j+4])=="1100":
                flag=True
                break
        
        if flag:
            print("YES")
        else:
            print("NO")
        