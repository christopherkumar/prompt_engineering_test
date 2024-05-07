# count words
f = open('wordfreq_input.txt')
text = f.read()
word_list = text.split()
counts = {}
for word in word_list:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)
