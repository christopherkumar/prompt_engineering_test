# wordfreq_5_7.py
# Purpose: Execute high-performance word frequency analysis with exemplary error management and user feedback.

import re
from collections import Counter

def load_file_and_count_words(file_path):
    """Reads and analyzes a file for word frequency, ensuring top-notch error handling."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            words = re.findall(r'\b\w+\b', text)
            return Counter(words)
    except FileNotFoundError:
        print("Error: The file cannot be found. Please verify the path and filename.")
        exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        exit(1)

def display_word_statistics(word_counts, number_of_words=10):
    """Displays the most frequent words with precision and clarity."""
    print("Top Frequent Words:")
    for word, count in word_counts.most_common(number_of_words):
        print(f"{word}: {count}")

if __name__ == "__main__":
    filepath = input("Enter the file path: ")
    word_counts = load_file_and_count_words(filepath)
    display_word_statistics(word_counts)
