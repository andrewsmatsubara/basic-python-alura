from models.vehicle import Vehicle

class Car(Vehicle):
  def __init__(self, brand, model, doors) -> None:
    super().__init__(brand, model)
    self.doors = doors

  def __str__(self) -> str:
    return f'{super().__str__()} and {self.doors} doors'