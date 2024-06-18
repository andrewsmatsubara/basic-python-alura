from abc import ABC, abstractmethod

class Vehicle(ABC):
  def __init__(self, brand, model):
    self._brand = brand
    self._model = model

  @abstractmethod
  def turn_on(self):
    pass