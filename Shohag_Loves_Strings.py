def fun(s):
    if len(s)>2:
        for j in range(len(s)-3):
            if s[j]!=s[j+1]!=s[j+2]:
                return s[j:j+3]
            
    else: 
        return -1
    return -1
t=int(input())
for i in range(t):
    s=input()
    print(fun(s))
    
    