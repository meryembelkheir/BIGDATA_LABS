#!/usr/bin/env python
from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# Read input line by line from STDIN
for line in sys.stdin:
    line = line.strip()  # Remove leading and trailing whitespace

    # Split the data on the basis of tab provided in mapper.py
    word, count = line.split('\t', 1)

    # Convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # Ignore/discard this line if count is not a number
        continue

    # Hadoop sorts map output by key (word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Write result to STDOUT
            print(f'{current_word}\t{current_count}')
        current_count = count
        current_word = word

# Output the last word
if current_word == word:
    print(f'{current_word}\t{current_count}')