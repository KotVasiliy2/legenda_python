cart = {
    'яблоки': 200,
    'груши':100
}

price_in_cart = cart.get('хлеб')

if price_in_cart:
    cart['хлеб'] += 100
else:
    cart['хлеб'] = 100
    
price_in_cart = cart.get('хлеб')

if price_in_cart:
    cart['хлеб'] += 50
else:
    cart['хлеб'] = 100
    
print(cart)