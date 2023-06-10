from random import *
n=[0]*12
print('Monthly Sales : ',end=' ')
for i in range(len(n)):
    n[i]=randint(10,99)
    print(n[i],end=' ')
print()
print()
print('Quarter 1 : ',end=' ')
s=0
for i in range(3):
    print(n[i],end=' ')
    s=s+n[i]
    max=n[0]
    if max<n[1]:
        max=n[1]
    if max<n[2]:
        max=n[2]
    min=n[0]
    if min>n[1]:
        min=n[1]
    if min>n[2]:
        min=n[2]
print(end='    ')
print('Min: ',min,end='     ')
print('Max: ',max,end='     ')
av=s/3
print(f'Average: {av:.2f}')
print('Quarter 2 : ',end=' ')
s=0
for i in range(3,6):
    print(n[i],end=' ')
    s=s+n[i]
    max=n[3]
    if max<n[4]:
        max=n[4]
    if max<n[5]:
        max=n[5]
    min=n[3]
    if min>n[4]:
        min=n[4]
    if min>n[5]:
        min=n[5]
print(end='    ')
print('Min: ',min,end='     ')
print('Max: ',max,end='     ')
av=s/3
print(f'Average: {av:.2f}')
print('Quarter 3 : ',end=' ')
s=0
for i in range(6,9):
    print(n[i],end=' ')
    s=s+n[i]
    max=n[6]
    if max<n[7]:
        max=n[7]
    if max<n[8]:
        max=n[8]
    min=n[6]
    if min>n[7]:
        min=n[7]
    if min>n[8]:
        min=n[8]
print(end='    ')
print('Min: ',min,end='     ')
print('Max: ',max,end='     ')
av=s/3
print(f'Average: {av:.2f}')
print('Quarter 4 : ',end=' ')
s=0
for i in range(9,12):
    print(n[i],end=' ')
    s=s+n[i]
    max=n[9]
    if max<n[10]:
        max=n[10]
    if max<n[11]:
        max=n[11]
    min=n[9]
    if min>n[10]:
        min=n[10]
    if min>n[11]:
        min=n[11]
print(end='    ')
print('Min: ',min,end='     ')
print('Max: ',max,end='     ')
av=s/3
print(f'Average: {av:.2f}')



    
    
    
    
