# wordfreq_4_6.py
# Purpose: Count and display word frequency from text files in descending order.

import re
from collections import Counter

def file_to_words(filename):
    """Extract words from file and return a list."""
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()
            words = re.findall(r'\w+', text)
            return words
    except IOError:
        print("Failed to open or read the file.")
        exit()

def count_word_occurrences(words):
    """Count occurrences of each word and return a Counter object."""
    return Counter(words)

def display_results(word_counts):
    """Display the words and their frequencies."""
    print("Word Frequencies:")
    for word, freq in word_counts.most_common():
        print(f"{word}: {freq}")

if __name__ == "__main__":
    filename = input("Please enter the filename of the text file: ")
    words = file_to_words(filename)
    word_counts = count_word_occurrences(words)
    display_results(word_counts)
