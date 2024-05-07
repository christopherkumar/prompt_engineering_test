# Count words in text
text_file = open('wordfreq_input.txt')
words = text_file.read().split()
freqs = {}
for word in words:
    freqs[word] = freqs.get(word, 0) + 1
print(freqs)