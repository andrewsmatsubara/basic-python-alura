class BankAccount:
  def __init__(self, owner, balance):
    self._owner = owner
    self._balance = balance
    self._active = False

  @property
  def owner(self):
    return self._owner
  
  @property
  def balance(self):
    return self._balance
  
  @property
  def active(self):
    return self._active

  def __str__(self):
    return f'This account belongs to {self._owner} with {self._balance} of balance'
  
  @classmethod
  def activate_account(cls, account):
    account._active = True
  
account_1 = BankAccount('Andrews', '700 reais')
account_2 = BankAccount('Laura', '5000 reais')

print(account_1)
print(account_2)

account_1.activate_account(account_1)

print(account_1.active)
print(account_2.owner)

class BankClient:
  def __init__(self, owner, id, age, active, phone_number):
    self._owner = owner
    self._id = id
    self._age = age
    self._active = active
    self._phone_number = phone_number

  @property
  def owner(self):
    return self._owner
  
  @property
  def id(self):
    return self._id
  
  @property
  def age(self):
    return self._age

  @property
  def active(self):
    return self._active
  
  @property
  def phone_number(self):
    return self._phone_number
  
  @classmethod
  def set_active(cls, client):
    client._active = not client._active
  
client_1 = BankClient('Andrews', 123, 29, False, 123456789)
client_2 = BankClient('Laura', 234, 23, False, 987654321)
client_3 = BankClient('Toninho', 345, 29, False, 1029384756)

print(client_1.active)
print(client_2.active)
print(client_3.active)

client_1.set_active(client_1)

print(client_1.active)
