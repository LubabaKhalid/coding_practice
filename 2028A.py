t=int(input())
for _ in range(t):
    m,a,b=map(int,input().split())
    s=(input())*15
    
    if m==1:
        if s[0]=="N" and a==0:
            print("YES")
        elif s[0]=="E" and b==0:
            print("YES")
        else:
            print("NO")
        
    else:
        x=0
        y=0
        flag=False
        for c in range(len(s)):
            if s[c]=="N":
                y=y+1
            elif s[c]=="E":
                x=x+1
            elif s[c]=="W":
                x=x-1
            elif s[c]=="S":
                y=y-1
            if x==a and y==b:
                flag=True
                print("YES")
                break
        if not flag:
            print("NO")
            
            
    