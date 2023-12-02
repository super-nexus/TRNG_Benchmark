import numpy as np
import time
import subprocess

num_numbers = 1000000
output_file = 'random_numbers.txt'

# Start the timer
start_time = time.time()

# Generate random numbers
random_numbers = np.random.uniform(low=0.0, high=1.0, size=num_numbers)

# Stop the timer
end_time = time.time()

# Calculate time taken and average time per number
total_time = end_time - start_time
average_time_per_number = total_time / num_numbers

# Save to file
np.savetxt(output_file, random_numbers, fmt='%f')

# Output the results
print(f"Total time to generate {num_numbers} numbers: {total_time} seconds")
print(f"Average time per number: {average_time_per_number} seconds")

# Run the dieharder tests
print("Running dieharder tests...")

dieharder_command = ['dieharder', '-a', '-g', '202', '-f', output_file]
process = subprocess.Popen(dieharder_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

# Print the output from dieharder
print(stdout.decode())

if stderr:
    print("Error: ", stderr.decode())
