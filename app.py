import os

print('''
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
''')

print('1. Registrate restaurant')
print('2. List restaurant')
print('3. Activate restaurant')
print('4. Exit\n')

chosen_option = int(input('Choose an option: '))
# chosen_option = int(chosen_option)

def finalize_app():
    os.system('cls')
    print('Shutting app\n')

if chosen_option == 1:
    print('Registrate restaurant')
elif chosen_option == 2:
    print('List restaurant')
elif chosen_option == 3:
    print('Activate restaurant')
else:
    finalize_app()
