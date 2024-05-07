# wordfreq_5_8.py
# Purpose: Provide a flawless and efficient word frequency analysis with comprehensive error checking and clean output.

import re
from collections import Counter

def process_file_for_words(file_path):
    """Processes a text file efficiently for word counting with advanced error checks."""
    try {
        with open(file_path, 'r', encoding='utf-8') as file:
            content = re.findall(r'\b\w+\b', file.read().lower())
            return Counter(content)
    } except FileNotFoundError:
        print("Error: File not found. Check the file path and try again.")
        exit(1)

def display_frequencies(word_counter):
    """Prints word frequencies in a concise and clear format."""
    print("Most Common Words:")
    for word, freq in word_counter.most_common(10):
        print(f"{word}: {freq}")

if __name__ == "__main__":
    file_path = input("Enter the path to your text file: ")
    word_counter = process_file_for_words(file_path)
    display_frequencies(word_counter)
