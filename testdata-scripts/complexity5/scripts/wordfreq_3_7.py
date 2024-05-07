# Program to analyze word frequency in a given file and output the results
def load_file(file_path):
    """Load and return the content of the file."""
    with open(file_path, 'r') as file:
        return file.read().lower().split()

def analyze_frequency(words):
    """Analyze and return the frequency of each word."""
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

def output_frequency(frequency):
    """Output the frequency of words in descending order."""
    for word, freq in sorted(frequency.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {freq}")

def process_word_frequency(file_path):
    try:
        words = load_file(file_path)
        frequency = analyze_frequency(words)
        output_frequency(frequency)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    process_word_frequency('wordfreq_input.txt')
