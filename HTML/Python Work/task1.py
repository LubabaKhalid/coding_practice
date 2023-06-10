file=open("lu.txt","r")
n=int(file.readline())
i=1
while i<=n:
    print(file.readline(),end='')
    i=i+1
file.close()
