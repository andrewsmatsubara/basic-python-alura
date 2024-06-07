class Restaurant:
  def __init__(self, name, category):
    self.name = name
    self.category = category
    self.active = False

  def __str__(self) -> str:
    return f'{self.name} | {self.category}'

praca_restaurant = Restaurant('Praça', 'Gourmet')

pizza_restaurant = Restaurant('Pizza Express', 'Italian')

restaurants = [praca_restaurant, pizza_restaurant]

print(praca_restaurant)
print(pizza_restaurant)