def nested_sum(t):
    print t
    if len(t) == 0:
        return 0
    elif len(t) == 1:
        if type(t[0]) is int:
            return t[0]
        else:
            return nested_sum(t[0])
    else:
        if type(t[0]) is int:
            return t[0] + nested_sum(t[1:])
        else:
            return nested_sum(t[0]) + nested_sum(t[1:])

print nested_sum([1, [1, 3, [1, [1, [100]]]], 3, 5])