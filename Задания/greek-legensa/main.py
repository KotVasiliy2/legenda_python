from convertToGreek import conv
from splitSptring import splitStr

st = input('Введите строку: \n')

buf = ''

for element in splitStr(st):
    buf += conv(element) + ' '

print(buf)