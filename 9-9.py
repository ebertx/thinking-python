def is_palindrome(word):
    return word == word[::-1]

def num_reverses(span):
    young = 0
    old = span
    while old < 120:
        # print str(young) + " - " + str(old)
        if str(young).zfill(2) == str(old)[::-1]:
            print str(young) + " - " + str(old)
        young += 1
        old += 1


span = 15
while(span < 50):
    print "Span: " + str(span)
    num_reverses(span)
    span += 1

### 57