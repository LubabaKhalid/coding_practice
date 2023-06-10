file=open('marks.txt','r')
file1=open('absent.txt','w')
n=int(file.readline())
c=c+1
for i in range(n):
    r=int(file.readline())
    x=int(file.readline())
    if x==-2:
        c=c+1
    else:
        file.readline()
        file.readline()
        file.readline()
file1.write(str(c)+'\n')
file.close()
file2=open('marks.txt','r')
n=int(file2.readline())
for i in range(n):
    r=int(file.readline())
    x=int(file.readline())
    if x==-2:
        file1.write((str(r)+'\n')
    elif x!=-2:
        file2.readline()
        file2.readline()
        file2.readline()
file1.close()
file2.close()

        

        
    
