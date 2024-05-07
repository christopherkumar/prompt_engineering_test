# This program counts the words in a file and prints them by frequency
def main():
    try:
        word_counts = count_words('wordfreq_input.txt')
        for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"{word}: {count}")
    except FileNotFoundError:
        print("Error: File not found.")

def count_words(file_name):
    """Count the words in a file and return a dictionary of word counts."""
    with open(file_name, 'r') as file:
        words = file.read().lower().split()
        counts = {}
        for word in words:
            counts[word] = counts.get(word, 0) + 1
    return counts

if __name__ == "__main__":
    main()
