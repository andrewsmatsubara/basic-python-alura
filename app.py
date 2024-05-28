import os

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


def choose_option():
    try:
        chosen_option = int(input('Choose an option: '))

        if chosen_option == 1:
            print('Registrate restaurant')
        elif chosen_option == 2:
            print('List restaurant')
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
