#practice23
#task6
'''from random import *
file1=open('Matrix1.txt','w')
file2=open('Matrix2.txt','w')
n=10
file1.write(str(n)+'\n')
file2.write(str(n)+'\n')
for i in range(10):
    r=randint(2,6)
    c=randint(2,6)
    file1.write(str(r)+'\n')
    file2.write(str(r)+'\n')
    file1.write(str(c)+'\n')
    file2.write(str(c)+'\n')
    for j in range(r):
        for k in range(c):
            x=randint(0,9)
            y=randint(0,9)
            file1.write(str(x)+'\n')
            file2.write(str(y)+'\n')
file1.close()
file2.close()'''
#PRACTICE23 
#TASK7

'''file1=open('Matrix1.txt','r')
file2=open('Matrix2.txt','r')
file3=open('Sum.txt','w')
file4=open('Difr.txt','w')
n=int(file1.readline())
file2.readline()
file3.write(str(n)+'\n')
file4.write(str(n)+'\n')
r=int(file1.readline())
c=int(file1.readline())
file2.readline()
file2.readline()
for k in range(n):
    file3.write(str(r)+'\n')
    file3.write(str(c)+'\n')
    file4.write(str(r)+'\n')
    file4.write(str(c)+'\n')
    for i in range(r):
        for j in range(c):
            x=int(file1.readline())
            y=int(file2.readline())
            s=x+y
            d=x-y
            file3.write(str(s)+'\n')
            file4.write(str(d)+'\n')


file3.close()
file4.close()
file1.close()
file2.close()'''

'''#task9
file1=open('marks.txt','r')
n=int(file1.readline())
c=0
for i in range(n):
    file1.readline()
    x=int(file1.readline())
    if x!=-2:
        c=c+1
        file1.readline()
        file1.readline()
        file1.readline()
print('Total students who appear in exams are ',c)
file1.close()'''
#task10
'''file1=open('marks.txt','r')
n=int(file1.readline())
roll=int(input())
s=0
c=0
for i in range(n):
    r=int(file1.readline())
    x=int(file1.readline())
    if roll==r:
        if x==-2:
            print('NOt appear in exams')
            break
        elif x==-1:
            print('Not appear in this subject ')
        else:
            print(x)
            c=c+1
            s=s+x
                    
    if x!=-2:
        for j in range(3):
            a=int(file1.readline())
            if roll==r:
                if a==-1:
                    print('NOt appear in this subject ')
                elif a!=-1:
                    print(a)
                    s=s+a
                    c=c+1
av=s/(c*100)
print('Average ',av)
file1.close()'''
#task11
'''file1=open('marks.txt','r')
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
file1.close()'''
#task12
'''file1=open("marks.txt",'r')
file2=open("marks_appear.txt",'w')
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
file2.write(str(c)+'\n')
file1.close()
file3=open("marks.txt",'r')
n=int(file3.readline())
for i in range(n):
    roll=int(file3.readline())
    x=int(file3.readline())
    if x==-2:
        break
    elif x==-1:
        file3.readline()
        file3.readline()
        file3.readline()
    else:
        a=int(file3.readline())
        b=int(file3.readline())
        c==int(file3.readline())
        if a!=-1 and b!=-1 and c!=-1:
            file2.write(str(roll)+'\n')
            file2.write(str(x)+'\n')
            file2.write(str(a)+'\n')
            file2.write(str(b)+'\n')
            file2.write(str(c)+'\n')
file3.close()
file2.close()'''

#task13
file1=open("marks.txt",'r')
file2=open("absent.txt",'w')
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
absent=n-c
print('total students absents are ',absent)
file2.write(str(absent)+'\n')
file1.close()
file3=open("marks.txt",'r')
n=int(file3.readline())
for i in range(n):
    roll=int(file3.readline())
    x=int(file3.readline())
    if x==-2:
        file2.write(str(roll)+'\n')
        break
    elif x==-1:
        file2.write(str(roll)+'\n')
        file3.readline()
        file3.readline()
        file3.readline()
    else:
        a=int(file3.readline())
        b=int(file3.readline())
        c==int(file3.readline())
        if a==-1 or b==-1 or c==-1:
            file2.write(str(roll)+'\n')
            
            
file3.close()
file2.close()
        
        
    












    
