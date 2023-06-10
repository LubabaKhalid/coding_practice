file=open("lubaba.txt","w")
n=int(input())
file.writelines(str(n)+'\n')
for i in range(n):
    a=int(input())
    file.writelines(str(a)+'\n')
file.close()
