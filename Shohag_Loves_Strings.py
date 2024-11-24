def fun(s):
    for j in range(len(s)-1):
        if s[j]==s[j+1]:
            return s[j:j+2]
    for j in range(len(s)-2):
        a=set(s[j:j+3])
        if len(a)==3:
            return s[j:j+3]
    return -1
t=int(input())
for i in range(t):
    s=input()
    print(fun(s))
    
    