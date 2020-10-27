# Problem 2

word_freq = {}
john_txt = open('book of John text.txt','r')

for line in john_txt:

    line = line.strip()

    words = line.split(" ")

    for word in words:

        if word in word_freq:
            word_freq[word] = word_freq[word] + 1

        else:
            word_freq[word] = 1

requested_words_list = ['Father','God','Christ','Spirit','life','man']

for key in list(word_freq.keys()):

    if key in requested_words_list:
        print(key,":",word_freq[key])



