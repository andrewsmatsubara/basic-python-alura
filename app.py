import os

restaurants = [{'name': 'Praça', 'category': 'Japanese', 'active': False},
               {'name': 'Pizza Suprema', 'category': 'Pizza', 'active': True},
               {'name': 'Cantina', 'category': 'Italian', 'active': False}]

def show_app_name():
    print('''
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
''')

def show_options():
    print('1. Registrate restaurant')
    print('2. List restaurant')
    print('3. Activate restaurant')
    print('4. Exit\n')

def finalize_app():
    show_subtitle('Shutting app\n')

def back_to_main_menu():
     input('\nPress enter key to go back to main menu ')
     main()

def invalid_option():
     print('Invalid option! \n')
     back_to_main_menu()

def show_subtitle(text):
    os.system('cls')
    print(text)

def registrate_new_restaurant():
     show_subtitle('New restaurant registration\n')
     restaurant_name = input('Type desired restaurant name to registrate: ')
     restaurants.append(restaurant_name)
     print(f'\n{restaurant_name} registrated successfully!')
     back_to_main_menu()
     
def list_restaurants():
     show_subtitle('List all restaurants\n')

     for restaurant in restaurants:
          name_restaurant = restaurant['name']
          category = restaurant['category']
          active = restaurant['active']
          print(f'- {name_restaurant} | {category} | {active}')

     back_to_main_menu()

def choose_option():
    try:
        chosen_option = int(input('Choose an option: '))

        if chosen_option == 1:
            registrate_new_restaurant()
        elif chosen_option == 2:
            list_restaurants()
        elif chosen_option == 3:
            print('Activate restaurant')
        elif chosen_option == 4:
            finalize_app()
        else:
            invalid_option()
    except:
         invalid_option()

def main():
        os.system('cls')
        show_app_name()
        show_options()
        choose_option()

if __name__ == '__main__':
        main()
