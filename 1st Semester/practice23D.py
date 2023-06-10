file=open('marks.txt','r')
file1=open('marks_appear.txt','w')
n=int(file.readline())
c=0
for i in range(n):
    file.readline()
    x=int(file.readline())
    if x!=-2 and x!=-1:
        a=int(file.readline())
        b=int(file.readline())
        c=int(file.readline())
        if a!=-1 and b!=-1 and c!=-1:
            c=c+1
print('How many students appeared in all subjects ',c)
file1.write(str(c)+'\n')
file.close()
file2=open('marks.txt','r')
n=int(file2.readline())
for i in range(n):
    roll=int(file2.readline())
    y=int(file2.readline())
    if y!=-2 and y!=-1:
        d=int(file2.readline())
        e=int(file2.readline())
        f=int(file2.readline())
        if d!=-1 and e!=-1 and f!=-1:
            file1.write(str(roll)+'\n')
            file1.write(str(y)+'\n')
            file1.write(str(d)+'\n')
            file1.write(str(e)+'\n')
            file1.write(str(f)+'\n')
file2.close()
file1.close()
            
