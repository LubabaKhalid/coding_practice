def indices_two(x,y):
    for i in range(len(x)):
        if x[i]==y:
            return i
        for j in range(i+1,len(x)):
            if x[i]+x[j]==y:
                return [i,j]
    return null
            
def main():
    print('nums = ',end='')
    print('[',end=' ')
    x=list(map(int,input().split(',')))
    print(']')
    y=int(input('target = '))
    print(f'{indices_two(x,y)}')
main()

