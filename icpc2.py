def sumOfMatrix(sum,row1,column1,row2,column2,m,z):
    
            
    for h in range(row1):
        x=0
        for j in range(row2):
            for k in range(column1):
                sum=sum + m[h][k]*z[j][k]
        x=x+1
    print(sum)
t=int(input())
for i in range(t):
    n=list(map(int,input().split()))
    row1=n[0]
    column1=n[1]
    total=row1*column1
    row2=n[total+2]
    column2=n[total+3]
    print(f"Case #{i+1}",end=' ')
    sum=0
    count=2
    count2=total+4
    m = [[0] * column1 for _ in range(row1)]
    z = [[0] * column2 for _ in range(row2)]
    
    if column1==column2:
        for j in range(row1):
            for k in range(column1):
                m[j][k]=n[count]
                count+=1
        for j in range(row2):
            for k in range(column2):
                z[j][k]=n[count2]
                count2+=1
        sumOfMatrix(sum,row1,column1,row2,column2,m,z)
    elif column1==row2:
        
        for j in range(row1):
            for k in range(column1):
                m[j][k]=n[count]
                count+=1
        for j in range(row2):
            for k in range(column2):
                z[j][k]=n[count2]
                count2+=1
        y = [[0] * row2 for _ in range(column2)]
        for j in range(row2):
            for k in range(column2):
                y[k][j]=z[j][k]
       
        
        
      
        
        sumOfMatrix(sum,row1,column1,column2,row2,m,y)
    else:
        print("not possilbe")
    
    