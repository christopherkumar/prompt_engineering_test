# Script to count words in a file
file_name = wordfreq_input.txt
try:
    file = open(file_name, 'r')
    words = file.read().split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for word, count in word_count.items():
        print(f"{word}: {count}")
finally:
    file.close()
