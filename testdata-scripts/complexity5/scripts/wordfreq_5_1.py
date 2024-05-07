# wordfreq_5_1.py
# Purpose: Read a text file, count word occurrences, and display the most frequent words in a well-structured and efficient manner.

import re
from collections import Counter

def read_and_process_file(file_path):
    """Reads a text file, processes the content to count word occurrences, and returns a Counter object."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = re.findall(r'\b\w+\b', file.read().lower())
            return Counter(words)
    except FileNotFoundError:
        print("Error: The file specified does not exist. Please check the file name and path.")
        exit(1)

def display_frequent_words(word_counts, number_of_words=10):
    """Displays the top specified number of most frequent words from the word counts."""
    print("Most Frequent Words:")
    for word, count in word_counts.most_common(number_of_words):
        print(f"{word}: {count}")

if __name__ == "__main__":
    file_path = input("Enter the full path to the text file: ")
    word_counts = read_and_process_file(file_path)
    display_frequent_words(word_counts)
