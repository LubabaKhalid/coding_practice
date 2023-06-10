from random import *
file1=open("matrix_set1","w")
file2=open("matrix_set2","w")
n=10
file1.write(str(n)+'\n')
file2.write(str(n)+'\n')
for i in range(n):
    r=randint(2,6)
    c=randint(2,6)
    file1.write(str(r)+'\n')
    file1.write(str(c)+'\n')
    file2.write(str(r)+'\n')
    file2.write(str(c)+'\n')
    for j in range(r):
        for k in range(c):
            x=randint(0,9)
            y=randint(0,9)
            file1.write(str(x)+'\n')
            file2.write(str(y)+'\n')
file1.close()
file2.close()

            
    
                        
    
