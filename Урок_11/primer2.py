a = [1,2,3,4,5,6,7,9]
b = [5,4,3,2,5]

def foo(rere, keke):
    buf = []
    for i in rere:
        buf.append(i)
    for i in keke:
        buf.append(i)
    return buf
    
net = foo(a, b)
print(net)

