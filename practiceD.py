file=open('marks.txt','r')
file1=open('marks_appear.txt','w')
n=int(file.readline())
count=0
for i in range(n):
    roll=int(file.readline())
    x=int(file.readline())
    if x!=-2 or x!=-1:
        a=int(file.readline())
        b=int(file.readline())
        c=int(file.readline())
        if a!=-1 or b!=-1 or c!=-1:
            count=count+1
            file1.write(str(roll)+'\n')
            file1.write(str(x)+'\n')
            file1.write(str(a)+'\n')
            file1.write(str(b)+'\n')
            file1.write(str(c)+'\n')
    else:
        file.readline()
        file.readline()
        file.readline()
print('How many students appeared in all subjects ',c)
file1.write(str(c)+'\n')
file.close()
file1.close()
