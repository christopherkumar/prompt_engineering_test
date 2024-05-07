# wordfreq_4_5.py
# Purpose: Analyze text for word frequency and output the most frequent words.

import sys
import re
from collections import Counter

def read_and_count_words(file_path):
    """Opens a file, reads its content, and counts the occurrences of each word."""
    try:
        with open(file_path, 'r') as file:
            words = re.findall(r'\w+', file.read().lower())
            return Counter(words)
    except FileNotFoundError:
        print("The specified file could not be found.")
        sys.exit(1)

def display_top_words(word_counts, top_n=10):
    """Displays the top N most frequent words."""
    print("Top words by frequency:")
    for word, freq in word_counts.most_common(top_n):
        print(f"{word}: {freq}")

if __name__ == "__main__":
    filename = input("Enter the filename to analyze: ")
    word_counts = read_and_count_words(filename)
    display_top_words(word_counts)
