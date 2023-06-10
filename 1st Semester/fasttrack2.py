#bear and balls
'''n=int(input())
m=list(map(int,input().split()))
m=sorted(set(m))
result='NO'
for i in range(len(m)-2):
    if m[i+2]-m[i]<=2:
        result='YES'
print(result)     '''

#Exam
'''x,y=map(int,input().split())
student=[]
maxscore=0
for i in range(x):

    student.append(input())
points=list(map(int,input().split()))
for q in range(y):
    answer={'A':0,'B':0,'C':0,'D':0,'E':0}
    for s in student:
        answer[s[q]]+=1
    maxpoint=max([answer[k] for k in answer]) * points[q]
    maxscore=maxscore+maxpoint
print(maxscore)'''

#lunch rush

'''

n,k=map(int,input().split())
joy=[]
f=[]
t=[]
for i in range(n):
    fi,ti=map(int,input().split())
    t.append(ti)
    f.append(fi)
for i in range(n):
    if t[i]>k:
        joy.append(f[i]-(t[i]-k))
    else:
        joy.append(f[i])
max=-10000000000
for i in range(n):
    if k==t[i]:
        max=joy[i]
        break
    elif max<joy[i]:
        max=joy[i]
print(max)'''

#A. Indian Summer

'''n=int(input())
name=[]
for i in range(n):
    x=input()
    name.append(x)
name=set(name)
print(len(name))'''

#B. Ksusha the Squirrel

'''n,m=map(int,input().split())
dot=0
has=0
x=input()
for i in range(n):
    if '.' in x:
        dot=dot+1
    if '#' in x:
        has=has+1
result='NO'
print(dot)
print(has)
if m==1:
    if dot==n:
        result='YES'
    else:
        result='NO'
elif m>1:
    if dot==m+1 and has==m and dot+has==n:
        result = 'YES'
    else:
        result='NO'
print(result)'''

#A. Codecraft III
n=input()
m=int(input())
c=0
x=['January','Feburary','March','April','May','June','July','August','September','october','November','December']
for i in range(len(x)):
    if n==x[i]:
        m=m+i
while m>11:
    m=m-11
    m=m-1
for i in range(len(x)):
    if m==i:
        print(x[i])
        break

        



























        
        
        
        



















    
        


    
    





























        

        
    

