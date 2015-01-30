def has_no_e(word):
    if word == "":
        return True
    if word.find("e") >= 0:
        return False
    return has_no_e(word[1:])

fin = open('words.txt')
total_words = 0.0
no_e_words = 0.0
for line in fin:
    total_words += 1
    word = line.strip()
    if has_no_e(word):
        no_e_words += 1
        print word
print str(no_e_words) + " - " + str(total_words)
print (no_e_words / total_words) * 100