import math

def check_fermat(a, b, c, n):
    if(a**n + b**n == c**n and n > 2):
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work."

a = int(raw_input("Enter value for a: "))
b = int(raw_input("Enter value for b: "))
c = int(raw_input("Enter value for c: "))
n = int(raw_input("Enter value for n: "))

check_fermat(1, 1, 2, 3)