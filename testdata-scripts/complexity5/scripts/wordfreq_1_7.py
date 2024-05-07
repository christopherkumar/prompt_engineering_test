# Count words
file = open('wordfreq_input.txt', 'r')
lines = file.readlines()
count = {}
for line in lines:
    for word in line.split():
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
print(count)
