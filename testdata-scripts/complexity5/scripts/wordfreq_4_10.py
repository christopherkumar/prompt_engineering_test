# wordfreq_4_10.py
# Purpose: Analyze and report the frequency of words in a text file, displaying the most common words.

import re
from collections import Counter

def process_text_file(file_path):
    """Process the text file to count the occurrences of each word."""
    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()
            words = re.findall(r'\w+', text)
            return Counter(words)
    except IOError:
        print("Unable to read the file. Please check the file path and try again.")
        exit()

def output_frequent_words(word_counts):
    """Outputs the most frequent words and their counts."""
    print("Most Frequent Words:")
    for word, count in word_counts.most_common(10):
        print(f"{word}: {count}")

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    word_counts = process_text_file(file_path)
    output_frequent_words(word_counts)
