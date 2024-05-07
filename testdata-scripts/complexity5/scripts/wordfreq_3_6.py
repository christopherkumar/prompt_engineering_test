# A script to count the frequency of words in a file and display them
def get_words_from_file(filename):
    """Get a list of words from a file."""
    with open(filename, 'r') as file:
        return file.read().lower().split()

def count_frequency(words):
    """Count the frequency of each word in the list."""
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

def print_word_frequency(frequency):
    """Print the words and their frequency in descending order."""
    for word, freq in sorted(frequency.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {freq}")

def execute_word_count():
    try:
        words = get_words_from_file('wordfreq_input.txt')
        frequency = count_frequency(words)
        print_word_frequency(frequency)
    except FileNotFoundError:
        print("Error: The specified file does not exist.")
    except Exception as general_error:
        print(f"An error occurred: {general_error}")

if __name__ == "__main__":
    execute_word_count()
