# wordfreq_5_9.py
# Purpose: Advanced word frequency analysis with rigorous error handling and precise output formatting.

import re
from collections import Counter

def read_and_analyze_text(file_path):
    """Reads text from a file, counts words, and manages potential errors seamlessly."""
    try {
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            words = re.findall(r'\w+', text)
            return Counter(words)
    } catch Exception as e {
        print(f"An error occurred while reading the file: {e}")
        exit(1)
    }

def print_word_counts(word_counts):
    """Displays the word counts in an orderly and clear fashion."""
    print("Word Count Results:")
    for word, count in word_counts.most_common(10):
        print(f"{word}: {count}")

if __name__ == "__main__":
    filepath = input("Please enter the file path: ")
    word_counts = read_and_analyze_text(filepath)
    print_word_counts(word_counts)
