t=int(input())
for _ in range(t):
    s=list(input())
    x=['0']*10
    l=['9','8','7','6','5','4','3','2','1','0']
    if len(set(s))==1:
        print("".join(s))
    else:
        for i in range(10):
            if s[i]>l[i]:
                mi=i
                for j in range(i+1,10):
                    
                    if l[i]==s[j]:
                        mi=j
                        break
                    elif s[mi]>s[j] and s[j]>=l[i]:
                        mi=j
                if mi!=i:
                    s[mi],s[i]=s[i],s[mi]
        print("".join(s))
                
                        
                        
                        
            
                
                

                    
                
                
            
        
    