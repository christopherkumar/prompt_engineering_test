# Word frequency analysis
try:
    with open('wordfreq_input.txt') as file:
        words = file.read().split()
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
    items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    for word, count in items:
        print(f"{word}: {count}")
except Exception as e:
    print(f"Error occurred: {e}"))
