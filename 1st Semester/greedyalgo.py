#push() function is used tom insert element in stack and same apeend()
#pop() used to remove elements in LIFO order
#stack using list way
'''stack=[]
stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')
print('stack after append ' ,stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)'''
#dictionary
'''thisdict =	{
  'brand': 'Ford',   #string
  "model": False,   #boolean
  "year": 2000,     #int
  'color':['red','black','blue']    #list
}
print(thisdict)   #dictionary print
print(thisdict['year'])   #value of dictionary  and no duplicate key allow
print(len(thisdict))    #length of dictionary
print(type(thisdict)) #type
print(type(thisdict['year']))'''     #type of distionary key value

'''thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
print(len(thisdict))
print(type(thisdict))
print(type(thisdict['country']))'''


'''from collections import deque
stack=deque()
stack.append('a')
stack.append('b')
print('stack after append ',stack)
print(stack.pop())
stack.pop()
print(stack)'''

'''from queue import LifoQueue
stack=LifoQueue(maxsize=3)
print(stack.qsize())
stack.put('a')
stack.put('b')
stack.put('c')
print('full  ',stack.full())
print('stack  ',stack.qsize())
print('elements after pop in stack ')
print(stack.get())
print(stack.get())
print(stack.get())
print('stack empty ', stack.empty())'''

# stack implementation using a linked list.
# node class
#greedy
'''class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Stack:
    def __init__(self):
        self.head=Node("head")
        self.size=0
    def __str__(self):
        cur=self.head.next
        out=""
        while cur:
            out+=str(cur.value) + "->"
        return out[:-2]
    def getSize(self):
        return self.size
    def isEmpty(self):
        return self.size==0
    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value
    def push(self,value):
        node=Node(value)
        node.next=self.head.next
        self.head.next=node
        self.size+=1
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove=self.head.next
        self.head.next=self.head.next.next
        self.size-=1
        return remove.value



    
if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")
 
    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")'''

#Subarray with given sum

n=int(input())
s=int(input())
print('sum ',s)
sum=0
x=list(map(int,input().split()))
for i in range(n):
    sum=0
    idx=0
    for j in range(i,n):
        idx=j
        sum=sum+x[j]
        if sum==s:
            print(i+1,j+1)
            break
    if idx!=n-1:
        break
    







        



