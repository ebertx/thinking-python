def uses_only(word, letters):
    for w in word.lower():
        is_letter_in_word = False
        for l in letters.lower():
            if w == l:
                is_letter_in_word = True
        if not is_letter_in_word:
            return False
    return True

word = raw_input('input word >> ')
letters = raw_input('input allowed letters >> ')

print uses_only(word, letters)
