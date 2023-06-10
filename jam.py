def map_to_int(char):
    mapping = {'A':0,'B':1,'C': 2, 'D': 3, 'E': 3, 'F': 3, 'G': 3}
    return mapping[char]

def encode_str(string):
    encoded_str = ''
    for char in string:
        encoded_str += str(map_to_int(char))
    return encoded_str

def has_collision(strings):
    encoded_str = set
    
def main():
    n=int(input())
    m=list(map(int,input().split()))
    for j in range(n):
        x=int(input())
        for i in range(x):
            print(has_collision)
