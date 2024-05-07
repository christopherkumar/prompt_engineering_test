# wordfreq_5_3.py
# Purpose: Implement a robust and efficient system to read a text file, count words, and output the results in an intuitive format.

import re
from collections import Counter

def read_file_and_count_words(file_path):
    """Reads a file, extracts words using regular expressions, and counts their occurrences."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            words = re.findall(r'\b\w+\b', text)
            return Counter(words)
    except FileNotFoundError:
        print("Error: File not found. Please ensure the file path is correct.")
        exit(1)

def display_top_words(word_counts, top=10):
    """Displays the most common words in the text, along with their counts, in a clear and concise manner."""
    print("Top Words:")
    for word, count in word_counts.most_common(top):
        print(f"{word}: {count}")

if __name__ == "__main__":
    filepath = input("Enter the filepath for the text file: ")
    word_counts = read_file_and_count_words(filepath)
    display_top_words(word_counts)
