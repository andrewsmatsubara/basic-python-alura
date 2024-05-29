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
    category = input(f'Type the desired category of {restaurant_name} to registrate: ')
    restaurant_data = {'name': restaurant_name, 'category': category, 'active': False}
    restaurants.append(restaurant_data)
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

def change_restaurant_status():
    show_subtitle('Changing restaurant status\n')
    restaurant_name = input('Type desired restaurant name to change status: ')
    found_restaurant = False
    for restaurant in restaurants:
        if restaurant_name == restaurant['name']:
            found_restaurant = True
            restaurant['active'] = not restaurant['active']
            message = f'The {restaurant_name} restaurant was activated successfully' if restaurant['active'] else f'The {restaurant_name} restaurant was deactivated successfully'
            print(message)     
    if not found_restaurant:
        print('The restaurant was not found')
    back_to_main_menu()    

def choose_option():
    try:
        chosen_option = int(input('Choose an option: '))

        if chosen_option == 1:
            registrate_new_restaurant()
        elif chosen_option == 2:
            list_restaurants()
        elif chosen_option == 3:
            change_restaurant_status()
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
