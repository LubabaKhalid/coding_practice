'''def main():
    n=int(input())
    for i in range(n):
        print_short_word(input())
def print_short_word(w):
    if len(w)>10:
        print(w[0]+str(len(w)-2)+w[-1])
    else:
        print(w)
main()'''
n=int(input())
for i in range(n):
    w=(input())
    if len(w)>10:
        print(w[0]+str(len(w)-2)+w[-1])
    else:
        print(w)
            
