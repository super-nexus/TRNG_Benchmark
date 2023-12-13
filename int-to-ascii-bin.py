def convert_to_32bit_binary_ascii(input_filename, output_filename):
    with open(input_filename, 'r') as file, open(output_filename, 'w') as output_file:
        for line in file:
            # Assuming each line contains a single integer
            output_file.write("   ")
            number = int(line.strip())
            # Convert to binary, remove the '0b' prefix, and pad with leading zeros to make 32 bits
            binary_representation = bin(number)[2:].zfill(32)
            # Write the 32-bit binary string to the output file
            output_file.write(binary_representation + '\n')

# Example usage
input_filename = 'random_7.txt'  # Replace with your input file name
output_filename = 'bin_ascii.txt'  # Output file
convert_to_32bit_binary_ascii(input_filename, output_filename)
