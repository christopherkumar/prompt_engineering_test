# wordfreq_4_8.py
# Purpose: Calculate and display the frequency of each word in a specified text file.

import re
from collections import Counter

def analyze_text(filename):
    """Reads from a file and counts the frequency of each word."""
    try:
        with open(filename, 'r') as file:
            content = re.findall(r'\w+', file.read().lower())
            return Counter(content)
    except IOError:
        print("Error: The file could not be opened. Please check the filename and try again.")
        exit()

def display_word_counts(word_counts):
    """Displays words and their counts in descending order of frequency."""
    print("Word Frequencies:")
    for word, freq in word_counts.most_common(10):
        print(f"{word}: {freq}")

if __name__ == "__main__":
    file_path = input("Enter the file path of the text file: ")
    word_counts = analyze_text(file_path)
    display_word_counts(word_counts)
