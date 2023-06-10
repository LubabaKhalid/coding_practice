file=open('marks.txt','r')
r=int(input('Roll no '))
n=int(file.readline())
s=0
c=0
for i in range(n):
    x=int(file.readline())
    if r==x:
        y=int(file.readline())
        if y!=-2:
            print(y)
            c=c+1
            s=s+y
            for j in range(3):
                a=int(file.readline())
                if a!=-1:
                    print(a)
                    c=c+1
                    s=s+a
                else:
                    print('failed to appear in the exam of this subject')
        else:
            print('Failed to appear in exam')
av=s/c
av1=s/4
print("average of marks in appear subjects ", av)
print("average of marks  ", av1)
file.close()

            
    
