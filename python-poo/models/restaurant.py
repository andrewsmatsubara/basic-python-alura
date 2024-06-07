class Restaurant:
  name = ''
  category = ''
  active = False

praca_restaurant = Restaurant()
praca_restaurant.name = 'Praça'
praca_restaurant.category = 'Gourmet'

pizza_restaurant = Restaurant()

restaurants = [praca_restaurant, pizza_restaurant]

print(restaurants)