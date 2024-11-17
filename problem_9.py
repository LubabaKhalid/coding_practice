def min_energy(N, p):
    dp = [[0] * N for _ in range(N)]
    
    for length in range(2, N + 1):  
        for i in range(N - length + 1):  
            j = i + length - 1  
            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1])
    
    return dp[0][N - 1]

t = int(input())
for _ in range(t):
    N = int(input())  
    p = list(map(int, input().split())) 
    print(min_energy(N, p))
