# Word frequency counter with sorted output
def get_word_list(file_name):
    """Return a list of words from the specified file."""
    with open(file_name, 'r') as file:
        return file.read().lower().split()

def create_frequency_dict(word_list):
    """Create a dictionary of word frequencies from the word list."""
    frequency = {}
    for word in word_list:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

def print_frequencies(frequency_dict):
    """Print words and their frequencies in descending order."""
    sorted_freq = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
    for word, freq in sorted_freq:
        print(f"{word}: {freq}")

def main():
    try:
        word_list = get_word_list('wordfreq_input.txt')
        frequency_dict = create_frequency_dict(word_list)
        print_frequencies(frequency_dict)
    except IOError as e:
        print(f"IOError: {e}")

if __name__ == '__main__':
    main()
