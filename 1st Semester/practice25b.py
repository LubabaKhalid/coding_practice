from random import*
marks = [0]*30
pas = 0
fail = 0
for i in range(len(marks)):
    marks[i] = randint(1,100)
    print(marks[i],end=' ')
    if marks[i] >=50:
        pas+=1

print('\n\nMarks of fail students:')
for i in range(len(marks)):
    if marks[i] <50:
        fail+=1
        print(f'{marks[i]}',end=' ')
        
average = pas/len(marks)*100
print(f'\n\nAverage of pass students: {average:.2f}')

greater = 0
below = 0
for i in range(len(marks)):
              
    if marks[i] > average:
              greater += 1
    if marks[i] < average:
        below += 1
greater = [0]*greater
below = [0]*below
a = 0
b = 0
print('\nMarks of students above average:')
for i in range(len(marks)):
              
    if marks[i] > average:    
        greater[a] = marks[i]
        print(f'{greater[a]}',end=' ')
        a = a+1
print()
print('\nMarks of Students below average:')
for i in range(len(marks)):
    if marks[i] < average:
        below[b] = marks[i]
         
        print(f'{below[b]}',end=' ')
        b = b+1
