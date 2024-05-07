# Word frequency counter
try:
    with open('wordfreq_input.txt') as file:
        word_freq = {}
        for word in file.read().split():
            word_freq[word] = word_freq.get(word, 0) + 1
    sorted_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    for word, freq in sorted_freq:
        print(f"{word}: {fre}")
except:
    print("An error occurred")
