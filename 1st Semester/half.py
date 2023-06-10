from random import *
e=[0]*12
q1=q2=q3=q4=0
firsthalf=sechalf=0
for i in range(12):
    e[i]=randint(1000,2000)
    print(e[i],end=' ')
    if i<6:
        firsthalf=firsthalf+e[i]
    else:
        sechalf=+e[i]
    if i<3:
        q1=q1+e[i]
    elif i<6:
        q2=q2+e[i]
    elif i<9:
        q3=q3+e[i]
    else:
        q4=q4+e[i]
print()
print('               Sale in two halves ')
print('First half : ',firsthalf)
print('Second half : ',sechalf)
print()
print('               Quarter wise Sale')
print('Sale in Quarter 1: ',q1)
print('Sale in Quarter 2: ',q2)
print('Sale in Quarter 3: ',q3)
print('Sale in Quarter 4: ',q4)
