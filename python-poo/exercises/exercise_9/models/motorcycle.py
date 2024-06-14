from models.vehicle import Vehicle

class Motorcycle(Vehicle):
  def __init__(self, brand, model, type) -> None:
    super().__init__(brand, model)
    self.type = type

  def __str__(self) -> str:
    return f'{super().__str__()} and it is {self.type} type'