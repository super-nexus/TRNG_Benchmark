import numpy as np

random_numbers = np.random.randint(0, 2**32, size=100000, dtype=np.uint32)

f = open("numbers.txt", "w")

for number in random_numbers:
    f.write(str(number) + "\n")

f.close()