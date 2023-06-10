s=input()
for i in range(len(s)):
    if s[i]=='*':
        output = s[:i-1] + s[i+1: ]
    print(output)
        
