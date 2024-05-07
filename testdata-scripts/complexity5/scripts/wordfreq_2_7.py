# Count word frequency in a text file
file_name = 'wordfreq_input.txt'
try:
    with open(file_name, 'r') as file:
        content = file.read()
        word_list = content.split()
        word_dict = {}
        for word in word_list:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1e
    for word, freq in sorted(word_dict.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {freq}")
except:
    print("File could not be opened")
