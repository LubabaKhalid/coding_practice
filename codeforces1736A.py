tests = int(input())
for j in range(tests):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    match0, match1 = True, True
    needed0 = 0
    for i in range(n):
        if b[i] == 0 and a[i] == 1:
            match0 = False
            needed0 += 1
        if b[i] == 1 and a[i] == 0:
            match1 = False
            needed0 -= 1
        print(needed0)
    ans = abs(needed0) + (not match0 and not match1)
    print(ans)
