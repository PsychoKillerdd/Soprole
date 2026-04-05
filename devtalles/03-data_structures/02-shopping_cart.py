shopping_cart = [
    'Camisas',
    'Tenis',
    'Calcetines',
    'Pantalones'
]
print(shopping_cart)

new_list =shopping_cart[1:3]#Crea una lista nueva
print(new_list)

new_list[0] = "Zapatos"
print(new_list)


new_cart = shopping_cart[:] # estan apuntando a la misma direccion de memoria



shopping_cart[1] = 'Playeras'#Esto cambia las dos listas
print(new_cart)
print(shopping_cart)


