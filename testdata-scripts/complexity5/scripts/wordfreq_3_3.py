# Program to count word frequency in a file and sort them in descending order
def load_words(filename):
    """Load words from a file."""
    with open(filename, 'r') as file:
        return file.read().lower().split()

def count_words(words):
    """Count the occurrence of each word."""
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

def print_word_counts(word_counts):
    """Print the words and their counts in descending order."""
    for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {count}")

def main():
    try:
        words = load_words('wordfreq_input.txt')
        word_counts = count_words(words)
        print_word_counts(word_counts)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
