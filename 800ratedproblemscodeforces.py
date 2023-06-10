#118A - String Task
'''s=input()
n=len(s)
x=''
for i in range(n):
    if s[i]!='a' and s[i]!='A' and s[i]!='e' and s[i]!='E' and s[i]!='i' and s[i]!='I' and s[i]!='o'and s[i]!='y' and s[i]!='Y' and s[i]!='O' and s[i]!='u' and s[i]!='U':
        print('.',end='')
        if s[i]<='a' and s[i]>='z':
            print(s[i],end='')
        else:
            x=s[i].lower()
            print(x,end='')'''

#A. Stones on the Table
#https://codeforces.com/problemset/problem/266/A
'''n = int(input())
R = B = G = 0
array = input()
if n <= 50:
    for i in range(n):
        if array[i] == 'R' or array[i] == 'G' or array[i] == 'B':
            if array[i] == 'R':
                if i < n-1 and array[i+1] == 'R':
                    R += 1
            if array[i] == 'B':
                if i < n-1 and array[i+1] == 'B':
                    B += 1
            if array[i] == 'G':
                if i < n-1 and array[i+1] == 'G':
                    G += 1
    sum=R+B+G
    print(sum)'''

#https://codeforces.com/problemset/problem/791/A
#Bear and Big brother
'''a, b = map(int, input().split())
c=0
if a<=b:
    while(a<=b):
        a=a*3
        b=b*2
        c=c+1
    print(c)
else:
    print(c)'''
#A. Soldier and Bananas
'''k,n,w=map(int,input().split())
total=0
for i in range(1,w+1):
    total=total+k*i
if total <n:
    print(0)
else:
    print(total-n)'''
    
#Elephant
'''import math
n=int(input())
x=math.ceil(n/5)
print(x)'''
#A. Word
#https://codeforces.com/problemset/problem/59/A
'''s=input()
c=C=0
for i in range(len(s)):
    if s[i]>='a' and s[i]<='z':
        c=c+1
    elif s[i]>='A' and s[i]<='Z':
        C=C+1
if c>=C:
    print(s.lower())
else:
    print(s.upper())'''
#https://codeforces.com/problemset/problem/69/A
#A. Young Physicist
'''n=int(input())
x=y=z=0
for i in range(n):
    a,b,c=map(int,input().split())
    x=x+a
    y=y+b
    z=z+c
if x==0 and y==0 and z==0:
    print("YES")
else:
    print("NO")'''
#https://codeforces.com/problemset/problem/977/A
#Wrong Subtraction
'''n,k=map(int,input().split())
for i in range(k):
    x=n%10
    if x==0:
        n=n//10
    elif x!=0:
        n=n-1
print(n)'''        
#https://codeforces.com/problemset/problem/96/A
#A. Football
'''n=input()
if '0000000' in n or '1111111' in n:
    print('YES')
else:
    print("NO")'''

#https://codeforces.com/problemset/problem/110/A
#Nearly lucky number
'''n=(input())
c=0
for i in range(len(n)):
    if n[i]=='4':
        c=c+1
    elif n[i]=='7':
        c=c+1
if c==4 or c==7:
    print('YES')
else:
    print('NO')'''
#https://codeforces.com/problemset/problem/734/A
#A. Anton and Danik
'''n=int(input())
s=input()
a=0
for i in range(n):
    if s[i]=='A':
        a=a+1
d=n-a
if d>a:
    print('Danik')
elif a>d:
    print('Anton')
else:
    print('Friendship')'''
#Tram
#https://codeforces.com/problemset/problem/116/A
'''n=int(input())
c=m=0
for i in range(n):
    a,b=map(int,input().split())
    c=c-a
    c=c+b
    if c>m:
        m=c
print(m)'''
#https://codeforces.com/problemset/problem/41/A
#Translation

'''t=input()
s=input()
x=t[::-1]
if x==s:
    print('YES')
else:
    print('NO')'''

#B. Queue at the School
#https://codeforces.com/problemset/problem/266/B
'''a=list(map(int,input().split()))
c=input()
b=list(c)
d=''
while a[1]>0:
    i=0
    while i<(len(b)-1):
        if b[i]=='B' and b[i+1]=='G':
            b[i],b[i+1]=b[i+1],b[i]
            i=i+1
        i=i+1
    a[1]=a[1]-1
for i in range(len(b)):
    d=d+b[i]
print(d)'''

#A. Vanya and Fence
#https://codeforces.com/problemset/problem/677/A
'''n, h = map(int, input().split())
a = list(map(int, input().split()))
stn = 0
bnd = 0
for i in range(n):
    if a[i] > h:
        bnd += 1
    else:
        stn+= 1
print(2 * bnd + stn)'''
#https://codeforces.com/problemset/problem/271/A
#A. Beautiful Year
'''y=int(input())
while True:
    y=y+1
    a=y//1000
    b=y//100%10
    c=y//10%10
    d=y%10
    if a!=b and a!=c and a!=d and b!=c and b!=d and c!=d:
        break
print(y)'''

#Chat Room
#https://codeforces.com/problemset/problem/58/A
'''w=input()
hello='hello'
j=p=0
for i in range(len(w)):
    if w[i]==hello[j]:
        j=j+1
        p=p+1
    if j==5:
        break
if p==5:
    print('YES')
else:
    print('NO')'''
#https://codeforces.com/problemset/problem/1030/A
#A. In Search of an Easy Problem
'''n=int(input())
x=list(map(int,input().split()))
s=list(set(x))
if 1 in s:
    print('HARD')
else:
    print('EASY')'''
#https://codeforces.com/problemset/problem/122/A
#Lucky division
'''n=int(input())
if n%4==0 or n%7==0 or n%44==0 or n%47==0 or n%74==0 or n%77==0 or n%474==0 or n%447==0 or n%444==0 or n%477==0 or n%774==0 or n%744==0 or n%747==0 or n%777==0:
    print('YES')

else:
    print('NO')'''
#Twins
#https://codeforces.com/problemset/problem/160/A
'''n=int(input())
a=list(map(int,input().split()))
s=sum(a)//2
sorted(a,reverse=True)
c=ans=0
for i in range(n):
    ans=ans+a[i]
    c=c+1
    if ans>s:
        break
    
print(c)'''
# set
'''py_set = [2,1,2]
print(sorted(py_set, reverse=True))'''
# George and Accommodation
#https://codeforces.com/problemset/problem/467/A
'''n=int(input())
c=0
for i in range(n):
    p,q=map(int,input().split())
    if p+2<=q:
        c=c+1
print(c)'''
#https://codeforces.com/problemset/problem/344/A
#Magnets
'''n=int(input())
x0=input()
c=1
for i in range(1,n):
    x=input()
    if x0!=x:
        x0=x
        c=c+1
print(c)'''
#Present
#https://codeforces.com/problemset/problem/136/A
'''n = int(input())
givers = list(map(int, input().split()))
receivers = [0] * n
for i in range(n):
    receivers[givers[i]-1] = i+1
print(receivers)'''
#https://codeforces.com/problemset/problem/486/A
#Calculating Function
'''n=int(input())
if n%2==0:
    ans=n//2
    print(ans)
else:
    ans=(n-1)//2
    print(ans-n)'''
# Drinks
#https://codeforces.com/problemset/problem/200/B
'''from decimal import *
getcontext().prec=12
n=int(input())
m=list(map(int,input().split()))
print(Decimal(sum(m))/Decimal(len(m)))'''
#Even Odds
#https://codeforces.com/problemset/problem/318/A
'''def evenodd(n,k):
    numbers=[]
    o=e=1
    while o<=n:
        if o%2!=0:
            numbers.append(o)
        o=o+1
    while e<=n:
        if e%2==0:
            numbers.append(e)
        e=e+1
    return numbers[k]

n,k=map(int,input().split())
print(evenodd(n,k-1))''' #time limit exceed

'''import math      
n,k=map(int,input().split())
if k<=(n+1)/2:
    print(k*2-1)
else:
    print(math.ceil(k-(n+1)/2)*2)'''
#https://codeforces.com/problemset/problem/61/A
# Ultra-Fast Mathematician
'''x=input()
y=input()
s='' 
for i in range(len(x)):
    if x[i]==y[i]:
        s=s+'0'
    else:
        s=s+'1'
print(s)'''
#https://codeforces.com/problemset/problem/133/A
#HQ9+
'''def fun(s):
    for i in range(len(s)):
        if s[i]=='H' or s[i]=='Q' or s[i]=='9':
            return 'YES'
        
    return 'NO'
    

s=input()
print(fun(s))'''
#Hulk
#https://codeforces.com/problemset/problem/705/A
'''n=int(input())
print('I hate ',end='')
for i in range(2,n+1):
    print('that ',end='')
    
    if i%2==0:
        print('I love ',end='')
    else:
        print('I hate ',end='')
print('it')'''
#A. Is your horseshoe on the other hoof?
#https://codeforces.com/problemset/problem/228/A
'''s=list(map(int,input().split()))
x=len(set(s))
print(len(s)-x)'''
#https://codeforces.com/problemset/problem/405/A
# Gravity Flip
'''n=(input())
s=list(map(int,input().split()))
print(*sorted(s))'''
#I wanna be the guy
'''n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
s=[]
c=0
for i in range(1,x[0]+1):
    s.append(x[i])
for i in range(1,y[0]+1):
    s.append(y[i])
for i in range(1,n+1):
    if i not in s:
        c=1
        print('Oh, my keyboard!' )
        break
        
if c==0:
    print('I become the guy.' )'''
#https://codeforces.com/problemset/problem/479/A
#Expression
'''a=int(input())
b=int(input())
c=int(input())
s1=a+b*c
s2=a*(b+c)
s3=a*b*c
s4=(a+b)*c
s5=a+b+c
max=s1
if s2>max:
    max=s2
if s3>max:
    max=s3
if s4>max:
    max=s4
if s5>max:
    max=s5
print(max)'''
#https://codeforces.com/problemset/problem/1328/A
#Divisibility problem
'''import math
n=int(input())
for i in range(n):
    c=0
    a,b=map(int,input().split())
    if a%b==0:
        print(c)
    else:
        ans=math.ceil(a/b)*b
        print(ans-a)'''
#Arrival of the general
#https://codeforces.com/problemset/problem/144/A
'''n=int(input())
a=list(map(int,input().split()))
min=a[0]
min_index=0
max=a[0]
max_index=0
for i in range(1,n):
    if min>=a[i]:
        min=a[i]
        min_index=i
    if max<a[i]:
        max=a[i]
        max_index=i
if min_index<max_index:
    min_index=(n-1)-min_index
    print(min_index+max_index-1)
else:
    min_index=(n-1)-min_index
    print(min_index+max_index)''' 
#A. Insomnia cure
#https://codeforces.com/problemset/problem/148/A
'''k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
c=d
if k==1 or l==1 or m==1 or n==1:
    print(d)
else:
    for i in range(1,d+1):
        if i%k!=0 and i%l!=0 and i%m!=0 and i%n!=0 :
            c=c-1
            print(c)
    print(c)'''
#codeforces.com/problemset/problem/580/A
#A. Kefa and First Steps
'''n=int(input())
x=list(map(int,input().split()))
c=1
a=[]
for i in range(n-1):
    if x[i]<=x[i+1]:
        c=c+1
    else:
        a.append(c)
        c=1
a.append(c)
b=sorted(a)
print(b[len(b)-1])'''
#Pangram
#https://codeforces.com/problemset/problem/520/A
'''n=int(input())
s=input()
if len(set(s.lower()))==26:
    print('YES')
else:
    print('NO')'''
#Taxi
#https://codeforces.com/problemset/problem/158/B
'''n=int(input())
c=[0]*5
s=list(map(int,input().split()))
for i in range(n):
    c[s[i]]+=1
t=c[4]+c[3]+c[2]//2
c[1]-=c[3]
if c[2]%2==1:
    t=t+1
    c[1]-=2
if c[1]>0:
    t=t+(c[1]+3)//4
print(t)'''
# Dubstep
#https://codeforces.com/problemset/problem/208/A
'''s=input()
flag=True
i=0
while i<len(s):
    if s[i:i+3]=='WUB':
        i=i+3
        if not flag:
            print(' ',end='')
    else:
        print(s[i],end='')
        i=i+1
        flag=False'''
#A. cAPS lOCK
#https://codeforces.com/problemset/problem/131/A
'''s=input()
up=lo=0
for i in s:
    if i.isupper():
        up=up+1
    else:
        lo=lo+1
if up==len(s):
    for i in range(len(s)):
        print(s[i].lower(),end='')
elif s[0].islower() and (len(s)-1)==up:
    for i in range(len(s)):
        if i==0:
            print(s[i].upper(),end='')
        else:
            print(s[i].lower(),end='')
else:
    print(s)
'''
#
'''s=list((input().strip(',')))
s.sort()
c=0
for i in range(len(s)):
    if s[i]!='{' and s[i]!='}' and s[i]!=',' and s[i]!=' ':
        if s[i]!=s[i-1]:
            c=c+1
print(c)'''

#IQ test
'''n=int(input())
e=o=lasteven=lastodd=0
s=list(map(int,input().split()))
for i in range(n):
    if s[i]%2==0:
        e=e+1
        lasteven=i
    else:
        o=o+1
        lastodd=i
if e==1:
    print(lasteven+1)
else:
    print(lastodd+1)'''
#A. Hit the Lottery
#https://codeforces.com/problemset/problem/996/A
'''n=int(input())
coins=[100,20,10,5,1]
ans=0
for coin in coins:
    ans=ans+n//coin
    n=n%coin
print(ans)'''
#Games
#https://codeforces.com/problemset/problem/268/A
'''n=int(input())
h={}
g={}
for i in range(n):
    x,y=map(int,input().split())
    if h.get(x)==None:
        h[x]=1
    else:
        h[x]+=1
    if g.get(y)==None:
        g[y]=1
    else:
        g[y]+=1
c=0
for i in h:
    try:
        c=c+g[i]*h[i]
    except KeyError:
        pass
print(c)'''
#A. Anton and Polyhedrons
#https://codeforces.com/problemset/problem/785/A
'''n=int(input())
c=0
for i in range(n):
    s=input()
    if s=='Tetrahedron':
        c=c+4
    elif s=='Cube':
        c=c+6
    elif s=='Octahedron':
        c=c+8
    elif s=='Dodecahedron':
        c=c+12
    elif s=='Icosahedron':
        c=c+20
print(c)'''
    
#https://codeforces.com/problemset/problem/337/A
#Puzzles
'''n,m=map(int,input().split())
f=list(map(int,input().split()))
f.sort()
least=f[n-1]-f[0]
for i in range(1,m-n+1):
    dif=f[i+n-1]-f[i]
    if dif<least:
        least=dif
print(least)'''
# Amusing Joke
#https://codeforces.com/problemset/problem/141/A
'''a=input()
b=input()
c=input()
s=a+b
if sorted(s)==sorted(c):
    print('YES')
else:
    print('NO')'''
# Candies and Two Sisters
#https://codeforces.com/problemset/problem/1335/A
'''import math
n=int(input())
for i in range(n):
    s=int(input())
    ans=(math.ceil(s/2)-1)
    print(ans)'''
#https://codeforces.com/problemset/problem/4/C
#C. Registration system
'''n=int(input())
d={}
for i in range(n):
    s=input()
    if s in d:
        print(s+str(d[s]))
        d[s]=d[s]+1
    else:
        print('OK')
        d[s]=1'''

#A. Fox And Snake
#https://codeforces.com/problemset/problem/510/A
'''n,m=map(int,input().split())
for i in range(1,n+1):
    if i%2==1:
        for j in range(m):
            print('#',end='')
        print()
    elif i%4==0:
        print('#',end='')
        for j in range(m-1):
            print('.',end='')
        print()
    else:
        for j in range(m-1):
            print('.',end='')
        print('#')'''
#https://codeforces.com/problemset/problem/230/A
#Dragon
'''while True:
    try:
        s, n = map(int, input().split())
        a = []
        for i in range(n):
            x, y = map(int, input().split())
            a.append((x, y))
        a.sort()
        for i in range(n):
            if s <= a[i][0]:
                print("NO")
                break
            else:
                s += a[i][1]
        else:
            print("YES")
    except:
        break'''

#https://codeforces.com/problemset/problem/492/B
#. Vanya and Lanterns
'''n,l=map(int,input().split())
p=list(map(int,input().split()))
p.sort()
r=max(p[0],l-p[-1])*2
for i in range(n-1):
    r=max(r,p[i+1]-p[i])
print(r/2)'''

#Police Recruits
#https://codeforces.com/problemset/problem/427/A
'''n=int(input())
c=list(map(int,input().split()))
t=a=0
if c[0]==-1:
    t=t+1
else:
    a=a+c[0]
for i in range(1,n):
    if c[i]==-1:
        if a>0:
            a=a-1
        else:
            t=t+1
    else:
        a=a+c[i]
print(t)'''
#codeforces.com/problemset/problem/155/A
#I_love_%username%
'''n=int(input())
point=list(map(int,input().split()))
max=min=point[0]
a=0
for i in range(n):
    if point[i]>max:
        max=point[i]
        a=a+1
    if point[i]<min:
        min=point[i]
        a=a+1
print(a)'''
#T-primes
#https://codeforces.com/problemset/problem/230/B
'''n=int(input())
x=list(map(int,input().split()))
for i in range(n):
    c=0
    for j in range(1,x[i]+1):
        if x[i]%j==0:
            c=c+1
    if c==3:
        print('YES')
    else:
        print('NO')
'''
#A. New Year and Hurry
#https://codeforces.com/problemset/problem/750/A
'''n,k=map(int,input().split())
res,s,c=240-k,0,0
for i in range(1,n+1):
    s=s+5*i
    if s>res:
        break
    c=c+1
print(c)'''
#B. Xenia and Ringroad
#https://codeforces.com/problemset/problem/339/B
'''n,m=map(int,input().split())
loc=1
ans=0
s=list(map(int,input().split()))
for i in range(m):
    if s[i]>=loc:
        ans+=(s[i]-loc)
    else:
        ans+=n-(loc-s[i])
    loc=s[i]
print(ans)
'''
#A. Sum of Round Numbers
#https://codeforces.com/problemset/problem/1352/A
'''t=int(input())
for i in range(t):
    l=[]
    c=0
    n=int(input())
    if n>=1000:
        s=(n//1000)*1000
        n=n%1000
        l.extend([s])
        c=c+1
    if n>=100:
        s=(n//100)*100
        n=n%100
        l.extend([s])
        c=c+1
    if n>=10:
        s=(n//10)*10
        n=n%10
        l.extend([s])
        c=c+1
    if n<10 and n>0:
        l.extend([n])
        c=c+1
    print(c)
    print(*l)'''
# Vasya the Hipster
#https://codeforces.com/problemset/problem/581/A
'''a,b=map(int,input().split())
s=0
if a>b:
    a=a-b
    s=a//2
    print(b,s)
elif b>a:
    b=b-a
    s=b//2
    print(a,s)
elif a==b:
    print(a,s)'''
#A. The New Year: Meeting Friends
#https://codeforces.com/problemset/problem/723/A
'''x=list(map(int,input().split()))
x.sort()
print((x[1]-x[0])+(x[2]-x[1]))
'''
#https://codeforces.com/problemset/problem/732/A
#A. Buy a Shovel
'''k,r=map(int,input().split())
n=0
ans=0
while True:
    if n!=0 and (10*n)%k==0:
        ans=(10*n)//k
        break
    if (10*n+r)%k==0:
        ans=(10*n+r)//k
        break
    n=n+1
print(ans)'''
#. Game With Sticks
#https://codeforces.com/problemset/problem/451/A
'''n=list(map(int,input().split()))
n.sort()
if n[0]%2==0:
    print('Malvika')
else:
    print('Akshat')'''
# Restoring Three Numbers
#https://codeforces.com/problemset/problem/1154/A
'''n=list(map(int,input().split()))
n.sort()
for i in range(3):
    print(n[3]-n[i],end=' ')
print()'''
#A. Remove Smallest
#https://codeforces.com/problemset/problem/1399/A
'''import sys
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        if n == 1:
            print("YES")
            continue
        a.sort()
        v = []
        for i in range(1, n):
            dif = abs(a[i] - a[i-1])
            v.append(dif)
        v.sort(reverse=True)
        if v[0] > 1:
            print("NO")
        else:
            print("YES")

if __name__ == '__main__':
    main()'''


n=int(input())
for i in range(n):
    x=int(input())
    a=list(map(int,input().split()))
    if x==1:
        print('YES')
        continue
    a.sort()
    v=[]
    for j in range(1,x):
        dif=a[j]-a[j-1]
        v.append(dif)
    v.sort(reverse=True)
    print(v)
    if v[0]>1:
        print('NO')
    else:
        print('YES')




























       
        
        












