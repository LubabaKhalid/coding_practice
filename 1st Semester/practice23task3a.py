file=open('marks.txt','r')
n=int(file.readline())
count=0
for i in range(n):
    x=int(file.readline())
    count=count+1
    if x!=(-2):
        for j in range(4):
            file.readline()
    else:
        count=count-1
print(count)
file.close()
