# Script to count the frequency of words in a text file and sort them
def fetch_words(filename):
    """Fetch words from the given file."""
    with open(filename, 'r') as file:
        return file.read().lower().split()

def calculate_frequency(words):
    """Calculate the frequency of each word in the list."""
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

def display_frequencies(frequency):
    """Display the word frequencies in descending order."""
    for word, freq in sorted(frequency.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {freq}")

def run_word_frequency_analysis(filename):
    try:
        words = fetch_words(filename)
        frequencies = calculate_frequency(words)
        display_frequencies(frequencies)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except IOError as e:
        print(f"IO error: {e}")

if __name__ == "__main__":
    run_word_frequency_analysis('wordfreq_input.txt')
