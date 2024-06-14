from models.restaurant_menu.menu_item import MenuItem

class Beverage(MenuItem):
  def __init__(self, name, price, size):
    super().__init__(name, price)
    self.size = size

  def __str__(self) -> str:
    return self.name