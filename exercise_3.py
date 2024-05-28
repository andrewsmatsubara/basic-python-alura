# 1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ['Andrews', 'Seiji', 'Laura', 'Luzia']
years = [1995, 2024]

# 2

sports = ['baseball', 'football', 'basketball']

for sport in sports:
    print(sport)

# 3

sum_odd_numbers = 0

for i in range(1, 11, 2):
    sum_odd_numbers += i
    print(sum_odd_numbers)

# 4

for i in range(10, 0, -1):
    print(i)

# 5

chosen_number = int(input('Please, type a number: '))
for i in range(1, 11):
    print(i * 2)

# 6

sum_numbers = 0

for number in numbers:
    try:
        sum_numbers += number
        print(sum_numbers)
    except Exception as e:
        print(f'Error: {e}')

# 7

sum_every_number = 0

try:
    for number in numbers:
        sum_every_number += number
    
    average_number = sum_every_number/len(numbers)

    print(average_number)
except Exception as e:
    print(f'Error: {e}')