n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))

sum1 = 0
sum2 = 0
for i in range(n):
    sum1 += mat[i][i]
    sum2 += mat[i][n-i-1]

diff = abs(sum1 - sum2)
print(diff)
