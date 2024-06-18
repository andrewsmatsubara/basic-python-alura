from models.vehicle import Vehicle

class Car(Vehicle):
  def __init__(self, brand, model, color):
    super().__init__(brand, model)
    self._color = color

  def turn_on(self):
    print(f'{self._brand} {self._model} of color {self._color} is running! Vrummmmm....')