from random import *
file=open("prices.txt","w")
n=int(input())
file.write(str(n)+'\n')
for i in range(n):
    x=randint(0,100)
    print(x)
    file.write(str(x)+'\n')
file.close()
    
