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
for i in range(1,3):
    max=n[i-1]
    if n[i]>max:
        max=n[i]
    min=n[i-1]
    if min>n[i]:
       min=n[i]
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
for i in range(3,6):
    max=n[i-1]
    if n[i]>max:
        max=n[i]
    min=n[i-1]
    if min>n[i]:
       min=n[i]
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
for i in range(1,3):
    max=n[i-1]
    if n[i]>max:
        max=n[i]
    min=n[i-1]
    if min>n[i]:
       min=n[i]

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
for i in range(1,3):
    max=n[i-1]
    if n[i]>max:
        max=n[i]
    min=n[i-1]
    if min>n[i]:
       min=n[i]
print(end='    ')
print('Min: ',min,end='     ')
print('Max: ',max,end='     ')
av=s/3
print(f'Average: {av:.2f}')
