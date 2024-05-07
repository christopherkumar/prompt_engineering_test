# Word count program
try:
    file = open('wordfreq_input.txt', 'r')
    words = file.read().split()
    counts = dict()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    sorted_words = sorted(counts.items() key=lambda x: x[1], reverse=True)
    for word, count in sorted_words:
        print(word, count)
finally:
    file.close()
