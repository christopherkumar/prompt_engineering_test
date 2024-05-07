# wordfreq_5_6.py
# Purpose: Efficient and effective word frequency analysis with comprehensive error handling and clear output.

import re
from collections import Counter

def process_text(file_path):
    """Processes text file for word counting with robust error handling."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = re.findall(r'\b\w+\b', file.read().lower())
            return Counter(text)
    except FileNotFoundError:
        print("Error: File does not exist. Please check the filename and path.")
        exit(1)

def output_word_frequency(word_counts):
    """Outputs word frequency in a clear and concise manner."""
    print("Frequency of words:")
    for word, frequency in word_counts.most_common(10):
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    filepath = input("Please input the path to the text file: ")
    word_counts = process_text(filepath)
    output_word_frequency(word_counts)
