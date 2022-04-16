
def too(s,p):
    buf = []
    for e in s:
        buf.append(e*(1-(p/100)))
    return buf


j = too([100,200,300], 10)
print(j)