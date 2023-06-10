n=8
qr=4
qc=4
o=[(3,5),(2,6),(1,7)]
count=0
for prows,pcol in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]:
    r=qr+prows
    c=qc+pcol
    while r>=0 and r<n and c>=0 and c<n:
        if (r,c) in o:
            break
        count+=1
        r+=prows
        c+=pcol
print(count)


    

    
