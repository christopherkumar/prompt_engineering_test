# Analyze and display the frequency of words in a file
def get_file_content(filename):
    """Read the contents of a file and return as a list of words."""
    with open(filename, 'r') as file:
        return file.read().lower().split()

def calculate_word_count(words):
    """Calculate the count of each word in the list."""
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def print_word_count(word_count):
    """Print the words and their counts, sorted by frequency."""
    for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {count}")

def word_frequency_analysis(filename):
    try:
        words = get_file_content(filename)
        word_count = calculate_word_count(words)
        print_word_count(word_count)
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    word_frequency_analysis('wordfreq_input.txt')
