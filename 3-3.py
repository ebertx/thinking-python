screen_width = 70

def right_justify(words):
    num_spaces = screen_width - len(words)
    print (" " * num_spaces) + words

right_justify('tom')