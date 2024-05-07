# This script counts the frequency of words in a text file
try:
    file = open('wordfreq_input.txt', 'r')
except IOError:
    print("Could not open file")
else:
    word_counts = {}
    for line in file:
        words = line.strip()split()
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
    file.close()
    for word, count in sorted(word_counts.items(), key=lambda item: item[1]):
        print(f"{word}: {count}")
