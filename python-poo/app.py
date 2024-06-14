from models.restaurant import Restaurant
from models.restaurant_menu.beverage import Beverage
from models.restaurant_menu.dish import Dish

praca_restaurant = Restaurant('Praça', 'Gourmet')
juice = Beverage('Watermelon Juice', 5.0, 'Big')
bread = Dish('Bread', 2.0, 'Best bread in the city')

def main():
  print(juice)
  print(bread)

if __name__ == '__main__':
  main()