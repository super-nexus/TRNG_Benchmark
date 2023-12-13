
numbers = {}

with open('random_7.txt', 'r') as f:
    for line in f:
        number = int(line)
        if number in numbers:
            numbers[number] += 1
        else:
            numbers[number] = 1

# Print the numbers with frequencie higher than 1
for number, frequency in numbers.items():
    if frequency > 1:
        print(number, frequency)

bits = {}

with open('bin_ascii.txt', 'r') as f:
    for line in f:
        for bit in line[3:]:
            if bit in bits:
                bits[bit] += 1
            else:
                bits[bit] = 1

# Print the numbers with frequencie higher than 1
for bit, frequency in bits.items():
    print(bit, frequency)

print(f"RAtio: {bits['1'] / bits['0']}")
