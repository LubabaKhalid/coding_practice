'''from random import *
n=int(input())
for i in range(n):
    x=list((input()))
    y=list((input()))
    if x==y :
        print('0')
    elif (x[0]==y[1] and x[1]==y[0]) or (x[0]==x[1] and y[0]==y[1]) :
        print(1)
    elif (x[0]==y[0] and x[1]!=y[1]) or (x[1]==y[1] and x[0]!=y[0]):
        print(1)
    elif (x[0]==x[1] and x[0]!=y[0] and y[0]!=y[1]) or (y[0]==y[1] and y[0]!=x[0] and x[0]!=x[1]):
        print(2)
    elif (x[0]==y[1] and x[1]!=y[0]) or ( y[0]==x[1] and y[1]!=x[0]):
        print(2)
    else:
        print(3)
    
'''
'''n=int(input())
for i in range(n):
    c=0
    x=list((input()))
    y=list((input()))
    if x==y:
        print(0)
    elif (x[0]==x[1] and y[0]==y[1] and x[0]!=y[0]):
        print(1)
    elif (x[0]==y[1] and x[1]==y[0]):
        print(1)
    elif x[0]==y[0] and x[1]==y[1]:
        print(1)
    elif x!=y:
        if x[0]!=x[1]:
            x[1]=x[0]
            c=c+1
        if x[0]!=y[0]:
            y[0]=x[0]
            c=c+1
        if x[0]!=y[1]:
            y[1]=x[0]
            c=c+1
        print(c)'''
#https://codeforces.com/contest/1721/problem/A
#image
'''tests = int(input())
for j in range(tests):
    alph = [0] * 26
    for i in range(2):
        ch1,ch2 = input().strip()
        alph[ord(ch1) - ord('a')] += 1
        alph[ord(ch2) - ord('a')] += 1
    totalColors = 0
    for i in range(26):
        if alph[i] != 0:
            totalColors += 1
            alph[i] = 0
    print(totalColors - 1)'''
#https://codeforces.com/contest/1721/problem/A
#Elevator
'''def main():
    m=int(input())
    for j in range(m):
        n=list(map(int,input().split()))
        a=n[0]
        b=n[1]
        c=n[2]
        t=a-1
        t1=abs(b-c)+(c-1)
        if t<t1:
            print(1)
        if t>t1:
            print(2)
        if t==t1:
            print(3)
main()
'''
#https://codeforces.com/contest/1740/problem/B
#B. Jumbo Extra Cheese 2
'''n=int(input())
for i in range(n):
    m=int(input())
    s=0
    b=0
    for j in range(m):
        x,y=list(map(int,input().split()))
        if x<y:
            s=s+x
            if b<y:
                b=y
        else:
            s=s+y
            if b<x:
                b=x
    print((2*s)+(2*b))'''
#https://codeforces.com/contest/1742/problem/A
#Sum
'''def main():
	n=int(input())
	for i in range(n):
		a=list(map(int,input().split()))
		if a[0]+a[1]==a[2] or a[1]+a[2]==a[0] or a[2] + a[0]==a[1]:
			print('yes')
		else:
			print('no')
main()'''
#Increasing
#https://codeforces.com/contest/1742/problem/B
'''x=int(input())
for i in range(x):
    n = int(input())
    a = list(map(int, input().split()))
    print(set(a))
    if len(set(a)) == n:
        print("YES")
    else:
        print("NO")'''
#https://codeforces.com/contest/299/submission/204700574
#B. Ksusha the Squirrel
'''n, k = map(int, input().split())
s = input().strip()

count = 0
for i in range(n):
    if s[i] == '#':
        count += 1
    else:
        count = 0
    if count >= k:
        print("NO")
        break
else:
    print("YES")'''
#Technical support
'''def solve():
    _ = int(input())
    t = input()
    ctn = 0
    for i in t:
        if i == 'Q':
            ctn += 1
        else:
            ctn -= 1
 
        if ctn < 0:
            ctn = 0
    if ctn == 0:
        return "Yes"
    else:
        return "No"
 
 
if _name_ == "_main_":
    t = int(input())
    for _ in range(t):
        print(solve())'''
    
    
        
        
            

        
