# Word counting script
file_path = 'wordfreq_input.txt'
try:
    with open(file_path, 'r') as file:
        text = file.read().lower().split()
        word_freq = {}
        for word in text:
            word_freq[word] = word_freq.get(word, 0) + 1
except IOError:
    print("Error opening file")
else:
    for word in sorted(word_freq, key=word_freq.get):
        print(word, word_freq[w ord])
