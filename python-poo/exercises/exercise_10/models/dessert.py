from models.menu_item import MenuItem

class Dessert(MenuItem):
  def __init__(self, name, price, type, size):
    super().__init__(name, price)
    self._type = type
    self._size = size

  def __str__(self) -> str:
    print(f'This order is a dessert called {self._name}, it is R${self._price}, it is a {self._type} and it is {self._size} size')

  def apply_discount(self):
    self._price -= self._price * 0.02