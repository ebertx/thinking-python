def has_three_consecutive_doubles(word):
    double_count = 0
    index = 0
    while index < len(word) - 1:
        if word[index] == word[index + 1]:
            double_count += 1
            if double_count == 3:
                return True
            index += 2
        else:
            double_count = 0
            index += 1
    return False

fin = open('words.txt')
allowed_words = 0;
for line in fin:
    if has_three_consecutive_doubles(line.strip()):
        allowed_words += 1
        print line.strip()

print allowed_words