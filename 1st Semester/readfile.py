file=open("lubaba.txt","r")
n=int(file.readline())
print(n)
for i in range(n):
    x=int(file.readline())
    print(x)
file.close()
