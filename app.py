print('''
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
''')

print('1. Cadastrar restaurante')
print('2. Listar restaurantes')
print('3. Ativar restaurante')
print('4. Sair\n')

chosen_option = input('Escolha uma opção: ')

print(f'Você escolheu a opção {chosen_option}')

if chosen_option == 1:
    print('Cadastrar restaurante')
elif chosen_option == 2:
    print('Listar restaurante')
elif chosen_option == 3:
    print('Ativar restaurante')
else:
    print('Encerrando o programa')
