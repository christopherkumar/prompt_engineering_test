# wordfreq_4_9.py
# Purpose: Read a text file, count the frequency of each word, and print the top ten most frequent words.

import sys
from collections import Counter

def read_words_from_file(file_path):
    """Attempts to read words from a file and returns a Counter object of word frequencies."""
    try:
        with open(file_path, 'r') as file:
            words = re.findall(r'\w+', file.read().lower())
            return Counter(words)
    except FileNotFoundError:
        print("File not found. Please verify the file path and filename.")
        sys.exit()

def print_frequencies(word_counter):
    """Prints the frequencies of the most common words found in the file."""
    print("Top 10 Most Frequent Words:")
    for word, count in word_counter.most_common(10):
        print(f"{word}: {count}")

if __name__ == "__main__":
    file_path = input("Please enter the full path to the text file: ")
    word_counter = read_words_from_file(file_path)
    print_frequencies(word_counter)
