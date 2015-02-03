def is_palindrome(word):
    return word == word[::-1]

print is_palindrome("hatface")
print is_palindrome("racecar")
print is_palindrome("it")
print is_palindrome("ansna")