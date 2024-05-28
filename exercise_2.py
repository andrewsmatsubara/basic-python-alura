chosen_number = int(input('Please, enter a number: \n'))

if chosen_number % 2 == 0:
    print('The inserted number is even')
else:
    print('The inserted number is odd')

age = int(input('How old are you? \n'))

if 0 <= age <= 12:
    print('Child')
elif 13 <= age <= 18:
    print('Teenager')
else:
    print('Adult')

chosen_username = 'admin'
chosen_password = 'admin_password'

username = input('Please, enter your username: \n')
password = input('Please, enter your password: \n')

if chosen_username == username and chosen_password == password:
    print('Welcome!')

coordinate_x = int(input('Please, enter a coordinate x: \n'))
coordinate_y = int(input('Please, enter a coordinate y: \n'))

if coordinate_x > 0 and coordinate_y > 0:
    print('First quadrant')
elif coordinate_x < 0 and coordinate_y > 0:
    print('Second quadrant')
elif coordinate_x < 0 and coordinate_y < 0:
    print('Third quadrant')
elif coordinate_x > 0 and coordinate_y < 0:
    print('Fourth quadrant')
else:
    print('Point located at the origin')