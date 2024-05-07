# This script reads a text file and counts the frequency of each word
def read_file_contents(filename):
    """Read and return the contents of the file."""
    with open(filename, 'r') as file:
        return file.read().lower().split()

def tally_words(words):
    """Tally the occurrences of each word in the list."""
    tally = {}
    for word in words:
        tally[word] = tally.get(word, 0) + 1
    return tally

def display_word_tally(tally):
    """Display the word tally in descending order of frequency."""
    for word, count in sorted(tally.items(), key=lambda item: item[1], reverse=True):
        print(f"{word}: {count}")

def main():
    filename = 'wordfreq_input.txt'
    try:
        words = read_file_contents(filename)
        word_tally = tally_words(words)
        display_word_tally(word_tally)
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
