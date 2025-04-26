t=int(input())
for _ in range(t):
    n,a,b=map(int,input().split())
    s=list(input())
    m=len(s)
    x=0
    y=0
    c=0
    while c<m:
        if s[c]=="N":
            y=y+1
        elif s[c]=="E":
            x=x+1
        elif s[c]=="W":
            x=x-1
        elif s[c]=="S":
            y=y-1
        if x==a and y==b:
            print("YES")
            break
        elif ((x==a and y>b) or (x>a and y>b)) and (c==(m-1)):
            print("NO")
            break
        if c==(m-1):
            if x==0 and y==0:
                print("NO")
                break
            c=-1
        c=c+1
    