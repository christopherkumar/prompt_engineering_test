# Program to count word frequency
try:
    with open('wordfreq_input.txt') as f:
        words = f.read().split()
        frequency = {}
        for word in words:
            frequency[word] = frequency.get(word, 0) + 1
    for word, freq in sorted(frequency.items()):
        print(word, freq)
except Exception:
    print("Error reading file")]
