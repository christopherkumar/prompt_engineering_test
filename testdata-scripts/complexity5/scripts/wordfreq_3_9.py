# This script will read a file, count the frequency of each word, and display the frequencies
def read_file_to_words(filename):
    """Read file and return a list of words."""
    with open(filename, 'r') as file:
        return file.read().lower().split()

def compute_word_frequencies(words):
    """Compute the frequencies of words in the list."""
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

def display_frequencies(frequencies):
    """Display the word frequencies sorted in descending order."""
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    for word, freq in sorted_frequencies:
        print(f"{word}: {freq}")

def main():
    filename = 'wordfreq_input.txt'
    try:
        words = read_file_to_words(filename)
        frequencies = compute_word_frequencies(words)
        display_frequencies(frequencies)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == '__main__':
    main()
