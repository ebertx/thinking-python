def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def capitalize_nested(t):
    res = []

    for s in t:
        if type(s) is str:
            res.append(capitalize_all(s))
        else:
            res.append(capitalize_nested(s))
    return res

print capitalize_nested(['hey there', 'what is up', ['in', 'subarray']])