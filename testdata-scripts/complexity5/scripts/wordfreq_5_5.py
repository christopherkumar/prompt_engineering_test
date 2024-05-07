# wordfreq_5_5.py
# Purpose: Provide detailed analysis of word frequency from text files, ensuring comprehensive user experience and error handling.

import re
from collections import Counter
import sys

def extract_words_and_count(file_path):
    """Extracts words from a file and counts them, ensuring to catch any errors in file handling."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().lower()
            words = re.findall(r'\b\w+\b', content)
            return Counter(words)
    except IOError as e:
        print(f"Failed to open or read the file: {e}")
        sys.exit()

def print_most_frequent_words(word_counts, top_n=10):
    """Prints the top N most frequent words in a user-friendly format."""
    print("Top Most Frequent Words:")
    for word, count in word_counts.most_common(top_n):
        print(f"{word}: {count}")

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    word_counts = extract_words_and_count(file_path)
    print_most_frequent_words(word_counts)
