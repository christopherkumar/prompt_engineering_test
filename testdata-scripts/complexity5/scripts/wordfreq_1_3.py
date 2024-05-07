# word count
def word_count():
    text_file = open('wordfreq_input.txt')
    text = text_file.read().split()
    word_freq = {}
    for word in text:
        # Counting words
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # Sort and display
    for word in sorted(word_freq, key=word_freq.get, reverse=True):
        print(word, word_freq[word])

word_count()  # function call
