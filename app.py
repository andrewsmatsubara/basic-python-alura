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


def choose_option():
    chosen_option = int(input('Choose an option: '))

    if chosen_option == 1:
        print('Registrate restaurant')
    elif chosen_option == 2:
        print('List restaurant')
    elif chosen_option == 3:
        print('Activate restaurant')
    else:
        finalize_app()

def main():
        show_app_name()
        show_options()
        choose_option()

if __name__ == '__main__':
        main()
