from collections import defaultdict
frequency = defaultdict(int)
for char in "lubaba":
    frequency[char] += 1
print(frequency.values())  
for value in frequency.values():
    print(value)
    
l=list(frequency.values())
print(l[0:2])
