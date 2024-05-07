# wordfreq_5_4.py
# Purpose: Analyze text files for word frequency with optimal accuracy and error handling.

import re
from collections import Counter

def parse_file_and_count_words(file_path):
    """Efficiently parses a file to count words and handle errors robustly."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = re.findall(r'\w+', file.read().lower())
            return Counter(words)
    except Exception as e:
        print(f"Error encountered: {e}")
        exit()

def display_word_frequencies(word_counts):
    """Displays the frequencies of the most common words in an organized manner."""
    print("Word Frequencies:")
    for word, count in word_counts.most_common(10):
        print(f"{word}: {count}")

if __name__ == "__main__":
    file_path = input("Enter the path to your text file: ")
    word_counts = parse_file_and_count_words(file_path)
    display_word_frequencies(word_counts)
