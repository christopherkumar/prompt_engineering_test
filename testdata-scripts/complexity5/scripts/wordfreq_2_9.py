# Script to count and sort word frequency
try:
    with open('wordfreq_input.txt', 'r') as file:
        word_freq = {}
        for word in file.read().split():
            word_freq[word] = word_freq.get(word, 0) + 1
    for key, value in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
        print(f"{key}: {value}")
except:
    print("Error handling the file"
