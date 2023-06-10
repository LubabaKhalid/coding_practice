#Capitalize()
'''s=list(map(str,input().split()))
for i in range(len(s)):
    print(s[i].capitalize(),end=' ')'''

'''def solve(s):
    s=s.split(" ")
    for i in range(len(s)):
        s[i]=s[i].capitalize()
    m=" ".join(s)
    return m
def main():
    s=input()
    print(solve(s))
main()'''
#The Minion Game
'''def minion_game(string):
    s=k=0
    vowel=['A','Ë','I','O','U']
    for i in range(len(string)):
        if string[i] in vowel:
            k+=len(string[i:])
        else:
            s+=len(string[i:])
    if s>k:
        print("Stuart",s)
    elif k>s:
        print("Kevin",k)
    else:
        print("Draw")
            
            

if __name__ == '__main__':
    s = input()
    minion_game(s)'''

'''vowels = 'AEIOU'
    stuart_score = 0
    kevin_score = 0
    n = len(string)
    for i in range(n):
        if string[i] in vowels:
            kevin_score += n - i
        else:
            stuart_score += n - i
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")'''

'''s=input()
k=int(input())
w=''
i=0
while i<=len(s)-k:
    w=''
    for j in range(k):
        if s[i+j] not in w:
            w+=s[i+j]
        
    i=i+k
    print(w)'''

#Mutations
'''def mutate_string(string, position, character):
    l=list(string)
    l[position]=character
    string=''.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)'''
#Find a string
'''def count_substring(string, sub_string):
    total = 0
    for i in range(len(string)):
        if string[i: i +len(sub_string) ] == sub_string:
            total+=1
    return total
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)'''

'''In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.'''


s=input()
alpha=digi=alphnu=up=lo=False
for i in s:
    if i.isdigit()==True:
        digi=True
    if i.isalnum()==True:
        alphnu=True
    if i.isalpha()==True:
        alpha=True
    if i.isupper()==True:
        up=True
    if i.islower()==True:
        lo=True
print(alphnu)
print(alpha)
print(digi)
print(lo)
print(up)

    
    
    
    































        
        
