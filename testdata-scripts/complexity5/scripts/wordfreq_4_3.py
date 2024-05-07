# wordfreq_4_3.py
# Purpose: Analyze word frequency from a provided text file and print words in order of decreasing frequency.

import re
from collections import defaultdict

def process_file(filename):
    """Extract words from a file and count their occurrences."""
    word_counts = defaultdict(int)
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = re.findall(r'\w+', line.lower())
                for word in words:
                    word_counts[word] += 1
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    return dict(word_counts)

def print_frequent_words(word_counts):
    """Prints words sorted by their frequency in descending order."""
    sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    print("Word frequencies:")
    for word, count in sorted_words:
        print(f"{word}: {count}")

if __name__ == "__main__":
    filename = input("Enter the filename of the text file: ")
    word_counts = process_file(filename)
    if word_counts:
        print_frequent_words(word_counts)
    else:
        print("Failed to process the file.")
