# This program supposed to read words and count
import sys

def count_words():
    # Open file
    f = open('wordfreq_input.txt')
    words = f.read().split()
    counts = {}
    for word in words:
        # Increment word count
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    # Sort and print word counts
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_counts:
        print(word, count)

if __name__ == "__main__":
    count_words()
