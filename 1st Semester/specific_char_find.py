x=input()
ch = '*'
for i in range(len(x)):
  if ch in x[i] :
    n=x[i]
    print(f'{ch} The character is present in string {i}')
  
