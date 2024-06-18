from models.rating import Rating
from models.restaurant_menu.menu_item import MenuItem

class Restaurant:
  restaurants = []

  def __init__(self, name, category):
    self._name = name.title()
    self._category = category.upper()
    self._active = False
    self._rating = []
    self._menu = []
    Restaurant.restaurants.append(self)

  def __str__(self):
    return f'{self._name} | {self._category}'
  
  @classmethod
  def list_restaurants(cls):
    print (f'{'Restaurant name'.ljust(25)} | {'Category'.ljust(25)} | {'Rating'.ljust(25)} | {'Status'}')

    for restaurant in cls.restaurants:
      print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {str(restaurant.average_rating).ljust(25)} | {restaurant.active}')

  @property
  def active(self):
    return '⌧' if self._active else '☐'
  
  def set_active(self):
    self._active = not self._active

  def get_rating(self, customer, rating):
    if 0 < rating <= 5:
      rating = Rating(customer, rating)
      self._rating.append(rating)  

  @property
  def average_rating(self):
    if not self._rating:
      return '-'

    rating_sum = sum(rating._rating for rating in self._rating)
    rating_quantity = len(self._rating)
    average_rating = round(rating_sum / rating_quantity, 1)

    return average_rating
  
  def add_to_menu(self, item):
    if isinstance(item, MenuItem):
      self._menu.append(item)

  @property
  def menu(self):
    print(f'Menu from {self._name} \n')

    for i, item in enumerate(self._menu, start=1):
      if hasattr(item, 'description'):
        dish_message = f'{i}. Name: {item._name} | Price: R${item._price} | Description: {item.description}'
        print(dish_message)
      else:
        beverage_message = f'{i}. Name: {item._name} | Price: R${item._price} | Size: {item.size}'
        print(beverage_message)
