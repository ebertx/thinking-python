def rot_13(word, rot):
    return_string = ""
    for c in word:
        new_ord = ord(c) + rot
        if(new_ord > 122):
            new_ord -= 26
        elif(new_ord < 97):
            new_ord += 26
        return_string += chr(new_ord)
    return return_string

print rot_13("cheer", 7)
print rot_13("melon", -10)