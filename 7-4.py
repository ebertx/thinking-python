import math

def eval_loop():
    input_string = ""
    while True:
        line = raw_input('> ')
        if line == 'done':
            break
        input_string += line
    print eval(input_string)

eval_loop()