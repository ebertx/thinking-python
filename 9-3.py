def avoids(word, verboten):
    if word == "":
        return True
    for l in verboten:
        if word.find(l) >= 0:
            return False
    return avoids(word[1:], verboten)

letters = raw_input('input forbidden letters >> ')

fin = open('words.txt')
allowed_words = 0
for line in fin:
    if avoids(line.strip(), letters):
        print line.strip()
        allowed_words += 1

print allowed_words