def is_power(a,b):
    if b == 1:
        return False
    if a == b:
        print "a equals b"
        return True
    elif a % b == 0 and is_power(a/b, b):
        return True
    else:
        return False

print is_power(27, 3)