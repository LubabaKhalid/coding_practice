#4A - Watermelon
'''n=int(input())
x=n%2
if n>2:
    if n%2==0:
        if x%2==0:
            print('YES')
        elif (x+1)%2==0 and (x-1)%2==0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')'''
#A. Way Too Long Words
#https://codeforces.com/problemset/problem/71/A
'''i=int(input())
for j in range(i):
    n=input()
    if len(n)>10:
        x=len(n)-2
        print(f'{n[0]}{x}{n[len(n)-1]}')

    else:
        print(n)'''
#A. Team
#https://codeforces.com/problemset/problem/231/A
'''n=int(input())
sol=0
for i in range(n):
    c=0
    x=list(map(int,input().split()))
    for j in range(3):
        if x[j]==1:
            c=c+1
    if c>=2:
        sol=sol+1
print(sol)'''
#A. Theatre Square
#https://codeforces.com/problemset/problem/1/A
'''import math
n, m, a = map(int, input().split())
h = math.ceil(n / a)
v = math.ceil(m / a)
flags = h * v
print(flags)'''
#A. Next Round
'''n,k = map(int, input().split())
x= list(map(int, input().split()))

t = 0
for i in range(n):
    if x[i] >= x[k-1] and x[i] != 0:
        t += 1
print(t)'''
#A. Domino piling
'''m,n=map(int,input().split())
t=int((m*n)/(2*1))
print(t)'''

#https://codeforces.com/problemset/problem/282/A
'''n=int(input())
x=0
for i in range(n):
    m=input()
    if m=='X++' or m=='++X':
        x=x+1
    elif m=='X--' or m=='--X':
        x=x-1
print(x)'''
#A. Beautiful Matrix
#https://codeforces.com/problemset/problem/263/A
'''a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=list(map(int,input().split()))
if sum(a)!=0:
    x,y=1,a.index(1)+1
elif sum(b)!=0:
    x,y=2,b.index(1)+1
elif sum(c)!=0:
    x,y=3,c.index(1)+1
elif sum(d)!=0:
    x,y=4,d.index(1)+1
elif sum(e)!=0:
    x,y=5,e.index(1)+1
r,c=3,3
print(abs(x-r)+abs(y-c))'''
#A. Petya and Strings
#https://codeforces.com/problemset/problem/112/A
'''f=input()
s=input()
f=f.lower()
s=s.lower()
c=0
if f>s:
    print(1)
elif f<s:
    print(-1)
elif f==s:
    print(0)'''
#https://codeforces.com/problemset/problem/339/A
'''arr = input().split('+')
arr.sort()
st = '+'.join(arr)
print(st)'''

#https://codeforces.com/problemset/problem/281/A
#Word Capitalization
'''s=input()
print(s[0].capitalize()+s[1::])'''
#
#insertion sort
'''def insertionSort(nlist):
   for i in range(1,len(nlist)):

     currentvalue = nlist[i]
     position = i

     while position>0 and nlist[position-1]>currentvalue:
         nlist[position]=nlist[position-1]
         position = position-1

     nlist[position]=currentvalue

nlist = [14,46,43,27,57,41,45,21,70]
insertionSort(nlist)
print(nlist)'''
#shell sorting
'''A=[6,3,2,7,5,5]
A=sorted(A)
print(A)
for i in  range(len(A)//2):
    print(A[i],A[~i])'''
#merge two lists
'''def merge_sort(a):
    if len(a)<=1:
        return 
    
    mid=len(a)//2
    left=a[:mid]
    right=a[mid:]
    merge_sort(left)
    merge_sort(right)
    merge_two_sorted_lists(left,right,a)
    


    
def merge_two_sorted_lists(a,b,arr):
    len_a=len(a)
    len_b=len(b)
    i=j=k=0
    while i<len_a and j<len_b:
        if a[i]<=b[j]:
            arr[k]=(a[i])
            i=i+1
        else:
            arr[k]=(b[j])
            j=j+1
        k=k+1
    while i<len_a:
        arr[k]=(a[i])
        i=i+1
        k=k+1
    while j<len_b:
        arr[k]=(b[j])
        j=j=1
        k=k+1
        
def main():
    a=[4,2,8,13,11,20,19,1]
    merge_sort(a)
    print(a)
main()'''

#A. Do Not Be Distracted!
#https://codeforces.com/problemset/problem/1520/A
t = int(input())

for j in range(t):
    n = int(input())
    s = input().strip()
    ss = ''
    for i in range(n):
        if s[i] in '13579':
            ss += s[i]
        if len(ss) == 2:
            break
    if len(ss) == 2:
        print(ss)
    else:
        print(-1)
    
        
        
    
    























