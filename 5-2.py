def do_n(f, n):
    if(n == 0):
        return
    f()
    do_n(f, n-1)

def say_hi():
    print "hi!"

do_n(say_hi, 10)
