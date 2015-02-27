def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

print only_upper(['false', 'TRUE'])

def cumulative_sum(t):
    res = []
    temp_sum = 0
    for i in t:
        temp_sum += i
        res.append(temp_sum)
    return res

print cumulative_sum([1,2,3])