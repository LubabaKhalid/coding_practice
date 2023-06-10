s=(input())
s=list(s)
x=[]
SEN=-1
for i in range(len(s)):
    c=1
    if s[i]!=SEN:
        for j in range(i+1,len(s)):
            if s[i]==s[j]:
                c=c+1
                s[j]=SEN
        x.append(c)
y=len(x)
print(x)
t=0
f=0
c=0
for i in range(y-1):
    if x[0]==x[i+1]:
        t=t+1
    elif x[i]!=x[i+1]:
        f=f+1
        if x[0]==x[i+1]-1:
            c=c+1
        elif x[0]-1==x[i+1]==x[1]:
            c=c+1
            x[0]=x[0]-1
if f>1:
    print('NO') 
elif t==y-1 or t+1==y-1:
    print('YES')

