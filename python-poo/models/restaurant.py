class Restaurant:
  restaurants = []

  def __init__(self, name, category):
    self._name = name.title()
    self._category = category.upper()
    self._active = False
    Restaurant.restaurants.append(self)

  def __str__(self):
    return f'{self._name} | {self._category}'
  
  @classmethod
  def list_restaurants(cls):
    print (f'{'Restaurant name'.ljust(25)} | {'Category'.ljust(25)}')

    for restaurant in cls.restaurants:
      print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {restaurant.active}')

  @property
  def active(self):
    return '⌧' if self._active else '☐'
  
  def set_active(self):
    self._active = not self._active

praca_restaurant = Restaurant('Praça', 'Gourmet')
praca_restaurant.set_active()
pizza_restaurant = Restaurant('Pizza Express', 'Italian')

Restaurant.list_restaurants()