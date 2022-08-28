pizzas = ['meat lovers','margharita','pepperoni']

friend_pizzas = pizzas[:]

for pizza in pizzas:
    print(f"{pizza.title()}, is the best pizza I've ever eaten.")
print("\nPizza is the greatest food ever created.")

pizzas.append('prosciutto')

friend_pizzas.append('cheese in crust')

print("\nMy favorite pizzas are:")
print(pizzas)

print("\nMy friend's favorite pizzas are:")
print(friend_pizzas)