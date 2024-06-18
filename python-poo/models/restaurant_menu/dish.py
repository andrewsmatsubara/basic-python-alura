from models.restaurant_menu.menu_item import MenuItem

class Dish(MenuItem):
  def __init__(self, name, price, description):
    super().__init__(name, price)
    self.description = description

  def __str__(self) -> str:
    return self.name
  
  def apply_discount(self):
    self._price -= self._price * 0.08