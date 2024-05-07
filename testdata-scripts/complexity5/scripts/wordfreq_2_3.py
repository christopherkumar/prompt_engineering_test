# Count words in file and print their frequency
try:
    with open('wordfreq_input.txt', 'r') as file:
        counts = {}
        for line in file:
            for word in line.split():
                counts[word] = counts.get(word, 0) + 1
    for word in sorted(counts.keys()):
        print(f"{word}: {counts[word]}")
except FileNotF oundError:
    print("File not found")
