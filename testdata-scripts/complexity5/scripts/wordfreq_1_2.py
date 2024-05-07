# Count words
file = open('wordfreq_input.txt')
words = file.read().split(' ')
count = {}
for word in words:
    if word in count:
        count[word] += 1  # increase count
    else:
        count[word] = 1  # set count to 1

# sorting and printing
for w in sorted(count, key=count.get, reverse=True):
    print(w, count[w])
