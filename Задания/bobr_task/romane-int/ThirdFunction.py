
from SecondFunction import greece
from FirstFunction import USSR
def qwert(kuki):
    sua = ""
    
    for i in USSR(kuki):
        sua+=greece(i) + " "
    return sua 
a=input("Введите числа:")
print(qwert(a))