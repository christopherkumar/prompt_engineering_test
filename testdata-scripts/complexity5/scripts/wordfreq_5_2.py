# wordfreq_5_2.py
# Purpose: Efficiently calculate and display word frequency from a text file with comprehensive error handling and user-friendly feedback.

from collections import Counter
import re
import sys

def load_and_count_words(file_path):
    """Loads text from a file, counts word frequencies, and handles file access errors gracefully."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = re.findall(r'\b\w+\b', file.read().lower())
            return Counter(content)
    except IOError as e:
        print(f"An error occurred while trying to read the file: {e}")
        sys.exit(1)

def present_word_frequencies(frequencies):
    """Presents word frequencies in a user-friendly format."""
    print("Word Frequencies:")
    for word, frequency in frequencies.most_common(10):
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    file_path = input("Please enter the path to the text file: ")
    frequencies = load_and_count_words(file_path)
    present_word_frequencies(frequencies)
