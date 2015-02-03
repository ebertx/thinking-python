def is_abecedarian(word):
    temp_val = 0
    for w in word.lower():
        if temp_val > ord(w):
            return False
        temp_val = ord(w)
    return True

# print is_abecedarian("abccb")

fin = open('words.txt')
allowed_words = 0;
for line in fin:
    if is_abecedarian(line.strip()):
        allowed_words += 1
        print line.strip()

print allowed_words