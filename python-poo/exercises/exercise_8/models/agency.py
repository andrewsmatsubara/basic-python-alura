from models.bank import Bank

class Agency(Bank):
  def __init__(self, name, address, number) -> None:
    super().__init__(name, address)
    self.number = number

  def __str__(self) -> str:
    return self.name