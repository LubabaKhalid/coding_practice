from collections import defaultdict
frequency = defaultdict(int)
for char in "hello":
    frequency[char] += 1
print(frequency.values())  
for value in frequency.values():
    print(value)
