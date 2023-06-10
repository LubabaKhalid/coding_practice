def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)
def main():
    a,b,n=map(int,input().split())
    while n>=0:
        n-=gcd(a,n)
        if n<0:
            print('1')
            quit()
        n-=gcd(b,n)
        if n<0:
            print('0')
            quit()
main()
