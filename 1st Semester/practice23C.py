file=open('marks.txt','r')
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
file.close()
                
        
