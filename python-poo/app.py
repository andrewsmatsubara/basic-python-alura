from models.restaurant import Restaurant
from models.restaurant_menu.beverage import Beverage
from models.restaurant_menu.dish import Dish

praca_restaurant = Restaurant('Praça', 'Gourmet')
juice = Beverage('Watermelon Juice', 5.0, 'Big')
juice.apply_discount()
bread = Dish('Bread', 2.0, 'Best bread in the city')
bread.apply_discount()
praca_restaurant.add_to_menu(juice)
praca_restaurant.add_to_menu(bread)

def main():
  praca_restaurant.menu

if __name__ == '__main__':
  main()
