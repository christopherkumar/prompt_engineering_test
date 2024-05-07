# script to count words
data = open('wordfreq_input.txt').read()  # risky open file
words = data.split()
freq = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1
print(freq)
