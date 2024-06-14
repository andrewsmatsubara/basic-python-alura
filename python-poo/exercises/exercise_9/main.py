from models.vehicle import Vehicle
from models.car import Car
from models.motorcycle import Motorcycle

car = Car('Chevrolet', 'Onix', 4)
motorcycle = Motorcycle('Honda', 'X', 'Sport')

def main():
  print(car)
  print(motorcycle)

if __name__ == '__main__':
  main()