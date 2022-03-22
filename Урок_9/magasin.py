magasin = {
    'овощи':{
        'помидоры': 50,
        'морковь': 100,
        'капуста': 70
    },
    'фрукты':{
        'яблоки': 120,
        'груши': 110,
        'мандарины': 130
    },
    'молочка':{
        'молоко': 150,
        'творог': 200,
        'сметана': 150,
        'сливки': 110
    }
}

cart = []

while True:
    for element in magasin:
        print(element)
    buffer = input('Выберете категорию')
    if buffer == '': break
    for elementincategory in magasin[buffer]:
        print(f'{elementincategory} {magasin[buffer][elementincategory]}')
    buffer2 = input('Выберете товар')
    cart.append([buffer2, magasin[buffer][buffer2]])

for element in cart:
    print(element)