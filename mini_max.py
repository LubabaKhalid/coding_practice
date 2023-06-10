#Birthday Cake Candles

'''n=int(input())
ar = list(map(int, input().split()))
ar=sorted(ar)
x=len(ar)
c=0
for i in range(len(ar)):
    if ar[i]==ar[x-1]:
        c=c+1
print(c)'''


'''s=input()
h1 = ord(s[1]) - ord('0')
print(h1)
h2 = ord(s[0]) - ord('0')
print(h2)
hh =h2 * 10 + h1 % 10
print(hh)
if s[8]=='A':
    if hh==12:
        print('00',end='')
        for i in range(2,8):
            print(s[i],end='')
    else:
        for i in range(0,8):
            print(s[i],end='')
elif s[8]=='P':
    if hh==12:
        print(hh,end='')
        for i in range(2,8):
            print(s[i],end='')
    else:
        hh=hh+12
        print(hh,end='')
        for i in range(2,8):
            print(s[i],end='')'''
'''800 hacker rank
1551A - Polycarp and Coins
n=int(input())
for i in range(n):
    x=int(input())
    c1=c2=x//3
    r=x%3
    if r==2:
        c2+=1
    elif r==1:
        c1+=1
    print(c1,c2)'''

'''#not Accepted
n=int(input())
for i in range(n):
    x=int(input())
    c=0
    y=list(map(int,input().split()))
    for k in range(len(y)-1):
        if (y[k]+y[k+1])%2==1:
            c=c+1
    if c==len(y)-1:
        print('Yes')
    else:
        print('No')'''

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    oc = 0
    ec = 0
    for j in a:
        if j % 2 == 0:
            ec += 1
        else:
            oc += 1
    if oc == ec:
        print("Yes")
    else:
        print("No")


        
            
        


    
        
    
