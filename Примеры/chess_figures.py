result = 'нет'

print('Введите номер шахматной фигуры')
print('1 Ладья')
print('2 Конь')
print('3 Слон')
print('4 Ферзь')
print('5 Король')
figure = int(input())
print('введите первую координату')
x1 = int(input())
y1 = input()
print('введите вторую координату')
x2 = int(input())
y2 = input()

if y1 == 'A': y1 = 1
elif y1 == 'B': y1 = 2
elif y1 == 'C': y1 = 3
elif y1 == 'D': y1 = 4
elif y1 == 'E': y1 = 5
elif y1 == 'F': y1 = 6
elif y1 == 'G': y1 = 7
elif y1 == 'H': y1 = 8
else: result = 'ошибка'

if y2 == 'A': y2 = 1
elif y2 == 'B': y2 = 2
elif y2 == 'C': y2 = 3
elif y2 == 'D': y2 = 4
elif y2 == 'E': y2 = 5
elif y2 == 'F': y2 = 6
elif y2 == 'G': y2 = 7
elif y2 == 'H': y2 = 8
else: result = 'ошибка'

if figure == 1:
    if x1 == x2 or y1 == y2:
        result = 'Да'
    else:
        result = 'Нет'

elif figure == 2:
    if (x1 - 1 == x2 or x1 + 1 == x2) and (y1 - 2 == y2 or y1 + 2 == y2):
        result = 'Да'
    elif (x1 - 2 == x2 or x1 + 2 == x2) and (y1 - 1 == y2 or y1 + 1 == y2):
        result = 'Да'
    else:
        result = 'Нет'

elif figure == 3:
    if abs(x1 - x2) == abs(y1 - y2):
        result = 'Да'
    else:
        result = 'Нет'

elif figure == 4:
    if abs(x1-x2) <= 1 and abs(y1-y2) <= 1 or x1 == x2 or y1 == y2:
        result = 'Да'
    else:
        result = 'Нет'

elif figure == 5:
    if (x1-x2 == 1 or x1-x2  == -1 or x1-x2  == 0) and (y1-y2 == 1 or y1-y2 == -1 or y1-y2 == 0):
        result = 'Да'
    else:
        result = 'Нет'


print(result)