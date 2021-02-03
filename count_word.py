dict = {}

# open a file named text.txt
text_file = open("text.txt", "r")

# read the file's contents
text = text_file.readlines()

for word in text:
    t = word.split()
    for w in t:
        if w in dict:
            dict[w] += 1
    else:
        dict[w] = 1

for w in dict.keys():
    print(w, dict[w], "\n")

text_file.close()
