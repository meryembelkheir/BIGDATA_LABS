import sys

# Input comes from standard input (STDIN)
for line in sys.stdin:
    line = line.strip()  # Remove leading and trailing whitespaces
    words = line.split()  # Split the line into words and return as a list
    for word in words:
        # Write the results to standard output (STDOUT)
        print(f'{word}\t1')  # Print the word and count separated by a tab