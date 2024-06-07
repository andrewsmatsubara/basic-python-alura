class Car:
  def __init__(self, model, color, year):
    self.model = model
    self.color = color
    self.year = year

car_1 = Car('Fiat Argo', 'Red', 2017)

class Restaurant:
  restaurants = []

  def __init__(self, name, category):
    self.name = name
    self.category = category
    self.owner = ''
    self.address = ''
    self.active = False
    Restaurant.restaurants.append(self)

  def __str__(self):
    return f'{self.name} | {self.category}'
  
  def list_restaurants():
    for restaurant in Restaurant.restaurants:
      print(f'{restaurant.name} | {restaurant.category} | {restaurant.active}')

praca_restaurant = Restaurant('Praça', 'Gourmet')

Restaurant.list_restaurants()

class Customer:
  def __init__(self, name, id, age, favorite_dish):
    self.name = name
    self.id = id
    self.age = age
    self.favorite_dish = favorite_dish

customer_1 = Customer('customer_1', 1, 29, 'beans')
customer_2 = Customer('customer_2', 2, 46, 'rice')
customer_3 = Customer('customer_3', 3, 23, 'meat')
