file1=open('marks.txt','r')
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
file1.close()
