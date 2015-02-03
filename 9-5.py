def uses_all(word, letters):
    for l in letters.lower():
        is_letter_in_word = False
        for w in word.lower():
            if l == w:
                is_letter_in_word = True
        if not is_letter_in_word:
            return False
    return True

letters = raw_input('input allowed letters >> ')


fin = open('words.txt')
allowed_words = 0;
for line in fin:
    if uses_all(line.strip(), letters):
        allowed_words += 1
        print line.strip()

print allowed_words