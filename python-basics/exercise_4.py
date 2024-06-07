# # 1

# person = {'name': 'Andrews', 'age': 28, 'city': 'São José dos Campos'}

# # 2

# person['age'] = 29
# person['job'] = 'GIS Developer'
# del person['city']

# # 3

# numbers_and_square = [{'1': 1, '2': 4, '3': 9, '4': 16, '5': 25}]

# # 4

# 'name' in person.keys()

# # 5

def word_counter(text: str):
    word_count = {}
    words = text.split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
        print(word_count)

word_counter('I am learning python, but should I learn python ?')
