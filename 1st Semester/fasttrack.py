n, m = map(int, input().split())
students = []
for i in range(n):
    students.append(input())
print(students)
points = list(map(int, input().split()))

max_score = 0
for q in range(m):
    answers = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
    for s in students:
        print(s[q])
        answers[s[q]] += 1
        
    max_points = max([answers[k] for k in answers]) * points[q]
    max_score += max_points
    print(max_score)

print(max_score)
        
