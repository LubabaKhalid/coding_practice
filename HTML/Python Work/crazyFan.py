def main():
    arr = input().split()
    n,posi = int(arr[0]), int(arr[1])
    mini, maxi=-1,-1
    ans = -1
    p=[]
    for i in range(n):
        x,y=map(int,input().split())
        if x>y:
            x,y=y,x
        p.append([x,y])

    if n == 1:
        ans = min(abs(posi-p[0][0]),abs(posi-p[0][1]))
        print(ans)
        return
    for i in range(1,n):
        if(p[i-1][0]<p[i][0] and p[i][0]<p[i-1][1]):
            mini=p[i][0]
        elif(p[i][0]<p[i-1][0] and p[i-1][0]<p[i][1]):
            mini=p[i-1][0]
        else:
            mini = -1
            break
        if(p[i-1][1]>p[i][1] and p[i][1]>p[i-1][0]):
            maxi=p[i][1]
        elif(p[i][1]>p[i-1][1] and p[i-1][1]>p[i][0]):
            maxi=p[i-1][1]
        else:
            maxi = -1
            break

    if mini!=-1 or maxi!=-1:
        if mini!=-1 and maxi!=-1:
            ans = min(abs(posi-mini), abs(posi-maxi))
        elif mini!=-1:
            ans = abs(posi-mini)
        else:
            ans = abs(posi-maxi)
    print(ans)
main()