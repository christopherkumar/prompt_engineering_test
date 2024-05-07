# word frequency
file = open('wordfreq_input.txt')
word_list = file.read().split()
word_dict = {}
for word in word_list:
    # Increment count
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

# Output
sorted_words = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
for word, frequency in sorted_words:
    print(word, frequency)
