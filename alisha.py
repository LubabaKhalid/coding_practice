size=int(input())
x=[0]*size
for i in range(len(x)):
    x[i]=int(input())
for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i]==x[j]:
            x[j]=-1
for i in range(len(x)):
    if x[i]>=0:
        print(x[i],end=' ')
