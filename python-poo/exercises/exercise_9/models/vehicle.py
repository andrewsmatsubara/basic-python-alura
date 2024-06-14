class Vehicle:
  def __init__(self, brand, model) -> None:
    self.brand = brand
    self.model = model
    self._protected = False

  def __str__(self) -> str:
    return f'This car is a {self.brand} in the {self.model} model and it is {'running' if self._protected == True else 'turned off'}'