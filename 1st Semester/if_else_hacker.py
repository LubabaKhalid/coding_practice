'''x=int(input())
if x%2!=0:
    print('Werid')
elif x>=2 and x<=5:
    if x%2==0:
        print('Not Werid')
elif  x>=6 and x<=20:
    if x%2==0:

        print('Werid')
else:
    if x>20:
        print('Not Werid')'''


'''a=int(input())
b=int(input())
print(a+b)
print(a-b)
print(a*b)'''

'''a=int(input())
b=int(input())
print(a//b)
print(a/b)'''

'''a=int(input())
for i in range(a):
    print(i*i)'''


'''a=int(input())
if a%4==0:
    print(True)
else:
    print(False)'''

''' def is_leap(year):
    leap = False
    if year%4==0:
        if year%100==0 and year%400==0:
            leap = True
        else:
            leap = False
    else:
        leap = False
    return leap
year = int(input())
print(is_leap(year))'''

'''a=int(input())
for i in range(1,a+1):
    print(i,end='')'''
s=list(map(str,input().split()))
for i in range(len(s)):
    if i==0:
        s[i]=chr(int(s[i])-32)
print(s)





































