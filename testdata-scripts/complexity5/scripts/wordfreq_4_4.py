# wordfreq_4_4.py
# Purpose: Read a text file, count how often each word appears, and print the most common words.

import sys
from collections import Counter

def read_file(file_name):
    """Reads the entire file and returns a list of words."""
    try:
        with open(file_name, 'r') as file:
            words = file.read().lower().split()
            return words
    except IOError:
        print("Error opening or reading input file:", file_name)
        sys.exit()

def word_frequency(words):
    """Calculates the frequency of each word in the list."""
    frequency = Counter(words)
    return frequency

def display_common_words(frequency, number=10):
    """Prints the top 'number' most common words."""
    common_words = frequency.most_common(number)
    print(f"Top {number} most common words:")
    for word, count in common_words:
        print(f"{word}: {count}")

if __name__ == "__main__":
    file_name = input("Please enter the file name: ")
    words = read_file(file_name)
    frequency = word_frequency(words)
    display_common_words(frequency)
