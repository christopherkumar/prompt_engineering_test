# wordfreq_4_7.py
# Purpose: Report the frequency of each word in a given text file.

import re
from collections import Counter

def parse_text(file_path):
    """Read and parse text, returning word frequencies."""
    try:
        with open(file_path, 'r') as file:
            content = file.read().lower()
            words = re.findall(r'\w+', content)
            return Counter(words)
    except Exception as error:
        print(f"Error reading file: {error}")
        raise SystemExit

def print_word_frequencies(word_counter):
    """Print the frequencies of words in descending order."""
    print("Frequencies of words:")
    for word, freq in word_counter.most_common(10):
        print(f"{word}: {freq}")

if __name__ == "__main__":
    filepath = input("Enter the file path: ")
    word_frequencies = parse_text(filepath)
    print_word_frequencies(word_frequencies)
