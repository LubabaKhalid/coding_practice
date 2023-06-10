'''n=int(input())
for i in range(n):
    x=input()
    l=list(x)
    for j in range(len(l)):
        if j%2==0:
            print(l[j],end='')
    print(end=' ')
    for j in range(len(l)):
        if j%2!=0:
            print(l[j],end='')
    print()'''
'''m=float(input())
tip=int(input())
tax=int(input())
t=(m*tip)/100
ta=(m*tax)/100
m=m+t+ta
print(round(m))'''

#Intro to Conditional Statements

'''n=int(input())
if n%2!=0:
    print('Weird')
elif n%2==0 and n>=2 and n<=5:
    print('Not Weird')
elif n%2==0 and n>=6 and n<=20:
    print('Weird')
elif n%2==0 and n>20:
    print('Not Weird')'''

n=int(input())
for i in range(n):
    
    x=int(input())
    for j in range(2):
        if x<0:
            print('Age is not valid, setting age to 0.')
            x=0
        if x<13:
            print('You are young')
        if x>=13 and x<18:
            print('You are teenager')
        if x>=18:
            print('You are old')
        x=x+3
    
    
    
