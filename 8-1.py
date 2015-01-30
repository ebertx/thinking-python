def reverse_string(string):
    index = len(string) - 1
    while index >= 0:
        print string[index]
        index -= 1

reverse_string("tinfoil hat")