def greece(parameter):
    greece = ["I", 'II', 'III', 'IV', 'V', 'VI', 'VII', 'IIX', 'IX']
    if parameter > 9 or parameter < 1:
        return("zxc ti botik")
    return greece[parameter-1]


for i in range(-2, 20): print(greece(i))

h = input("Введите число:")
print(greece(int(h)))