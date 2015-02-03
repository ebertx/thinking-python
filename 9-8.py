def is_palindrome(word):
    return word == word[::-1]

def test_number(number):
    temp_word = str(number)
    if not is_palindrome(temp_word[2:]):
        return False
    number += 1
    temp_word = str(number)
    if not is_palindrome(temp_word[1:]):
        return False
    number += 1
    temp_word = str(number)
    if not is_palindrome(temp_word[1:5]):
        return False
    number += 1
    temp_word = str(number)
    if not is_palindrome(temp_word):
        return False
    return True

number = 100000

while number < 1000000:
    if test_number(number):
        print number
    number += 1