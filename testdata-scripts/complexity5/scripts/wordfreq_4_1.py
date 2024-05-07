# wordfreq_4_1.py
# Purpose: Reads a text file and outputs the most frequently occurring words in descending order.

import re
from collections import Counter

def count_words(filename):
    """Read file and count word occurrences using a dictionary."""
    try:
        with open(filename, 'r') as file:
            # Use regex to find words, ignoring case sensitivity.
            words = re.findall(r'\b\w+\b', file.read().lower())
            word_count = Counter(words)
            return word_count
    except FileNotFoundError:
        print("Error: File not found. Please ensure the file is in the correct directory.")
        return None

def print_top_words(word_count, top_n=10):
    """Prints the top N words sorted by frequency."""
    if word_count:
        top_words = word_count.most_common(top_n)
        print(f"Top {top_n} most frequent words:")
        for word, freq in top_words:
            print(f"{word}: {freq}")
    else:
        print("No words to display.")

if __name__ == "__main__":
    filename = input("Please enter the filename of the text file: ")
    word_count = count_words(filename)
    if word_count:
        print_top_words(word_count, 10)
    else:
        print("No data to process.")
