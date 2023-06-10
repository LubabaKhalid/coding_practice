file=open("prices.txt","r")
file1=open("highprices.txt","w")
file2=open("lowprices.txt","w")
n=int(file.readline())
print(n)
s=0
for i in range(n):
    x=int(file.readline())
    s=s+x
av=s/n
print("average",av)
file.close()
file=open("prices.txt","r")
m=int(file.readline())
for i in range(m):
    y=int(file.readline())
    if av<y:
        file1.write(str(y))
    else:
        file2.write(str(y))
file.close()
file1.close()
file2.close()

    
