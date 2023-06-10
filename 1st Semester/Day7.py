'''n=int(input())
x=list(map(int,input().split()))
for j in range(n-1,-1,-1):
    print(x[j],end=' ')'''


'''if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().split()))
    for i in reversed(arr):
        print(i, end=" ")'''

'''class Person:
    def __init__(self,initialAge):
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = initialAge
    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
        self.age += 1
t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")'''

n=int(input())
x=[0]*n
for i in range(n):
    x[i]=input()
for j in range(n):
    m=input()
    for k in range(n):
        if m==x[k]:
            print(x[k])
        else:
            print('Not found')
    
    






