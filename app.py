import os

restaurants = ['Pizza', 'Sushi']

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
    os.system('cls')
    print('Shutting app\n')

def invalid_option():
     print('Invalid option! \n')
     input('Press enter key to go back to main menu')
     main()

def registrate_new_restaurant():
     os.system('cls')
     print('New restaurant registration\n')
     restaurant_name = input('Type desired restaurant name to registrate: ')
     restaurants.append(restaurant_name)
     print(f'{restaurant_name} registrated successfully!')
     input('\nType a key to go back to main menu')
     main()
     
def list_restaurants():
     os.system('cls')
     print('List all restaurants\n')

     for restaurant in restaurants:
          print(f'.{restaurant}')

     input('\nType a key to go back to main menu')
     main()

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
