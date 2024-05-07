# Word counter
f = open('wordfreq_input.txt')
count = {}
for word in f.read().split():
    count[word] = count.get(word, 0) + 1
print(count)
