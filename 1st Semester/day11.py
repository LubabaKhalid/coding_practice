#2D array
'''if __name__ == '__main__':

    arr = []

    for i in range(6):
        arr.append(list(map(int, input().rstrip().split())))

t=[]
for row in range(0,4):
    for col in range(0,4):
        first=arr[row][col]+arr[row][col+1]+arr[row][col+2]
        mid=arr[row+1][col+1]
        third=arr[row+2][col]+arr[row+2][col+1]+arr[row+2][col+2]
        t.append(first+mid+third)
        
        
print(max(t))'''
#Day 12: Inheritance
'''class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
            Person.__init__(self, firstName, lastName, idNumber)
            self.firstName = firstName
            self.lastName = lastName
            self.idNumber = idNumber
            self.scores = scores
    def calculate(self):
        s=0
        grade=''
        l=len(scores)
        for i in scores:
            s=s+i
        avg=s//l
        if avg >= 90 and avg <= 100:
            grade = "O"
        elif avg >= 80 and avg < 90:
            grade = "E"
        elif avg >= 70 and avg < 80:
            grade = "A"
        elif avg >= 55 and avg < 70:
            grade = "P"
        elif avg >= 40 and avg < 55:
            grade = "D"
        else:
            grade = "T"
            
        return grade
            
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())'''
#Abstract classes
'''ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass
class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price
    def display(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nPrice: {self.price}")
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()'''

def Difference(a):
    print(a)
    x=0
    d=[]
    for i in range(len(a)-1):
        for j in range(len(a)):
            d=a[i]-a[i+1]
            if d>x:
                x=d
    print('maximum distance ',x)
        
        
e=int(input())
a=list((int,input().split()))
Difference(a)












