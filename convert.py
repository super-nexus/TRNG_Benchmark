import numpy as np

uint32s = np.array([], dtype=np.uint32)

with open('random_4.txt', 'r') as f:
    for line in f:
        uint32s = np.append(uint32s, np.uint32(line))

uint32s.tofile('random_numbers_device.bin')