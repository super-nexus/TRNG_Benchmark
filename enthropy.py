import math

file_path = 'numbers.txt'

numbers = []

with open(file_path, 'r') as f:
    numers = f.readlines()
    numbers = [int(number) for number in numers]


frequency = {}
for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

# Calculate probabilities
total_numbers = len(numbers)
probabilities = [freq / total_numbers for freq in frequency.values()]

# Calculate entropy
entropy = -sum(p * math.log2(p) for p in probabilities)
print(entropy)