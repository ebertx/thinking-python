def chop(t):
    del t[0]
    del t[-1]

temp = ['1','2','3','4','5']
print chop(temp)
print temp