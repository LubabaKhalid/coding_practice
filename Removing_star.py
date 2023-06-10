s=input()
for i in range(len(s)):
    if i=='*':
        del (i-1)
        del (i)
print(s)
