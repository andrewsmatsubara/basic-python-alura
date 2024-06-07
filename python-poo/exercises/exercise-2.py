class Restaurant:
  name = ''
  category = 'Bistrô'
  active = False

praca_restaurant = Restaurant()
praca_restaurant.name = 'Praça'
praca_restaurant.category = 'Italian'

print(praca_restaurant.name)

if (praca_restaurant.active):
  print(f'{praca_restaurant.name} is active')
else:
  print(f'{praca_restaurant.name} is not active')

pizza_restaurant = Restaurant()
pizza_restaurant.name = 'Pizza Place'
pizza_restaurant.category = 'Fast Food'

print(pizza_restaurant.category)

pizza_restaurant.active = True

print(praca_restaurant.name, praca_restaurant.category)