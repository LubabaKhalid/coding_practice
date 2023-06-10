file1=open('marks.txt','r')
n=int(file1.readline())
c=0
for i in range(n):
    file1.readline()
    x=int(file1.readline())
    if x==-2:
        break
    elif x==-1:
        file1.readline()
        file1.readline()
        file1.readline()
    else:
        a=int(file1.readline())
        b=int(file1.readline())
        c==int(file1.readline())
        if a!=-1 and b!=-1 and c!=-1:
            c=c+1
print('total students appear in all subjects are ',c)
file1.close()
        
