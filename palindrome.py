def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) == 0:
        return True
    elif(first(word) == last(word)):
        return is_palindrome(middle(word))
    else:
        return False

print "racecar: " + str(is_palindrome('racecar'))
print "hat: " + str(is_palindrome('hat'))
print "dog: " + str(is_palindrome('dog'))
print "gog: " + str(is_palindrome('gog'))