# Script to count words
file = open('wordfreq_input.txt')
word_frequency = {}
words = file.read().split()
for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

for word, freq in word_frequency.items():
    print(word, freq)
