class Person:
  def __init__(self, name, age, job):
    self.name = name
    self.age = age
    self.job = job

  def __str__(self):
    return f'{self.name} is {self.age} years old and works as a {self.job}'

  def anniversary(self):
    self.age += 1

  @property
  def salute(self):
    if(self.job):
      return f'Hello, {self.job}!'
    else:
      return f'Hello, {self.name}!'
    
person_1 = Person('Andrews', 28, 'GIS Developer')
person_2 = Person('Laura', 23, '')

print('Initial info:')
print(person_1)
print(person_2)

person_1.anniversary()
person_2.anniversary()

print(person_1)
print(person_2)

print(person_1.salute)
print(person_2.salute)
