'''i = 4
d = 4.0
s = 'HackerRank '
sec_i=int(input())
sec_d=float(input())
sec_s=input()
print(i+sec_i)
print(d+sec_d)
print(s+sec_s)
'''

'''def simpleArraySum(ar):
    s=0
    for i in range(len(ar)):
        s=s+ar[i]
    return s

def main():
    ar_count=int(input())
    ar=list(map(int,input().split()))
    res= simpleArraySum(ar)
    print(res)
main()'''

'''def compareTriplets(a, b):
    ca=cb=0
    for i in range(len(a)):
        if a[i]>b[i]:
            ca=ca+1
        elif a[i]<b[i]:
            cb=cb+1  #2 lists and each corresponding element check
    return ca,cb
def main():
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    res=compareTriplets(a,b)
    print(' '.join(map(str,res)))
main()'''

'''def aVeryBigSum(ar):
    s=0
    for i in range(len(ar)):
        s=s+ar[i]
    return s
def main():
    ar_count=int(input().strip())
    ar=list(map(int,input().rstrip().split()))
    res=aVeryBigSum(ar)
    print(res)
main()'''


'''def diagonalDif(ar,n):
    sum1 = 0
    sum2 = 0
    for i in range(n):
        sum1 += ar[i][i]
        sum2 += ar[i][n-i-1]

    diff = abs(sum1 - sum2)
    return diff
    

def main():
    n=int(input().strip())
    ar=[]
    for i in range(n):
        ar.append(list(map(int,input().rstrip().split())))
    res=diagonalDif(ar,n)
    print(res)
main()'''

'''n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))

sum1 = 0
sum2 = 0
for i in range(n):
    sum1 += mat[i][i]
    sum2 += mat[i][n-i-1]
if sum1>sum2:
    diff=sum1-sum2
else:
    diff=sum2-sum1   #left and right diagonal of square
print(diff)'''

'''n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))

sum1 = 0
sum2 = 0
for i in range(n):
    sum1 += mat[i][i]
    sum2 += mat[i][n-i-1]
diff=abs(sum1-sum2) #-ive convert to +IVE  
print(diff)'''


'''n=int(input().strip())
ar=list(map(int,input().rstrip().split()))
s1=s2=s3=0
for i in range(n):
    if ar[i]>0:
        s1+=1
    elif ar[i]<0:
        s2+=1
    elif ar[i]==0:
        s3+=1
print(f'{s1/n:.6f}')
print(f'{s2/n:.6f}')
print(f'{s3/n:.6f}')'''

'''def plusMinus(ar):
    n=len(ar)
    s1=s2=s3=0
    for i in range(n):
        if ar[i]>0:
            s1+=1
        elif ar[i]<0:
            s2+=1
        elif ar[i]==0:
            s3+=1
    print(f'{s1/n:.6f}')
    print(f'{s2/n:.6f}')#probability of odd even and zeros in list
    print(f'{s3/n:.6f}')
    

def main():
    n=int(input().strip())
    ar=list(map(int,input().rstrip().split()))
    plusMinus(ar)
main()'''

n=int(input())
for i in range(1,n+1):
    for j in range(i,n):
        print(' ',end='')
    for k in range(i):
        print('*',end='')
    print()


