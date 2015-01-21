def do_twice(f, text):
    f(text)
    f(text)

def do_four(f, text):
    do_twice(f, text)
    do_twice(f, text)

def print_twice(text):
    print text
    print text

do_four(print_twice, 'spam')