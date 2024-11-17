import itertools
t=int(input())
for i in range(t):
    s1,f1,h1,s2,f2,h2,s3,f3,h3=map(int,input().split())
    moves={}
    moves['SFH']=(f1+h1)+(s2+h2)+(s3+f3)
    moves['SHF']=(f1+h1)+(s2+f2)+(s3+h3)
    moves['FSH']=(s1+h1)+(f2+h2)+(s3+f3)
    moves['FHS']=(s1+h1)+(f2+s2)+(f3+h3)
    moves['HSF']=(s1+f1)+(s2+h2)+(f3+h3)
    moves['HFS']=(s1+f1)+(h2+f2)+(s3+h3)
    min_moves=min(moves.values())
    minsequence=[key for key in moves.keys() if moves[key]==min_moves]
    minsequence=sorted(minsequence)
    print(f"{minsequence[0]} {min_moves}")
    
    
    
    