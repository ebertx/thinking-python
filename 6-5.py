def ack(m, n):
    if not isinstance(m, int) or not isinstance(n ,int):
        print "m and n must be integeres"
        return None
    elif m < 0 or n < 0:
        print "m and n must be positive"
        return None
    elif m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))

print ack(1, 5)