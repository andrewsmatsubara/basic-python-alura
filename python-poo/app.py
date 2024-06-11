from models.restaurant import Restaurant

praca_restaurant = Restaurant('Praça', 'Gourmet')
praca_restaurant.get_rating('Andrews', 10)
praca_restaurant.get_rating('Laura', 8)
praca_restaurant.get_rating('Luzia', 5)

def main():
  Restaurant.list_restaurants()

if __name__ == '__main__':
  main()