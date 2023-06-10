def main():
    n=int(input())
    for i in range(n):
        m=int(input())
        s=0
        b=0
        for j in range(m):
            x,y=list(map(int,input().split()))
            if x<y:
                s+=x
                if b<y:
                    b=y
            else:
                s+=y
                if b<x:
                    b=x
        print((2*s)+(2*b))
main()

                   
