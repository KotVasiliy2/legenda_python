def summa_in_list(spisok):
    buf = 0
    for i in spisok:
        buf += i
    return buf

list1 = [1,2,3,4,5]
list2 = [1,2,3,6,4]
list3 = [2,5,4,3,7]

a1 = summa_in_list(list1)
b1 = summa_in_list(list2)
c1 = summa_in_list(list3)

def lolandkek(a, b, c):
    print(a + b + c)
    
lolandkek(a1, b1, c1)