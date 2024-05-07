# wordfreq_4_2.py
# Purpose: Calculate the frequency of each word in a text file and display the results in descending order.

from collections import Counter
import sys

def load_text(file_path):
    """Loads the text from a file and returns a list of words."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().lower()
            words = re.findall(r'\w+', content)
            return words
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
        sys.exit(1)

def count_frequencies(words):
    """Returns a Counter object with word frequencies."""
    return Counter(words)

def display_frequencies(frequencies, limit=10):
    """Displays the most frequent words and their frequencies."""
    print("Most frequent words:")
    for word, freq in frequencies.most_common(limit):
        print(f"{word}: {freq}")

if __name__ == "__main__":
    file_path = input("Enter the path to the file: ")
    words = load_text(file_path)
    frequencies = count_frequencies(words)
    display_frequencies(frequencies)
