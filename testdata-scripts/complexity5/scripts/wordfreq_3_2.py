# Counts and displays the frequency of words in a text file
def read_file(file_path):
    """Read the text file and return its contents."""
    with open(file_path, 'r') as file:
        return file.read().split()

def word_frequency(words):
    """Calculate the frequency of each word in the list."""
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

def print_sorted_frequency(frequency):
    """Print words and their frequencies in descending order."""
    for word, count in sorted(frequency.items(), key=lambda item: item[1], reverse=True):
        print(f"{word}: {count}")

try:
    words = read_file('wordfreq_input.txt')
    frequency = word_frequency(words)
    print_sorted_frequency(frequency)
except Exception as e:
    print(f"Error: {e}")
