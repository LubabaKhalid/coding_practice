file=open('marks.txt','r')
n=int(file.readline())
count=0
for i in range(n):
    x=int(file.readline())
    b=int(file.readline())
    count=count+1
    if b!=(-2):
        for j in range(3):
            file.readline()
    else:
        count=count-1
print(count)
file.close()
